# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.


def computer(program):
    def read_value(mode, pos):
        if mode == 0:
            return program[program[int(pos)]]
        elif mode == 1:
            return program[pos]
    counter = 0
    while counter < len(program):
        raw_opcode = str(program[counter])
        opcode = int(raw_opcode[-2:])
        parameter_mode = [int(x) for x in list(raw_opcode[:-2])]
        parameter_mode.insert(0, 0)
        parameter_mode.insert(0, 0)
        parameter_mode.insert(0, 0)
        parameter_mode.insert(0, 0)
        if opcode == 1:
            program[program[counter + 3]] = read_value(parameter_mode[-1], counter + 1) + read_value(parameter_mode[-2], counter + 2)
            counter += 4
        elif opcode == 2:
            program[program[counter + 3]] = read_value(parameter_mode[-1], counter + 1) * read_value(parameter_mode[-2], counter + 2)
            counter += 4
        elif opcode == 3:
            program[program[counter + 1]] = int(input('input'))
            counter += 2
        elif opcode == 4:
            print(program[program[counter + 1]])
            counter += 2
        elif opcode == 5:
            if read_value(parameter_mode[-1], counter + 1) != 0:
                counter = read_value(parameter_mode[-2], counter + 2)
            else:
                counter += 3
        elif opcode == 6:
            if read_value(parameter_mode[-1], counter + 1) == 0:
                counter = read_value(parameter_mode[-2], counter + 2)
            else:
                counter += 3
        elif opcode == 7:
            if read_value(parameter_mode[-1], counter + 1) < read_value(parameter_mode[-2], counter + 2):
                program[program[counter + 3]] = 1
            else:
                program[program[counter + 3]] = 0
            counter += 4
        elif opcode == 8:
            if read_value(parameter_mode[-1], counter + 1) == read_value(parameter_mode[-2], counter + 2):
                program[program[counter + 3]] = 1
            else:
                program[program[counter + 3]] = 0
            counter += 4

        elif opcode == 99:
            break
        else:
            print("kaoos")
            break


def main():
    computer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    with open('day_5.input') as input_file:
        memory = [int(x) for x in input_file.readline().strip().split(',')]
        computer(memory)


if __name__ == '__main__':
    main()
