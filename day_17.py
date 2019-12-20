from intcode import IntCodeComputer


def main():
    computer = IntCodeComputer('day_17.input')
    computer.set_io_format(IntCodeComputer.UNICODE)
    memory, _, _ = computer.save()
    result = []
    # computer.run(output_data=result)
    # print("".join(result))
    # rows = "".join(result).split()
    # intersections = []
    # for y in range(len(rows) - 2):
    #     for x in range(len(rows[y]) - 2):
    #         if rows[y][x] == '#' and rows[y + 1][x] == '#' and rows[y - 1][x] == '#' and rows[y][x + 1] == '#' and rows[y][x - 1] == '#':
    #             intersections.append((x, y))
    # print(sum([x * y for x, y in intersections]))
    memory[0] = 2
    computer.load(memory, 0, 0)
    # 'R,10,R,8,L,10,L,10,R,8,L,6,L,6,R,8,L,6,L,6,R,10,R,8,L,10,L,10,L,10,R,10,L,6,R,8,L,6,L,6,L,10,R,10,L,6,L,10,R,10,L,6,R,8,L,6,L,6,R,10,R,8,L,10,L,10'
    input_data = [
        'B,A,A,B,C,A,C,C,A,B\n',
        'R,8,L,6,L,6\n',
        'R,10,R,8,L,10,L,10\n',
        'L,10,R,10,L,6\n',
        'n\n'
    ]

    computer.run(input_data=[x for x in "".join(input_data)], output_data=result)
    print(result)


if __name__ == '__main__':
    main()
