from functools import reduce
from math import atan2, pi, sqrt
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


def get_angle(a, b, c):
    angle = atan2(c[1]-b[1], c[0]-b[0]) - atan2(a[1]-b[1], a[0]-b[0])
    return angle + (2 * pi) if angle < 0 else angle


def main():
    with open('day_10.input') as input_file:
        plan = [list(x.strip()) for x in input_file.readlines()]
        asteroids = []
        for row_index, row in enumerate(plan):
            for col_index, col in enumerate(row):
                if col == '#':
                    asteroids.append([col_index, row_index])

        for current_asteroid in asteroids:
            offset_asteroids = []
            factorised_asteroid_positions = []
            for asteroid in asteroids:
                if current_asteroid == asteroid:
                    continue
                offset_asteroid = [asteroid[0] - current_asteroid[0], asteroid[1] - current_asteroid[1]]
                x_factors = factors(offset_asteroid[0])
                assert reduce(mul, x_factors) == offset_asteroid[0]
                y_factors = factors(offset_asteroid[1])
                assert reduce(mul, y_factors) == offset_asteroid[1]
                common_factors = []
                i = 0
                while True:
                    if x_factors[i] in y_factors:
                        y_factors.pop(y_factors.index(x_factors[i]))
                        common_factors.append(x_factors.pop(i))
                    else:
                        i += 1
                    if i >= len(x_factors):
                        break
                if common_factors:
                    multiplier = reduce(mul, common_factors)
                else:
                    multiplier = 1

                if offset_asteroid[0] == 0:
                    factorised_asteroid_positions.append((0, int(offset_asteroid[1]/abs(offset_asteroid[1]))))
                    offset_asteroids.append((offset_asteroid, (0, int(offset_asteroid[1]/abs(offset_asteroid[1])))))
                elif offset_asteroid[1] == 0:
                    factorised_asteroid_positions.append((int(offset_asteroid[0]/abs(offset_asteroid[0])), 0))
                    offset_asteroids.append((offset_asteroid, (int(offset_asteroid[0]/abs(offset_asteroid[0])), 0)))
                else:
                    factorised_asteroid_positions.append(
                        (int(offset_asteroid[0]/abs(multiplier)), int(offset_asteroid[1]/abs(multiplier)))
                    )
                    offset_asteroids.append(
                        (offset_asteroid,
                         (int(offset_asteroid[0]/abs(multiplier)), int(offset_asteroid[1]/abs(multiplier)))
                         )
                    )

            current_asteroid.append(len(set(factorised_asteroid_positions)))
            current_asteroid.append(offset_asteroids)
        selected_asteroid = sorted(asteroids, key=lambda x: x[2], reverse=True)[0]

        print((selected_asteroid[0], selected_asteroid[1]), selected_asteroid[2])

        surrounding = selected_asteroid[3]
        surrounding = [(
            get_angle((0, -1), (0, 0), (asteroid[0][0], asteroid[0][1])),
            sqrt((asteroid[0][0]) ** 2 + (asteroid[0][1]) ** 2),
            (asteroid[0][0] + selected_asteroid[0], asteroid[0][1] + selected_asteroid[1]),
            asteroid
        ) for asteroid in surrounding]
        surrounding = sorted(surrounding, key=lambda x: (x[0], x[1]))
        vaporized = []
        left = list(surrounding)
        while True:
            save_to_next_lap = []
            vaporized_this_lap = []
            for asteroid in left:
                if asteroid[3][1] not in vaporized_this_lap:
                    vaporized_this_lap.append(asteroid[3][1])
                    vaporized.append(asteroid[2])
                else:
                    save_to_next_lap.append(asteroid)
            if len(save_to_next_lap) == 0:
                break
            left = save_to_next_lap

        print(vaporized[199])


if __name__ == '__main__':
    main()
