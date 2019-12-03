import math

with open('day_1.input') as input_file:
    input_data = [int(x.strip()) for x in input_file.readlines()]

    total_sum = 0
    for module_weight in input_data:
        sum = math.floor(module_weight / 3) - 2
        total_sum += sum
        while sum > 0:
            sum = math.floor(sum / 3) - 2
            if sum < 0:
                break
            total_sum += sum

    print(total_sum)
