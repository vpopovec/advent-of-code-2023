import re

with open('input.txt') as rf:
    sorts, parts = rf.read().split('\n\n')

sorts = {s.split('{')[0]: s.split('{')[1][:-1].split(',') for s in sorts.split('\n')}
print(sorts)


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


def get_prev(k, steps):
    # xmas = {'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)}
    for step in steps[::-1]:
        if ':' not in step:
            if step in 'A':



ttl = 0
for p in parts.split('\n'):
    acc = get_next(p)
    ttl += acc
print(ttl)

for k, steps in sorts.items():
    get_prev(k, steps)
