# AI report — LAB-5

Công cụ: **Claude Code (Opus) trong VS Code** làm agent chính, chạy trên thư mục local chứa bộ LAB-4, estimate LAB-1, RFP và quy định giờ lái (chỉ đọc local, không đưa lên repo). Takumi kit core v6.2.0 + extras v1.1.0. GitHub qua `gh` CLI (scope `repo`, `project`).

## 1. Skill và prompt đã dùng cho từng việc

| Việc | Skill / agent | Prompt và cách làm |
|---|---|---|
| **Break task** | Agent chính (không dùng skill sinh backlog); skill tự viết `skills/github-backlog-sync` để đẩy lên GitHub | Prompt gốc là toàn văn đề LAB-5 kèm câu "nội dung Lab 4 nằm trong thư mục Lab 4". Agent đọc screen spec, architecture, ADR, DB diagram, rồi hỏi người dùng 3 quyết định: trục epic (**theo màn hình**), cách dùng Phụ lục B (**truy vết đủ 237 mục**), 41 màn LAB-1 chưa thiết kế (**issue theo màn, tách sub-issue theo pattern**). Backlog viết thành dữ liệu (`key, parent, type, title, owner, spec, goal, scope, DoD, deps, codes`), kèm script kiểm: mọi mã Phụ lục B có đúng 1 issue nhận, mục "phải sửa" không được rơi vào issue làm rõ. Tạo issue bằng GraphQL `createIssue` với `parentIssueId` + `projectV2Ids`: mỗi issue 1 request vừa tạo, vừa gắn sub-issue, vừa thêm vào Project. Số issue được dự đoán trước để body ghi sẵn `#số` phụ thuộc |
| **Chấm SWP** | `tkm:sun-estimate` (swp-matrix-v2) + `tkm:confidence` + agent `sun-estimate-worker` | Gọi `/tkm:sun-estimate <URL Project>`. Làm đúng các bước của skill: preflight `tool_policy.py` trước mỗi lần đọc GitHub (chỉ query) → `selection.py` (258 việc lá, 90 container) → `orchestration.py` (5 lô) → worker chấm → `sun_estimate.py validate/select/calibrate/render`. Prompt worker = rubric của skill (bảng Scope/Complexity, ma trận 6×6, enum, signature, luật chống đếm trùng) + 3 dòng bối cảnh dự án (stack, màn nào đã có code, màn L1 chưa có thiết kế) + lô issue dạng JSON. Thêm 1 luật từ lỗi của lần chạy thử: "discipline Unknown thì confidence phải low". Issue mẫu: agent hỏi người kiểm từng issue một, 2 lượt (mức khó → điểm), có lựa chọn "chấp nhận cả 5" |
| **Quy giờ** | Agent chính, script `plan-sprints.py` | Prompt: "chọn cách quy giờ giải thích được, áp nhất quán". Agent đề xuất neo hệ số vào issue mẫu đã duyệt (ước trực tiếp 4 issue → 3,7 h/SWP → 4 h/SWP), loại #348 khỏi phép neo và nói rõ lý do. Năng lực 56h/người/sprint lấy từ 7h/ngày của template LAB-1 × hệ số tập trung 0,8 |
| **Xếp sprint** | Agent chính, `plan-sprints.py` | Xếp tham lam theo ưu tiên → thứ tự epic → phụ thuộc (kể cả phụ thuộc kế thừa từ issue cha), không vượt 56h/người/sprint, giao lại cho người cùng nhóm vai trò khi người gốc đã kín. Kết quả ghi đè owner trong backlog để body issue và trường Owner thống nhất |
| **Giả lập sprint + báo cáo tiến độ** | Agent chính, `sprint1-simulation.py`, `build-doc-vars.py` | Agent viết kịch bản trạng thái cuối Sprint 1 (Done kèm ngày, In Review/In Progress/Blocked kèm lý do), script kiểm kịch bản phủ đúng 37 issue của Sprint 1. Mọi số trong `progress-report.md`/`estimate.md` (bảng trạng thái, burndown, tổng theo epic, so LAB-1, truy vết 237 mã) do script sinh từ dữ liệu, không gõ tay |
| **Ghi SWP lên Project bằng Agent** | Skill tự viết `github-backlog-sync` (`sync-backlog.py set` + `verify`) | Sau khi người kiểm chốt 5 mẫu, file `values-swp.json` lấy **nguyên** `finalSWP` trong payload đã validate của skill (không tính lại). Agent gọi GraphQL `updateProjectV2ItemFieldValue` cho từng issue lá (trường **SWP** chỉ chứa SWP; giờ ghi trường **Estimate (h)** riêng), rồi chạy `verify`: đọc ngược toàn bộ item bằng GraphQL và so với file; kết quả 258/258 issue lá khớp (cùng lần đọc ngược: Estimate (h) 258/258, Owner 348/348, Sprint 220/220, Status 348/348, Done date 26/26). Cùng cách cho Estimate (h), Owner, Sprint, Status, Done date (sim) |

## 2. Review output của AI

**Con người review ở các bước:** (1) chọn trục epic, cách dùng Phụ lục B, phạm vi 41 màn; (2) **dừng lần chạy đầu** vì "backlog chưa sát LAB-4" → làm lại từ đầu, xoá Project cũ, đổi tên repo cũ; (3) duyệt 5 issue mẫu của skill, kể cả lượt hỏi lại riêng #348; (4) chọn cách xử lý repo cũ.

