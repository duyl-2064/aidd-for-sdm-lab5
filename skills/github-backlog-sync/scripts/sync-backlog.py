#!/usr/bin/env python3
"""Đẩy backlog (epic → issue → sub-issue) lên GitHub repo + Project v2 và ghi field.

Chỉ dùng stdlib + gh CLI. Trạng thái (key → số issue, node id, item id) lưu ở
state JSON nên chạy lại an toàn: mục đã tạo thì bỏ qua.

Lệnh:
  issues   --backlog backlog.py --repo owner/name --state state.json
  issues-gql (như issues, nhưng 1 request GraphQL/issue: tạo + gắn cha + thêm vào Project)
  link     --state state.json --repo owner/name          (gắn sub-issue theo parent)
  deps     --backlog backlog.py --repo owner/name --state state.json  (thay key phụ thuộc bằng #số)
  project  --state state.json --owner login --title T --repo owner/name  (tạo project + field + add item)
  set      --state state.json --field NAME --values values.json        (ghi number/text/date/single-select)
  status   --state state.json --values values.json                     (ghi Status)
  iteration --state state.json --values values.json                    (ghi Iteration theo tên sprint)
  verify   --state state.json --field NAME --values values.json        (đọc ngược, báo key lệch)
"""
import argparse
import importlib.util
import json
import subprocess
import sys
import time


def gh(args, input_text=None, retries=4):
    for attempt in range(retries):
        p = subprocess.run(["gh"] + args, input=input_text, capture_output=True, text=True)
        if p.returncode == 0:
            return p.stdout
        err = p.stderr.strip()
        transient = ("secondary rate limit", "abuse", "502", "something went wrong", "timeout")
        if any(t in err.lower() for t in transient):
            time.sleep(30 * (attempt + 1))
            continue
        raise RuntimeError(f"gh {' '.join(args[:3])}… failed: {err}")
    raise RuntimeError("gh retries exhausted")


def graphql(query, **variables):
    payload = json.dumps({"query": query, "variables": variables})
    out = gh(["api", "graphql", "--input", "-"], input_text=payload)
    data = json.loads(out)
    if data.get("errors"):
        raise RuntimeError(json.dumps(data["errors"], ensure_ascii=False))
    return data["data"]


def load_backlog(path):
    spec = importlib.util.spec_from_file_location("backlog", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ITEMS


def load_state(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"issues": {}, "project": {}}


def save_state(path, state):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1)


def render_body(it, numbers=None):
    numbers = numbers or {}
    lines = [f"**Mục tiêu:** {it['goal']}", "", f"**Spec LAB-4 / PREMISE:** {it['spec']}", "", "**Phạm vi**"]
    lines += [f"- {s}" for s in it["scope"]]
    lines += ["", "**Định nghĩa xong (DoD)**"]
    lines += [f"- [ ] {d}" for d in it["dod"]]
    lines.append("- [ ] Đạt DoD chung (task-breakdown.md §1)")
    if it.get("codes"):
        lines += ["", f"**Mục Phụ lục B (LAB-4) xử lý trong issue này:** {', '.join(it['codes'])}"]
    if it["deps"]:
        refs = [f"#{numbers[k]}" if k in numbers else k for k in it["deps"]]
        lines += ["", f"**Phụ thuộc:** {', '.join(refs)}"]
    lines += ["", f"**Phụ trách (giả định):** {it['owner']} · **Ưu tiên:** {it['prio']} · **Key:** `{it['key']}`"]
    return "\n".join(lines)


LABEL_COLORS = {"type:epic": "5319e7", "type:feature": "1d76db", "type:task": "c5def5",
                "constraint:driver-hours-2024": "b60205", "constraint:temp-zone": "d93f0b",
                "needs-design": "fbca04", "clarify": "f9d0c4", "P0": "e11d21", "P1": "eb6420", "P2": "fef2c0"}


