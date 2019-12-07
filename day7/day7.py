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
            program_obj.recv_input([phase, inputt])
            program_obj.run()
            [inputt] = program_obj.OUT

        if inputt > best:
            best = inputt

    return best


def get_best2(base_program):
    best = -math.inf
    for phases in itertools.permutations([i for i in range(5, 10)]):
        amps = [computer.Program(copy.copy(base_program)).recv_input([phase]) for phase in phases]
        cur_inp = [0]
        amp_index = 0

        # While ampE did not halt
        while not amps[-1].is_halted:
            # get_next_amp
            cur_amp = amps[amp_index]
            # run amp with current input
            cur_amp.recv_input(cur_inp)
            cur_amp.run()
            # when amp yields, retrieve generated output
            cur_inp = cur_amp.OUT
            # update amp_index
            amp_index += 1
            amp_index %= 5

        if cur_inp[0] > best:
            best = cur_inp[0]

    return best


def main():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].strip().split(',')]
    get_best2(program)

if __name__ == '__main__':
    main()
