from day2 import *
import unittest


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(run_program([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
        self.assertEqual(run_program([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
        self.assertEqual(run_program([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])

if __name__ == '__main__':
    unittest.main()
