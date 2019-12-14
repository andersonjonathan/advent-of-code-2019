import math


def main():
    with open('day_14.input') as input_file:
        data = [[[t.split(' ') for t in s.strip().split(', ')] for s in reaction.split('=>')] for reaction in
                input_file.readlines()]
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
        req_list = [('ORE', 0)]
        multiplier = 3440
        nr_of_fuel = 1000 * multiplier
        left_over = {'FUEL': 0, 'JPKGW': 5, 'STJNH': 2, 'JBPFQ': 0, 'GXSTP': 0, 'QRFRQ': 0, 'ZVBX': 0, 'HJNP': 0,
                     'DVRSL': 2, 'KZBW': 0, 'RVXMK': 1, 'VHJM': 0, 'MCQK': 0, 'RMRPX': 2, 'NMWV': 0, 'MXWK': 3,
                     'ZLVG': 1, 'JFSDT': 3, 'SGBQP': 0, 'GWDVS': 2, 'HKWV': 3, 'CPXW': 0, 'CKRXP': 1, 'QTRJ': 0,
                     'WQCSD': 2, 'PZNJ': 0, 'QXNK': 0, 'ZKDG': 0, 'DHWR': 0, 'WCJM': 0, 'BSKC': 3, 'RMHKH': 0,
                     'SGSBS': 6, 'DHRN': 7, 'KMHG': 2, 'LNWD': 0, 'XTLB': 2, 'XVQDV': 2, 'RBCPD': 0, 'XVPB': 2,
                     'JCVCG': 1, 'ZRKZ': 2, 'JFRPS': 1, 'DNDTC': 3, 'SLPZ': 3, 'KHLSP': 1, 'DGDNX': 0, 'TPXQR': 4,
                     'GVWZR': 5, 'PBJMZ': 0, 'TLKRB': 1, 'VFTDK': 0, 'XKSXK': 1, 'TQXFD': 0, 'PQXHB': 3, 'WLMCM': 0,
                     'QDTNQ': 0, 'MGHBF': 2, 'XPFRX': 0, 'FDGBF': 3}
        total_ore = 290279939 * multiplier
        for x, y in left_over.items():
            left_over[x] = y * multiplier
        while total_ore < 1000000000000:
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
            total_ore += ore
            nr_of_fuel += 1
            print(nr_of_fuel, total_ore, left_over)


if __name__ == '__main__':
    main()
