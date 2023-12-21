from collections import defaultdict

with open('input.txt') as rf:
    grid = rf.read().split('\n')
print(grid)

start_pos = [(x.index('S'), x_indx) for x_indx, x in enumerate(grid) if 'S' in x][0]
print(start_pos)

steps = 64
options = defaultdict(list)
# options[start_pos].append(0)


def next_pos(pos, i):
    positions = []
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # Check out of bounds
        new_x, new_y = pos[0] + x, pos[1] + y
        if new_x < 0 or new_x >= len(grid[0]):
            continue
        if new_y < 0 or new_y >= len(grid):
            continue
        if grid[new_y][new_x] not in ['.', 'S']:
            continue
        positions.append((new_x, new_y))
        if i not in options[(new_x, new_y)]:
            options[(new_x, new_y)].append(i)
    return positions


positions = [start_pos]
for i in range(1, steps + 1):
    next_positions = []
    for pos in positions:
        next_positions.extend(next_pos(pos, i))
        print(f"{i=} {positions}")
    positions = set(next_positions)
    # for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    #     # Check out of bounds
    #     new_x, new_y = pos[0] + x, pos[1] + y
    #     if new_x < 0 or new_x >= len(grid[0]):
    #         continue
    #     if new_y < 0 or new_y >= len(grid):
    #         continue
    #     if grid[new_y][new_x] != '.':
    #         continue
    #     options[(new_x, new_y)].append(i)

print(options)
print(len(options))
ttl = 0
for k, vl in options.items():
    if any([x % 2 == steps % 2 for x in vl]):
        print(k, vl)
        ttl += 1
print(ttl)
