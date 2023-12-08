import re
from math import lcm
from collections import defaultdict

with open('input.txt') as rf:
    txt = [ln.strip() for ln in rf.readlines()]
    steps, txt = txt[0], txt[1:]

path = []

# codes = defaultdict(set)
codes = {}
start_nodes = {}
for ln in txt[1:]:
    start, lft, rgt = re.findall(r'\w+', ln)
    codes[start] = (lft, rgt)
    if start[-1] == 'A':
        start_nodes[start] = start
    # if start == lft == rgt:
    #     print(f"Skipping useless {ln=}")
    #     continue
    # print(ln)
    # print(start, lft, rgt)
    # codes[lft].append(start)
    # if rgt != lft:
    #     codes[rgt].append(start)

print(codes)
print(len(steps))
print(start_nodes)
total_steps = 0
lcms = []
for i in range(10 ** 8):
    for step in steps:
        total_steps += 1
        # next_in_path = codes[path[-1]][0] if step == 'L' else codes[path[-1]][1]
        # path.append(next_in_path)
        to_del = []
        for start_node in start_nodes:
            last_node = start_nodes[start_node]
            next_in_path = codes[last_node][0] if step == 'L' else codes[last_node][1]
            start_nodes[start_node] = next_in_path
            if next_in_path.endswith('Z'):
                to_del.append(start_node)

        for node_to_del in to_del:
            last_node = start_nodes.pop(node_to_del)
            lcms.append(total_steps)

        if not start_nodes:
            break
        # if all([node[-1] == 'Z' for node in start_nodes.values()]):
        #     break
    if not start_nodes:
        break
    # if all([node[-1] == 'Z' for node in start_nodes.values()]):
    #     break
print(start_nodes)
print(f"{lcms=}")
print(f"{lcm(*lcms)=}")
# path = ['AAA']
# for step in steps:
#     next_in_path = codes[path[-1]][0] if step == 'L' else codes[path[-1]][1]
#     path.append(next_in_path)
#     if path[-1] == 'ZZZ':
#         break
# print(f"{path=}")
# print(f"{len(path) -1}")


# def iterate(path):
#     if 'AAA' in codes[path[-1]]:
#         path.append('AAA')
#         return path
#     for possible_path in codes[path[-1]]:
#         path.append(possible_path)
#         return iterate(path)
#
#
# path = ['ZZZ']
# res = iterate(path)
# print(f"{res=}")
# print(len(res) - 1)