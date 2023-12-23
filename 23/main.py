import sys
sys.setrecursionlimit(15000)

with open('input.txt') as rf:
    rows = rf.read().split('\n')

print(rows)
start_pos = (1, 0)
end_pos = (len(rows[0]) - 2, len(rows) - 1)
pos = start_pos
slope_add = {'^': (0, -1), '<': (-1, 0), '>': (1, 0), 'v': (0, 1)}
all_moves = []


def get_next(pos, prev_pos, moves=0, tst_lst=''):
    global all_moves
    if not tst_lst:
        tst_lst = []

    # print(f"get_next {moves=} {pos}")
    for dr in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # print(pos, end_pos)
        if pos == end_pos:
            print(moves)
            all_moves.append(moves)
            return moves

        x, y = dr[0] + pos[0], dr[1] + pos[1]

        if (x < 0) or (x >= len(rows[0])) or (y < 0) or (y >= len(rows)):
            continue
        c = rows[y][x]
        if c == '#' or (x, y) == prev_pos:  # do not return
            continue
        if c == '.':
            get_next((x, y), pos, moves + 1)
        if c in slope_add:
            if dr != slope_add[c]:  # wrong direction of slope, non-passable
                continue
            prev_slope = (x, y)
            x, y = x + slope_add[c][0], y + slope_add[c][1]  # maybe check for overflow?
            get_next((x, y), prev_slope, moves + 2)

print(get_next(start_pos, start_pos))
print(all_moves)
print(max(all_moves))
# for dr in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#     if pos == end_pos:
#         break
#     x, y = dr
#     x1, y1 = pos
#     if (x + x1 < 0) or (x + x1 >= len(rows[0])) or (y + y1 < 0) or (y+y1 >= len(rows)):
#         continue
#     c = rows[y][x]
#     if c == '#':
#         continue
#     if c in slope_add:
#         x, y = x + slope_add[c][0], y + slope_add[c][1]  # maybe check for overflow?



