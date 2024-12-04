import re
from math import lcm

with open('input.txt') as rf:
    txt = [ln.strip() for ln in rf.readlines()]
    steps, txt = txt[0], txt[1:]


codes = {}
start_nodes = {}
for ln in txt[1:]:
    start, lft, rgt = re.findall(r'\w+', ln)
    codes[start] = (lft, rgt)
    if start[-1] == 'A':
        start_nodes[start] = start

print(start_nodes)
total_steps = 0
lcms = []
for i in range(10 ** 8):
    for step in steps:
        total_steps += 1
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
    if not start_nodes:
        break
print(f"{lcms=}")
print(f"{lcm(*lcms)=}")