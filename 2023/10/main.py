from matplotlib.path import Path
with open('input.txt') as rf:
    squares = [ln.strip() for ln in rf.readlines()]


start_pos = ''
print(squares)
allowed_pipes = {(-1, 0): ['-', 'F', 'L'],
                 (0, -1): ['|', 'F', '7'],
                 (1, 0): ['-', 'J', '7'],
                 (0, 1): ['|', 'L', 'J']}
# allowed_moves = {'-': [(-1, 0), (1, 0)],
#                  '|': [(0, -1), (0, 1)],
#                  'F': [(1, 0), (0, 1)],
#                  'L': [],
#                  'J': [],
#                  '7': []}

for row_indx, row in enumerate(squares):
    if 'S' not in row:
        continue
    start_pos = (row.index('S'), row_indx)
    print(start_pos)
    break

large_loop = [start_pos]
reverse = {1: -1, 0: 0, -1: 1}


def find_start(this_pos, prev_pos):
    pipe = squares[this_pos[1]][this_pos[0]]
    prev_move = this_pos[0] - prev_pos[0], this_pos[1] - prev_pos[1]
    # print(f"{this_pos=} {prev_pos=} {pipe=} {prev_move=}")

    next_pos = [pos for pos, vals in allowed_pipes.items() if pipe in vals and pos != prev_move][0]
    next_pos = reverse[next_pos[0]], reverse[next_pos[1]]

    next_x, next_y = this_pos[0] + next_pos[0], this_pos[1] + next_pos[1]
    next_pipe = squares[next_y][next_x]
    if next_pipe == 'S':
        return '', ''
    # print(next_pos, allowed_pipes[next_pos], f"{next_pipe=}")
    return (next_x, next_y), this_pos
    # large_loop.append((next_x, next_y))
    # return find_start((next_x, next_y), this_pos)


for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    new_x, new_y = start_pos[0] + x, start_pos[1] + y
    if (new_x < 0 or new_x >= len(squares[0])) or new_y < 0 or new_y >= len(squares):
        continue
    next_pipe = squares[new_y][new_x]
    allowed = next_pipe in allowed_pipes[(x, y)]
    print(f"{next_pipe=} {allowed=}")
    if allowed:
        next_pos = new_x, new_y
        large_loop.append(next_pos)

        next_pos, this_pos = find_start(next_pos, start_pos)
        for i in range(100000):
            large_loop.append(next_pos)
            next_pos, this_pos = find_start(next_pos, this_pos)
            if not next_pos:
                break
        break

print(f"{len(large_loop)=} PART1={len(large_loop) // 2}")

total_points = 0
p = Path(large_loop)
for y in range(len(squares)):
    for x in range(len(squares[0])):
        if (x, y) in large_loop:
            continue
        if p.contains_point((x, y)):
            total_points += 1
print(f"PART2={total_points}")