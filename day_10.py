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
    with open('day_10_test_1.input') as input_file:
        plan = [list(x.strip()) for x in input_file.readlines()]
        asteroids = []
        for row_index, row in enumerate(plan):
            for col_index, col in enumerate(row):
                if col == '#':
                    asteroids.append([col_index, row_index])

        for current_asteroid in asteroids:
            offseted_astroids = []
            factorised_asteroid_positions = []
            for asteroid in asteroids:
                if current_asteroid == asteroid:
                    continue
                offseted_astroid = [asteroid[0] - current_asteroid[0], asteroid[1] - current_asteroid[1]]
                x_factors = factors(offseted_astroid[0])
                y_factors = factors(offseted_astroid[1])
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
                offseted_astroids.append(offseted_astroids)
                factorised_asteroid_positions.append(
                    (offseted_astroid[0]/abs(multiplier), offseted_astroid[1]/abs(multiplier))
                )
            current_asteroid.append(len(set(factorised_asteroid_positions)))
        print(sorted(asteroids, key=lambda x: x[2], reverse=True))


if __name__ == '__main__':
    main()