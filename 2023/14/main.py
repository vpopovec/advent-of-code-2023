with open('input.txt') as rf:
    txt = rf.read()
rows = txt.split('\n')
rotate_board = lambda x: list(zip(*x[::-1]))  # clockwise

# for row_indx, row in enumerate(rows):
# Move all chars below
ttl = 0
cycle_n = 1000000000
count = 0
previous_maps = []
results = {}

for i in range(1, cycle_n):
    count += 1
    for j in range(4):
        new_cols = []

        for row_pos, char in enumerate(rows[0]):
            chars_in_col = [r[row_pos] for r in rows]
            # print(f"{row_pos=} {chars_in_col}")
            for c_indx, c in enumerate(chars_in_col):
                if c == '.':
                    if 'O' not in chars_in_col[c_indx:]:
                        break
                    sub_list = chars_in_col[c_indx:]
                    next_rounded_rock = sub_list.index('O')
                    next_cube_rock = sub_list.index('#') if '#' in sub_list else len(sub_list)
                    if next_rounded_rock < next_cube_rock:
                        chars_in_col[c_indx] = 'O'
                        chars_in_col[c_indx + next_rounded_rock] = '.'
                        # print(chars_in_col)

            new_cols.append(chars_in_col)

        rows = rotate_board(list(map(list, zip(*new_cols))))
        # print("ROWS")
        # for row in rows:
        #     print(row)

    test_ttl = 0
    for row_indx, row in enumerate(rows):
        test_ttl += sum([len(rows) - row_indx for c in row if c == 'O'])
    results[count] = test_ttl
    # print(test_ttl)

    if str(rows) in previous_maps:
        start = previous_maps.index(str(rows))
        length = len(previous_maps) - start
        target = (1000000000 - start) % length + start + length

        if len(previous_maps) == target and target:
            print(f"FOUND LOOP {count=} {test_ttl=} {results[count-1]}")
            print(f"RESULT PART2: {results[count-1]}")
            break
        #     break
        # break
    previous_maps.append(str(rows))

for row_indx, row in enumerate(rows):
    print(row, sum([len(rows) - row_indx for c in row if c == 'O']))
    ttl += sum([len(rows) - row_indx for c in row if c == 'O'])
    # for c_indx, c in enumerate(col):
    #     if c == 'O':
    #         ttl += len(col) - c_indx

    # for c_indx, c in enumerate(chars_in_col):
    #     if c == 'O':
    #         ttl += len(chars_in_col) - c_indx
