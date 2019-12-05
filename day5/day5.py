from enum import Enum

class Modes(Enum):
    POSITION = 1
    IMMEDIATE = 2

class Operation(Enum):
    ADD = 1
    MULT = 2
    HALT = 3
    READ = 4
    WRITE = 5

class Instruction:
    def __init__(self, op, modes):
        super().__init__()
        self.op = op
        self.modes = modes


def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def parse_opcode(opcode):
    opcode = '{:05d}'.format(int(opcode))
    mode_conv = { '0': Modes.POSITION, '1': Modes.IMMEDIATE }
    op_conv = {
        '01': Operation.ADD,
        '02': Operation.MULT,
        '03': Operation.READ,
        '04': Operation.WRITE,
        '99': Operation.HALT
    }
    modes = [mode_conv[code] for code in opcode[:3]]
    modes.reverse()
    op = op_conv[''.join(opcode[3:])]

    return Instruction(op, modes)


def increase_pc(opcode, pc):
    inc = 2 if opcode in [Operation.READ, Operation.WRITE] else 4

    return pc + inc


def resolve_args(program, args, modes):
    def resolve_arg(arg, mode):
        if mode == Modes.POSITION:
            return program[arg]

        return arg

    return [resolve_arg(arg, mode) for arg, mode in zip(args, modes)]


def get_args(program, op, pc):
    if op in [Operation.READ, Operation.WRITE]:
        return program[pc+1:pc+2]
    else:
        return program[pc+1:pc+4]


def run_command(program, operation, args):
    if operation == Operation.ADD:
        program[args[2]] = args[0] + args[1]
    elif operation == Operation.MULT:
        program[args[2]] = args[0] * args[1]
    elif operation == Operation.READ:
        program[args[0]] = int(input())
    elif operation == Operation.WRITE:
        print(program[args[0]])



def run_program(program):
    opcode = None
    pc = 0
    while opcode != Operation.HALT:
        opcode = program[pc]
        parsed_code = parse_opcode(opcode)
        args = get_args(program, parsed_code.op, pc)
        resolved_args = resolve_args(program, args, parsed_code.modes)
        resolved_args[-1] = args[-1]
        run_command(program, parsed_code.op, resolved_args)

        pc = increase_pc(parsed_code.op, pc)


def main():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].strip().split(',')]
    run_program(program)


if __name__ == '__main__':
    main()
