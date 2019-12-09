import itertools


# Signals:
# 0: Exited
# 1: Waiting for input returns program and counter


def computer(program, input_data=None, output_data=None, counter=0, debug=False):
    """The computer."""
    program += [0 for _ in range(10000)]
    offset = 0

    def read(mode, position):
        if mode == 0:
            return program[program[int(position)]]
        elif mode == 1:
            return program[position]
        elif mode == 2:
            return program[offset + program[int(position)]]

    while counter < len(program):
        if debug:
            print(counter, program, end=' ')
        # Explanation for the interpretation of instruction to opcode and param_mode
        # ABCDE
        #  1002
        #
        # DE - two-digit opcode,      02 == opcode 2
        # C - mode of 1st parameter,  0 == position mode
        # B - mode of 2nd parameter,  1 == immediate mode
        # A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero
        instruction = str(program[counter])
        opcode = int(instruction[-2:])
        param_mode = [0 for _ in range(4)]
        param_mode += [int(x) for x in list(instruction[:-2])]

        if opcode == 1:  # Add - 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
            if param_mode[-3] == 0:
                program[program[counter + 3]] = read(param_mode[-1], counter + 1) + read(param_mode[-2], counter + 2)
            elif param_mode[-3] == 1:
                program[counter + 3] = read(param_mode[-1], counter + 1) + read(param_mode[-2], counter + 2)
            elif param_mode[-3] == 2:
                program[offset + program[counter + 3]] = read(param_mode[-1], counter + 1) + read(param_mode[-2],
                                                                                                  counter + 2)
            counter += 4
        elif opcode == 2:  # Multiply - 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
            if param_mode[-3] == 0:
                program[program[counter + 3]] = read(param_mode[-1], counter + 1) * read(param_mode[-2], counter + 2)
            elif param_mode[-3] == 1:
                program[program[counter + 3]] = read(param_mode[-1], counter + 1) * read(param_mode[-2], counter + 2)
            elif param_mode[-3] == 2:
                program[offset + program[counter + 3]] = read(param_mode[-1], counter + 1) * read(param_mode[-2],
                                                                                                  counter + 2)
            counter += 4
        elif opcode == 3:  # Input - 3,50 would take an input value and store it at address 50.
            if input_data is not None:
                if len(input_data) == 0:
                    return 1, program, counter
                if param_mode[-1] == 0:
                    program[program[counter + 1]] = input_data.pop(0)
                elif param_mode[-1] == 1:
                    program[counter + 1] = input_data.pop(0)
                elif param_mode[-1] == 2:
                    program[offset + program[counter + 1]] = input_data.pop(0)
            else:
                if param_mode[-1] == 0:
                    program[program[counter + 1]] = int(input('input: '))
                elif param_mode[-1] == 1:
                    program[counter + 1] = int(input('input: '))
                elif param_mode[-1] == 2:
                    program[offset + program[counter + 1]] = int(input('input: '))
            counter += 2
        elif opcode == 4:  # Output - 4,50 would output the value at address 50.
            if output_data is not None:
                output_data.append(read(param_mode[-1], counter + 1))
            else:
                print(read(param_mode[-1], counter + 1))
            counter += 2
        elif opcode == 5:  # Jump if not 0 - 105,2,20 would change the counter to the value at address 20.
            if read(param_mode[-1], counter + 1) != 0:
                counter = read(param_mode[-2], counter + 2)
            else:
                counter += 3
        elif opcode == 6:  # Jump if 0 - 106,0,20 would change the counter to the value at address 20.
            if read(param_mode[-1], counter + 1) == 0:
                counter = read(param_mode[-2], counter + 2)
            else:
                counter += 3
        elif opcode == 7:  # Less than - 1107,2,5,20 would change the value to 1 at address 20.
            if read(param_mode[-1], counter + 1) < read(param_mode[-2], counter + 2):
                if param_mode[-3] == 0:
                    program[program[counter + 3]] = 1
                elif param_mode[-3] == 1:
                    program[counter + 3] = 1
                elif param_mode[-3] == 2:
                    program[offset + program[counter + 3]] = 1
            else:
                if param_mode[-3] == 0:
                    program[program[counter + 3]] = 0
                elif param_mode[-3] == 1:
                    program[counter + 3] = 0
                elif param_mode[-3] == 2:
                    program[offset + program[counter + 3]] = 0
            counter += 4
        elif opcode == 8:  # Equal to - 1108,2,5,20 would change the value to 0 at address 20.
            if read(param_mode[-1], counter + 1) == read(param_mode[-2], counter + 2):
                if param_mode[-3] == 0:
                    program[program[counter + 3]] = 1
                elif param_mode[-3] == 1:
                    program[counter + 3] = 1
                elif param_mode[-3] == 2:
                    program[offset + program[counter + 3]] = 1
            else:
                if param_mode[-3] == 0:
                    program[program[counter + 3]] = 0
                elif param_mode[-3] == 1:
                    program[counter + 3] = 0
                elif param_mode[-3] == 2:
                    program[offset + program[counter + 3]] = 0
            counter += 4
        elif opcode == 9:  # Output - 4,50 would output the value at address 50.
            offset += read(param_mode[-1], counter + 1)
            counter += 2
        elif opcode == 99:  # Exit
            return 0,
        else:
            raise RuntimeError('Unknown operation', opcode)
        if debug:
            print(program)

    if debug:
        print()


def main():
    """Main function that loads a program to the 'computer'."""
    with open('day_9.input') as input_file:
        memory = [int(x) for x in input_file.readline().strip().split(',')]
        #           0  1   2  3   4     5   6   7   8  9   10  11  12 13  14  15 16
        # memory = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        # memory = [104,1125899906842624,99]
        # memory = [1102,34915192,34915192,7,4,7,99,0]
        result = []
        out = computer(memory.copy())

        print(out)


if __name__ == '__main__':
    main()
