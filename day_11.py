from intcode import IntCodeComputer


def main():
    """Main function that loads a program to the 'computer'."""
    computer = IntCodeComputer('day_11.input')
    drawn_tiles = []
    color_map = {(0, 0): 1}
    current_pos = (0, 0)
    current_direction = 0  # 0=up, 1=right, 2=down, 3=left
    exit_code = 1
    while exit_code != 0:
        input_data = [color_map[current_pos] if current_pos in color_map else 0]
        result = []
        exit_code = computer.run(input_data=input_data, output_data=result)
        if len(result) > 0:
            color_map[current_pos] = result[0]
            drawn_tiles.append(current_pos)
            if result[1] == 0:
                current_direction = (current_direction - 1) % 4
            elif result[1] == 1:
                current_direction = (current_direction + 1) % 4

            if current_direction == 0:
                current_pos = (current_pos[0], current_pos[1] + 1)
            elif current_direction == 1:
                current_pos = (current_pos[0] + 1, current_pos[1])
            elif current_direction == 2:
                current_pos = (current_pos[0], current_pos[1] - 1)
            elif current_direction == 3:
                current_pos = (current_pos[0] - 1, current_pos[1])

    print(len(set(drawn_tiles)))
    max_x = max([x[0] for x in drawn_tiles])
    min_x = min([x[0] for x in drawn_tiles])
    max_y = max([x[1] for x in drawn_tiles])
    min_y = min([x[1] for x in drawn_tiles])
    for y in range(max_y, min_y - 1, -1):
        print(
            "".join(['█' if (x, y) in color_map and color_map[(x, y)] == 1 else ' ' for x in range(min_x, max_x + 1)])
        )


if __name__ == '__main__':
    main()
