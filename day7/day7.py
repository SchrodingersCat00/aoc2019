import computer
import copy
import itertools
import math

def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def get_best1(base_program):
    best = -math.inf
    for phases in itertools.permutations([i for i in range(5)]):
        amps = [(copy.copy(base_program), phase) for phase in phases]
        inputt = 0
        for program, phase in amps:
            program_obj = computer.Program(program)
            program_obj.set_input([phase, inputt])
            program_obj.run()
            [inputt] = program_obj.OUT

        if inputt > best:
            best = inputt

    return best


def get_best2(base_program):
    best = -math.inf
    for phases in itertools.permutations([i for i in range(5, 10)]):
        amps = [(copy.copy(base_program), [phase], []) for phase in phases]
        inputt = 0
        # While ampE did not halt
            # get_next_amp
            # run amp with current input
            # when amp yields, retrieve generated output
            # save amp pc and amp program state


def main():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].strip().split(',')]
    get_best2(program)

if __name__ == '__main__':
    main()
