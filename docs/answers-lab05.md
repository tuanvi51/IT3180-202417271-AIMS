# Báo cáo thảo luận Lab 05 - IT3180

## 1. Ưu, nhược điểm của Upstream First so với Release First?
- **Upstream First (sửa trên master trước rồi cherry-pick về nhánh release)**:
  - *Ưu điểm*: Đảm bảo mã nguồn trên nhánh chính (`master`) luôn nhận được bản sửa lỗi sớm nhất, loại trừ nguy cơ "quên" đưa bản vá về master gây lỗi hồi quy (regression) ở các bản phát hành tương lai. Đây là mô hình tiêu chuẩn được áp dụng rộng rãi tại Microsoft và các dự án mã nguồn mở quy mô lớn.
  - *Nhược điểm*: Quy trình phát hành bản vá nóng cho khách hàng có thể bị chậm trễ hơn vì phải vượt qua các bài kiểm thử và chính sách tích hợp trên master trước khi đưa về bản release.
- **Release First (sửa trên nhánh release bị lỗi trước rồi lan truyền sang master)**:
  - *Ưu điểm*: Tối ưu tốc độ phát hành bản vá khẩn cấp cho người dùng đang gặp sự cố trên phiên bản sản phẩm đang vận hành (hoặc bài đã nộp theo tuần).
  - *Nhược điểm*: Rất dễ bỏ sót việc lan truyền (propagate) bản vá về `master` hoặc các nhánh release song song khác nếu không có quy trình kiểm toán cấu hình chặt chẽ.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- Lệnh **`git cherry -v origin/release/lab05 origin/release/lab04`** (hoặc kiểm tra commit cherry-pick bằng `git log --all --grep "cherry picked from commit <FIX_SHA>"`).
- Khi chạy `git cherry -v`, nếu bản sửa lỗi chưa có trên nhánh đích, Git sẽ hiển thị tiền tố dấu cộng `+` trước mã SHA của commit sửa lỗi (chỉ thị commit này chưa có bản tương đương trên nhánh).
- Ngoài ra, vòng lặp kiểm tra tự động chạy trên 3 ref (`v1.0.1`, `v1.1.0`, `master`) sẽ trả về kết quả `0` (thất bại) trên nhánh bị quên sửa lỗi.
