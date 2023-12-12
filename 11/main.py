import itertools

EXPANSION = 1
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
for r_indx, row in enumerate(rows):
    for col_indx in expand['cols'][::-1]:
        rows[r_indx] = f"{rows[r_indx][:col_indx]}{'.'*EXPANSION}{rows[r_indx][col_indx:]}"

empty_row = '.' * len(rows[0])
for expand_indx in expand['rows'][::-1]:
    rows_start, rows_end = rows[:expand_indx], rows[expand_indx:]
    rows = [*rows_start, *[empty_row * EXPANSION], *rows_end]

galaxies = []
for r_indx, r in enumerate(rows):
    galaxies.extend([(i, r_indx) for i, letter in enumerate(r) if letter == '#'])

paths = itertools.combinations(galaxies, 2)
total_lens = 0
for path in paths:
    (x, y), (x2, y2) = path
    path_len = (abs(x - x2) + abs(y - y2))
    total_lens += path_len
    # print(path, path_len)
print(total_lens)