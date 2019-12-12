def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(a, b):
    return int(a * b / gcd(a, b))


def main():
    with open('day_12.input') as input_file:
        positions = [[int(y[2:]) for y in x.strip()[1:-1].split(', ')] for x in input_file.readlines()]
        initial_positions = [pos.copy() for pos in positions]
        velocities = [[0 for _ in range(3)] for _ in range(4)]
        initial_velocities = [[0 for _ in range(3)] for _ in range(4)]

        step = 0
        number_of_steps = {}

        while True:
            for i in range(len(positions)):
                for j in range(len(positions)):
                    if i == j:
                        continue
                    for pos in range(3):
                        if positions[i][pos] > positions[j][pos]:
                            velocities[i][pos] -= 1
                        elif positions[i][pos] < positions[j][pos]:
                            velocities[i][pos] += 1
            for i in range(len(positions)):
                for pos in range(3):
                    positions[i][pos] += velocities[i][pos]

            step += 1
            for i in range(3):
                is_equal = True
                for r in range(4):
                    is_equal = is_equal and positions[r][i] == initial_positions[r][i] and velocities[r][i] == initial_velocities[r][i]
                if is_equal and i not in number_of_steps:
                    number_of_steps[i] = step
                    print(step)

            if len(number_of_steps) == 3:
                break
        print(lcm(lcm(number_of_steps[0], number_of_steps[1]), number_of_steps[2]))


if __name__ == '__main__':
    main()
