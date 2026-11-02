# Báo cáo thảo luận Lab 01 - IT3180

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- Cấu hình `--global` được lưu tại tệp `~/.gitconfig` (trên Windows: `C:\Users\<Tên_User>\.gitconfig`). Áp dụng cho toàn bộ repository của user trên máy tính.
- Cấu hình `--local` được lưu tại `.git/config` trong từng repository cụ thể, chỉ có hiệu lực với repo đó và có độ ưu tiên cao hơn cấu hình global.

## 2. Vì sao dùng `git mv`?
- `git mv` vừa di chuyển/đổi tên file trên đĩa vừa tự động đưa thao tác đổi tên vào Staging Area (chỉ mục).
- Giúp Git nhận diện rõ ràng đây là hành động Đổi tên (Renamed) chứ không phải Xóa tệp cũ + Thêm tệp mới, qua đó bảo toàn trọn vẹn toàn bộ lịch sử commit trước đây của tệp khi dùng lệnh `git log --follow`.

## 3. `release/lab01` có phải baseline?
- Có. `release/lab01` đóng vai trò là một Baseline cấu hình phần mềm (phiên bản chuẩn đã được kiểm tra, review qua PR và thống nhất đóng băng tại mốc nộp bài Lab 01). Nhánh này sẽ không nhận thêm commit phát triển mới nào nữa, ngoại trừ các bản vá hotfix sau này nếu có.

## 4. Vì sao không commit thẳng master dù làm một mình?
- Rèn luyện kỷ luật quản lý cấu hình (SCM): Mọi thay đổi đều được phân nhánh độc lập, có mục đích rõ ràng.
- Giữ cho nhánh `master` luôn luôn sạch sẽ, ổn định và chạy được bất kỳ lúc nào.
- Thao tác qua Pull Request giúp dễ dàng rà soát tổng thể những gì đã thay đổi (Files changed) trước khi hợp nhất.