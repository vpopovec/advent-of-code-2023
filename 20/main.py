with open('input.txt') as rf:
    rows = rf.read().split('\n')
swap = {0: 1, 1: 0}

d = {}
for r in rows:
    nm = r.split()[0] if r.split()[0][0] not in '%&' else r.split()[0][1:]
    d[nm] = {'tp': r[0], 'dest': r.split('-> ')[1].split(', '), 'on': 0, 'inputs': {}}

for nm in d:
    if d[nm]['tp'] == '&' and not d[nm]['inputs']:
        for nm2 in d:
            # Fill default values
            if nm in d[nm2]['dest']:
                d[nm]['inputs'][nm2] = 0

for k, vl in d.items():
    print(k, vl)

ttl_pulses = {0: 0, 1: 0}
end_cycle = 0
# for j in range(1, 1001:
wanted = {'st', 'tn', 'hh', 'dt'}
for j in range(1, 5000):
    # TODO: Count button presses
    todo = [('broadcaster', 0, '')]
    # rx_num = 0
    for i in range(10**9):  # TODO: try increasing
        # print(f'todo {j}', todo)
        if not todo:  # Press button again
            # print(ttl_pulses)
            break
        nm, high_pulse, prev_nm = todo.pop(0)
        # if nm == 'rx' and not high_pulse:
        #     rx_num += 1

        ttl_pulses[high_pulse] += 1
        if nm not in d:
            continue

        # # Check all buttons are off
        # end = 1
        # for n in d:
        #     if d[n]['tp'] == '%' and d[n]['on']:
        #         end = 0
        #         break

        if d[nm]['tp'] == '%' and not high_pulse:
            d[nm]['on'] = swap[d[nm]['on']]

        if d[nm]['tp'] == '&':
            d[nm]['inputs'][prev_nm] = high_pulse

        for dest in d[nm]['dest']:
            # if not end_cycle:
            if d[nm]['tp'] == 'b':
                todo.append((dest, high_pulse, nm))
            if d[nm]['tp'] == '%' and not high_pulse:
                todo.append((dest, 1 if d[nm]['on'] else 0, nm))
            if d[nm]['tp'] == '&':
                todo.append((dest, 0 if all(d[nm]['inputs'].values()) else 1, nm))

        # Check all buttons are off
        end = 1
        for n in d:
            if d[n]['tp'] == '%' and d[n]['on']:
                end = 0
                break
        if end and 'broadcaster' not in [nm, prev_nm]:
            end_cycle = 1
            #     continue
            # for td in todo:
            #     ttl_pulses[td[1]] += 1
            # print("SHOULD BREAK", ttl_pulses, f"{todo}")
            # if end_cycle and not todo:
            #     break

    for nm in wanted:
        # print('check', nm, d[nm])
        if d[nm]['inputs'] and all(d[nm]['inputs'].values()):
            print('FOUND', nm, j, d[nm])

    # if rx_num == 1:
    #     break
    # if j % 1 == 0:
    #     print(f"{rx_num=} xxx")
        # print(f"button={j}", ttl_pulses)
    # if end_cycle:
    #     break

print('presses:', j, f"{ttl_pulses=}")
to_mult = 1000 / j
res = ttl_pulses[0] * to_mult * ttl_pulses[1] * to_mult
print(res)