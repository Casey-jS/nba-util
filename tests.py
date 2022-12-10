import unittest
import db_util

# Note: Because my database is dynamic, most of these tests are temporary

class Tests(unittest.TestCase):

    def test_favorites(self):
        self.assertEquals(True, db_util.is_favorited('admin', 2544))
        self.assertEquals(False, db_util.is_favorited('admin', 67233))


if __name__ == '__main__':
    unittest.main()
