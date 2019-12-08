from day8 import *
import unittest


class Tests(unittest.TestCase):
    def test(self):
        result = part1('123456789012', 3, 2)
        self.assertEqual(result, 1)

    def test2(self):
        result = part2('0222112222120000', 2, 2)
        self.assertEqual(result, '01\n10')

if __name__ == '__main__':
    unittest.main()
