import unittest
import Charecter


class MyTestCase(unittest.TestCase):

    def test_level_system(self):
        self.someCharecter = Charecter

        self.assertEqual(self.someCharecter.level, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
