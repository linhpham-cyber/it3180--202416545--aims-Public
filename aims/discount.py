def apply_discount(total, percent):
    # Ràng buộc dữ liệu đầu vào (Validate percent)
    if percent < 0 or percent > 100:
        raise ValueError("Phần trăm giảm giá phải nằm trong khoảng từ 0 đến 100")
        
    # Công thức trả về số tiền PHẢI TRẢ sau khi giảm giá (return discounted total)
    return total * (1 - percent / 100)
