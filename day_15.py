import random

from intcode import IntCodeComputer


def get_tile(tile, color_map):
    if tile in color_map:
        if color_map[tile] == 0:
            return '#'
        elif color_map[tile] == 1:
            return '█'
        elif color_map[tile] == 2:
            return 'O'
        elif color_map[tile] == 3:
            return 'X'
        else:
            return ' '
    else:
        return ' '


def get_new_position(pos, instruction):
    if instruction == 1:  # North
        return pos[0], pos[1] + 1
    elif instruction == 2:  # South
        return pos[0], pos[1] - 1
    elif instruction == 3:  # West
        return pos[0] - 1, pos[1]
    elif instruction == 4:  # East
        return pos[0] + 1, pos[1]


def print_map(game_map):
    max_x = max([x[0] for x in game_map])
    min_x = min([x[0] for x in game_map])
    max_y = max([x[1] for x in game_map])
    min_y = min([x[1] for x in game_map])

    for y in range(min_y, max_y + 1):
        print(
            "".join([get_tile((x, y), game_map) for x in range(min_x, max_x + 1)])
        )


def find_shortest_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


def convert_to_graph(game_map):
    graph = {}
    for pos in game_map:
        if game_map[pos] != 0:
            neighbours = []
            if (pos[0] - 1, pos[1]) in game_map and game_map[(pos[0] - 1, pos[1])] != 0:
                neighbours.append((pos[0] - 1, pos[1]))
            if (pos[0] + 1, pos[1]) in game_map and game_map[(pos[0] + 1, pos[1])] != 0:
                neighbours.append((pos[0] + 1, pos[1]))
            if (pos[0], pos[1] - 1) in game_map and game_map[(pos[0], pos[1] - 1)] != 0:
                neighbours.append((pos[0], pos[1] - 1))
            if (pos[0], pos[1] + 1) in game_map and game_map[(pos[0], pos[1] + 1)] != 0:
                neighbours.append((pos[0], pos[1] + 1))
            graph[pos] = neighbours
    return graph
            
            
def main():
    computer = IntCodeComputer('day_15.input')
    droid = (0, 0)
    game_map = {droid: 3}
    instructions = []

    not_visited = {droid: [1, 2, 3, 4]}

    while True:
        result = []
        if droid in not_visited and len(not_visited[droid]) > 0:
            back_tracking = False
            instruction = not_visited[droid].pop()
        else:
            back_tracking = True
            if not instructions:
                # Done
                break

            prev = instructions.pop()
            if prev == 1:
                instruction = 2
            elif prev == 2:
                instruction = 1
            elif prev == 3:
                instruction = 4
            elif prev == 4:
                instruction = 3

        computer.run([instruction], result)

        new_pos = get_new_position(droid, instruction)
        if new_pos not in game_map:
            game_map[new_pos] = result[0]

        if result[0] != 0:
            droid = new_pos
            if not back_tracking:
                instructions.append(instruction)
            if droid not in not_visited:
                not_visited[droid] = [1, 2, 3, 4]
    print_map(game_map)
    oxygen = [x[0] for x in game_map.items() if x[1] == 2][0]
    graph = convert_to_graph(game_map)
    path = find_shortest_path(graph, (0, 0), oxygen)
    print(oxygen)
    print(path)
    print(len(path) - 1)

    max_x = max([x[0] for x in game_map])
    min_x = min([x[0] for x in game_map])
    max_y = max([x[1] for x in game_map])
    min_y = min([x[1] for x in game_map])

    longest_minimum = 0

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in graph:
                longest_minimum = max(longest_minimum, len(find_shortest_path(graph, (x, y), oxygen)) - 1)
    print(longest_minimum)


if __name__ == '__main__':
    main()
