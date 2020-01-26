import copy
from enum import Enum


class Modes(Enum):
    POSITION = 1
    IMMEDIATE = 2
    RELATIVE = 3


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
    CHANGE_BASE = 10


class Instruction:

    def __init__(self, op, modes):
        self.op = op
        self.modes = modes


class ComputerMemory:

    def __init__(self, initstate=None):
        if initstate is None:
            initstate = []

        self.mem = initstate
        self.relative_base = 0

    def update_relative_base(self, delta):
        self.relative_base += delta

    def _get_value(self, arg, mode):
        if mode == Modes.IMMEDIATE:
            return arg
        elif mode == Modes.POSITION:
            return self.mem[arg]
        elif mode == Modes.RELATIVE:
            return self.mem[self.relative_base + arg]
        else:
            raise ValueError

    def _set_value(self, arg, mode, value):
        if mode == Modes.POSITION:
            self.mem[arg] = value
        elif mode == Modes.RELATIVE:
            self.mem[arg + self.relative_base] = value
        else:
            raise ValueError

    def __getitem__(self, key):
        arg, mode = key
        if mode is None:
            raise ValueError

        if len(self.mem) <= arg and mode == Modes.POSITION:
            return 0
        elif len(self.mem) <= self.relative_base + arg and mode == Modes.RELATIVE:
            return 0
        else:
            return self._get_value(arg, mode)

    def __setitem__(self, key, value):
        arg, mode = key
        if mode is None:
            raise ValueError
        while len(self.mem) <= arg and mode == Modes.POSITION:
            self.mem.append(0)
        while len(self.mem) <= self.relative_base + arg and mode == Modes.RELATIVE:
            self.mem.append(0)
        self._set_value(arg, mode, value)

class Computer:

    def __init__(self, state):
        self.pc = 0
        self.IN = []
        self.OUT = []
        self.state = ComputerMemory(copy.copy(state))
        self.is_halted = False
        self.is_suspended = True

    def recv_input(self, inp):
        self.IN = self.IN + inp
        return self

    def send_output(self):
        out = self.OUT
        self.OUT = []
        return out

    def parse_opcode(self, opcode):
        opcode = '{:05d}'.format(int(opcode))
        mode_conv = {
            '0': Modes.POSITION,
            '1': Modes.IMMEDIATE,
            '2': Modes.RELATIVE
        }
        op_conv = {
            '01': Operation.ADD,
            '02': Operation.MULT,
            '03': Operation.READ,
            '04': Operation.WRITE,
            '05': Operation.TRUE,
            '06': Operation.FALSE,
            '07': Operation.LESS,
            '08': Operation.EQUAL,
            '09': Operation.CHANGE_BASE,
            '99': Operation.HALT,
        }
        modes = [mode_conv[code] for code in opcode[:3]]
        modes.reverse()
        op = op_conv[''.join(opcode[3:])]

        return Instruction(op, modes)

    def get_args(self, op):
        if op in [Operation.READ, Operation.WRITE, Operation.CHANGE_BASE]:
            return [self.state[self.pc+1, Modes.POSITION]]
        elif op in [Operation.TRUE, Operation.FALSE]:
            return [self.state[self.pc+i, Modes.POSITION] for i in range(1, 3)]
        else:
            return [self.state[self.pc+i, Modes.POSITION] for i in range(1, 4)]

    def run_command(self, operation, args, modes):
        if operation == Operation.ADD:
            self.state[args[2], modes[2]] = self.state[args[0], modes[0]] + self.state[args[1], modes[1]]
            return 4
        elif operation == Operation.MULT:
            self.state[args[2], modes[2]] = self.state[args[0], modes[0]] * self.state[args[1], modes[1]]
            return 4
        elif operation == Operation.READ:
            if self.IN:
                self.state[args[0], modes[0]] = self.IN.pop(0)
                return 2
            else:
                self.is_suspended = True
                return 0
        elif operation == Operation.WRITE:
            self.OUT.append(self.state[args[0], modes[0]])
            return 2
        elif operation == Operation.TRUE:
            if self.state[args[0], modes[0]] != 0:
                return self.state[args[1], modes[1]] - self.pc
            else:
                return 3
        elif operation == Operation.FALSE:
            if self.state[args[0], modes[0]] == 0:
                return self.state[args[1], modes[1]] - self.pc
            else:
                return 3
        elif operation == Operation.LESS:
            if self.state[args[0], modes[0]] < self.state[args[1], modes[1]]:
                self.state[args[2], modes[2]] = 1
            else:
                self.state[args[2], modes[2]] = 0
            return 4
        elif operation == Operation.EQUAL:
            if self.state[args[0], modes[0]] == self.state[args[1], modes[1]]:
                self.state[args[2], modes[2]] = 1
            else:
                self.state[args[2], modes[2]] = 0
            return 4
        elif operation == Operation.CHANGE_BASE:
            self.state.update_relative_base(self.state[args[0], modes[0]])
            return 2
        elif operation == Operation.HALT:
            return 0
        else:
            raise ValueError

    def run(self):
        self.is_suspended = False
        self.is_halted = False
        opcode = None
        while not self.is_suspended:
            opcode = self.state[self.pc, Modes.POSITION]
            parsed_code = self.parse_opcode(opcode)
            if parsed_code.op == Operation.HALT:
                self.is_halted = True
                break
            args = self.get_args(parsed_code.op)

            self.pc += self.run_command(parsed_code.op, args, parsed_code.modes)
