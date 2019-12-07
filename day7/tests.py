from day7 import *
import unittest


class Tests(unittest.TestCase):
    def test(self):
        best = get_best1([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
        self.assertEqual(best, 43210)

if __name__ == '__main__':
    unittest.main()
