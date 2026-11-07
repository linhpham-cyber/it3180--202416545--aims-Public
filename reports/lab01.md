## BÁO CÁO TRẢ LỜI CÂU HỎI THẢO LUẬN LAB 01

### 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
*   **Vị trí lưu trữ:** 
    *   Cấu hình `--global` được lưu trong tệp `.gitconfig` tại thư mục người dùng của hệ điều hành (Đường dẫn trên Windows thường là `C:\Users\<Tên_User>\.gitconfig`).
    *   Cấu hình `--local` được lưu trong tệp `config` nằm bên trong thư mục ẩn `.git` của riêng kho lưu trữ đó (`<thư_mục_dự_án>/.git/config`).
*   **Điểm khác biệt:**
    *   `--global`: Áp dụng cài đặt (Tên, Email, Trình soạn thảo...) cho **tất cả các dự án Git** của người dùng đó trên máy tính.
    *   `--local` (Mặc định): Chỉ áp dụng cài đặt riêng cho **duy nhất kho lưu trữ hiện tại**, có quyền ghi đè lên cấu hình `--global`.

### 2. Vì sao dùng `git mv`?
*   Khi sử dụng `git mv`, Git hiểu ngay lập tức đây là hành động đổi tên hoặc di chuyển vị trí tệp tin (`Renamed`) và đưa thẳng tệp vào hàng đợi (Staging Area).
*   Lệnh này giúp Git **giữ nguyên vẹn toàn bộ lịch sử các commit cũ** của tệp tin đó từ trước khi di chuyển. Nếu dùng lệnh di chuyển thủ công của hệ điều hành, Git sẽ coi đó là hai hành động tách biệt (Xóa file cũ và Tạo file mới tinh), làm đứt gãy lịch sử chỉnh sửa code.

### 3. Nhánh `release/lab01` có phải baseline?
*   **Không.** Nhánh `release/lab01` đóng vai trò là một nhánh **nhánh phân phối phiên bản (Release Branch)** dùng để đóng gói và lưu giữ trạng thái mã nguồn hoàn chỉnh tại thời điểm nộp bài Lab 01 để thầy cô chấm điểm. 
*   Nhánh chính `master` (hoặc `main`) mới đóng vai trò là **nhánh cơ sở (Baseline Branch)** - nơi lưu trữ dòng lịch sử mã nguồn chính thống, ổn định và liên tục của toàn bộ dự án từ đầu đến cuối.

### 4. Vì sao không commit thẳng master dù làm một mình?
*   **Bảo vệ mã nguồn ổn định:** Nhánh phụ (Feature/Refactor Branch) là nơi an toàn để thử nghiệm các tính năng mới hoặc tối ưu hóa code. Nếu code bị lỗi hoặc không chạy được, ta có thể dễ dàng hủy bỏ nhánh phụ mà không làm hỏng phiên bản code đang chạy ổn định trên nhánh `master`.
*   **Hỗ trợ Code Review:** Việc tạo nhánh riêng giúp chúng ta có thể tạo Pull Request (PR) trên GitHub để tự kiểm tra lại các dòng code thay đổi (tab *Files changed*) trước khi chính thức gộp vào dự án.
