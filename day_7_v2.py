import itertools

from intcode import IntCodeComputer


def main():
    """Main function that loads a program to the 'computer'."""
    result = []
    buss_map = {}
    input_values = [5, 6, 7, 8, 9]
    for r in input_values:
        buss_map[r] = IntCodeComputer('day_7.input')
        buss_map[r].run(input_data=[r])
        buss_map[r].save()
    for busses in itertools.permutations(input_values):
        for r in input_values:
            buss_map[r].reset()
        previous_output = 0
        has_exited = False
        while not has_exited:
            for r in busses:
                output_data = []
                out = buss_map[r].run(input_data=[previous_output], output_data=output_data)
                if out == 0:
                    has_exited = True
                previous_output = output_data[0]
            result.append((previous_output, busses))
    result = sorted(result, key=lambda r: r[0], reverse=True)
    print(result[0])


if __name__ == '__main__':
    main()
