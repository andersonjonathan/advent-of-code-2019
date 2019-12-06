def calculate_distance(node_1, node_2):
    common_bodies = 0
    for x in range(len(node_1)):
        if node_1[x] != node_2[x]:
            common_bodies = x
            break
    return len(node_1) + len(node_2) - (2 * common_bodies)


def main():
    with open('day_6.input') as input_file:
        input_data = [x.strip().split(')') for x in input_file.readlines()]
        nr_of_orbits = 0
        bodies = []
        current_body = 'COM'
        orbit_info = {
            'COM': [],
        }
        while True:
            start_nodes = [x[1] for x in input_data if x[0] == current_body]
            for x in start_nodes:
                orbit_info[x] = list(orbit_info[current_body]) + [current_body]
            nr_of_orbits += (len(start_nodes) * (len(orbit_info[current_body]) + 1))
            bodies += start_nodes
            if len(bodies) > 0:
                current_body = bodies.pop()
            else:
                break

        print(nr_of_orbits)
        print(calculate_distance(orbit_info['SAN'], orbit_info['YOU']))


if __name__ == '__main__':
    main()
