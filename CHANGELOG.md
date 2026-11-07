## [Unreleased]

## - 2026-11-07
### Added
- `cart.print_cart()`: Chức năng in thông tin các tệp tin/sản phẩm có trong giỏ hàng.
- `search_by_title()`: Chức năng tìm kiếm đĩa DVD theo tiêu đề sản phẩm.
- `total_cost_with_discount()`: Hàm tính toán tổng số tiền hóa đơn sau khi đã áp dụng giảm giá.

### Fixed
- Giỏ hàng nhận đĩa thứ 21 (#6): Sửa lỗi logic chặn không cho thêm đĩa vượt quá số lượng MAX_NUMBERS_ORDERED = 20.
### Added
- Thêm tính năng sắp xếp giỏ hàng theo tiêu đề (`sort_by_title`) và theo giá tiền (`sort_by_cost`).
