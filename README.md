# Yuki Cold Logistics — 食品コールドチェーン業務支援システム · Backlog LAB-5

**Mã học viên:** le-duy · **Đề:** Product B (ràng buộc đặc thù: giới hạn giờ lái xe tải từ 2024 — 改善基準告示)

## Tổng quan

- Backlog break từ bộ **LAB-4 nộp ngày 27/09/2026** (screen spec 17 màn + 2 màn con, architecture, 6 ADR, database diagram). Góp ý review LAB-4 lấy từ bản PREMISE của LAB-4 viết lại ngày 24/10/2026.
- [PREMISE.md](PREMISE.md) **có thay đổi** so với LAB-4: 5 dòng theo góp ý review (R-01…R-05), 8 dòng chỗ hở tự phát hiện khi break (P-01…P-08), 11 giả định (A-01…A-11), 6 hướng đã chốt (H-01…H-06).
- **15 epic**, 136 issue, 197 sub-issue (258 việc lá được chấm SWP). Epic đi theo màn hình LAB-4; mỗi issue ghi mã Phụ lục B (237 mục) nó xử lý.
- Sprint giả lập đã chạy: **Sprint 1** (giả lập 2026-11-30 → 2026-12-11). Sprint 2–9 đã xếp trên trường Sprint, chưa chạy.

## Link

| | |
|---|---|
| Repo | https://github.com/duyl-2064/aidd-for-sdm-lab5 |
| GitHub Project | [https://github.com/users/duyl-2064/projects/2](https://github.com/users/duyl-2064/projects/2) |
| Báo cáo HTML của skill chấm SWP | [swp-report/sun-estimate-yuki-lab5-project2-20261024-1647.html](swp-report/sun-estimate-yuki-lab5-project2-20261024-1647.html) |

**Kiểm tra truy cập không đăng nhập (24/10/2026):** gửi request HTTP không cookie/token tới repo, `README.md`, file báo cáo HTML, Project và issue #98 — cả 6 link trả HTTP 200, Project hiện đúng tiêu đề.
Cách xem báo cáo HTML: GitHub hiện file `.html` dưới dạng mã nguồn → bấm **Download raw file** rồi mở bằng trình duyệt (file tự chứa, không gọi mạng).

- [x] Chủ repo đã mở thử repo + Project bằng cửa sổ ẩn danh (điền ngày): 24/10/2026

## Cấu trúc repo

| File / thư mục | Nội dung |
|---|---|
| `README.md` | File này: tổng quan, link, cấu trúc, bảng spec → epic |
| `PREMISE.md` | Backlog khác LAB-4 ở đâu: spec thêm/bỏ/sửa, giả định bổ sung, hướng đã chốt |
| `task-breakdown.md` | Nguyên tắc chia task + DoD, bảng spec → issue, truy vết đủ 237 mục Phụ lục B, hạng mục chịu ràng buộc giờ lái 2024, chỗ hở của spec LAB-4 |
| `estimate.md` | Issue mẫu skill chọn và kết quả kiểm, cách quy ra giờ, tổng theo epic, so với estimate LAB-1 |
| `progress-report.md` | Báo cáo tiến độ sau Sprint 1: trạng thái, burndown, rủi ro trễ |
| `AI-report.md` | Skill và prompt đã dùng, cách review output AI, điểm làm tốt/chưa tốt |
| `swp-report/` | Báo cáo HTML do skill `tkm:sun-estimate` xuất |
| `skills/github-backlog-sync/` | Skill tự viết: tạo issue + sub-issue + thêm vào Project bằng GraphQL, ghi SWP/giờ/Status/Sprint từ file đã review, đọc ngược để kiểm |

## Spec → epic

| Spec (mã/file LAB-4 hoặc dòng PREMISE) | Epic trên Project | Ghi chú |
|---|---|---|
| ADR-01, ADR-02, ADR-06; §6 cross-cutting; migration 0002/0008/0009 | [#1](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/1) — Nền kỹ thuật & DB dùng chung | Nền cho mọi màn |
| SCR-000, SCR-001 | [#23](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/23) — 共通レイアウト・ログイン | |
| SCR-002 | [#28](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/28) — ダッシュボード | |
| SCR-003, SCR-004 | [#32](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/32) — 入荷一覧・入荷検品 | Kiểm nhiệt khi nhập dùng ngưỡng có version (BR-TEMP) |
| SCR-005 | [#46](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/46) — 在庫・ロット照会 | |
| SCR-006, SCR-007, SCR-008; ADR-03; migration 0004 | [#51](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/51) — 出荷指示・引当・日付逆転 | 日付逆転 chặn mặc định (H-05) |
| SCR-009, SCR-017; migration 0006 | [#65](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/65) — 出荷検品・出荷前チェック | Nhiệt xe/hàng theo ngưỡng có version |
| SCR-010 | [#77](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/77) — 納品確認（POD） | |
| SCR-011 | [#85](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/85) — 温度アラーム | |
| SCR-012 | [#94](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/94) — SKU・顧客・契約マスタ (tra cứu) | |
| SCR-014, SCR-014-1, SCR-014-2; ADR-05; PREMISE R-05, P-05, P-06 | [#98](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/98) — ★ ルート計画・拘束時間チェック | **Ràng buộc đặc thù: giờ lái 2024** — 12 ràng buộc, chặn 公開 |
| SCR-015; migration 0007 | [#127](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/127) — ★ 予期し得ない事象・遵守記録 | **Ràng buộc đặc thù: giờ lái 2024** — chỉ trừ C04/C08/C10 |
| SCR-016; ADR-04; migration 0003, 0005 (phần rule); PREMISE P-07 | [#138](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/138) — 温度帯閾値・ルール版管理 | Tab ドライバー規則 thuộc ràng buộc giờ lái 2024; tab 温度帯 thuộc ngưỡng nhiệt |
| PREMISE R-01 (43 màn LAB-1) | [#157](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/157) — Màn LAB-1 chưa có detail design | `needs-design`, mỗi màn: thiết kế → BE → FE |
| PREMISE R-02 (IF, migration, NFR) | [#330](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/330) — Tích hợp, migration dữ liệu, NFR | `needs-design` |
