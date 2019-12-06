from day6 import *
import unittest


class Tests(unittest.TestCase):
    def test(self):
        count = part1([
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
        ])
        self.assertEqual(count, 42)

    def test2(self):
        count = part2([
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
            "K)YOU",
            "I)SAN",
        ])
        self.assertEqual(count, 4)

if __name__ == '__main__':
    unittest.main()