def ensure_labels(items, repo):
    labels = set()
    for it in items:
        labels.update(it["labels"] + [f"type:{it['type']}", it["prio"]])
    existing = {l["name"] for l in json.loads(gh(["label", "list", "--repo", repo, "--limit", "200", "--json", "name"]))}
    for name in sorted(labels - existing):
        gh(["label", "create", name, "--repo", repo, "--color", LABEL_COLORS.get(name, "ededed")])


def cmd_issues_gql(a):
    """Tạo issue bằng GraphQL: 1 request = tạo + gắn cha + thêm vào Project.

    Repo mới tạo, issue tạo tuần tự → số issue dự đoán = vị trí + 1, nên body ghi sẵn #số phụ thuộc.
    Số thực khác dự đoán thì dừng (chạy lệnh `deps` để sửa body).
    """
    items, state = load_backlog(a.backlog), load_state(a.state)
    ensure_labels(items, a.repo)
    owner, name = a.repo.split("/")
    q = """query($o:String!,$n:String!){repository(owner:$o,name:$n){id labels(first:100){nodes{id name}}}
      viewer{id}}"""
    meta = graphql(q, o=owner, n=name)
    repo_id = meta["repository"]["id"]
    label_ids = {l["name"]: l["id"] for l in meta["repository"]["labels"]["nodes"]}
    me = meta["viewer"]["id"]
    predicted = {it["key"]: i + 1 for i, it in enumerate(items)}
    m = """mutation($in:CreateIssueInput!){createIssue(input:$in){issue{id databaseId number}}}"""
    for it in items:
        if it["key"] in state["issues"]:
            continue
        inp = {"repositoryId": repo_id, "title": it["title"], "body": render_body(it, predicted),
               "assigneeIds": [me], "labelIds": [label_ids[l] for l in it["labels"] + [f"type:{it['type']}", it["prio"]]]}
        if it["parent"]:
            inp["parentIssueId"] = state["issues"][it["parent"]]["node_id"]
        if state["project"].get("id"):
            inp["projectV2Ids"] = [state["project"]["id"]]
        issue = graphql(m, **{"in": inp})["createIssue"]["issue"]
        state["issues"][it["key"]] = {"number": issue["number"], "id": issue["databaseId"], "node_id": issue["id"],
                                      "parent": it["parent"], "type": it["type"], "linked": bool(it["parent"])}
        save_state(a.state, state)
        print(it["key"], "→ #", issue["number"], flush=True)
        if issue["number"] != predicted[it["key"]]:
            raise SystemExit(f"số issue lệch dự đoán ở {it['key']}: {issue['number']} ≠ {predicted[it['key']]}")
        time.sleep(1.0)


def cmd_issues(a):
    items, state = load_backlog(a.backlog), load_state(a.state)
    ensure_labels(items, a.repo)
    for it in items:
        if it["key"] in state["issues"]:
            continue
        labs = it["labels"] + [f"type:{it['type']}", it["prio"]]
        args = ["issue", "create", "--repo", a.repo, "--title", it["title"], "--body", render_body(it),
                "--assignee", "@me"]
        for l in labs:
            args += ["--label", l]
        url = gh(args).strip().splitlines()[-1]
        number = int(url.rstrip("/").split("/")[-1])
        meta = json.loads(gh(["api", f"repos/{a.repo}/issues/{number}"]))
        state["issues"][it["key"]] = {"number": number, "id": meta["id"], "node_id": meta["node_id"],
                                      "parent": it["parent"], "type": it["type"]}
        save_state(a.state, state)
        print(it["key"], "→", url)
        time.sleep(1.2)  # tránh secondary rate limit khi tạo nội dung


def cmd_link(a):
    state = load_state(a.state)
    for key, info in state["issues"].items():
        if not info["parent"] or info.get("linked"):
            continue
        parent = state["issues"][info["parent"]]["number"]
        gh(["api", "-X", "POST", f"repos/{a.repo}/issues/{parent}/sub_issues",
            "-F", f"sub_issue_id={info['id']}"])
        info["linked"] = True
        save_state(a.state, state)
        print(f"{key} (#{info['number']}) ⊂ #{parent}")
        time.sleep(0.5)