| # | Vấn đề trong output AI | Phát hiện bằng cách | Xử lý |
|---|---|---|---|
| 1 | Lần chạy đầu: backlog do AI tự chia (63 issue), không truy được về block ④/⑦ và Phụ lục B của LAB-4 | Người dùng review và dừng | Làm lại: epic theo màn, mỗi issue ghi mã Phụ lục B, script kiểm phủ 237/237 |
| 2 | Lần chạy đầu: AI coi PREMISE của LAB-4 (viết sau ngày nộp) là một phần bản nộp | Hỏi lại người dùng | Coi là góp ý review → 5 dòng R-01…R-05 trong PREMISE |
| 3 | 129 sub-issue của 43 màn E14 có body gần như giống hệt nhau → worker sẽ chấm cả 43 màn bằng nhau | Agent đọc lô input trước khi giao worker | Bổ sung mô tả chức năng LAB-1 của từng màn vào body, cập nhật lên GitHub rồi mới chấm |
| 4 | Worker lô 1 bỏ sót 2 issue (#16 RLS, #137) | Script gộp đối chiếu input/output từng lô | Chạy 1 lô sửa đúng 2 issue (worker contract cho phép 1 lần sửa) |
| 5 | 18 dòng ghi mảng signature sai thứ tự từ vựng | Script kiểm trước khi chạy validator | Sắp lại theo thứ tự (không đổi nội dung/điểm), ghi caveat trong report |
| 6 | Lần chạy thử: worker cho discipline `Unknown` nhưng confidence `high` → validator từ chối | `sun_estimate.py validate` | Thêm luật vào prompt worker của lần chạy chính |
| 7 | Worker gắn `legacy-unknown` cho một việc hỏi khách (#137) | Đọc output | Giữ điểm (main agent không được sửa trục ngoài bước hiệu chỉnh), ghi chú ở `estimate.md` §1 |
| 8 | AI đánh giá #348 hạ tầng AWS = 10 SWP, thấp xa LAB-1 (8 MM) | So với LAB-1 trước khi chốt | Hỏi lại người kiểm; người kiểm giữ 10 → ghi lý do + rủi ro R-04 |
| 9 | Kế hoạch team 5 người của AI không chứa nổi backlog (BE-2 1.280h so với 504h năng lực) | Script tính tải theo owner | Sửa giả định A-01 thành 9 người, cân tải trong nhóm vai trò; phần vẫn vượt (38 issue) đưa thành rủi ro R-03 |
| 10 | Backlog thiếu khai báo phụ thuộc #56 → RPC `allocate_order` | Lộ ra khi giả lập Sprint 1 | Bổ sung phụ thuộc, rủi ro R-06 |
| 11 | Đoạn nhận xét burndown AI viết trước khi có số bị sai số (ghi "chậm ~10 SWP", thực tế 26–30; "Blocked 15 SWP", thực tế 7) | Đối chiếu với bảng sinh từ dữ liệu | Thay bằng biến lấy từ dữ liệu |
| 12 | Một agent trung chuyển bị dừng giữa chừng khi chép prompt dài sang worker (lô 3) | Báo cáo của agent | Tách lô 3 làm đôi (26 + 26 issue) và chạy lại |
| 13 | GitHub tự thêm sub-issue vào Project khi issue cha đã ở trong Project → lệnh thêm lặp báo lỗi "already exists" | Lỗi khi chạy script | Script đọc danh sách item có sẵn trước, bắt lỗi "already exists" |

## 3. Điểm đặc biệt trong cách dùng AI

**Chỗ tin là hiệu quả**
- **Truy vết máy kiểm được:** backlog là dữ liệu + script kiểm phủ 237 mã Phụ lục B, nên khi đổi cấu trúc (lần 2) biết ngay mã nào mất chủ. Cách này dùng lại được cho LAB-6 khi spec đổi.
- **Số liệu không gõ tay:** mọi bảng trong estimate/progress-report sinh từ payload của skill + plan + kịch bản sprint. Lỗi số trong đoạn văn AI viết trước (mục 2, #11) bị bắt nhờ có bảng sinh tự động đặt cạnh.
- **1 request/issue** (GraphQL `createIssue` có `parentIssueId` + `projectV2Ids`): 348 issue + quan hệ sub-issue + thêm vào Project xong trong 1 lần chạy, số issue khớp dự đoán 348/348, không vướng giới hạn tạo nội dung của GitHub (lần chạy đầu dùng `gh issue create` + lệnh gắn riêng thì cần 3 lượt request).
- **Người chỉ quyết ở chỗ cần quyết** (trục epic, phạm vi, issue mẫu); phần lặp (chấm 258 issue, ghi field, đọc ngược kiểm) để agent làm.

**Chỗ chưa tốt, cần cải thiện khi làm thật**
- **Hiệu chỉnh 5 mẫu không chạm được nhóm đáng ngờ:** 5 issue engine giờ lái (4 SWP mỗi cái) không thuộc nhóm nào có issue mẫu nên không được kiểm. Khi làm thật nên chạy thêm 1 lượt `tkm:sun-estimate` với ref chỉ định cho nhóm rủi ro cao (≤5 issue thì skill hỏi cả nhóm).
- **Chi phí token của worker:** worker của skill không có tool nên lô 52 issue phải dán nguyên vào prompt (~30–40KB); phải dùng agent trung chuyển và một lần bị dừng giữa chừng. Lần sau chia lô nhỏ hơn (~25 issue) ngay từ đầu.
- **Hệ số giờ neo trên 4 issue:** đủ cho bài lab, chưa đủ khi làm thật. Cần đo giờ thật 2–3 sprint rồi chỉnh hệ số (trường Estimate (h) giữ để so).
- **Sprint giả lập do AI viết kịch bản:** trạng thái/lý do chặn là giả định có lý, không phải dữ liệu thật; báo cáo ghi rõ là giả lập.
- **E14 (43 màn chưa thiết kế) có độ tin cậy thấp:** điểm của 129 sub-issue là ước theo pattern; cần chấm lại sau khi sub-issue thiết kế của từng màn xong.
