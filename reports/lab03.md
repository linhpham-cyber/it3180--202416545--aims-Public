# BÁO CÁO TRẢ LỜI CÂU HỎI THẢO LUẬN LAB 03


1. Merge base là gì?

• Merge base là commit chung gần nhất (tổ tiên chung gần nhất) của hai nhánh khác nhau trong lịch sử Git.
• Khi bạn thực hiện gộp nhánh (lệnh git merge), Git sẽ tự động tìm kiếm commit Merge base này để làm điểm tham chiếu. Hệ thống sẽ so sánh sự thay đổi của nhánh hiện tại so với Merge base, và sự thay đổi của nhánh kia so với Merge base, từ đó tự động tích hợp các dòng code lại với nhau (hoặc phát hiện lỗi xung đột CONFLICT nếu cả hai nhánh cùng sửa một dòng tính từ điểm Merge base đó).

2. Vì sao các nhánh như master, release/* phải dùng lệnh revert khi muốn hoàn tác?

Các nhánh như master hay release/* được gọi là các nhánh chung công khai (Public/Shared Branches) – nơi lưu trữ mã nguồn ổn định và có nhiều thành viên trong nhóm cùng kéo (pull) về làm việc. Khi muốn hủy bỏ một tính năng lỗi trên các nhánh này, ta bắt buộc phải dùng revert thay vì reset vì các lý do sau:
• Bảo vệ lịch sử, tránh xung đột cho nhóm: Lệnh revert hoạt động bằng cách tạo ra một commit mới có nội dung đảo ngược hoàn toàn để triệt tiêu lỗi, không làm thay đổi hoặc xóa bỏ các commit cũ. Nhờ đó, dòng thời gian Git của các thành viên khác trong nhóm không bị lệch, tránh được lỗi xung đột dữ liệu nghiêm trọng khi đồng bộ.
• Lưu lại vết lịch sử sửa sai: Giúp cả nhóm và thầy cô khi kiểm tra lịch sử (git log) vẫn nhìn thấy tệp tin đó từng bị lỗi gì, ai đã sửa và sửa vào lúc nào, giúp quy trình quản lý cấu hình phần mềm minh bạch tuyệt đối.
