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
    TRUE = 6
    FALSE = 7
    LESS = 8
    EQUAL = 9

class Instruction:
    def __init__(self, op, modes):
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
        '05': Operation.TRUE,
        '06': Operation.FALSE,
        '07': Operation.LESS,
        '08': Operation.EQUAL,
        '99': Operation.HALT,
    }
    modes = [mode_conv[code] for code in opcode[:3]]
    modes.reverse()
    op = op_conv[''.join(opcode[3:])]

    return Instruction(op, modes)


def resolve_args(program, args, modes):
    def resolve_arg(arg, mode):
        if mode == Modes.POSITION:
            return program[arg]

        return arg

    return [resolve_arg(arg, mode) for arg, mode in zip(args, modes)]


def get_args(program, op, pc):
    if op in [Operation.READ, Operation.WRITE]:
        return program[pc+1:pc+2]
    elif op in [Operation.TRUE, Operation.FALSE]:
        return program[pc+1:pc+3]
    else:
        return program[pc+1:pc+4]


def run_command(program, operation, args, pc):
    if operation == Operation.ADD:
        program[args[2]] = args[0] + args[1]
        return 4
    elif operation == Operation.MULT:
        program[args[2]] = args[0] * args[1]
        return 4
    elif operation == Operation.READ:
        program[args[0]] = int(input())
        return 2
    elif operation == Operation.WRITE:
        print(program[args[0]])
        return 2
    elif operation == Operation.TRUE:
        if args[0] != 0:
            return args[1] - pc
        else:
            return 3
    elif operation == Operation.FALSE:
        if args[0] == 0:
            return args[1] - pc
        else:
            return 3
    elif operation == Operation.LESS:
        if args[0] < args[1]:
            program[args[2]] = 1
        else:
            program[args[2]] = 0
        return 4
    elif operation == Operation.EQUAL:
        if args[0] == args[1]:
            program[args[2]] = 1
        else:
            program[args[2]] = 0
        return 4



def run_program(program):
    opcode = None
    pc = 0
    while opcode != Operation.HALT:
        opcode = program[pc]
        parsed_code = parse_opcode(opcode)
        args = get_args(program, parsed_code.op, pc)
        resolved_args = resolve_args(program, args, parsed_code.modes)
        if parsed_code.op not in [Operation.TRUE, Operation.FALSE]:
            resolved_args[-1] = args[-1]

        pc += run_command(program, parsed_code.op, resolved_args, pc)


def main():
    lines = read_file_lines()
    program = [int(code) for code in lines[0].strip().split(',')]
    run_program(program)


if __name__ == '__main__':
    main()
