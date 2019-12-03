# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.


def computer(program):
    counter = 0
    while counter < len(program):
        opcode = program[counter]
        if opcode == 1:
            program[program[counter + 3]] = program[program[counter + 1]] + program[program[counter + 2]]
        elif opcode == 2:
            program[program[counter + 3]] = program[program[counter + 1]] * program[program[counter + 2]]
        elif opcode == 99:
            break
        else:
            print("kaoos")
            break
        counter += 4


def part_1():
    input_data = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 2, 19, 6, 23, 2, 13, 23, 27, 1, 9, 27,
                  31, 2, 31, 9, 35, 1, 6, 35, 39, 2, 10, 39, 43, 1, 5, 43, 47, 1, 5, 47, 51, 2, 51, 6, 55, 2, 10, 55,
                  59, 1, 59, 9, 63, 2, 13, 63, 67, 1, 10, 67, 71, 1, 71, 5, 75, 1, 75, 6, 79, 1, 10, 79, 83, 1, 5, 83,
                  87, 1, 5, 87, 91, 2, 91, 6, 95, 2, 6, 95, 99, 2, 10, 99, 103, 1, 103, 5, 107, 1, 2, 107, 111, 1, 6,
                  111, 0, 99, 2, 14, 0, 0]
    computer(input_data)
    print(input_data)


def main():
    for i in range(0, 100):
        for j in range(0, 100):
            input_data = [1, i, j, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 2, 19, 6, 23, 2, 13, 23, 27, 1,
                          9, 27, 31, 2, 31, 9, 35, 1, 6, 35, 39, 2, 10, 39, 43, 1, 5, 43, 47, 1, 5, 47, 51, 2, 51, 6,
                          55, 2, 10, 55, 59, 1, 59, 9, 63, 2, 13, 63, 67, 1, 10, 67, 71, 1, 71, 5, 75, 1, 75, 6, 79, 1,
                          10, 79, 83, 1, 5, 83, 87, 1, 5, 87, 91, 2, 91, 6, 95, 2, 6, 95, 99, 2, 10, 99, 103, 1, 103, 5,
                          107, 1, 2, 107, 111, 1, 6, 111, 0, 99, 2, 14, 0, 0]
            computer(input_data)
            if input_data[0] == 19690720:
                print(i, j)
                exit(0)


if __name__ == '__main__':
    main()
