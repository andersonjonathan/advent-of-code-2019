from functools import reduce
from operator import mul


def factors(n):
    list_of_factors = []
    if n < 0:
        list_of_factors.append(-1)
        n *= -1
    while n > 1:
        for i in range(2, int(n) + 1):
            if n % i == 0:
                n /= i
                list_of_factors.append(int(i))
                break
    if len(list_of_factors) == 0:
        list_of_factors.append(n)
    return list_of_factors


def main():
    with open('day_12.input') as input_file:
        positions = [[int(y[2:]) for y in x.strip()[1:-1].split(', ')] for x in input_file.readlines()]
        velocities = [[0 for _ in range(3)] for _ in range(4)]
        initial_value = (*positions[0], *positions[1], *positions[2], *positions[3], *velocities[0], *velocities[1], *velocities[2], *velocities[3])
        steps = 100
        def print_data(step):
            print(f"After {step} steps:")
            for i in range(len(positions)):
                print(f"pos=<x={positions[i][0]}, y={positions[i][1]}, z={positions[i][2]}>, "
                      f"vel=<x={velocities[i][0]}, y={velocities[i][1]}, z={velocities[i][2]}>")

        def print_energy(step):
            print(f"Energy after {step} steps:")
            total_sum = 0
            for i in range(len(positions)):
                pot = abs(positions[i][0]) + abs(positions[i][1]) + abs(positions[i][2])
                kin = abs(velocities[i][0]) + abs(velocities[i][1]) + abs(velocities[i][2])
                total_sum += pot * kin
                print(f"pot: {pot};   kin: {kin};   total: {pot} * {kin} = {pot * kin}")
            print(f"Total energy: {total_sum}")
        step = 0

        steps_until_initial_value = [None for _ in range(4*6)]
        # for step in range(steps):
        #     velocities_diff = [[0 for _ in range(3)] for _ in range(4)]
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
            data = (*positions[0], *positions[1], *positions[2], *positions[3], *velocities[0], *velocities[1], *velocities[2], *velocities[3])
            for index, value in enumerate(data):
                if value == initial_value[index] and steps_until_initial_value[index] is None:
                    steps_until_initial_value[index] = step
            if None not in steps_until_initial_value:
                break
            step += 1
        print(set(steps_until_initial_value))
        print([factors(f) for f in set(steps_until_initial_value)])


if __name__ == '__main__':
    main()
