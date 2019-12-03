def convert_string_to_path(data):
    return data.split(',')


def convert_path_to_coordinates(data, origo=(0, 0)):
    start_point = (origo[0], origo[1], 0)
    path = [start_point]
    point = [origo[0], origo[1]]
    steps = 0
    for d in data:
        instruction = d[0]
        value = int(d[1:])
        if instruction == 'U':
            point[1] += value
        elif instruction == 'D':
            point[1] -= value
        elif instruction == 'R':
            point[0] += value
        elif instruction == 'L':
            point[0] -= value
        steps += value
        path.append((point[0], point[1], steps))
    return path


def find_intersection(line_1, line_2):
    x1_0, y1_0, steps_1 = line_1[0]
    x1_1, y1_1, _ = line_1[1]
    x2_0, y2_0, steps_2 = line_2[0]
    x2_1, y2_1, _ = line_2[1]

    if x1_0 == x1_1:  # |
        if y2_0 == y2_1:  # -
            if (x2_0 < x1_0 < x2_1 or x2_1 < x1_0 < x2_0) and (y1_0 < y2_0 < y1_1 or y1_1 < y2_0 < y1_0):
                return x1_0, y2_0, steps_1 + steps_2 + abs(y1_0 - y2_0) + abs(x2_0 - x1_0)
    else:  # -
        if x2_0 == x2_1:  # |
            if (x1_0 < x2_0 < x1_1 or x1_1 < x2_0 < x1_0) and (y2_0 < y1_0 < y2_1 or y2_1 < y1_0 < y2_0):
                return x2_0, y1_0, steps_1 + steps_2 + abs(y2_0 - y1_0) + abs(x1_0 - x2_0)
    return None


def find_intersections(path_1, path_2):
    intersections = []
    prev_point_1 = None
    prev_point_2 = None
    for point_1 in path_1:
        if prev_point_1:
            for point_2 in path_2:
                if prev_point_2:
                    intersection = find_intersection((prev_point_1, point_1), (prev_point_2, point_2))
                    if intersection:
                        intersections.append(intersection)
                prev_point_2 = point_2
        prev_point_1 = point_1
    return intersections


def get_manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def main():
    with open('day_3.input') as input_file:
        input_data_1 = input_file.readline().strip()
        input_data_2 = input_file.readline().strip()
        # input_data_1 = 'R8,U5,L5,D3'
        # input_data_2 = 'U7,R6,D4,L4'
        path_1 = convert_string_to_path(input_data_1)
        path_2 = convert_string_to_path(input_data_2)
        poly_1 = convert_path_to_coordinates(path_1)
        poly_2 = convert_path_to_coordinates(path_2)
        intersections = find_intersections(poly_1, poly_2)
        # intersections = sorted(intersections, key=lambda x: get_manhattan_distance(x), reverse=False)
        intersections = sorted(intersections, key=lambda x: x[2], reverse=False)
        print(intersections)
        print(get_manhattan_distance(intersections[0]))
        print(intersections[0][2])


if __name__ == '__main__':
    main()
