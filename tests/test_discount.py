import unittest
from aims.discount import apply_discount

class TestDiscountCalculation(unittest.TestCase):
    def test_valid_discount(self):
        # Kiểm tra tính toán thông thường: 100$ giảm 20% phải trả về giá sau giảm là 80$
        self.assertEqual(apply_discount(100, 20), 80)

    def test_invalid_percent_too_high(self):
        # Kiểm tra phần trăm không hợp lệ (150%): Hệ thống phải ném ra lỗi ValueError
        with self.assertRaises(ValueError):
            apply_discount(100, 150)

    def test_invalid_percent_negative(self):
        # Kiểm tra phần trăm âm (-10%): Hệ thống cũng phải ném ra lỗi ValueError
        with self.assertRaises(ValueError):
            apply_discount(100, -10)

if __name__ == '__main__':
    unittest.main()
