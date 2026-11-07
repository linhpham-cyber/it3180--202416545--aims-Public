import unittest
# Import class Cart và hằng số giới hạn từ package aims của bạn
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc

class TestCartLimit(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        
        # 1. Giả lập thêm liên tiếp 20 đĩa DVD đầu tiên vào giỏ hàng
        # Tất cả 20 đĩa này bắt buộc phải thêm thành công (trả về True)
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD Title {i}")
            result = cart.add_digital_video_disc(dvd)
            self.assertTrue(result) 
            
        # 2. Cố tình thêm tiếp đĩa DVD thứ 21 vào giỏ hàng
        extra_dvd = DigitalVideoDisc("The 21st DVD")
        result_21st = cart.add_digital_video_disc(extra_dvd)
        
        # Kiểm thử kỳ vọng đĩa thứ 21 phải bị từ chối (trả về False)
        # Vì code cũ đang bị lỗi (dùng dấu >) nên dòng này sẽ bị FAIL (True is not false)
        self.assertFalse(result_21st)

if __name__ == '__main__':
    unittest.main()
