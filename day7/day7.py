import computer
import copy
import itertools
import math

def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def get_best(base_program):
    best = -math.inf
    for phases in itertools.permutations([i for i in range(5)]):
        amps = [(copy.copy(base_program), phase) for phase in phases]
        inputt = 0
        for program, phase in amps:
            inputt = computer.run_program(program, inputt, phase)

        if inputt > best:
            best = inputt

    return best


def part1():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].strip().split(',')]
    print(get_best(program))


def main():
    part1()

if __name__ == '__main__':
    main()
