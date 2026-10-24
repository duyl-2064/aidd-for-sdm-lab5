---
name: github-backlog-sync
description: Đẩy backlog epic → issue → sub-issue (định nghĩa trong 1 file Python) lên GitHub repo + Project v2, gắn sub-issue thật, tạo field (SWP, Estimate, Owner, Ràng buộc, Done date, Sprint) và ghi giá trị field từ file JSON đã review, rồi đọc ngược để kiểm. Dùng khi cần tạo backlog hàng loạt từ detail design, hoặc để agent ghi SWP/giờ/Status/Iteration đã chốt lên Project.
---

# github-backlog-sync

Skill tự viết cho LAB-5. Không tự quyết số liệu: chỉ đẩy lên GitHub những gì đã có trong file backlog hoặc file JSON đã được người review.

## Đầu vào

- `backlog.py` — danh sách `ITEMS`, mỗi phần tử có `key` (E11 / I1105 / S111001), `parent`, `type` (epic|feature|task), `title`, `owner`, `prio`, `labels`, `spec`, `goal`, `scope`, `dod`, `deps`, `codes` (mã Phụ lục B của spec mà issue xử lý).
- `state.json` — do script tạo, lưu key → số issue, id, node id, item id trên Project. Chạy lại thì bỏ qua mục đã có.
- `values.json` — `{key: giá trị}` cho lệnh `set` / `status` / `iteration` / `verify`.

## Quy trình (cách đã dùng ở LAB-5)

1. `sync-backlog.py project` — tạo Project (cần scope `project`), link repo, tạo field. Trường Iteration và lựa chọn Status tạo bằng GraphQL (`createProjectV2Field`, `updateProjectV2Field`) vì gh CLI chưa hỗ trợ.
2. `sync-backlog.py issues-gql` — **1 request GraphQL `createIssue` cho mỗi issue**: tạo issue + gắn cha (`parentIssueId`) + thêm vào Project (`projectV2Ids`). Repo mới nên số issue dự đoán được (= vị trí + 1), body ghi sẵn `#số` phụ thuộc; số thực lệch dự đoán thì dừng.
3. `sync-backlog.py set --field SWP --values swp.json` — ghi SWP **sau khi người đã review** report của `tkm:sun-estimate`; giá trị lấy nguyên `finalSWP` trong payload đã validate. Tương tự cho `Estimate (h)`, `Owner (giả định)`, `Ràng buộc đặc thù`, `Done date (sim)`.
4. `sync-backlog.py status|iteration --values …` — cập nhật Status/Sprint khi giả lập sprint.
5. `sync-backlog.py verify --field NAME --values …` — đọc ngược toàn bộ item bằng GraphQL, so với file JSON; lệch thì báo đích danh key và trả exit 1.
6. `render-docs.py --vars vars.json` — thay `{{KEY}}` trong template markdown bằng link issue thật và `{{TÊN}}` bằng số liệu sinh sẵn.

Lệnh cũ `issues` / `link` / `deps` (tạo bằng `gh issue create`, gắn sub-issue bằng REST, sửa body lần 2) vẫn giữ để dùng với repo đã có issue.

## Ràng buộc

- Chỉ ghi SWP vào trường **SWP**; giờ ghi trường **Estimate (h)**. Không ghi lẫn.
- SWP và giờ chỉ ghi ở issue lá; issue cha để trống (tổng xem ở report).
- Không đọc/ghi token ra file; dùng phiên `gh auth` hiện có.
- Lỗi tạm thời của GitHub (rate limit, 502, "something went wrong") được retry có giãn cách; "Content already exists" khi thêm vào Project nghĩa là GitHub đã tự thêm sub-issue theo cha → đọc lại item id thay vì thêm lần nữa.
