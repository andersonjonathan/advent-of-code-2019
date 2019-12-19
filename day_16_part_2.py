from timeit import default_timer as timer


def main():
    with open('day_16.input') as input_file:
        raw_input_data = "".join([input_file.readline().strip()] * 10000)
        input_data = [int(x) for x in str(raw_input_data)]

        index_offset = int("".join([str(x) for x in input_data[:7]]))
        input_data = input_data[index_offset:][::-1]
        phases = 100
        length = len(input_data)
        print('length', length)

        start = timer()
        for phase in range(phases):
            tmp = 0
            for idx, data in enumerate(input_data):
                tmp += data
                input_data[idx] = tmp % 10

        input_data.reverse()
        end = timer()

        print(end - start)
        data = "".join([str(x) for x in input_data][:8])
        print(data)


if __name__ == '__main__':
    main()
