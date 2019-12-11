import itertools
import unittest
from intcode import IntCodeComputer


class TestIntCodeComputer(unittest.TestCase):
    def test_day_2_part_1(self):
        computer = IntCodeComputer('day_2.input')
        program, counter, offset = computer.save()
        program[1] = 12
        program[2] = 2
        computer.load(program)
        computer.run()
        program, counter, offset = computer.save()
        self.assertEqual(3716293, program[0])

    def test_day_2_part_2(self):
        value = None
        for i in range(0, 100):
            for j in range(0, 100):
                computer = IntCodeComputer('day_2.input')
                program, counter, offset = computer.save()
                program[1] = i
                program[2] = j
                computer.load(program)
                computer.run()
                program, counter, offset = computer.save()
                if program[0] == 19690720:
                    value = i * 100 + j
                    break
            if value:
                break
        self.assertEqual(6429, value)

    def test_day_5_part_1(self):
        computer = IntCodeComputer('day_5.input')
        result = []
        computer.run(input_data=[1], output_data=result)
        self.assertEqual(0, result[0])
        self.assertEqual(0, result[1])
        self.assertEqual(0, result[2])
        self.assertEqual(0, result[3])
        self.assertEqual(0, result[4])
        self.assertEqual(0, result[5])
        self.assertEqual(0, result[6])
        self.assertEqual(0, result[7])
        self.assertEqual(0, result[8])
        self.assertEqual(7157989, result[9])

    def test_day_5_part_2(self):
        computer = IntCodeComputer('day_5.input')
        result = []
        computer.run(input_data=[5], output_data=result)
        self.assertEqual(7873292, result[0])

    def test_day_7_part_1(self):
        result = []
        buss_map = {}
        input_values = [0, 1, 2, 3, 4]
        for r in input_values:
            buss_map[r] = IntCodeComputer('day_7.input')
            buss_map[r].run(input_data=[r])
            buss_map[r].save()
        for busses in itertools.permutations(input_values):
            for r in input_values:
                buss_map[r].reset()
            previous_output = 0
            for r in busses:
                output_data = []
                buss_map[r].run(input_data=[previous_output], output_data=output_data)
                previous_output = output_data[0]
            result.append((previous_output, busses))
        result = sorted(result, key=lambda r: r[0], reverse=True)
        self.assertEqual(99376, result[0][0])

    def test_day_7_part_2(self):
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
        self.assertEqual(8754464, result[0][0])

    def test_day_9_part_1(self):
        computer = IntCodeComputer('day_9.input')
        output_data = []
        computer.run(input_data=[1], output_data=output_data)
        self.assertEqual(2752191671, output_data[0])

    def test_day_9_part_2(self):
        computer = IntCodeComputer('day_9.input')
        output_data = []
        computer.run(input_data=[2], output_data=output_data)
        self.assertEqual(87571, output_data[0])

    def test_day_11_part_1(self):
        computer = IntCodeComputer('day_11.input')
        drawn_tiles = []
        color_map = {}
        current_pos = (0, 0)
        current_direction = 0  # 0=up, 1=right, 2=down, 3=left
        exit_code = 1
        while exit_code != 0:
            input_data = [color_map[current_pos] if current_pos in color_map else 0]
            result = []
            exit_code = computer.run(input_data=input_data, output_data=result)
            if len(result) > 0:
                color_map[current_pos] = result[0]
                drawn_tiles.append(current_pos)
                if result[1] == 0:
                    current_direction = (current_direction - 1) % 4
                elif result[1] == 1:
                    current_direction = (current_direction + 1) % 4

                if current_direction == 0:
                    current_pos = (current_pos[0], current_pos[1] + 1)
                elif current_direction == 1:
                    current_pos = (current_pos[0] + 1, current_pos[1])
                elif current_direction == 2:
                    current_pos = (current_pos[0], current_pos[1] - 1)
                elif current_direction == 3:
                    current_pos = (current_pos[0] - 1, current_pos[1])
        self.assertEqual(2343, len(set(drawn_tiles)))

    def test_day_11_part_2(self):
        computer = IntCodeComputer('day_11.input')
        drawn_tiles = []
        color_map = {(0, 0): 1}
        current_pos = (0, 0)
        current_direction = 0  # 0=up, 1=right, 2=down, 3=left
        exit_code = 1
        while exit_code != 0:
            input_data = [color_map[current_pos] if current_pos in color_map else 0]
            result = []
            exit_code = computer.run(input_data=input_data, output_data=result)
            if len(result) > 0:
                color_map[current_pos] = result[0]
                drawn_tiles.append(current_pos)
                if result[1] == 0:
                    current_direction = (current_direction - 1) % 4
                elif result[1] == 1:
                    current_direction = (current_direction + 1) % 4

                if current_direction == 0:
                    current_pos = (current_pos[0], current_pos[1] + 1)
                elif current_direction == 1:
                    current_pos = (current_pos[0] + 1, current_pos[1])
                elif current_direction == 2:
                    current_pos = (current_pos[0], current_pos[1] - 1)
                elif current_direction == 3:
                    current_pos = (current_pos[0] - 1, current_pos[1])

        max_x = max([x[0] for x in drawn_tiles])
        min_x = min([x[0] for x in drawn_tiles])
        max_y = max([x[1] for x in drawn_tiles])
        min_y = min([x[1] for x in drawn_tiles])
        drawn_result = []
        for y in range(max_y, min_y - 1, -1):
            drawn_result.append("".join(
                ['█' if (x, y) in color_map and color_map[(x, y)] == 1 else ' ' for x in range(min_x, max_x + 1)]
            ))
        self.assertListEqual([
            "   ██ ████ ███  ████ ███  ███  █  █ █  █   ",
            "    █ █    █  █ █    █  █ █  █ █  █ █  █   ",
            "    █ ███  ███  ███  █  █ ███  █  █ ████   ",
            "    █ █    █  █ █    ███  █  █ █  █ █  █   ",
            " █  █ █    █  █ █    █ █  █  █ █  █ █  █   ",
            "  ██  █    ███  ████ █  █ ███   ██  █  █   "
        ], drawn_result)


if __name__ == '__main__':
    unittest.main()
