# Báo cáo thảo luận Lab 02 - IT3180

## 1. Vì sao phải đồng bộ master trước khi gửi PR?
- Để phát hiện và xử lý sớm xung đột mã nguồn (merge conflict) ngay trên môi trường local của lập trình viên, thay vì để xung đột xảy ra trên remote/PR.
- Đảm bảo mã nguồn trên nhánh tính năng được kiểm thử tích hợp (integration test) với trạng thái mới nhất của `master`, tránh gây hỏng bản build khi được gộp vào `master`.

## 2. Khi nào không được rebase?
- Theo "Quy tắc vàng của Rebase": **Tuyệt đối không rebase trên các nhánh công khai/nhánh chung (shared branches)** như `master`, `main`, `release/*` hoặc nhánh đang có nhiều người cùng phối hợp làm việc.
- Việc rebase sẽ viết lại lịch sử commit (tạo ra các mã SHA mới), khiến cho lịch sử của các lập trình viên khác bị phân kỳ (diverged) và gây xung đột nghiêm trọng.

## 3. `feature/*` khác `topic/*` ra sao?
- Nhánh `feature/*`: Dùng cho việc phát triển các **tính năng nghiệp vụ phần mềm** cụ thể của dự án (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- Nhánh `topic/*`: Dùng cho các chủ đề ngắn hạn không phải tính năng cốt lõi của người dùng cuối, thường là việc phụ trợ như: cấu hình template, tài liệu kỹ thuật, sơ đồ phân tích hoặc thử nghiệm kỹ thuật (ví dụ: `topic/pr-template`, `topic/use-case-diagram`).