import math


def main():
    with open('day_14.input') as input_file:
        data = [[[t.split(' ') for t in s.strip().split(', ')] for s in reaction.split('=>')] for reaction in input_file.readlines()]
        reactions = {}
        for input_data, output_data in data:
            requires = []
            for mineral in input_data:
                requires.append((mineral[1], int(mineral[0])))
            reaction_info = {
                'quantity': int(output_data[0][0]),
                'requires': requires
            }
            if output_data[0][1] in reactions:
                print('duplicate')
            reactions[output_data[0][1]] = reaction_info

        left_over = {}
        req_list = [('FUEL', 1)]
        while not all([t[0] == 'ORE' for t in req_list]):
            req = None
            for req_index in range(len(req_list)):
                if req_list[req_index][0] != 'ORE':
                    req = req_list.pop(req_index)
                    break
            if req:
                multiplier = 0
                reaction_data = reactions[req[0]]
                already_produced = 0
                if req[0] in left_over:
                    already_produced = left_over[req[0]]
                    left_over[req[0]] = 0
                while (req[1] - already_produced) > reaction_data['quantity'] * multiplier:
                    multiplier += 1
                left_over[req[0]] = (reaction_data['quantity'] * multiplier) - (req[1] - already_produced)
                for mineral, quantity in reaction_data['requires']:
                    req_list.append((mineral, quantity * multiplier))
        ore = sum([req[1] for req in req_list])

        print(ore, left_over)


if __name__ == '__main__':
    main()
