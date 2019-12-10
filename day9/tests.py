from day9 import *
import unittest
import computer


class Tests(unittest.TestCase):
    def test(self):
        result = part1([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
        self.assertEqual(result, [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])

    def test2(self):
        [result] = part1([1102,34915192,34915192,7,4,7,99,0])
        self.assertEqual(len(str(result)), 16)

    def test3(self):
        [result] = part1([104,1125899906842624,99])
        self.assertEqual(result, 1125899906842624)

if __name__ == '__main__':
    unittest.main()