def cmd_deps(a):
    items, state = load_backlog(a.backlog), load_state(a.state)
    numbers = {k: v["number"] for k, v in state["issues"].items()}
    for it in items:
        if it["deps"]:
            gh(["issue", "edit", str(numbers[it["key"]]), "--repo", a.repo, "--body", render_body(it, numbers)])
            print("deps", it["key"])


FIELDS = [("SWP", "NUMBER", None), ("Estimate (h)", "NUMBER", None), ("Done date (sim)", "DATE", None),
          ("Owner (giả định)", "SINGLE_SELECT", ["BE-1", "BE-2", "FE-1", "FE-2", "QA-1", "BrSE"]),
          ("Ràng buộc đặc thù", "SINGLE_SELECT", ["Giờ lái 2024", "温度帯"])]


def project_fields(project_id):
    q = """query($id:ID!){node(id:$id){... on ProjectV2{fields(first:50){nodes{
      ... on ProjectV2FieldCommon{id name dataType}
      ... on ProjectV2SingleSelectField{options{id name}}
      ... on ProjectV2IterationField{configuration{iterations{id title startDate duration}}}}}}}}"""
    return graphql(q, id=project_id)["node"]["fields"]["nodes"]


def project_item_ids(project_id):
    q = """query($id:ID!,$after:String){node(id:$id){... on ProjectV2{items(first:100,after:$after){
      pageInfo{hasNextPage endCursor} nodes{id content{... on Issue{id}}}}}}}"""
    out, after = {}, None
    while True:
        page = graphql(q, id=project_id, after=after)["node"]["items"]
        out.update({n["content"]["id"]: n["id"] for n in page["nodes"] if n.get("content")})
        if not page["pageInfo"]["hasNextPage"]:
            return out
        after = page["pageInfo"]["endCursor"]


def cmd_project(a):
    state = load_state(a.state)
    pj = state["project"]
    if not pj.get("id"):
        out = json.loads(gh(["project", "create", "--owner", a.owner, "--title", a.title, "--format", "json"]))
        pj.update(id=out["id"], number=out["number"], url=out["url"])
        save_state(a.state, state)
        gh(["project", "link", str(pj["number"]), "--owner", a.owner, "--repo", a.repo])
    have = {f["name"] for f in project_fields(pj["id"])}
    for name, dtype, options in FIELDS:
        if name in have:
            continue
        args = ["project", "field-create", str(pj["number"]), "--owner", a.owner, "--name", name, "--data-type", dtype]
        if options:
            args += ["--single-select-options", ",".join(options)]
        gh(args)
    existing = project_item_ids(pj["id"])  # content node id → item id (lần thêm trước có thể đã thành công)
    for key, info in state["issues"].items():
        if not info.get("item_id") and info["node_id"] in existing:
            info["item_id"] = existing[info["node_id"]]
            save_state(a.state, state)
        if info.get("item_id"):
            continue
        q = "mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p,contentId:$c}){item{id}}}"
        try:
            info["item_id"] = graphql(q, p=pj["id"], c=info["node_id"])["addProjectV2ItemById"]["item"]["id"]
        except RuntimeError as e:
            # GitHub tự thêm sub-issue khi issue cha đã nằm trong Project → lấy item id có sẵn
            if "already exists" not in str(e):
                raise
            existing = project_item_ids(pj["id"])
            info["item_id"] = existing[info["node_id"]]
        save_state(a.state, state)
        time.sleep(0.3)
    print("project", pj["url"])


def set_value(project_id, item_id, field_id, value):
    q = """mutation($p:ID!,$i:ID!,$f:ID!,$v:ProjectV2FieldValue!){
      updateProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,fieldId:$f,value:$v}){projectV2Item{id}}}"""
    graphql(q, p=project_id, i=item_id, f=field_id, v=value)


