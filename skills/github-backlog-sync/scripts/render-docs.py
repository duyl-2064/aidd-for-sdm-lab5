#!/usr/bin/env python3
"""Thay {{KEY}} trong template markdown bằng link issue thật.

  render-docs.py --state state.json --repo owner/name --src tpl/ --dst repo/ [--project-url URL]

{{E05}} → [#57](https://github.com/owner/name/issues/57); {{PROJECT_LINK}} → link Project.
Key không có trong state → báo lỗi, không để sót placeholder.
"""
import argparse
import json
import pathlib
import re
import sys

TOKEN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--src", required=True)
    ap.add_argument("--dst", required=True)
    ap.add_argument("--project-url", default="")
    ap.add_argument("--vars", help="JSON {TOKEN: text} cho placeholder không phải issue")
    a = ap.parse_args()
    issues = json.load(open(a.state, encoding="utf-8"))["issues"]
    extra = json.load(open(a.vars, encoding="utf-8")) if a.vars else {}
    project_url = a.project_url or json.load(open(a.state, encoding="utf-8")).get("project", {}).get("url", "")
    missing = set()

    def sub(m):
        key = m.group(1)
        if key == "PROJECT_LINK":
            return f"[{project_url}]({project_url})" if project_url else m.group(0)
        if key in extra:
            return str(extra[key])
        if key in issues:
            n = issues[key]["number"]
            return f"[#{n}](https://github.com/{a.repo}/issues/{n})"
        missing.add(key)
        return m.group(0)

    for src in sorted(pathlib.Path(a.src).glob("*.md")):
        out = TOKEN.sub(sub, src.read_text(encoding="utf-8"))
        (pathlib.Path(a.dst) / src.name).write_text(out, encoding="utf-8")
        print("rendered", src.name)
    if missing:
        print("missing keys:", sorted(missing), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
