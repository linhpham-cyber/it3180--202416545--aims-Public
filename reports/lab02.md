## BÁO CÁO TRẢ LỜI CÂU HỎI THẢO LUẬN LAB 02

### 1. Vì sao phải đồng bộ master trước khi PR?
*   **Giải quyết xung đột sớm (Resolve Conflicts Cục bộ):** Khi làm việc nhóm (hoặc phát triển song song nhiều tính năng), nhánh `master` trên GitHub có thể đã đi trước và chứa code mới của người khác. Đồng bộ bằng cách kéo `master` về gộp vào nhánh phụ giúp phát hiện và xử lý xung đột ngay dưới máy mình trước khi đẩy lên mạng.
*   **Đảm bảo tính tích hợp (Integration Testing):** Giúp bạn chạy thử nghiệm (`python main.py`) để chắc chắn rằng tính năng mới bạn viết khi chạy chung với code mới cập nhật của dự án vẫn hoạt động hoàn hảo, không gây lỗi hệ thống.

### 2. Khi nào không được rebase?
*   **Không rebase trên các nhánh công khai (Public/Shared Branches) hoặc nhánh chung đã đẩy lên GitHub (như `master`, `main`):** Lệnh `rebase` thực chất là viết lại lịch sử Git và làm thay đổi toàn bộ mã băm (SHA) của các commit cũ. 
*   Nếu bạn rebase một nhánh chung mà nhiều người khác đang kéo về làm việc, dòng thời gian Git trên máy của họ sẽ bị lệch hoàn toàn, gây ra xung đột nghiêm trọng và làm rối loạn lịch sử đóng gói của dự án. *(Chỉ nên rebase trên nhánh tính năng cá nhân dưới máy local chưa push).*

### 3. Quy ước đặt tên: `feature/*` khác `topic/*` ra sao?
Đây là quy ước đặt tên nhánh (Branch Naming Convention) giúp quản lý luồng công việc khoa học:
*   **`feature/*` (Nhánh tính năng):** Dùng để phát triển một **chức năng cụ thể, mới hoàn toàn** cho sản phẩm phần mềm và có thời gian tồn tại dài hơn (Ví dụ: `feature/cart-print` để in giỏ hàng, `feature/search-by-title` để tìm kiếm).
*   **`topic/*` (Nhánh chủ đề/ngắn hạn):** Dùng cho các tác vụ mang tính chất **thử nghiệm ngắn hạn, sửa một lỗi nhỏ, nghiên cứu giải pháp kỹ thuật hoặc cấu hình hệ thống** mà không tạo trực tiếp tính năng mới cho người dùng (Ví dụ: `topic/pr-template` bạn dùng để cấu hình tệp mẫu PR).
