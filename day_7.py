import itertools


# Signals:
# 0: Exited
# 1: Waiting for input returns program and counter


def computer(program, input_data=None, output_data=None, counter=0, debug=False):
    """The computer."""

    def read(mode, position):
        if mode == 0:
            return program[program[int(position)]]
        elif mode == 1:
            return program[position]

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
            counter += 4
        elif opcode == 2:  # Multiply - 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
            if param_mode[-3] == 0:
                program[program[counter + 3]] = read(param_mode[-1], counter + 1) * read(param_mode[-2], counter + 2)
            elif param_mode[-3] == 1:
                program[program[counter + 3]] = read(param_mode[-1], counter + 1) * read(param_mode[-2], counter + 2)
            counter += 4
        elif opcode == 3:  # Input - 3,50 would take an input value and store it at address 50.
            if input_data is not None:
                if len(input_data) == 0:
                    return 1, program, counter
                if param_mode[-1] == 0:
                    program[program[counter + 1]] = input_data.pop(0)
                elif param_mode[-1] == 1:
                    program[counter + 1] = input_data.pop(0)
            else:
                if param_mode[-1] == 0:
                    program[program[counter + 1]] = int(input('input: '))
                elif param_mode[-1] == 1:
                    program[counter + 1] = int(input('input: '))
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
                program[program[counter + 3]] = 1
            else:
                program[program[counter + 3]] = 0
            counter += 4
        elif opcode == 8:  # Equal to - 1108,2,5,20 would change the value to 0 at address 20.
            if read(param_mode[-1], counter + 1) == read(param_mode[-2], counter + 2):
                program[program[counter + 3]] = 1
            else:
                program[program[counter + 3]] = 0
            counter += 4

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
    with open('day_7.input') as input_file:
        memory = [int(x) for x in input_file.readline().strip().split(',')]
        #           0  1   2  3   4     5   6   7   8  9   10  11  12 13  14  15 16
        # memory = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        # memory = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6,
        #           99, 0, 0, 5]
        result = []
        for busses in itertools.permutations([5, 6, 7, 8, 9]):
            previous_output = 0
            has_exited = False
            persistent_memory = {}
            while not has_exited:
                for r in busses:
                    output_data = []
                    if r in persistent_memory:
                        program_memory, counter = persistent_memory[r]
                        out = computer(program_memory,
                                       input_data=[previous_output],
                                       output_data=output_data,
                                       counter=counter)
                    else:
                        out = computer(memory.copy(), input_data=[r, previous_output], output_data=output_data)

                    if out[0] == 0:
                        has_exited = True
                    elif out[0] == 1:
                        persistent_memory[r] = (out[1], out[2])

                    previous_output = output_data[0]
                result.append((previous_output, busses))
        result = sorted(result, key=lambda r: r[0], reverse=True)
        print(result[0])


if __name__ == '__main__':
    main()
