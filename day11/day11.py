import computer

def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def add_vect(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def part1(program):
    white_panels = set()
    robot = computer.Program(program)
    # rotate left = index - 1
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir = 0
    seen = set()
    cur_coord = (0, 0)
    while not robot.is_halted:
        inp = 1 if cur_coord in white_panels else 0
        robot.recv_input([inp])
        robot.run()
        [color, direction] = robot.send_output()
        # paint black
        if color == 0 and cur_coord in white_panels:
            white_panels.remove(cur_coord)
        # paint white
        elif color == 1 and cur_coord not in white_panels:
            white_panels.add(cur_coord)
        seen.add(cur_coord)
        # update direction
        cur_dir = (cur_dir + 1) % 4 if direction == 1 else (cur_dir - 1) % 4
        # update location
        cur_coord = add_vect(cur_coord, dirs[cur_dir])
    
    return len(seen)


def part2(program):
    robot = computer.Program(program)
    # rotate left = index - 1
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir = 0
    cur_coord = (0, 0)
    white_panels = {cur_coord}
    while not robot.is_halted:
        inp = 1 if cur_coord in white_panels else 0
        robot.recv_input([inp])
        robot.run()
        [color, direction] = robot.send_output()
        # paint black
        if color == 0 and cur_coord in white_panels:
            white_panels.remove(cur_coord)
        # paint white
        elif color == 1 and cur_coord not in white_panels:
            white_panels.add(cur_coord)
        # update direction
        cur_dir = (cur_dir + 1) % 4 if direction == 1 else (cur_dir - 1) % 4
        # update location
        cur_coord = add_vect(cur_coord, dirs[cur_dir])
    
    return white_panels


def print_coords(coords):
    out = []
    for r in range(max(i for i, j in coords) + 1):
        for c in range(max(j for i, j in coords) + 1):
            if (r, c) in coords:
                out.append("■")
            else:
                out.append(" ")

        out.append("\n")

    print(''.join(out))


def main():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].strip().split(',')]
    print_coords(part2(program))


if __name__ == '__main__':
    main()
