# Báo cáo thảo luận Lab 04 - IT3180

## 1. Vì sao cần chuẩn bị phiên bản phát hành trên master trước mà không sửa trực tiếp trên nhánh release?
- Nhánh `release/*` có vai trò là đường phân nhánh để đóng băng phiên bản (baseline freeze) chuẩn bị bàn giao hoặc nộp bài. Nếu sửa các thông tin phát hành (cập nhật phiên bản, viết CHANGELOG) trực tiếp trên nhánh release, những thay đổi này sẽ bị tách biệt khỏi nhánh phát triển chính `master`, dẫn đến sự sai lệch (divergence) trong mã nguồn và master sẽ thiếu lịch sử hoàn chỉnh của bản release.
- Thực hiện chuẩn bị trên `master` trước đảm bảo toàn bộ mã nguồn, tài liệu và kiểm thử đã được rà soát đầy đủ và tích hợp hoàn chỉnh trước khi cắt nhánh release. Khi nhánh release được tạo ra từ master, nó đã ở trạng thái ổn định và sẵn sàng phát hành ngay lập tức.

## 2. Vì sao trong Release Flow của học phần, nhánh `release/*` không bao giờ merge ngược vào master? So sánh với GitFlow.
- **Trong Release Flow**: Nhánh `release/labXX` dùng để đánh dấu cột mốc nộp bài (baseline) và duy trì bảo trì phiên bản cũ độc lập. Mọi bản vá (hotfix) trên nhánh release sau đó được chọn lọc và lan truyền sang `master` bằng lệnh `git cherry-pick` (hoặc PR riêng). Việc không merge ngược cả nhánh release vào `master` giúp ngăn chặn việc kéo theo các cấu hình hoặc tệp chỉ thuộc về môi trường bàn giao cũ vào luồng phát triển mới.
- **So sánh với GitFlow**: Trong mô hình GitFlow, nhánh `release` khi đóng gói sẽ được merge đồng thời vào cả nhánh `main/master` (để release) và nhánh `develop` (để tiếp tục phát triển). Mô hình này cồng kềnh hơn vì đòi hỏi phải duy trì song song cả 2 nhánh vĩnh cửu (`main` và `develop`), trong khi Release Flow tinh gọn hơn khi chỉ sử dụng một nhánh chính duy nhất (`master`).

## 3. Vì sao phiên bản này lại được đánh số là 1.0.0 mà không phải 0.4.0?
- Theo quy ước Semantic Versioning (SemVer: `MAJOR.MINOR.PATCH`):
  + Các phiên bản `0.y.z` (như `v0.1.0` đến `v0.3.0` ở Lab 01–03) là giai đoạn xây dựng sơ khai (Initial Development), khi kiến trúc chưa hoàn chỉnh và API có thể thay đổi liên tục.
  + Mốc `1.0.0` đánh dấu phiên bản phát hành chính thức đầu tiên (First Stable Release), biểu thị rằng sản phẩm đã đạt đến trạng thái ổn định (đầy đủ các tính năng cơ bản: thêm/xóa/in giỏ hàng, tìm kiếm, tính chiết khấu), có bộ kiểm thử tự động toàn diện và cam kết về tính tương thích của API đối với người dùng.
