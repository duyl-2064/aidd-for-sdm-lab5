# Estimate — SWP đã review và số giờ ước lượng

**Báo cáo HTML của skill:** [swp-report/sun-estimate-yuki-lab5-project2-20261024-1647.html](swp-report/sun-estimate-yuki-lab5-project2-20261024-1647.html) — skill `tkm:sun-estimate` (Takumi extras v1.1.0, swp-matrix-v2), nguồn là chính Project [https://github.com/users/duyl-2064/projects/2](https://github.com/users/duyl-2064/projects/2), chạy ngày 24/10/2026.

Kết quả run: **258 việc lá** được chấm, 90 container (epic + issue cha) lấy tổng của con, không container nào `needs-breakdown`. Tổng **1000 SWP**, trạng thái hiệu chỉnh `accepted`. Độ tin cậy: 2 high · 208 medium · 48 low.

## 1. Issue mẫu skill chọn để kiểm

Skill chọn tất định 5 issue (nhỏ nhất, trung vị, lớn nhất, ngoại lệ, tin cậy thấp nhất) và hỏi từng issue 2 lượt (mức khó → điểm). Người kiểm chọn **chấp nhận cả 5**; riêng #348 được hỏi lại vì AI đề xuất sửa, người kiểm vẫn giữ.

| Issue | Skill chấm (Scope × Complexity → SWP) | Bạn chốt | Lý do |
|---|---|---|---|
| [#4](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/4) Rule ESLint cấm import chéo module | S1 × C0 → **1** | 1 (giữ) | Chỉ là cấu hình 1 rule có plugin sẵn + 1 bước CI; ước trực tiếp ~3h, khớp mức "rất dễ" |
| [#321](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/321) [FE] L1-SCR-803 HACCP月次パック | S2 × C1 → **3** | 3 (giữ) | 1 màn PC: chọn tháng, nút sinh pack, bảng lịch sử — đúng pattern màn danh sách của LAB-4 (SCR-003/SCR-006); ~12h. Issue này đại diện cho nhóm 25 issue FE cùng loại, giữ nguyên để không làm trôi cả nhóm khi chưa có thiết kế màn |
| [#348](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/348) [Thực hiện] Hạ tầng AWS Tokyo | S5 × C3 → **10** | 10 (giữ — quyết định của người kiểm) | AI đề xuất sửa lên 40 (S8 × C5): issue phủ 4 môi trường, Multi-AZ, PITR, Object Lock, Transfer Family, LAB-1 ước 8 MM, và vượt ngưỡng ≤ 3 ngày của nguyên tắc chia task. Người kiểm được hỏi lại riêng và chọn giữ 10. Cách theo dõi: chấm lại và tách issue sau khi sub-issue thiết kế [#347](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/347) xong; phần chênh với LAB-1 ghi thành rủi ro R-04 (`progress-report.md`) |
| [#16](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/16) Migration 0008 RLS theo role | S5 × C3 → **10** | 10 (giữ) | ~40 bảng × 6 role + pgTAP + chạy lại 13 màn; rủi ro khoá nhầm người dùng là thật. Ước trực tiếp ~40h, khớp 10 SWP × 4 h |
| [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) Làm rõ câu hỏi SCR-000/001 | S2 × C1 → **3** | 3 (giữ) | 12 câu hỏi, 1–2 vòng hỏi đáp + cập nhật PREMISE; ~8h. Confidence thấp vì phụ thuộc khách, đúng như skill gắn |

Vì không có điều chỉnh nào nên skill không lan điểm sang issue khác (0 dòng thay đổi).

**Chỗ AI chấm mà người kiểm thấy đáng ngờ nhưng không thuộc 5 mẫu** (ghi lại để theo dõi, không sửa điểm ngoài quy trình của skill):
- 5 issue engine giờ lái ([#107](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/107)…[#111](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/111)) chỉ 4 SWP mỗi cái. Logic rolling window có nhiều case biên luật định, dễ bị đánh giá thấp. Theo dõi bằng giờ thực tế ở Sprint 2–3.
- [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) (làm rõ SCR-015) bị worker gắn signature `legacy-unknown`, không hợp với một việc hỏi khách; điểm 3 SWP vẫn hợp lý.

## 2. Cách quy ra giờ

**Cách chọn:** quy ước đổi SWP ra giờ với **một hệ số cố định 4 giờ/SWP**, neo bằng các issue mẫu đã được người kiểm duyệt.

**Vì sao:** SWP đã chấm theo một thang chung cho 258 issue, nên một hệ số cố định giữ đúng tỉ lệ giữa các issue. Ước trực tiếp từng issue (258 lần) tốn công và lại đưa cảm tính vào, tức là đúng cái SWP sinh ra để tránh. Neo hệ số vào issue mẫu (đã có người kiểm) thay vì lấy từ dữ liệu lịch sử, vì dự án chưa có lịch sử giờ/SWP trên KPI Insight.

**Quy tắc cụ thể:**
1. Ước trực tiếp các issue mẫu đã duyệt: #4 = 3h (1 SWP), màn HACCP pack = 12h (3 SWP), làm rõ SCR-000/001 = 8h (3 SWP), RLS 0008 = 40h (10 SWP). Tổng 63h / 17 SWP = 3,7 h/SWP → **làm tròn 4 h/SWP**.
2. #348 (hạ tầng AWS) **không** dùng làm neo: ước trực tiếp (~400h+) lệch quá xa điểm đã chốt; giữ quy tắc chung (40h) và đưa phần chênh vào rủi ro.
3. **Giờ = SWP × 4**, áp cho mọi issue lá, không làm tròn thêm, không cộng hệ số riêng theo người.
4. Giờ là công của người phụ trách tới khi đạt DoD (code, unit/golden test, sửa sau review). **Không gồm** QA system test, PM, họp định kỳ — các phần này LAB-1 tính bằng hệ số riêng.
5. Issue cha/epic không ghi giờ trên Project; tổng = cộng giờ của lá.
6. Năng lực sprint tính cùng đơn vị: 10 ngày × 7h × hệ số tập trung 0,8 = **56h/người/sprint** (PREMISE A-01).

## 3. Tổng theo epic

| Epic | Số issue lá | Tổng SWP | Tổng giờ | Ghi chú |
|---|---|---|---|---|
| [#1](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/1) Nền kỹ thuật & DB dùng chung (ADR-01/02/06, migration 0002/0008/0009) | 17 | 79 | 316 | Nền dùng chung; LAB-1 tính trong hệ số/FUNC chung nên nhỏ hơn |
| [#23](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/23) SCR-000/001 共通レイアウト・ログイン | 4 | 14 | 56 |  |
| [#28](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/28) SCR-002 ダッシュボード | 3 | 8 | 32 |  |
| [#32](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/32) SCR-003/004 入荷一覧・入荷検品 | 10 | 36 | 144 |  |
| [#46](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/46) SCR-005 在庫・ロット照会 | 4 | 11 | 44 |  |
| [#51](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/51) SCR-006/007/008 出荷指示・引当・日付逆転 | 11 | 40 | 160 |  |
| [#65](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/65) SCR-009/017 出荷検品・出荷前チェック | 9 | 36 | 144 |  |
| [#77](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/77) SCR-010 納品確認（POD） | 6 | 21 | 84 |  |
| [#85](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/85) SCR-011 温度アラーム | 7 | 27 | 108 |  |
| [#94](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/94) SCR-012 SKU・顧客・契約マスタ (tra cứu) | 3 | 8 | 32 |  |
| [#98](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/98) ★ SCR-014/014-1/014-2 ルート計画・拘束時間チェック (giờ lái 2024) | 22 | 92 | 368 | ★ Ràng buộc giờ lái 2024 |
| [#127](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/127) ★ SCR-015 予期し得ない事象・遵守記録 (giờ lái 2024) | 8 | 30 | 120 | ★ Ràng buộc giờ lái 2024 |
| [#138](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/138) SCR-016 温度帯閾値・ルール版管理 (2 tab) | 13 | 41 | 164 | Tab ドライバー規則 thuộc ★ giờ lái; tab 温度帯 thuộc ngưỡng nhiệt |
| [#157](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/157) Màn LAB-1 chưa có detail design (43 màn, break theo pattern 17 màn LAB-4) | 129 | 493 | 1972 | needs-design: SWP confidence thấp (PREMISE A-11) |
| [#330](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/330) Tích hợp, migration dữ liệu, NFR chưa có detail design | 12 | 64 | 256 | needs-design; #348 hạ tầng giữ 10 SWP (xem §1) |
| **Tổng** | **258** | **1000** | **4000** | Số issue lá = issue không có con (được chấm); issue cha/epic = tổng con |

Ràng buộc đặc thù giờ lái 2024 (nhãn `constraint:driver-hours-2024`): **24 issue lá, 88 SWP, 352 giờ**. Ngưỡng nhiệt có version (`constraint:temp-zone`): 14 issue lá, 47 SWP, 188 giờ.

## 4. So với estimate LAB-1

LAB-1 (`[YCL] Product B - Effort Estimation`, sheet 01_Server) tính theo man-day BE + FE (Implement + FixBug + Unit Test), quy trình Normal; đổi ra giờ bằng 7h/ngày. Cột "LAB-1 AIDD" áp mức giảm của sheet Appendix (BE −35 %, FE −40 %) — đây là mô hình PREMISE LAB-4 §2 chọn làm cơ sở (H-06). Infra LAB-1 lấy từ 00_Summary (8 MM Normal / 5,6 MM AIDD, 1 MM = 140h) và tính vào E15. Không so QA, BrSE, Spec, PM vì LAB-5 không tách các phần đó thành issue (trừ issue làm rõ và thiết kế E14).

| Phần (epic) | LAB-1 Normal (h) | LAB-1 AIDD (h) | LAB-5 (h) | Chênh LAB-5 − LAB-1 AIDD | Vì sao |
|---|---|---|---|---|---|
| E01 Nền kỹ thuật & DB dùng chung (ADR-01/02/06, migration 0002/0008/0009) | 241 | 156 | 316 | +160 | LAB-5 tách nền (RBAC, audit, idempotency, JST, storage, mail, CI) thành issue riêng; LAB-1 chỉ có vài FUNC chung. PREMISE P-03, P-04, P-08 thêm việc |
| E02 SCR-000/001 共通レイアウト・ログイン | 33 | 21 | 56 | +35 | LAB-5 thêm hardening từ Phụ lục B (redirect, message, rate-limit) mà LAB-1 chưa biết |
| E03 SCR-002 ダッシュボード | 61 | 38 | 32 | -6 | LAB-4 đã có dashboard chạy thật (LAB-3), LAB-5 chỉ sửa 9 mục Phụ lục B; LAB-1 tính làm mới |
| E04 SCR-003/004 入荷一覧・入荷検品 | 189 | 119 | 144 | +25 | Prototype đã có 入荷検品; LAB-5 chỉ làm phần lệch RFP. Appointment/受入判定 tách sang E14 |
| E05 SCR-005 在庫・ロット照会 | 75 | 47 | 44 | -3 | Prototype đã có màn tra cứu; LAB-1 tính làm mới |
| E06 SCR-006/007/008 出荷指示・引当・日付逆転 | 302 | 195 | 160 | -35 | Prototype đã có engine 6 bước + test; LAB-5 port sang RPC và sửa luật thay vì làm mới |
| E07 SCR-009/017 出荷検品・出荷前チェック | 132 | 82 | 144 | +62 | LAB-5 nặng hơn: scan + nhập tay có duyệt + seal + 出荷確認 RPC (SCR-017 thiết kế chi tiết hơn LAB-1) |
| E08 SCR-010 納品確認（POD） | 80 | 51 | 84 | +33 | Gần bằng: POD đã có ở prototype, thêm điều kiện giao + revision |
| E09 SCR-011 温度アラーム | 203 | 130 | 108 | -22 | LAB-1 gồm cả framework CSV chung; LAB-5 dùng lại một phần ở E01 |
| E10 SCR-012 SKU・顧客・契約マスタ (tra cứu) | 0 | 0 | 32 | +32 | LAB-1 không có màn tra cứu master riêng (chỉ CRUD, nằm ở E14) |
| E11 ★ SCR-014/014-1/014-2 ルート計画・拘束時間チェック (giờ lái 2024) | 548 | 346 | 368 | +22 | Thấp hơn LAB-1 Normal, gần LAB-1 AIDD; engine chia theo nhóm ràng buộc, 5 issue engine chỉ 4 SWP (§1 — đáng ngờ, theo dõi) |
| E12 ★ SCR-015 予期し得ない事象・遵守記録 (giờ lái 2024) | 33 | 21 | 120 | +99 | LAB-5 cao hơn nhiều: thiết kế SCR-015 thêm bất biến, duyệt tách vai, 訂正版, báo cáo tách (PREMISE P-06 liên quan số dư) |
| E13 SCR-016 温度帯閾値・ルール版管理 (2 tab) | 175 | 112 | 164 | +52 | Gần bằng: 2 tab version + resolver; PREMISE P-07 dời bảng deviation vào đây |
| E14 Màn LAB-1 chưa có detail design (43 màn, break theo pattern 17 màn LAB-4) | 2527 | 1589 | 1972 | +383 | Cao hơn LAB-1 AIDD vì mỗi màn có thêm sub-issue thiết kế (BA-1) mà LAB-1 tính ở dòng Specification chứ không ở 01_Server (PREMISE R-01, A-11) |
| E15 Tích hợp, migration dữ liệu, NFR chưa có detail design | 1417 | 977 | 256 | -721 | Thấp hơn rất nhiều vì #348 hạ tầng giữ 10 SWP thay cho 8 MM của LAB-1 (§1, rủi ro R-04); PREMISE R-02 |
| **Tổng** | **6017** | **3884** | **4000** | **+116** | LAB-5 gần mô hình AIDD tổng thể; lệch lớn nằm ở E12 (tăng) và E15 (giảm) |
