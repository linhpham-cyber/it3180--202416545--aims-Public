# Báo cáo Thực hành Lab 02: Checklist & Lỗi thường gặp trong Git & GitHub

##  Nội dung Thảo luận (Discussion Answers)

### Câu hỏi 1: Vì sao phải đồng bộ master trước khi PR?
* **Phát hiện xung đột sớm:** Giúp kiểm tra và giải quyết các xung đột mã nguồn (Conflict) ngay tại máy cá nhân trước khi đưa lên hệ thống chung.
* **Đảm bảo tính ổn định:** Đảm bảo mã nguồn mới hoạt động trơn tru sau khi kết hợp với những thay đổi mới nhất từ các thành viên khác.
* **Tối ưu hóa quy trình:** Giúp reviewer dễ dàng merge Pull Request mà không gặp trở ngại kỹ thuật.

### Câu hỏi 2: Khi nào không được rebase?
* **Quy tắc vàng:** Không rebase trên các nhánh công khai (`master`, `develop`) hoặc nhánh đang có nhiều người cùng làm việc.
* **Lý do:** Rebase thay đổi lịch sử commit (tạo commit hash mới). Việc này gây đồng bộ lệch hướng nghiêm trọng cho các thành viên khác khi họ tiến hành `git pull`.

### Câu hỏi 3: Naming Convention: `feature/*` khác `topic/*` ra sao?
* **`feature/*`**: Dùng cho việc phát triển một tính năng lớn, hoàn chỉnh và có kế hoạch tích hợp cụ thể vào sản phẩm.
* **`topic/*`**: Dùng cho các tác vụ ngắn hạn, sửa đổi nhỏ, mang tính thử nghiệm hoặc nghiên cứu (Spike) và có thể hủy bỏ nếu không đạt yêu cầu.
