import math
from timeit import default_timer as timer
import numpy as np

def main():
    with open('day_16.input') as input_file:
        base_pattern = [0, 1, 0, -1]
        raw_input_data = input_file.readline().strip()
        # raw_input_data = "".join([input_file.readline().strip()] * 10000)
        # raw_input_data = "".join(['03036732577212944063491565474664']*10000)
        # raw_input_data = "90871223585914546619083218645595"

        input_data = [int(x) for x in str(raw_input_data)]
        index_offset = int("".join([str(x) for x in input_data[:7]]))
        # input_data = input_data[index_offset:]
        phases = 100
        length = len(input_data)
        print('length', length)
        patterns = []
        for p in range(length):
            pattern = []
            for pat_val in base_pattern:
                for _ in range(p + 1):
                    pattern.append(pat_val)
            pattern = pattern * (math.ceil(length / (4 * (p+1))) + 1)
            patterns.append(pattern[1:length + 1])
        a = np.array(patterns)

        start = timer()
        for phase in range(phases):
            b = np.array(input_data)
            input_data = [int(str(x)[-1]) for x in a.dot(b)]
        end = timer()
        print(end - start)
        # print("".join([str(x) for x in result]))
        data = "".join([str(x) for x in input_data])
        print(data)


if __name__ == '__main__':
    main()
