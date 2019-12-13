from intcode import IntCodeComputer


def get_tile(tile, color_map):
    if tile in color_map:
        if color_map[tile] == 1:
            return '#'
        elif color_map[tile] == 2:
            return '█'
        elif color_map[tile] == 3:
            return '_'
        elif color_map[tile] == 4:
            return 'o'
        else:
            return ' '
    else:
        return ' '


def main():
    computer = IntCodeComputer('day_13.input')
    memory, counter, offset = computer.save()
    memory[0] = 2
    computer.load(memory)
    in_data = []
    out = 1
    result = []
    ball = None
    player = None
    while out:
        out = computer.run(input_data=in_data, output_data=result)
        game_plan = [result[x:x+3] for x in range(0, len(result), 3)]
        color_map = {}
        for pixel in game_plan:
            if pixel[0] == -1 and pixel[1] == 0 and out == 0:
                print(pixel[2])
            if pixel[2] == 3:
                player = (pixel[0], pixel[1])
            if pixel[2] == 4:
                ball = (pixel[0], pixel[1])
            color_map[(pixel[0], pixel[1])] = pixel[2]
        # print([x[1] for x in color_map.items()].count(2))
        max_x = max([x[0] for x in game_plan])
        min_x = min([x[0] for x in game_plan])
        max_y = max([x[1] for x in game_plan])
        min_y = min([x[1] for x in game_plan])

        for y in range(min_y, max_y):
            print(
                "".join([get_tile((x, y), color_map) for x in range(min_x, max_x + 1)])
            )
        if out == 1 and ball and player:
            if ball[0] < player[0]:
                in_data = [-1]
            elif ball[0] > player[0]:
                in_data = [1]
            else:
                in_data = [0]


if __name__ == '__main__':
    main()
