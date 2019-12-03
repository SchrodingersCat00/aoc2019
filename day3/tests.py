from day3 import *
import unittest


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            part1(
                "R8,U5,L5,D3",
                "U7,R6,D4,L4"
                ), 6
        )
        self.assertEqual(
            part1(
                "R75,D30,R83,U83,L12,D49,R71,U7,L72",
                "U62,R66,U55,R34,D71,R55,D58,R83"
                ), 159
        )
        self.assertEqual(
            part1(
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
                ), 135
        )

    def test2(self):
        self.assertEqual(
            part2(
                "R75,D30,R83,U83,L12,D49,R71,U7,L72",
                "U62,R66,U55,R34,D71,R55,D58,R83"
                ), 610
        )
        self.assertEqual(
            part2(
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
                ), 410
        )

if __name__ == '__main__':
    unittest.main()
