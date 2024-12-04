import re
import math

with open('input.txt') as rf:
    sorts, parts = rf.read().split('\n\n')

sorts = {s.split('{')[0]: s.split('{')[1][:-1].split(',') for s in sorts.split('\n')}
print(sorts)
range_overlap = lambda x, y: range(max(x[0], y[0]), min(x[-1], y[-1])+1)
mult_ranges = lambda lst: math.prod([x[-1] - x[0] + 1 for x in lst])


def get_next(p, k='in', reverse=False):
    x, m, a, s = re.findall(r'\d+', p)
    xmas = {'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)}
    # print(xmas)
    if k in 'AR':
        return sum(xmas.values()) if k == 'A' else 0
    for step in sorts[k]:
        if ':' not in step:
            if step in 'AR':
                return sum(xmas.values()) if step == 'A' else 0
            return get_next(p, step)
        cond, res_key = step.split(':')
        if '<' in cond:
            if xmas[cond[0]] < int(cond.split('<')[1]):
                return get_next(p, k=res_key)
        if '>' in cond:
            if xmas[cond[0]] > int(cond.split('>')[1]):
                return get_next(p, k=res_key)

ttl_opts = 0


def get_prev(k, steps, wanted_key='A', xmas=''):
    global ttl_opts
    # xmas = {'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)}
    for step_indx, step in enumerate(steps[::-1]):
        if ':' not in step:
            if step != wanted_key:
                continue
            # TODO: Include all other options when 'A' is the last element
            options = work_way_back(k, steps[::-1][step_indx+1:], wanted_key, xmas)  # TODO: Work your way back
            print(f'1.{options=}')
            if options:
                ttl_opts += options
                print(f"{ttl_opts=}")
            continue  # ?

        cond, res_key = step.split(':')
        if res_key == wanted_key:
            # print('END', step)
            options = work_way_back(k, steps[::-1][step_indx:], wanted_key, xmas)  # TODO: Work your way back
            if options:
                print(f'2.{options=}')
                ttl_opts += options

    # if wanted_key == 'A':
    #     print('returning', ttl_opts)
    #     return ttl_opts

def work_way_back(k, steps, wanted_key, xmas=''):
    # TODO: Iterate back over keys (k)
    '''
    TODO: 'lnx': ['m>1548:A', 'A'] when there are two A's then merge the xmas...
    '''
    if not xmas:
        xmas = {l: range(1, 4001) for l in 'xmas'}
    for step in steps:
        print(f"{step=}")
        cond, res_key = step.split(':')
        if res_key == wanted_key:
            if '<' in cond:  # <
                rng1 = range(1, int(cond.split('<')[1]))
                rng = range_overlap(rng1, xmas[cond[0]])
                xmas[cond[0]] = rng

            elif '>' in cond:  # >
                rng1 = range(int(cond.split('>')[1]) + 1, 4001)
                rng = range_overlap(rng1, xmas[cond[0]])
                xmas[cond[0]] = rng

        elif res_key != wanted_key:  # 'R' or a key, e.g. 'px'
            if '<' in cond:  # >=
                rng1 = range(int(cond.split('<')[1]), 4001)
                rng = range_overlap(rng1, xmas[cond[0]])
                xmas[cond[0]] = rng

            elif '>' in cond:  # <=
                # rng1 = range(1, int(cond.split('>')[1]) + 1)
                rng1 = range(1, int(cond.split('>')[1]) + 1)
                rng = range_overlap(rng1, xmas[cond[0]])
                xmas[cond[0]] = rng


    print(k, xmas)
    # if k != 'in':
    if k == 'in':
        return mult_ranges(xmas.values())
    # TODO: Get to 'in' key
    for new_k, steps in sorts.items():
        get_prev(new_k, steps, k, xmas)


ttl = 0
for p in parts.split('\n'):
    acc = get_next(p)
    ttl += acc
print(ttl)

for k, steps in sorts.items():
    get_prev(k, steps)
print(ttl_opts)
