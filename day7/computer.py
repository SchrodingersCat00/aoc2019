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


class Program:
    def __init__(self, state):
        self.pc = 0
        self.IN = []
        self.OUT = []
        self.state = state
        self.is_halted = False
        self.is_suspended = True

    def recv_input(self, inp):
        self.IN = self.IN + inp
        return self

    def parse_opcode(self, opcode):
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

    def resolve_arg(self, arg, mode):
            if mode == Modes.POSITION:
                return self.state[arg]

            return arg

    def resolve_args(self, args, modes):
        return [self.resolve_arg(arg, mode) for arg, mode in zip(args, modes)]

    def get_args(self, op):
        if op in [Operation.READ, Operation.WRITE]:
            return self.state[self.pc+1:self.pc+2]
        elif op in [Operation.TRUE, Operation.FALSE]:
            return self.state[self.pc+1:self.pc+3]
        else:
            return self.state[self.pc+1:self.pc+4]

    def run_command(self, operation, args):
        if operation == Operation.ADD:
            self.state[args[2]] = args[0] + args[1]
            return 4
        elif operation == Operation.MULT:
            self.state[args[2]] = args[0] * args[1]
            return 4
        elif operation == Operation.READ:
            if self.IN:
                self.state[args[0]] = self.IN.pop(0)
                return 2
            else:
                self.is_suspended = True
                return 0
        elif operation == Operation.WRITE:
            self.OUT.append(self.state[args[0]])
            return 2
        elif operation == Operation.TRUE:
            if args[0] != 0:
                return args[1] - self.pc
            else:
                return 3
        elif operation == Operation.FALSE:
            if args[0] == 0:
                return args[1] - self.pc
            else:
                return 3
        elif operation == Operation.LESS:
            if args[0] < args[1]:
                self.state[args[2]] = 1
            else:
                self.state[args[2]] = 0
            return 4
        elif operation == Operation.EQUAL:
            if args[0] == args[1]:
                self.state[args[2]] = 1
            else:
                self.state[args[2]] = 0
            return 4
        elif operation == Operation.HALT:
            return 0
        else:
            raise ValueError

    def run(self):
        self.is_suspended = False
        self.is_halted = False
        opcode = None
        while not self.is_suspended:
            opcode = self.state[self.pc]
            parsed_code = self.parse_opcode(opcode)
            if parsed_code.op == Operation.HALT:
                break
            args = self.get_args(parsed_code.op)
            resolved_args = self.resolve_args(args, parsed_code.modes)
            if parsed_code.op not in [Operation.TRUE, Operation.FALSE]:
                resolved_args[-1] = args[-1]

            self.pc += self.run_command(parsed_code.op, resolved_args)

        self.is_halted = True
