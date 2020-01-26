from computer import Computer

def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines

def part1():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].split(',')]
    computer = Computer(program)
    computer.run()
    out = computer.send_output()
    print(len([x for x in out[2:-1:3] if x == 2]))


def main():
    part1()


if __name__ == '__main__':
    main()
