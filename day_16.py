def main():
    with open('day_16.input') as input_file:
        base_pattern = [0, 1, 0, -1]
        pattern_offset = 1
        # raw_input_data = input_file.readline().strip()
        raw_input_data = "".join([input_file.readline().strip()] * 10000)
        raw_input_data = "".join(['03036732577212944063491565474664'] * 10000)

        input_data = [int(x) for x in str(raw_input_data)]
        length = len(input_data)
        index_offset = int("".join([str(x) for x in input_data[:7]]))
        input_data = input_data[index_offset : index_offset+8]
        pattern_offset = index_offset
        print(index_offset)
        phases = 100
        for phase in range(phases):
            print(phase)
            result = []
            pattern_offset = 1
            for p in range(length)[index_offset : index_offset+8]:
                pattern = []
                for pat_val in base_pattern:
                    for _ in range(p + 1):
                        pattern.append(pat_val)
                iteration_result = []
                for i in range(len(input_data)):
                    iteration_result.append(pattern[(i+pattern_offset) % len(pattern)] * input_data[i])

                result.append(int(str(sum(iteration_result))[-1]))
            input_data = result.copy()
        # print("".join([str(x) for x in result]))
        data = "".join([str(x) for x in result])
        print(data)





if __name__ == '__main__':
    main()
