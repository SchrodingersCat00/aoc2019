import computer

def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def part1(program):
    sensor = computer.Program(program)
    sensor.recv_input([2])
    sensor.run()
    if sensor.is_suspended:
        raise ValueError("The machine was suspended")

    return sensor.send_output()

def main():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].strip().split(',')]
    print(part1(program))

if __name__ == '__main__':
    main()
