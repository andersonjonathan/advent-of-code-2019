import sys


class IntCodeComputer:
    UNICODE = 'unicode'
    INT = 'int'

    def __init__(self, program_file=None):
        self.counter = 0
        self.offset = 0
        self.program = []
        self.original_data = None
        self.io_format = IntCodeComputer.INT
        if program_file:
            self.open(program_file)

    def open(self, file):
        with open(file) as input_file:
            self.program = [int(x) for x in "".join([x.strip() for x in input_file.readlines()]).split(',')]
            self.original_data = (self.program.copy(), self.counter, self.offset)

    def load(self, program, counter=None, offset=None):
        self.program = program
        if counter is not None:
            self.counter = counter
        if offset is not None:
            self.offset = offset
        self.original_data = (self.program.copy(), self.counter, self.offset)

    def set_io_format(self, output_format=INT):
        self.io_format = output_format

    def get(self, position):
        try:
            return self.program[int(position)]
        except IndexError:
            while len(self.program) < position:
                self.program.append(0)
            return 0

    def set(self, position, value):
        try:
            self.program[int(position)] = value
        except IndexError:
            while len(self.program) <= position:
                self.program.append(0)
            self.program[int(position)] = value

    def read(self, mode, position):
        try:
            if mode == 0:
                return self.get(self.get(position))
            elif mode == 1:
                return self.get(position)
            elif mode == 2:
                return self.get(self.offset + self.get(position))
        except IndexError:
            return 0

    def write(self, mode, position, value):
        if mode == 0:
            self.set(self.get(position), value)
        elif mode == 1:
            self.set(position, value)
        elif mode == 2:
            self.set(self.offset + self.get(position), value)

    def reset(self):
        self.load(*self.original_data)

    def clear(self):
        self.program = []
        self.counter = 0
        self.offset = 0

    def save(self):
        self.original_data = (self.program.copy(), self.counter, self.offset)
        return self.original_data

    def get_instruction(self):
        # Explanation for the interpretation of instruction to opcode and param_mode
        # ABCDE
        #  1002
        #
        # DE - two-digit opcode,      02 == opcode 2
        # C - mode of 1st parameter,  0 == position mode
        # B - mode of 2nd parameter,  1 == immediate mode
        # A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero
        instruction = str(self.get(self.counter))
        opcode = int(instruction[-2:])
        param_mode = [0 for _ in range(4)]
        param_mode += [int(x) for x in list(instruction[:-2])]
        params = [
            (param_mode[-1], self.counter + 1),
            (param_mode[-2], self.counter + 2),
            (param_mode[-3], self.counter + 3),
        ]
        return opcode, params

    def run(self, input_data=None, output_data=None):
        for _ in self.run_internal(input_data=input_data, output_data=output_data):
            pass


    def run_with_yield(self, input_data=None):
        for out in self.run_internal(input_data=input_data, yield_output=True):
            yield out

    def run_internal(self, input_data=None, output_data=None, yield_output=False):
        # Signals:
        # 0: Exited
        # 1: Waiting for input
        while True:
            opcode, params = self.get_instruction()
            if opcode == 1:  # Add - 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
                self.write(*params[2], self.read(*params[0]) + self.read(*params[1]))
                self.counter += 4
            elif opcode == 2:  # Multiply - 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
                self.write(*params[2], self.read(*params[0]) * self.read(*params[1]))
                self.counter += 4
            elif opcode == 3:  # Input - 3,50 would take an input value and store it at address 50.
                if input_data is not None:
                    if len(input_data) == 0:
                        return 1
                    if self.io_format == IntCodeComputer.INT:
                        self.write(*params[0], int(input_data.pop(0)))
                    elif self.io_format == IntCodeComputer.UNICODE:
                        self.write(*params[0], ord(input_data.pop(0)))
                else:
                    if self.io_format == IntCodeComputer.INT:
                        self.write(*params[0], int(input('input: ')))
                    elif self.io_format == IntCodeComputer.UNICODE:
                        self.write(*params[0], ord(input('input: ')))
                self.counter += 2
            elif opcode == 4:  # Output - 4,50 would output the value at address 50.
                if yield_output:
                    if self.io_format == IntCodeComputer.INT:
                        yield self.read(*params[0])
                    elif self.io_format == IntCodeComputer.UNICODE:
                        yield self.read(*params[0])
                        # yield chr(self.read(*params[0]))
                elif output_data is not None:
                    if self.io_format == IntCodeComputer.INT:
                        output_data.append(self.read(*params[0]))
                    elif self.io_format == IntCodeComputer.UNICODE:
                        output_data.append(chr(self.read(*params[0])))
                else:
                    if self.io_format == IntCodeComputer.INT:
                        print(self.read(*params[0]))
                    elif self.io_format == IntCodeComputer.UNICODE:
                        print(chr(self.read(*params[0])), end='')
                self.counter += 2
            elif opcode == 5:  # Jump if not 0 - 105,2,20 would change the counter to the value at address 20.
                if self.read(*params[0]) != 0:
                    self.counter = self.read(*params[1])
                else:
                    self.counter += 3
            elif opcode == 6:  # Jump if 0 - 106,0,20 would change the counter to the value at address 20.
                if self.read(*params[0]) == 0:
                    self.counter = self.read(*params[1])
                else:
                    self.counter += 3
            elif opcode == 7:  # Less than - 1107,2,5,20 would change the value to 1 at address 20.
                if self.read(*params[0]) < self.read(*params[1]):
                    self.write(*params[2], 1)
                else:
                    self.write(*params[2], 0)
                self.counter += 4
            elif opcode == 8:  # Equal to - 1108,2,5,20 would change the value to 0 at address 20.
                if self.read(*params[0]) == self.read(*params[1]):
                    self.write(*params[2], 1)
                else:
                    self.write(*params[2], 0)
                self.counter += 4
            elif opcode == 9:  # Output - 4,50 would output the value at address 50.
                self.offset += self.read(*params[0])
                self.counter += 2
            elif opcode == 99:  # Exit
                return 0
            else:
                raise RuntimeError('Unknown operation', opcode)


def main(args):
    """Main function that loads a program to the 'computer'."""
    computer = IntCodeComputer(args[1])
    computer.set_io_format(IntCodeComputer.UNICODE)
    result = []
    computer.run(output_data=result)
    print("".join(result))


if __name__ == '__main__':
    main(sys.argv)
