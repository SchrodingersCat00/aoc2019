import math

class Coord:
    def __init__(self, coord, dist):
        super().__init__()
        self.coord = coord
        self.dist = dist

    def __eq__(self, o):
        return self.coord == o.coord

    def __hash__(self):
        return hash(self.coord)

    def __repr__(self):
        return f"Coord({self.coord}, {self.dist})"


def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def add_vector(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def scalar_mult(a, v):
    return (v[0]*a, v[1]*a)


def parse_string(s):
    coords = set()
    loc = (0, 0)
    dirs = {'R': (0,1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
    dist = 1
    for token in s.strip().split(','):
        direction = dirs[token[0]]
        amount = int(token[1:])
        for i in range(1,amount+1):
            dest = add_vector(loc, scalar_mult(i, direction))
            coords.add(Coord(dest, dist))
            dist += 1
        loc = dest

    return coords


def part1(s1, s2):
    coords1 = parse_string(s1)
    coords2 = parse_string(s2)

    intersections = coords1.intersection(coords2)

    return min(abs(coord.coord[0]) + abs(coord.coord[1]) for coord in intersections)

def part2(s1, s2):
    coords1 = parse_string(s1)
    coords2 = parse_string(s2)

    intersections = coords1.intersection(coords2)

    mini = math.inf

    for intersection in intersections:
        for coord in coords1:
            if coord.coord == intersection.coord:
                dist1 = coord.dist
                break

        for coord in coords2:
            if coord.coord == intersection.coord:
                dist2 = coord.dist
                break

        if dist1 + dist2 < mini:
            mini = dist1 + dist2

    return mini


def main():
    lines = read_file_lines()
    # dist = part1(lines[0], lines[1])
    # print(dist)

    print(part2(lines[0], lines[1]))

if __name__ == '__main__':
    main()
