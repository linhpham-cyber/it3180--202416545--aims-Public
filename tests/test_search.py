import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

class TestSearchCaseInsensitive(unittest.TestCase):
    def test_search_lowercase(self):
        dvds = [DigitalVideoDisc("The Lion King")]
        results = search_by_title(dvds, "lion")
        # Tìm từ khóa viết thường 'lion' phải ra kết quả phim viết hoa thành công
        self.assertEqual(len(results), 1)

if __name__ == '__main__':
    unittest.main()
