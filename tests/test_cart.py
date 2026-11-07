import unittest
# Import class Cart và hằng số giới hạn từ package aims của bạn
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc

class TestCartLimit(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        
        # 1. Thêm liên tiếp 20 đĩa DVD đầu tiên vào giỏ hàng
        # Sử dụng chính xác tên hàm add_dvd của thầy cô
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD Title {i}")
            result = cart.add_dvd(dvd)
            self.assertTrue(result) 
            
        # 2. Cố tình thêm tiếp đĩa DVD thứ 21 vào giỏ hàng để kích hoạt lỗi
        extra_dvd = DigitalVideoDisc("The 21st DVD")
        result_21st = cart.add_dvd(extra_dvd)
        
        # Kiểm thử kỳ vọng đĩa thứ 21 phải bị từ chối (trả về False)
        # Vì code cũ ở cart.py đang dùng dấu > nên dòng này sẽ bị lỗi FAIL chuẩn (True is not false)
        self.assertFalse(result_21st)

if __name__ == '__main__':
    unittest.main()
