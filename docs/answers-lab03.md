# Báo cáo thảo luận Lab 03 - IT3180

## 1. Merge base là gì?
- **Merge base** là commit tổ tiên chung gần nhất (best common ancestor) giữa hai nhánh trong đồ thị lịch sử Git (commit DAG).
- Git sử dụng commit merge base này làm mốc so sánh trong thuật toán Three-way Merge (Hợp nhất ba chiều). Khi hợp nhất hai nhánh, Git sẽ so sánh trạng thái của cả hai nhánh so với merge base để tự động tích hợp các thay đổi và phát hiện các vị trí xung đột (nếu hai nhánh cùng sửa một dòng code tính từ merge base).

## 2. Vì sao trên nhánh `master` và `release/*` phải dùng `revert` thay vì `reset`?
- Lệnh `git reset` thay đổi vị trí trỏ của con trỏ nhánh và viết lại lịch sử commit. Nếu commit đã được đẩy lên nhánh công khai (như `master`, `release/*`), việc reset sẽ khiến lịch sử bị đứt đoạn, gây lỗi cho các thành viên khác khi kéo mã nguồn về và vi phạm nguyên tắc SCM.
- Lệnh `git revert` tạo ra một commit mới để đảo ngược lại nội dung của một commit trước đó mà không làm mất hay thay đổi bất kỳ commit nào trong quá khứ. Do đó, toàn bộ lịch sử phát triển vẫn được bảo toàn trọn vẹn và an toàn tuyệt đối cho các nhánh dùng chung.
