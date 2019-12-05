def computer(program):
    """The computer."""
    def read(mode, position):
        if mode == 0:
            return program[program[int(position)]]
        elif mode == 1:
            return program[position]

    counter = 0
    while counter < len(program):
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
            program[program[counter + 3]] = read(param_mode[-1], counter + 1) + read(param_mode[-2], counter + 2)
            counter += 4
        elif opcode == 2:  # Multiply - 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
            program[program[counter + 3]] = read(param_mode[-1], counter + 1) * read(param_mode[-2], counter + 2)
            counter += 4
        elif opcode == 3:  # Input - 3,50 would take an input value and store it at address 50.
            program[program[counter + 1]] = int(input('input: '))
            counter += 2
        elif opcode == 4:  # Output - 4,50 would output the value at address 50.
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
            break
        else:
            raise RuntimeError('Unknown operation')


def main():
    """Main function that loads a program to the 'computer'."""
    computer([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
              20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])
    with open('day_5.input') as input_file:
        memory = [int(x) for x in input_file.readline().strip().split(',')]
        computer(memory)


if __name__ == '__main__':
    main()