def field_value(field, raw):
    if field["dataType"] == "NUMBER":
        return {"number": float(raw)}
    if field["dataType"] == "DATE":
        return {"date": raw}
    if field["dataType"] == "TEXT":
        return {"text": str(raw)}
    if field["dataType"] == "SINGLE_SELECT":
        opt = {o["name"]: o["id"] for o in field["options"]}
        return {"singleSelectOptionId": opt[raw]}
    if field["dataType"] == "ITERATION":
        its = {i["title"]: i["id"] for i in field["configuration"]["iterations"]}
        return {"iterationId": its[raw]}
    raise ValueError(field["dataType"])


def cmd_set(a, field_name):
    state = load_state(a.state)
    values = json.load(open(a.values, encoding="utf-8"))
    fields = {f["name"]: f for f in project_fields(state["project"]["id"]) if "name" in f}
    field = fields[field_name]
    for key, raw in values.items():
        info = state["issues"][key]
        set_value(state["project"]["id"], info["item_id"], field["id"], field_value(field, raw))
        print(f"{field_name}: {key} (#{info['number']}) = {raw}")
        time.sleep(0.2)


def cmd_verify(a):
    """Đọc ngược giá trị field trên Project, so với values.json; lệch thì báo key."""
    state = load_state(a.state)
    values = json.load(open(a.values, encoding="utf-8"))
    by_item = {v["item_id"]: k for k, v in state["issues"].items() if v.get("item_id")}
    q = """query($id:ID!,$after:String){node(id:$id){... on ProjectV2{items(first:100,after:$after){
      pageInfo{hasNextPage endCursor} nodes{id fieldValues(first:30){nodes{
        ... on ProjectV2ItemFieldNumberValue{number field{... on ProjectV2FieldCommon{name}}}
        ... on ProjectV2ItemFieldTextValue{text field{... on ProjectV2FieldCommon{name}}}
        ... on ProjectV2ItemFieldDateValue{date field{... on ProjectV2FieldCommon{name}}}
        ... on ProjectV2ItemFieldSingleSelectValue{name field{... on ProjectV2FieldCommon{name}}}
        ... on ProjectV2ItemFieldIterationValue{title field{... on ProjectV2FieldCommon{name}}}}}}}}}}"""
    actual, after = {}, None
    while True:
        page = graphql(q, id=state["project"]["id"], after=after)["node"]["items"]
        for node in page["nodes"]:
            for fv in node["fieldValues"]["nodes"]:
                if fv.get("field", {}).get("name") == a.field:
                    val = next(fv[k] for k in ("number", "text", "date", "name", "title") if k in fv)
                    actual[by_item.get(node["id"])] = val
        if not page["pageInfo"]["hasNextPage"]:
            break
        after = page["pageInfo"]["endCursor"]
    bad = [k for k, v in values.items() if str(actual.get(k)) != str(v) and
           not (isinstance(actual.get(k), float) and float(v) == actual.get(k))]
    print(f"{a.field}: {len(values) - len(bad)}/{len(values)} khớp")
    for k in bad:
        print("  lệch", k, "file =", values[k], "project =", actual.get(k))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["issues", "issues-gql", "link", "deps", "project", "set", "status", "iteration", "verify"])
    ap.add_argument("--backlog")
    ap.add_argument("--repo")
    ap.add_argument("--state", required=True)
    ap.add_argument("--owner")
    ap.add_argument("--title")
    ap.add_argument("--field")
    ap.add_argument("--values")
    a = ap.parse_args()
    if a.cmd == "issues":
        cmd_issues(a)
    elif a.cmd == "issues-gql":
        cmd_issues_gql(a)
    elif a.cmd == "link":
        cmd_link(a)
    elif a.cmd == "deps":
        cmd_deps(a)
    elif a.cmd == "project":
        cmd_project(a)
    elif a.cmd == "set":
        cmd_set(a, a.field)
    elif a.cmd == "status":
        cmd_set(a, "Status")
    elif a.cmd == "iteration":
        cmd_set(a, a.field or "Sprint")
    elif a.cmd == "verify":
        return cmd_verify(a)


if __name__ == "__main__":
    sys.exit(main())
