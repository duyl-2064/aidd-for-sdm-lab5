# Task breakdown — từ detail design LAB-4 sang backlog trên GitHub Project

Nguồn break: bộ LAB-4 nộp 27/09/2026 + các thay đổi khai ở [PREMISE.md](PREMISE.md). Project: [https://github.com/users/duyl-2064/projects/2](https://github.com/users/duyl-2064/projects/2).
Quy mô: **15 epic · 136 issue · 197 sub-issue** (258 việc lá được chấm SWP).

## 1. Nguyên tắc chia task

### Trục chia

Epic đi theo **màn hình của screen spec LAB-4** (13 epic E02–E13 cho 17 màn + 2 màn con), cộng 1 epic nền dùng chung (E01: migration, ADR-01/02/06, RBAC…), 1 epic cho 43 màn LAB-1 chưa có detail design (E14, PREMISE R-01) và 1 epic cho tích hợp/migration/NFR chưa thiết kế (E15, PREMISE R-02). Nhờ vậy mỗi issue truy về đúng block của màn: ④ (action) cho chức năng, ⑦ / Phụ lục B cho chỗ prototype lệch RFP.

### Độ hạt — chia tới đâu thì dừng

| Cấp | Là gì | Dừng chia khi |
|---|---|---|
| Epic (`type:epic`) | Một màn/nhóm màn LAB-4, hoặc E01/E14/E15 | Không chấm điểm; SWP = tổng con |
| Issue (`type:feature` hoặc `type:task`) | Một kết quả kiểm được của màn: một action ④, một RPC, một nhóm ràng buộc, một nhóm mục ⑦ cùng chỗ sửa | Một người làm xong trong **≤ 3 ngày**, chạm **1 tầng** → để `type:task`, không tách nữa |
| Sub-issue (`type:task`) | Lát cắt của issue theo tầng (DB/RPC, API, UI, test) hoặc theo bước (thiết kế → BE → FE ở E14/E15) | Luôn là lá; ≤ 3 ngày, 1 người |

Tách issue thành sub-issue khi có **một trong ba** điều kiện:
1. Issue chạm từ 2 tầng trở lên và mỗi tầng một người phụ trách (ví dụ [#38](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/38): server tính nhiệt / FE hiển thị ngưỡng).
2. Ước tính vượt 3 ngày.
3. Một phần phải chờ khách, phần còn lại làm được ngay (ví dụ [#123](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/123): làm rõ số dư đầu kỳ tách khỏi công cụ import).

Không tách "viết code / viết test" — test nằm trong DoD của issue. Ngoại lệ: golden test TS↔SQL của engine 引当 ([#55](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/55)) do QA làm, chạy trong CI riêng.

Engine giờ lái (E11) **chia theo nhóm ràng buộc** chứ không theo action: mỗi nhóm có cách tính riêng (theo ngày, rolling 2 ngày/2 tuần, liên tục, tháng/năm) và bộ case biên riêng.

Mỗi màn LAB-4 có **1 issue làm rõ** (BrSE) nhận các mục "Hỏi khách / Chưa xác định / Giả định" của màn đó trong Phụ lục B. Mục "Khác RFP / Khác thiết kế / Rủi ro / Lỗi" luôn gán vào issue sửa cụ thể.

Màn E14 (chưa có thiết kế) dùng **pattern cố định 3 sub-issue**: `[Thiết kế]` theo khuôn ①–⑦ của LAB-4 → `[BE]` bảng/RPC/API + RLS → `[FE]` màn theo loại thiết bị (PC / 共有端末 / PWA).

### Định nghĩa xong (DoD chung, áp cho mọi issue lá)

- [ ] Có người phụ trách (trường Owner) và tiêu chí nghiệm thu (ô DoD riêng) **trước khi** vào sprint — theo luật quản trị của RFP: việc chưa có owner và tiêu chí nghiệm thu thì không đưa vào sprint
- [ ] Code merge qua PR, có 1 người review khác người viết
- [ ] CI xanh: typecheck, lint, unit/golden test, pgTAP ([#5](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/5))
- [ ] Migration có up và down, chạy được trên DB có seed LAB-3
- [ ] Thay đổi dữ liệu nghiệp vụ có event trong `event_log` (actor, correlation_id, rule_version_id nếu có)
- [ ] Message đúng nguyên văn và mã V-nn trong spec LAB-4; message mới thêm vào Phụ lục C
- [ ] Màn mới/sửa kiểm bàn phím, focus, contrast (WCAG 2.2 AA mục tiêu)
- [ ] Mọi mã Phụ lục B ghi trong issue đã xử lý xong hoặc ghi rõ còn chờ gì
- [ ] Đủ các ô DoD riêng ghi trong issue

Issue cha (feature, epic) xong khi mọi con xong và ô DoD riêng của cha đạt.

### Cách dùng epic → issue → sub-issue trên Project

- Cha–con dùng **sub-issue thật của GitHub**; cột "Parent issue" và "Sub-issues progress" trên Project hiện tiến độ của cha.
- Nhãn: `type:*`, tầng (`db`, `api`, `ui`, `engine`, `infra`, `test`, `clarify`), ưu tiên `P0/P1/P2`, `constraint:driver-hours-2024`, `constraint:temp-zone`, `needs-design`.
- Trường Project: Status (Todo / In Progress / In Review / Blocked / Done), Sprint (Iteration), SWP (number — chỉ ghi SWP đã review), Estimate (h), Owner (giả định), Priority, Ràng buộc đặc thù, Done date (sim).
- SWP và giờ chỉ ghi ở **issue lá**. Issue cha/epic để trống trên trường; tổng xem ở `estimate.md` và report HTML (cha = tổng con).
- Repo cá nhân chỉ gán được chủ repo nên Assignee là `duyl-2064`; người phụ trách giả định nằm ở trường **Owner (giả định)**.
- Body mỗi issue ghi: mục tiêu, spec LAB-4/PREMISE, phạm vi, DoD, mã Phụ lục B xử lý, phụ thuộc (#số), owner, ưu tiên.

## 2. Spec → issue

| Spec (LAB-4) | Epic | Issue / sub-issue | Phần spec chưa thành issue và vì sao |
|---|---|---|---|
| SCR-000 共通レイアウト | [#23](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/23) | [#24](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/24), [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25); RBAC nền [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14) | — |
| SCR-001 ログイン | [#23](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/23) | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25), [#26](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/26), [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27); audit đăng nhập [#12](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/12) | SSO/MFA thật thuộc IdP ([#331](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/331)); quên mật khẩu/đăng ký: không làm vì đăng nhập sẽ qua IdP |
| SCR-002 ダッシュボード | [#28](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/28) | [#29](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/29), [#30](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/30), [#31](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/31); JST [#17](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/17) | Badge realtime (Q-SCR-000-12): làm polling theo quyền ở [#24](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/24), không làm realtime vì RFP không đòi |
| SCR-003 入荷一覧 | [#32](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/32) | [#33](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/33), [#34](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/34), [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Tạo appointment (G-1, G-2) → màn L1-SCR-102 [#186](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/186) |
| SCR-004 入荷検品 | [#32](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/32) | [#35](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/35) ([#36](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/36), [#37](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/37)), [#38](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/38) ([#39](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/39), [#40](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/40)), [#41](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/41) ([#42](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/42), [#43](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/43)), [#44](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/44), [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | 受入/拒否/保留 (G-6) → [#190](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/190); 一時温度帯 (G-7) → [#210](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/210); release 隔離 (G-14 phần màn) → [#226](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/226) |
| SCR-005 在庫・ロット照会 | [#46](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/46) | [#47](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/47), [#48](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/48), [#49](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/49), [#50](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/50) | Lịch sử move lot (⑦#5) → [#206](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/206) |
| SCR-006 出荷指示一覧 | [#51](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/51) | [#58](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/58), [#63](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/63), [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64); window theo hợp đồng [#8](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/8) | Tạo/sửa đơn (⑦#1) → [#234](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/234); điều kiện giao (⑦#3) → [#79](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/79) |
| SCR-007 出荷指示詳細・引当 | [#51](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/51) | [#52](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/52), [#53](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/53) ([#54](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/54), [#55](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/55), [#56](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/56)), [#57](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/57), [#58](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/58), [#63](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/63); seed [#18](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/18) | Gom picking task (⑦#14) → [#242](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/242) |
| SCR-008 日付逆転アラート | [#51](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/51) | [#59](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/59) ([#60](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/60), [#61](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/61)), [#62](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/62), [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Mail khi có alert: RFP không yêu cầu, không làm |
| SCR-009 出荷検品 | [#65](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/65) | [#67](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/67), [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76); scan/xe/seal/nhiệt chuyển sang SCR-017 ([#68](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/68), [#71](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/71), [#74](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/74)) | Gom task theo zone (Q-SCR-009-12) → [#242](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/242) |
| SCR-010 納品確認 POD | [#77](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/77) | [#78](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/78), [#79](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/79) ([#80](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/80), [#81](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/81)), [#82](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/82), [#83](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/83), [#84](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/84) | Hàng đợi offline PWA (phần offline của Q-SCR-010-03) → [#258](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/258) |
| SCR-011 温度アラーム | [#85](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/85) | [#86](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/86), [#87](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/87) ([#88](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/88), [#89](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/89)), [#90](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/90), [#91](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/91), [#92](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/92), [#93](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/93) | Màn 逸脱ケース (Q-SCR-011-04) → [#274](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/274); bảng deviation có ở [#143](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/143) |
| SCR-012 SKU・顧客・契約マスタ | [#94](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/94) | [#95](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/95), [#96](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/96), [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97); EXCLUDE [#8](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/8); audit master [#11](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/11) | CRUD master (Q-SCR-012-08) → [#162](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/162), [#166](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/166), [#170](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/170) |
| SCR-014 ルート計画・拘束時間チェック | [#98](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/98) | [#99](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/99)…[#112](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/112), [#121](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/121)…[#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | VRP tối ưu tuyến: option ngoài giá (LAB-1, ADR-05) |
| SCR-014-1 版履歴 | [#98](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/98) | [#115](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/115) ([#116](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/116), [#117](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/117)) | — |
| SCR-014-2 itinerary | [#98](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/98) | [#118](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/118) ([#119](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/119), [#120](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/120)) | iOS: bỏ theo PREMISE R-04 |
| SCR-015 予期し得ない事象・遵守記録 | [#127](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/127) | [#128](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/128)…[#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | — |
| SCR-016 温度帯閾値・ルール版管理 | [#138](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/138) | [#139](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/139)…[#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Override ngưỡng theo vị trí (ADR-04 câu 2): chưa có yêu cầu RFP, chỉ hỏi ở [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) |
| SCR-017 出荷前チェック | [#65](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/65) | [#66](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/66), [#68](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/68)…[#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Tách `loaded`/`dispatched` (G-SCR-017-01): giữ gộp `shipped` theo LAB-4 |
| ADR-01 stack + module | [#1](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/1) | [#2](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/2), [#5](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/5) | Hạ tầng AWS production → [#346](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/346) |
| ADR-02 引当/xác nhận nguyên tử | [#51](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/51), [#32](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/32), [#65](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/65), [#77](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/77) | [#53](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/53), [#35](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/35), [#75](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/75), [#78](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/78) | — |
| ADR-03 日付逆転 | [#51](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/51) | [#57](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/57), [#59](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/59), [#62](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/62) | — |
| ADR-04 rule version + fail-closed | [#138](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/138) | [#139](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/139), [#144](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/144), [#150](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/150) | — |
| ADR-05 engine 改善基準告示 | [#98](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/98), [#127](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/127) | [#107](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/107)…[#112](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/112), [#122](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/122), [#128](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/128)…[#134](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/134) | 2人乗務/隔日勤務/フェリー/分割休息: G-SCR-014-11, Yuki không có ở bản đầu |
| ADR-06 audit | [#1](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/1) | [#10](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/10), [#21](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/21), [#22](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/22) | Partition `event_log` theo năm: chỉ khi > 50M dòng |
| §6 cross-cutting | [#1](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/1) | [#13](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/13), [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14), [#17](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/17), [#19](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/19), [#20](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/20) | — |
| `04_database` §7 migration 0002–0009 | nhiều | 0002 [#6](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/6) · 0003 [#139](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/139), [#86](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/86) · 0004 [#52](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/52) · 0005 [#99](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/99), [#150](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/150) · 0006 [#66](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/66) · 0007 [#128](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/128) · 0008 [#16](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/16) · 0009 [#21](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/21) | Đổi qty sang numeric (Đ-18): LAB-4 xếp "chấp nhận ở prototype" |
| §5 điểm tích hợp | [#85](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/85), [#98](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/98), [#1](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/1), [#330](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/330) | IF-LOG-01 [#87](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/87) · IF-MAP-01 [#106](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/106) · IF-MAIL-01 [#20](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/20) · IF-IDP-01 [#331](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/331) · IF-ERP-01 [#334](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/334) · IF-ARCH-01 [#337](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/337) | — |
| 43 màn LAB-1 ngoài LAB-4 (PREMISE R-01) | [#157](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/157) | [#158](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/158)…[#326](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/326), mỗi màn 3 sub-issue | — |

### Truy vết đủ 237 mục Phụ lục B

Mỗi mã nằm ở đúng một issue (cột Issue). "Sửa" = issue thay đổi code/DB; "Làm rõ" = issue BrSE gửi khách.

<details><summary><b>SCR-000</b> — 14 mục (7 sửa, 7 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-000-01 | Chưa xác định | Thời hạn session / tự đăng xuất (cấu hình Supabase Auth) | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-000-02 | Chưa xác định | Có cần hộp thoại xác nhận trước khi ログアウト | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-000-03 | Chưa xác định | Ngưỡng hiển thị badge ("99+") — code không giới hạn | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-000-04 | Chưa xác định | Xử lý user có trong Auth nhưng chưa có dòng profiles | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-000-05 | Chưa xác định | Menu cho màn mới SCR-014…017 chưa có | [#24](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/24) | Làm rõ |
| Q-SCR-000-06 | Chưa xác định | Mã FR/ACC cụ thể của RFP cho auth/layout | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-000-07 | Khác RFP | Không RBAC: 11 mục menu cho mọi role; RLS/API chỉ kiểm tra đã đăng nhập (NFR-SEC-02) | [#24](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/24) | Sửa |
| Q-SCR-000-08 | Khác RFP | Không có màn quản trị user/role | [#158](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/158) | Sửa |
| Q-SCR-000-09 | Khác thiết kế | /api/** chưa đăng nhập bị redirect HTML thay vì 401 JSON | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25) | Sửa |
| Q-SCR-000-10 | Khác thiết kế | PUBLIC_PATHS so bằng startsWith("/login") | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25) | Sửa |
| Q-SCR-000-11 | Khác RFP | Không audit đăng nhập/đăng xuất (event_log chỉ bảng nghiệp vụ) | [#12](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/12) | Sửa |
| Q-SCR-000-12 | Khác RFP | Badge đếm toàn hệ thống, không realtime, không theo phạm vi phụ trách | [#24](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/24) | Sửa |
| Q-SCR-000-13 | Khác thiết kế | Layout redirect /login không kèm next (middleware kèm) | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25) | Sửa |
| Q-SCR-000-14 | Giả định | Chỉ Supabase email/password, không IdP/SSO (Q-04 LAB-1) | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |

</details>

<details><summary><b>SCR-001</b> — 12 mục (6 sửa, 6 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-001-01 | Chưa xác định | Chính sách mật khẩu, khóa tài khoản, MFA, thời hạn session (cấu hình Supabase Auth) | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-001-02 | Chưa xác định | Không có パスワードを忘れた / đổi mật khẩu / đăng ký | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-001-03 | Chưa xác định | Message trình duyệt cho required/type=email phụ thuộc locale | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-001-04 | Chưa xác định | Danh sách lỗi Supabase có thể xuất hiện ở V04 | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-001-05 | Hỏi khách | Yêu cầu IdP/SSO (Q-04 LAB-1, Yuki chưa chốt) | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-001-06 | Giả định | Đăng nhập email/password Supabase, không IdP/SSO | [#27](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/27) | Làm rõ |
| Q-SCR-001-07 | Khác thiết kế | V04 ghép lỗi tiếng Anh của Supabase vào câu JP | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25) | Sửa |
| Q-SCR-001-08 | Khác thiết kế | Nhận diện lỗi bằng chuỗi "Invalid" | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25) | Sửa |
| Q-SCR-001-09 | Khác thiết kế | next chỉ kiểm tra bắt đầu "/", chưa loại "//host" (open-redirect mức thấp) | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25) | Sửa |
| Q-SCR-001-10 | Khác RFP | Không audit đăng nhập thành công/thất bại | [#12](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/12) | Sửa |
| Q-SCR-001-11 | Khác RFP | Không khóa tài khoản/CAPTCHA/MFA trong code | [#26](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/26) | Sửa |
| Q-SCR-001-12 | Khác thiết kế | Gợi ý "デモアカウントは README.md を参照してください。" chỉ cho prototype | [#25](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/25) | Sửa |

</details>

<details><summary><b>SCR-002</b> — 14 mục (9 sửa, 5 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-002-01 | Chưa xác định | Ngưỡng "3 ngày" K3 hard-code; ngưỡng cảnh báo 賞味期限 theo khách (Q-05 LAB-1) chưa chốt | [#31](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/31) | Làm rõ |
| Q-SCR-002-02 | Chưa xác định | Giới hạn 8 đơn / 6 lot hard-code, không xem thêm/phân trang | [#31](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/31) | Làm rõ |
| Q-SCR-002-03 | Chưa xác định | KPI theo RFP (tra lot ≤60s, POD sửa <2%, alarm review trễ <1%, chênh kho, HACCP) có cần tr… | [#31](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/31) | Làm rõ |
| Q-SCR-002-04 | Chưa xác định | Tần suất làm mới / realtime | [#31](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/31) | Làm rõ |
| Q-SCR-002-05 | Chưa xác định | Phạm vi dữ liệu theo vai trò/khu vực | [#31](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/31) | Làm rõ |
| Q-SCR-002-06 | Khác thiết kế | Lệch múi giờ: today JST, in3 UTC, days_remaining theo DB → 0:00–9:00 JST lệch 1 ngày | [#17](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/17) | Sửa |
| Q-SCR-002-07 | Khác thiết kế | K3 (status=available, expiry ∈ [today,in3]) khác điều kiện lọc SCR-005 ?expiring=3 (days_r… | [#29](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/29) | Sửa |
| Q-SCR-002-08 | Khác thiết kế | K4 (available/hold) khác SCR-005 ?expiring=expired (days_remaining<0, mọi status) | [#29](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/29) | Sửa |
| Q-SCR-002-09 | Khác thiết kế | T1 không lọc trạng thái: 取消/納品済 vẫn hiện | [#30](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/30) | Sửa |
| Q-SCR-002-10 | Khác thiết kế | Nhãn 期限区分 ở T2 hard-code thay vì EXPIRY_LABEL | [#30](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/30) | Sửa |
| Q-SCR-002-11 | Khác thiết kế | 入荷検品待ち chỉ là text, không link | [#30](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/30) | Sửa |
| Q-SCR-002-12 | Khác thiết kế | T2 không có trạng thái rỗng | [#30](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/30) | Sửa |
| Q-SCR-002-13 | Khác RFP | Chỉ KPI đếm; không có 12 báo cáo/HACCP レポート (FR-RPT) | [#310](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/310) | Sửa |
| Q-SCR-002-14 | Khác RFP | Không phân quyền: mọi role cùng KPI (NFR-SEC-02) | [#29](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/29) | Sửa |

</details>

<details><summary><b>SCR-003</b> — 11 mục (6 sửa, 5 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| SCR-003 G-1 | Khác RFP | Không có chức năng tạo 入荷 appointment (FR-REC-01) — không nút, không API POST inbound | [#186](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/186) | Sửa |
| SCR-003 G-2 | Khác RFP | Thiếu cột ETA giờ, 車両温度帯, 仕入先参照コード | [#186](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/186) | Sửa |
| SCR-003 G-3 | Khác RFP | Không filter / tìm kiếm / phân trang; toàn bộ inbound render | [#33](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/33) | Sửa |
| SCR-003 G-4 | Khác RFP | Phân quyền mock, page không kiểm role | [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14) | Sửa |
| SCR-003 G-5 | Khác RFP | Trạng thái 取消 có enum/nhãn nhưng không có API/nút hủy | [#34](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/34) | Sửa |
| SCR-003 G-6 | Rủi ro | Lỗi DB bị nuốt (data ?? []) | [#33](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/33) | Sửa |
| Q-SCR-003-01 | Chưa xác định | Không giới hạn số hàng / không phân trang | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-003-02 | Chưa xác định | Không có message khi bảng rỗng | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-003-03 | Chưa xác định | Không có khóa sort thứ 2 khi trùng planned_date | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-003-04 | Chưa xác định | Không có cách tạo phiếu nhập mới (chỉ seed) | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-003-05 | Hỏi khách | Tên màn: mã gọi 入荷一覧, h1 trong code 入荷・入荷検品 | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |

</details>

<details><summary><b>SCR-004</b> — 23 mục (15 sửa, 8 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| SCR-004 G-1 | Khác RFP | Ngưỡng nhiệt hard-code FE ZONE_RANGE frozen [−25,−15] / chilled [0,5] / ambient [5,25] ≠ B… | [#38](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/38) | Sửa |
| SCR-004 G-2 | Khác RFP | Không version ngưỡng theo 有効日; không lưu 版 vào inbound_line/lot | [#38](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/38) | Sửa |
| SCR-004 G-3 | Khác RFP | 温度帯乖離 không block 入庫確定, không tạo 逸脱; API không kiểm nhiệt | [#38](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/38) | Sửa |
| SCR-004 G-4 | Khác RFP | Không so SKU温度帯 vs 位置温度帯; Q-01 chilled nhận cả lot 冷凍/常温 NG | [#38](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/38) | Sửa |
| SCR-004 G-5 | Khác RFP | Thiếu trường FR-REC-02 (梱包状態, 写真, 期限タイプ nhập tay, ロット/期限 sửa được); 受入温度 không bắt buộc | [#41](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/41) | Sửa |
| SCR-004 G-6 | Khác RFP | Không có 受入/拒否/保留 + 理由コード (FR-REC-03) | [#190](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/190) | Sửa |
| SCR-004 G-7 | Khác RFP | Không có 一時温度帯 / 理由 / 承認 | [#210](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/210) | Sửa |
| SCR-004 G-8 | Khác RFP | Idempotency chỉ dựa lot_no unique; song song → 500; lot_no trùng phiếu khác → mất tồn kho … | [#35](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/35) | Sửa |
| SCR-004 G-9 | Khác RFP | inbound_line ghi đè tại chỗ, không sự kiện đảo/version (DR-LOT-01) | [#41](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/41) | Sửa |
| SCR-004 G-10 | Khác thiết kế | Không atomic (check 2 UPDATE; complete SELECT→INSERT→UPDATE không transaction); lỗi UPDATE… | [#35](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/35) | Sửa |
| SCR-004 G-11 | Khác RFP | Phân quyền mock; không lưu completed_by; người kiểm = người xác nhận được (NFR-SEC-02) | [#44](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/44) | Sửa |
| SCR-004 G-12 | Khác RFP | Không lưu ルールバージョン / correlationID trên giao dịch | [#10](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/10) | Sửa |
| SCR-004 G-13 | Lỗi logic | cancelled không bị chặn ở 入庫確定 | [#35](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/35) | Sửa |
| SCR-004 G-14 | Khác RFP | NG vẫn tạo lot qty = 実数, không có màn release 隔離中 | [#226](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/226) | Sửa |
| SCR-004 G-15 | Khác thiết kế | Mã Q-01 ghi cứng trong notice | [#40](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/40) | Sửa |
| Q-SCR-004-01 | Chưa xác định | Thứ tự chọn vị trí đầu tiên cùng dải: select * không order by | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-004-02 | Chưa xác định | Không có vị trí cách ly/cùng dải → lot location_id = null, không lỗi | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-004-03 | Chưa xác định | Đơn vị 実数 (sku.unit) không hiển thị | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-004-04 | Chưa xác định | Độ chính xác 受入温度: DB numeric(5,2), FE step 0.1 | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-004-05 | Chưa xác định | line_id không thuộc phiếu → trả ok, không sửa gì | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-004-06 | Chưa xác định | Người xác nhận nhập kho không được lưu | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-004-07 | Chưa xác định | Không có luồng tạo cancelled; Mode B với 取消 chưa kiểm chứng | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |
| Q-SCR-004-08 | Chưa xác định | fetch throw không được bắt → busy kẹt, nút khóa tới khi reload | [#45](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/45) | Làm rõ |

</details>

<details><summary><b>SCR-005</b> — 15 mục (10 sửa, 5 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-005-01 | Chưa xác định | Timezone Postgres cho current_date (残日数) — có thể lệch 1 ngày với ngày JST ở header | [#50](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/50) | Làm rõ |
| Q-SCR-005-02 | Chưa xác định | Hành vi khi > 200 lot khớp (không phân trang, không thông báo cắt) | [#50](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/50) | Làm rõ |
| Q-SCR-005-03 | Chưa xác định | Ý nghĩa và luồng vào/ra trạng thái 保留 (hold) — không màn/API nào đặt/gỡ | [#50](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/50) | Làm rõ |
| Q-SCR-005-04 | Chưa xác định | Có hiện trạng thái đơn / ngày giao trong card 有効な引当 không | [#50](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/50) | Làm rõ |
| Q-SCR-005-05 | Hỏi khách | operator có được xem 納品履歴 (tên khách) không | [#50](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/50) | Làm rõ |
| SCR-005 ⑦#1 | Khác RFP | Thiếu filter 仕入先 / 位置 / 期限タイプ (FR-INV-06) | [#47](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/47) | Sửa |
| SCR-005 ⑦#2 | Khác RFP | Không có 倉庫権限, RLS select = true (FR-INV-06, NFR-SEC-02) | [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14) | Sửa |
| SCR-005 ⑦#3 | Khác RFP | 残日数 theo ngày DB, không theo 納品日 (BR-DELWIN-01, BR-EXP-02) | [#17](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/17) | Sửa |
| SCR-005 ⑦#4 | Khác RFP | Lot 消費期限 quá hạn vẫn 引当可, không tự chuyển 隔離/廃棄, không exception event (BR-EXP-02, FR-INV-… | [#48](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/48) | Sửa |
| SCR-005 ⑦#5 | Khác RFP | Không có lịch sử move / trạng thái lot (FR-INV-03, FR-INV-05) | [#206](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/206) | Sửa |
| SCR-005 ⑦#6 | Khác thiết kế | q không escape, select không validate, lỗi DB bị nuốt | [#47](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/47) | Sửa |
| SCR-005 ⑦#7 | Khác RFP | Limit 200, không phân trang / sort (FR-INV-06) | [#47](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/47) | Sửa |
| SCR-005 ⑦#8 | Khác thiết kế | Card 有効な引当 không link SCR-007, không hiện status / 納品日 | [#47](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/47) | Sửa |
| SCR-005 ⑦#9 | Khác thiết kế | Khối chi tiết chỉ hiện khi gõ đúng lot_no, hẹp hơn sub-header | [#47](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/47) | Sửa |
| SCR-005 ⑦#10 | Khác RFP | Không có xuất CSV / báo cáo truy vết (KPI S1-03) | [#49](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/49) | Sửa |

</details>

<details><summary><b>SCR-006</b> — 10 mục (7 sửa, 3 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-006-01 | Chưa xác định | Cách tạo 出荷指示 (FR-OUT-01): nguồn đơn thật (file 受注 16:00, ERP) | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-006-02 | Chưa xác định | Cần filter/tìm kiếm (ngày giao, khách, trạng thái), phân trang? | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-006-03 | Chưa xác định | Ý nghĩa vận hành của shipped 出荷済 / cancelled 取消 (không có luồng đặt) | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| SCR-006 ⑦#1 | Khác RFP | Không có chức năng tạo/sửa dòng đơn, không xử lý lỗi master / trùng tham chiếu (FR-OUT-01) | [#234](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/234) | Sửa |
| SCR-006 ⑦#2 | Khác RFP | 納品時間帯 từ master khách, không theo contract customer-SKU (BR-DELWIN-01) | [#8](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/8) | Sửa |
| SCR-006 ⑦#3 | Khác RFP | Không có điều kiện giao, tham chiếu, route / 積み込み順序 (FR-OUT-01, FR-OUT-03) | [#79](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/79) | Sửa |
| SCR-006 ⑦#4 | Khác thiết kế | Không filter / phân trang; đơn hôm nay không nổi bật | [#63](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/63) | Sửa |
| SCR-006 ⑦#5 | Khác RFP | 引当数 < 指示数 không cảnh báo (FR-OUT-02 gián tiếp) | [#58](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/58) | Sửa |
| SCR-006 ⑦#6 | Khác thiết kế | 判断済 gộp cả alert reallocated của đơn đã về 未引当 | [#63](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/63) | Sửa |
| SCR-006 ⑦#7 | Khác RFP | Không phân quyền, mọi role thấy mọi đơn (NFR-SEC-02) | [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14) | Sửa |

</details>

<details><summary><b>SCR-007</b> — 21 mục (15 sửa, 6 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-007-01 | Chưa xác định | Cách tạo đơn / dòng đơn và điều kiện giao (車上渡し / 軒先渡し) — không có trong code | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-007-02 | Chưa xác định | Xử lý shortage sau 引当: backorder, hủy dòng, hay chờ nhập rồi 引当 bổ sung? | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-007-03 | Chưa xác định | Có cho phép 引当 thủ công (chọn lot tay, có lý do) không? | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-007-04 | Chưa xác định | Timezone tính "số ngày còn lại" (UTC midnight trên app) so với ngày DB — lệch ±1 ngày | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-007-05 | Chưa xác định | Ý nghĩa lot 保留 (hold) trong 引当 — bị loại bước 3 「ステータス hold」 | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-007-06 | Chưa xác định | min_remaining_days = 0: ngưỡng 0 nhưng note log hiển thị theo ratio (?? vs truthy) | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| SCR-007 ⑦#1 | Khác RFP (FR-OUT-02 原子的) | Không nguyên tử: ghi tuần tự 5 bảng, lỗi giữa chừng không rollback | [#53](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/53) | Sửa |
| SCR-007 ⑦#2 | Khác RFP (FR-OUT-02 over-allocation) | Optimistic lock không chặn: 0 dòng update không báo lỗi → over-allocate cùng lot | [#53](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/53) | Sửa |
| SCR-007 ⑦#3 | Khác RFP (べき等) | Không idempotency key; chặn duy nhất = status draft | [#53](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/53) | Sửa |
| SCR-007 ⑦#4 | Khác RFP (BR-DELWIN-01) | Bước 4 chỉ kiểm 残存日数; không đối chiếu 納品時間帯 / route / 拘束時間 | [#57](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/57) | Sửa |
| SCR-007 ⑦#5 | Khác RFP (BR-EXP-02) | 消費期限 = 納品日 (còn 0 ngày) vẫn qua bước 1; mốc so sánh là 納品日 | [#57](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/57) | Sửa |
| SCR-007 ⑦#6 | Khác RFP (BR-EXP-02, FR-INV-05) | Không exception event bất biến; step_log không lưu khi 0 pick | [#52](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/52) | Sửa |
| SCR-007 ⑦#7 | Khác RFP (BR-DATE-01) | RFP chặn 日付逆転, prototype cho override có alert; bước 5 tô đỏ dù lot được dùng | [#57](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/57) | Sửa |
| SCR-007 ⑦#8 | Khác RFP (FR-OUT-02) | Đơn luôn 引当済 kể cả thiếu / 0 lot; shortage không lưu DB | [#58](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/58) | Sửa |
| SCR-007 ⑦#9 | Khác RFP (NFR-SEC-02) | Mọi user chạy 引当; không tách người khởi tạo / duyệt | [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14) | Sửa |
| SCR-007 ⑦#10 | Khác RFP (BR-TEMP-02) | Bước 2 chỉ so dải danh nghĩa, không đọc 温度アラーム open | [#57](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/57) | Sửa |
| SCR-007 ⑦#11 | Khác thiết kế (chất lượng) | step_log seed "selected" là chuỗi → s.selected.join lỗi render | [#18](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/18) | Sửa |
| SCR-007 ⑦#12 | Khác thiết kế (seed) | Bẫy T4 L-C-010 status hold → bị loại bước 3, không phải bước 4 | [#18](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/18) | Sửa |
| SCR-007 ⑦#13 | Khác thiết kế (bảo trì) | Tính lại hợp đồng / lần giao trên app thay vì active_contract() / last_delivered_expiry() | [#53](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/53) | Sửa |
| SCR-007 ⑦#14 | Khác RFP (FR-OUT-03) | Không picking task theo khu / route / 積み込み順 | [#242](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/242) | Sửa |
| SCR-007 ⑦#15 | Khác thiết kế (UX) | Thang 6 bước chỉ lấy step_log của allocation active đầu tiên; 引当 bổ sung → mất log lần 2 | [#54](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/54) | Sửa |

</details>

<details><summary><b>SCR-008</b> — 10 mục (6 sửa, 4 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-008-01 | Khác RFP / Hỏi khách | BR-DATE-01 là 日付逆転禁止, prototype cho override có lý do | [#59](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/59) | Sửa |
| Q-SCR-008-02 | Khác RFP | Không tách 起票者/承認者, không RBAC (NFR-SEC-02) | [#59](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/59) | Sửa |
| Q-SCR-008-03 | Khác RFP | Cancel không transaction, không kiểm lỗi, không optimistic lock (FR-OUT-02) | [#62](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/62) | Sửa |
| Q-SCR-008-04 | Khác thiết kế | Nhãn 再引当 nhưng không tự 引当 lại; lot không chuyển hold → vòng lặp alert | [#62](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/62) | Sửa |
| Q-SCR-008-05 | Chưa xác định | Phạm vi hủy 引当 (theo lot / dòng / đơn); alert dòng khác vẫn open | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-008-06 | Khác thiết kế | Không kiểm outbound_order.status khi judge | [#59](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/59) | Sửa |
| Q-SCR-008-07 | Chưa xác định / Hỏi khách | Bằng chứng override (đính kèm, 2 cấp duyệt), maxLength, confirm | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-008-08 | Chưa xác định | Bảng lịch sử thiếu order_no, 判断者, 判断日時; không màn event_log | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-008-09 | Chưa xác định / Hỏi khách | Filter/phân trang/CSV/thông báo/SLA xử lý alert | [#64](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/64) | Làm rõ |
| Q-SCR-008-10 | Khác thiết kế | Cancel có thể để dữ liệu nửa vời (alert reallocated, allocation vẫn active) | [#62](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/62) | Sửa |

</details>

<details><summary><b>SCR-009</b> — 12 mục (9 sửa, 3 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-009-01 | Khác RFP | Không barcode / không quét lot, SKU (FR-OUT-04) | [#71](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/71) | Sửa |
| Q-SCR-009-02 | Khác RFP | Không có 車両・シール (FR-OUT-04/05) | [#74](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/74) | Sửa |
| Q-SCR-009-03 | Khác RFP | Không kiểm 温度帯 SKU/vị trí/thực đo (BR-TEMP-02) | [#68](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/68) | Sửa |
| Q-SCR-009-04 | Khác RFP | Không có 積み込み確認, không set shipped | [#75](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/75) | Sửa |
| Q-SCR-009-05 | Khác thiết kế | API tin result từ client | [#67](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/67) | Sửa |
| Q-SCR-009-06 | Chưa xác định / Hỏi khách | Xử lý sau NG (đổi lot, 引当 bổ sung, partial ship, ai duyệt) | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-009-07 | Khác RFP | Không transaction / optimistic lock (FR-OUT-02) | [#67](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/67) | Sửa |
| Q-SCR-009-08 | Khác RFP | Không RBAC / tách vai (NFR-SEC-02) | [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14) | Sửa |
| Q-SCR-009-09 | Chưa xác định | 再検品 không giới hạn, không lịch sử, không nút vào lại khi picking | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-009-10 | Chưa xác định / Hỏi khách | Giới hạn 実数; danh mục NG理由 chuẩn | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-009-11 | Khác thiết kế | Notice NG màu ok; V09 lộ enum tiếng Anh | [#67](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/67) | Sửa |
| Q-SCR-009-12 | Khác RFP | Không gom task theo zone/route (FR-OUT-03) | [#242](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/242) | Sửa |

</details>

<details><summary><b>SCR-010</b> — 11 mục (8 sửa, 3 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-010-01 | Khác RFP / Hỏi khách | BR-POD-01: không phân nhánh 車上渡し / 軒先渡し, không 配送条件 | [#79](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/79) | Sửa |
| Q-SCR-010-02 | Khác RFP | FR-OUT-06: không ảnh/chữ ký/GPS/mã ngoại lệ | [#79](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/79) | Sửa |
| Q-SCR-010-03 | Khác RFP | Không offline queue / hash / custody; không chống trùng revision | [#78](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/78) | Sửa |
| Q-SCR-010-04 | Khác RFP / Hỏi khách | Không luồng sửa POD → không đo KPI PP-05 | [#82](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/82) | Sửa |
| Q-SCR-010-05 | Khác RFP / Hỏi khách | Ai đăng ký POD; RBAC; role driver | [#83](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/83) | Sửa |
| Q-SCR-010-06 | Khác thiết kế | Không transaction (5 lệnh rời) | [#78](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/78) | Sửa |
| Q-SCR-010-07 | Khác RFP | Không có thao tác tạo shipped; nhảy picked → delivered | [#75](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/75) | Sửa |
| Q-SCR-010-08 | Chưa xác định / Hỏi khách | signed_at / delivered_at = giờ đăng ký web, không phải giờ giao thực | [#84](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/84) | Làm rõ |
| Q-SCR-010-09 | Chưa xác định / Hỏi khách | Lot → 出荷済 khi qty_available=0 (có thể sớm); không ghi qty vào 納品履歴 | [#84](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/84) | Làm rõ |
| Q-SCR-010-10 | Chưa xác định | Không kiểm picking NG; lịch sử POD không sort/revision/người ghi; mất dữ liệu khi rời màn | [#84](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/84) | Làm rõ |
| Q-SCR-010-11 | Khác thiết kế | Message lộ enum tiếng Anh / Postgres thô / tooltip trình duyệt | [#83](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/83) | Sửa |

</details>

<details><summary><b>SCR-011</b> — 12 mục (9 sửa, 3 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-011-01 | Khác RFP / Hỏi khách | Ngưỡng hard-code trên sensor, không policy version 有効日 (BR-TEMP-01); seed khác policy RFP | [#90](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/90) | Sửa |
| Q-SCR-011-02 | Khác RFP | Không ingest CSV (hash, idempotent, 15'/lần) (FR-TEMP-01, BR-HACCP-01) | [#87](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/87) | Sửa |
| Q-SCR-011-03 | Khác RFP | Không engine đánh giá; alarm không có first/last/peak/duration, không gắn lot (FR-TEMP-02) | [#90](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/90) | Sửa |
| Q-SCR-011-04 | Khác RFP | Không HACCP record / deviation case / cách ly lot; thiếu investigated/closed (FR-TEMP-04) | [#274](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/274) | Sửa |
| Q-SCR-011-05 | Khác thiết kế / Hỏi khách | エスカレーション xử lý giống 確認済; không thông báo/người nhận | [#92](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/92) | Sửa |
| Q-SCR-011-06 | Giả định (Q-01) / Hỏi khách | Mốc SLA 15' = imported_at | [#93](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/93) | Làm rõ |
| Q-SCR-011-07 | Khác RFP | Không báo cáo quản lý; hiển thị mốc tuyệt đối thay vì thời gian còn lại; không real-time (… | [#92](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/92) | Sửa |
| Q-SCR-011-08 | Khác RFP | Không RBAC; không hiển thị reviewed_by (NFR-SEC-02) | [#92](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/92) | Sửa |
| Q-SCR-011-09 | Chưa xác định / Hỏi khách | 確認メモ có bắt buộc (escalation / quá hạn)? | [#93](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/93) | Làm rõ |
| Q-SCR-011-10 | Chưa xác định | Filter/phân trang; cột bổ sung; alarm dưới min có tạo không | [#93](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/93) | Làm rõ |
| Q-SCR-011-11 | Khác thiết kế | Ghi đè khi 2 người cùng xác nhận; không message lỗi UI; V04 dùng chung | [#92](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/92) | Sửa |
| Q-SCR-011-12 | Khác thiết kế | Đọc toàn bộ reading để lấy mới nhất — không dùng được với 2,5M reading | [#86](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/86) | Sửa |

</details>

<details><summary><b>SCR-012</b> — 17 mục (10 sửa, 7 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-012-01 | Chưa xác định | Màn CRUD master / tạo phiên bản / ai duyệt (DR-MST-01) | [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97) | Làm rõ |
| Q-SCR-012-02 | Chưa xác định | Có cần hiển thị/lọc theo is_active | [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97) | Làm rõ |
| Q-SCR-012-03 | Chưa xác định | Xử lý 2 phiên bản cùng cặp chồng lấn khoảng hiệu lực | [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97) | Làm rõ |
| Q-SCR-012-04 | Chưa xác định | Quy tắc làm tròn 残存日数 (code dùng ceil) | [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97) | Làm rõ |
| Q-SCR-012-05 | Chưa xác định | Lịch sử thay đổi / audit cho master | [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97) | Làm rõ |
| Q-SCR-012-06 | Chưa xác định | Dịch nhãn FEFO/FIFO sang JP hay giữ nguyên | [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97) | Làm rõ |
| Q-SCR-012-07 | Chưa xác định | Import master từ Excel/hệ thống cũ (migration 3 wave) | [#97](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/97) | Làm rõ |
| Q-SCR-012-08 | Khác RFP | Chỉ đọc, không CRUD/phiên bản mới qua UI (DR-MST-01, LAB-1 có màn マスタ編集) | [#162](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/162) | Sửa |
| Q-SCR-012-09 | Khác thiết kế | Tỷ lệ 0.334 ≠ 1/3; với 期間 540 ngày có thể lệch 1 ngày sau ceil | [#96](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/96) | Sửa |
| Q-SCR-012-10 | Khác thiết kế | floor tính từ shelf_life_days hiện tại của SKU, không chốt tại thời điểm ký | [#96](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/96) | Sửa |
| Q-SCR-012-11 | Khác thiết kế | Không kiểm tra chồng lấn / khoảng trống giữa 2 bản | [#8](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/8) | Sửa |
| Q-SCR-012-12 | Khác thiết kế | Bản tương lai hiển thị giống bản đã 失効 (đều mờ) | [#95](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/95) | Sửa |
| Q-SCR-012-13 | Khác thiết kế | Không lọc is_active | [#95](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/95) | Sửa |
| Q-SCR-012-14 | Khác RFP | 納品時間帯 chỉ hiển thị; engine 引当 bước 4 chưa đối chiếu route/ETA | [#95](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/95) | Sửa |
| Q-SCR-012-15 | Khác RFP | Master không có audit trail | [#11](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/11) | Sửa |
| Q-SCR-012-16 | Khác thiết kế | Không tìm kiếm/lọc/phân trang | [#95](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/95) | Sửa |
| Q-SCR-012-17 | Khác RFP | Không phân quyền: mọi role đọc toàn bộ điều khoản hợp đồng (NFR-SEC-02) | [#14](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/14) | Sửa |

</details>

<details><summary><b>SCR-014</b> — 18 mục (1 sửa, 17 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-014-01 | Hỏi khách | Đơn trạng thái nào được đưa vào route (RFP created→validated→allocated→picked→loaded→dispa… | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-02 | Hỏi khách | Yuki có 労使協定 (3,400h/年, 310h/月)? Cần bản/ngày ký cho labor_agreement_ref | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-03 | Hỏi khách | Có 宿泊を伴う長距離便 (≥450km) không? Không → ẩn B5 option và C05/C07-8h | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-04 | Hỏi khách | 始業/終業 tính từ đâu; số phút 点呼・積込 trước 出庫/sau 帰庫 (giả định 30/30) | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-05 | Hỏi khách | 運転時間 thực tế lấy từ デジタコ hay driver tự ghi 到着/出発 (I6)? | [#124](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/124) | Làm rõ |
| Q-SCR-014-06 | Hỏi khách | Migrate 拘束 tháng/năm trước go-live vào driver_work_record? Không → route đầu kỳ 評価不能 | [#124](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/124) | Làm rõ |
| Q-SCR-014-07 | Hỏi khách | Map service nào (IF-MAP-01)? Tọa độ khách/geocode; TTL cache 24h? | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-08 | Hỏi khách | Xe 2室 (nhiều 温度帯)? → bảng vehicle_zone, V04 theo tập | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-09 | Hỏi khách | 1 đơn tách lên 2 route/2 xe? Hiện 1 đơn = 1 stop | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-10 | Hỏi khách | Kênh thông báo driver khi 公開/変更 (IF-MAIL-01, push, hay chỉ SCR-014-2)? | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-11 | Hỏi khách | Cần in/xuất PDF itinerary thay 配車・ドライバー計画表 (R-05)? | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-12 | Hỏi khách | Ngoài 05:00–23:00 JST: chặn 公開 hay chỉ cảnh báo? | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-13 | Hỏi khách | Ai là 運送部門所有者 đánh giá slot vượt kế hoạch (D5)? Cần role transport_manager? | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-14 | Chưa xác định | C12 休日労働 ≤1回/2週 (driver-rules Unresolved #4) — encode hard constraint? | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-15 | Hỏi khách | Có 2人乗務／隔日勤務／フェリー／分割休息? Hiện không đưa vào | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| Q-SCR-014-16 | Hỏi khách | 所定労働時間/ngày (8h?) để tính 時間外 C01; xử lý 休憩 trong 拘束 | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| G-SCR-014-01..11 | Giả định | Đơn đủ điều kiện allocated/picking/picked (G-01); route_type unknown = nhánh chặt (G-02); … | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Làm rõ |
| P-SCR-014-1..5 | Khác prototype | Không có vehicle/driver/route; customer thiếu service_time_min/tọa độ; profiles.role thiếu… | [#99](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/99) | Sửa |

</details>

<details><summary><b>SCR-015</b> — 10 mục (1 sửa, 9 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-015-01 | Hỏi khách | Ai duyệt 予期し得ない事象 (運送部門責任者 là ai; có phải 配車担当 trưởng → cần role riêng)? | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| Q-SCR-015-02 | Hỏi khách | Có báo cáo 労働基準監督署 / retention bao lâu (DR-RET-01)? | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| Q-SCR-015-03 | Hỏi khách | Loại bằng chứng bắt buộc cứng theo loại sự kiện hay chỉ khuyến nghị (hiện chỉ 異常気象 cứng)? | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| Q-SCR-015-04 | Hỏi khách | Driver nhập từ mobile ngay khi xảy ra (offline queue như POD)? Hiện online | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| Q-SCR-015-05 | Hỏi khách | Có ghi nhận riêng 連続運転 4h30 (SA/PA満車)? Không phải 予期し得ない事象 → bảng ghi chú riêng hoặc bỏ | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| Q-SCR-015-06 | Hỏi khách | 遵守レポート tháng có khóa (締め) sau xác nhận? → status closed cho compliance_calc | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| Q-SCR-015-07 | Hỏi khách | Tự cảnh báo route ngày kế (SCR-014 C06/C07) dựa trên event approved? | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| Q-SCR-015-08 | Hỏi khách | 年度 bắt đầu tháng 4 hay 1 cho C01/C02/C09? | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| G-SCR-015-01..08 | Giả định | applies_to cố định 3 chỉ tiêu (G-01); gắn route_version cụ thể + rule_version snapshot (G-… | [#137](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/137) | Làm rõ |
| P-SCR-015-1..2 | Khác prototype | Không có driver/route/事象, chưa có bảng bất biến với trigger; không có storage đính kèm + h… | [#128](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/128) | Sửa |

</details>

<details><summary><b>SCR-016</b> — 13 mục (1 sửa, 12 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-016-01 | Hỏi khách | 3 dải nhiệt cố định (không thêm 「氷温」)? Thiết kế khóa 3 hàng | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-02 | Hỏi khách | Ngưỡng có khác theo SKU/位置 hay chỉ theo dải? Nếu cần → sku_threshold_override versioned | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-03 | Hỏi khách | Kích hoạt trong ngày (theo giờ) hay chỉ 00:00 JST? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-04 | Hỏi khách | Dải chồng nhau (V08) có cần chặn cứng? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-05 | Hỏi khách | Ai duyệt ドライバー規則版 (運送部門責任者)? Cần 2 cấp duyệt? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-06 | Hỏi khách | 労使協定 có sẵn? Hết hạn D'8 → tự tắt hay cảnh báo trước 30 ngày? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-07 | Hỏi khách | 年度開始月 = 4 hay 1 cho C01/C02/C03? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-08 | Chưa xác định | C12 休日労働 (driver-rules Unresolved #4): enabled mặc định true hay false? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-09 | Hỏi khách | Cần version cho 2人乗務/隔日勤務/フェリー/分割休息? → driver_rule_exception_module | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-10 | Hỏi khách | Ngưỡng sensor prototype có migrate thành TEMP_INITIAL (effective_from = go-live)? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| Q-SCR-016-11 | Hỏi khách | Khi luật đổi: admin sửa hàng hard + 出典 + 承認 — cần thêm 法務確認? | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| G-SCR-016-01..08 | Giả định | 1 version = trọn bộ (G-01); hiệu lực 00:00 JST, effective_from ≥ ngày mai (G-02); job kích… | [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) | Làm rõ |
| P-SCR-016-1..4 | Khác prototype | Ngưỡng lưu ở sensor.threshold_min_c/max_c không version/有効日/duyệt (P-1); temperature_alarm… | [#139](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/139) | Sửa |

</details>

<details><summary><b>SCR-017</b> — 14 mục (1 sửa, 13 làm rõ/giả định)</summary>

| Mã | Phân loại | Nội dung (tóm tắt) | Issue | Loại |
|---|---|---|---|---|
| Q-SCR-017-01 | Hỏi khách | RFP có loaded/dispatched riêng, prototype chỉ shipped — tách 積込確認 và 出荷確認 thành 2 bước/2 t… | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-02 | Hỏi khách | Đo 貨物温度 bằng cách nào (品温計 / hồng ngoại)? 1 điểm/đơn hay theo dải/ロット? | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-03 | Hỏi khách | 車両温度 lấy tay hay từ logger xe (IF)? | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-04 | Hỏi khách | Đơn nhiều dải trên xe 2室? Hiện chặn khi xe 1 dải ≠ bất kỳ dải nào của đơn | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-05 | Hỏi khách | Format barcode ラベル (GS1-128 AI 01/10/30 hay nội bộ)? | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-06 | Hỏi khách | NG nhiệt độ lúc xuất: lot tự quarantined hay chỉ block để quality quyết? Hàng đã lên xe có… | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-07 | Hỏi khách | 再測定: giữ scan lần trước hay scan lại toàn bộ? | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-08 | Hỏi khách | Số seal/xe; ai cấp seal (S1 driver nhận); đối chiếu seal khi POD (SCR-010)? | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-09 | Hỏi khách | 「制御された手入力」: 2 người (4-eyes) hay chỉ lý do + log? Hiện 2 người (V12) | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-10 | Hỏi khách | Thiết bị dùng chung 出荷口: phiên ngắn bao lâu, re-auth PIN/badge? (NFR-SEC-02) | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-11 | Hỏi khách | Ngưỡng 貨物温度 khác 車両温度 (cho phép lệch +2 °C khi 積込)? | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| Q-SCR-017-12 | Hỏi khách | 一時温度帯 (出荷票 D2) có áp dụng ở màn này? BR-TEMP-02 tách khỏi check; hiện không hỗ trợ | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| G-SCR-017-01..09 | Giả định | picked → shipped chỉ qua confirm_preship, POD nhận shipped, loaded/dispatched gộp (G-01); … | [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76) | Làm rõ |
| P-SCR-017-1..6 | Khác prototype | Không có bước 出荷前チェック — POD nhận picked/shipped → delivered, shipped chưa bao giờ set cho … | [#75](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/75) | Sửa |

</details>

## 3. Hạng mục chịu ràng buộc đặc thù của đề (Product B: giới hạn giờ lái xe tải từ 2024)

Mọi issue dưới đây có nhãn `constraint:driver-hours-2024`, trường "Ràng buộc đặc thù = Giờ lái 2024" và tiêu đề bắt đầu bằng ★. Tổng SWP và giờ của nhóm này tính riêng ở `estimate.md` §4.

| Ràng buộc | Issue | Vì sao tách riêng |
|---|---|---|
| Rule 改善基準告示 là dữ liệu có version, bind vào route lúc 公開, không hồi tố | [#150](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/150) ([#151](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/151), [#152](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/152)), [#153](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/153) ([#154](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/154), [#155](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/155)) | Luật có thể đổi và 労使協定 có thể nâng mức; viết lẫn vào màn route thì mỗi lần đổi luật phải sửa code route |
| Timeline 拘束 (点呼, 移動, サービス, 休憩) | [#107](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/107) | Đầu vào chung của mọi ràng buộc; sai ở đây thì 12 ràng buộc sai theo |
| 1日拘束 13/15/16h, 休息 11/9/8h (C04–C07) | [#108](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/108) | Theo ngày, cần record hôm trước, có ngoại lệ 長距離便 |
| 運転 2日平均 9h, 2週平均 44h (C08, C09) | [#109](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/109) | Rolling window, hay sai ở ranh giới tuần/tháng |
| 連続運転 4h, 中断 ≥10′ tổng ≥30′ (C10, C11) + 休憩自動挿入 | [#110](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/110) | Trả đúng khoảng vi phạm để tô đỏ; chèn nghỉ dựa trên kết quả này |
| Tháng/năm, 労使協定, 休日労働 (C01–C03, C12) | [#111](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/111) | Cần dữ liệu tích luỹ, có thông số theo thoả thuận lao động; C01 đang chờ khách (P-05) |
| Chặn 公開 khi 違反/評価不能 | [#112](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/112) ([#113](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/113), [#114](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/114)) | Điểm luật tác động vận hành: chặn sai thì giao hàng đứng, bỏ sót thì Yuki vi phạm luật |
| Route version bind rule version | [#116](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/116) | Nguyên tắc D5: rule mới không áp ngược cho route đã 公開 |
| Số liệu tuân thủ và số dư đầu kỳ | [#122](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/122), [#123](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/123) ([#124](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/124), [#125](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/125)) | Không có số dư thì từ ngày go-live mọi route bị chặn (P-06) |
| 予期し得ない事象 chỉ trừ C04/C08/C10, báo cáo tách 通常/事象 | [#127](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/127): [#128](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/128)…[#134](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/134) | Luật chỉ cho trừ 3 chỉ tiêu ngày; gộp với báo cáo thường thì không chứng minh được với cơ quan quản lý |
| Câu hỏi khách về giờ lái (労使協定, 長距離便, デジタコ…) | [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) | Câu trả lời đổi tham số rule, cần theo dõi riêng |

Ràng buộc nghiệp vụ thứ hai của đề là **ngưỡng 3 dải nhiệt có version** (BR-TEMP-01/02), nhãn `constraint:temp-zone`: [#139](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/139), [#147](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/147), [#38](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/38), [#68](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/68), [#90](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/90) và các issue làm rõ [#76](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/76), [#93](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/93), [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156).

## 4. Chỗ hở hoặc mâu thuẫn của spec LAB-4 phát hiện khi break

| Spec | Chỗ hở / mâu thuẫn | Xử lý |
|---|---|---|
| ADR-02 ↔ `04_database` §7 | ADR-02 có RPC `complete_inbound`, danh sách migration không có | Đã sửa thiết kế — PREMISE P-01 |
| `04_database` §7 (0004 ↔ 0006) | `register_pod` ở 0004 cần cột POD mà 0006 mới thêm | Đã sửa thiết kế — PREMISE P-02 |
| §6.2, `04_database` §5, ADR-06 | Ba tài liệu nói +3, +4, +5 cột cho `event_log` | Đã sửa thiết kế — PREMISE P-03 |
| §6.4 ↔ `04_database` §5 | Hai cơ chế idempotency khác nhau | Đã sửa thiết kế — PREMISE P-04 (hướng H-01) |
| SCR-014 G-02 ↔ PREMISE LAB-4 §3.2 | `route_type = unknown` + V12 trong spec màn, PREMISE chỉ có 2 giá trị | Đã sửa thiết kế — PREMISE R-05 |
| SCR-016 C01 + SCR-014 V17 | C01 cần dữ liệu 勤怠 hệ thống không có → luôn 評価不能 → chặn mọi route | Đã sửa thiết kế — PREMISE P-05; tạo issue làm rõ [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) |
| SCR-014 V14 + Q-SCR-014-06 | Thiếu lịch sử tháng/năm lúc go-live → chặn mọi route | Đã sửa thiết kế — PREMISE P-06; tạo issue làm rõ [#124](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/124) |
| `04_database` §7 (0003 ↔ 0006) | `deviation` ở 0006 nhưng 入荷 và 温度 cần trước | Đã sửa thiết kế — PREMISE P-07 |
| SCR-004 ②, SCR-010 ②, SCR-015 ② | Ba màn tự mô tả upload/hash riêng | Đã sửa thiết kế — PREMISE P-08 |
| Q-SCR-014-01 | Đơn ở trạng thái nào được đưa vào route | Giả định — PREMISE A-07 |
| Q-SCR-008-05 | Hủy 引当 theo lot, dòng hay đơn | Giả định — PREMISE H-02 |
| Q-13 (SCR-014/015/016) | Ai duyệt phía 運送部門 | Giả định — PREMISE A-09 |
| SCR-011 Q-SCR-011-06 / §7.2 G-A2 | SLA 15′ tính từ `imported_at` hay giờ đo | Để mở: LAB-4 đã giả định `imported_at`; đổi mốc chỉ sửa 1 cột trong [#91](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/91), câu hỏi ở [#93](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/93) |
| SCR-016 C05 + Q-SCR-014-03 | Yuki có 長距離便 hay không | Để mở: C05 có toggle mặc định tắt; khách trả lời chỉ đổi dữ liệu. Câu hỏi ở [#126](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/126) |
| ADR-04 câu 2 | Override ngưỡng theo vị trí | Để mở: RFP chưa yêu cầu; câu hỏi ở [#156](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/156) |
| SCR-011 Q-SCR-011-04 / FR-TEMP-04 | Có bảng `deviation` nhưng LAB-4 không có màn xử lý case tới `closed` | Đã sửa thiết kế — PREMISE R-01 (màn L1-SCR-604 vào backlog: [#274](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/274)) |
| SCR-012 Q-SCR-012-08 | LAB-4 chỉ có màn tra master, không có CRUD/duyệt bản mới | Đã sửa thiết kế — PREMISE R-01 ([#162](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/162), [#166](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/166), [#170](https://github.com/duyl-2064/aidd-for-sdm-lab5/issues/170)) |
