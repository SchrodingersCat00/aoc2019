from day7 import *
import unittest


class Tests(unittest.TestCase):
    def test(self):
        best = get_best1([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
        self.assertEqual(best, 43210)


    def test2(self):
        best = get_best2([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5])
        self.assertEqual(best, 139629729)

if __name__ == '__main__':
    unittest.main()
