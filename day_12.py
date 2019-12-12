

def main():
    with open('day_12.input') as input_file:
        positions = [[int(y[2:]) for y in x.strip()[1:-1].split(', ')] for x in input_file.readlines()]
        velocities = [[0 for _ in range(3)] for _ in range(4)]
        steps = 1000

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

        for step in range(steps):
            velocities_diff = [[0 for _ in range(3)] for _ in range(4)]
            for i in range(len(positions)):
                for j in range(len(positions)):
                    if i == j:
                        continue
                    for pos in range(3):
                        if positions[i][pos] > positions[j][pos]:
                            velocities[i][pos] -= 1
                            velocities_diff[i][pos] -= 1
                        elif positions[i][pos] < positions[j][pos]:
                            velocities[i][pos] += 1

            for i in range(len(positions)):
                for pos in range(3):
                    positions[i][pos] += velocities[i][pos]
        print_energy(steps)


if __name__ == '__main__':
    main()
