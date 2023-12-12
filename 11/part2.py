import itertools

EXPANSION = 1000000 - 1
with open('input.txt') as rf:
    rows = [ln.strip() for ln in rf.readlines()]

expand = {'cols': [i for i in range(len(rows[0]))],
          'rows': [i for i in range(len(rows))]}
for i in range(len(rows[0])):
    for j, row in enumerate(rows):
        if row[i] == '#':
            if j in expand['rows']:
                expand['rows'].remove(j)
            if i in expand['cols']:
                expand['cols'].remove(i)
print(f"{expand=}")

galaxies = []
for r_indx, r in enumerate(rows):
    galaxies.extend([(i, r_indx) for i, letter in enumerate(r) if letter == '#'])

paths = itertools.combinations(galaxies, 2)

total_lens = 0
for path in paths:
    (x, y), (x2, y2) = path
    min_x, max_x = min([x, x2]), max([x, x2])
    min_x = min_x + sum([EXPANSION for i in expand['cols'] if i < min_x])
    max_x = max_x + sum([EXPANSION for i in expand['cols'] if i < max_x])

    min_y, max_y = min([y, y2]), max([y, y2])
    min_y = min_y + sum([EXPANSION for i in expand['rows'] if i < min_y])
    max_y = max_y + sum([EXPANSION for i in expand['rows'] if i < max_y])
    path_len = (abs(max_x - min_x)
                + abs(max_y - min_y))
    # print(path, (min_x, min_y), (max_x, max_y), f"{path_len=}")
    total_lens += path_len

print(total_lens)