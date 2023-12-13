with open('input.txt') as rf:
    txt = rf.read()


def find_line(rows, cols, orig_pos=0):
    # ['..##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.']
    for col_indx, col in enumerate(cols):
        if col_indx == len(cols) - 1:
            break
        if col == cols[col_indx + 1]:
            min_iter = min([col_indx - 0, len(cols) - col_indx - 2])
            short_cols = cols[col_indx - min_iter: col_indx + min_iter + 2]
            is_mirror = True
            for i in range(len(short_cols) // 2):
                # print(short_cols[i], short_cols[-i-1])
                if short_cols[i] != short_cols[-i - 1]:
                    is_mirror = False
            # print(min_iter, short_cols, is_mirror)
            if is_mirror:
                # print(f"Found Match on {col_indx=}")
                return_val = col_indx + 1
                if not orig_pos or (col_indx, 0, return_val) != orig_pos:
                    return return_val, (col_indx, 0, return_val)

        # TODO: Add row
    for row_indx, row in enumerate(rows):
        if row_indx == len(rows) - 1:
            break
        if row == rows[row_indx + 1]:
            min_iter = min([row_indx - 0, len(rows) - row_indx - 2])
            short_rows = rows[row_indx - min_iter: row_indx + min_iter + 2]
            is_mirror = True
            # print(f"Checking row (horizontal) match {row_indx=} {short_rows=}")
            for i in range(len(short_rows) // 2):
                # print(short_cols[i], short_cols[-i-1])
                if short_rows[i] != short_rows[-i - 1]:
                    is_mirror = False
            # print(min_iter, short_cols, is_mirror)
            if is_mirror:
                print(f"Found Match on {row_indx=} {orig_pos=}")
                return_val = (row_indx + 1) * 100
                if not orig_pos or (0, row_indx, return_val) != orig_pos:
                    print(row_indx+1)
                    return return_val, (0, row_indx, return_val)
    return '', ''

ttl = 0
for pattern in txt.split('\n\n'):
    rows = pattern.split()
    cols = []
    for j in range(len(rows[0])):
        col_str = ''
        for i in range(len(rows)):
            col_str += rows[i][j]
        cols.append(col_str)
    # print(rows)
    # print(cols)
    original_ttl, orig_pos = find_line(rows, cols)
    new_ttl_found = 0
    for row_indx, row in enumerate(rows):
        opposite_char = lambda x: '.' if x == '#' else '#'
        for i in range(len(row)):
            new_row = row[:i] + opposite_char(row[i]) + row[i+1:]
            # print(f"Old row: {row[:]}")
            # print(f"New row: {new_row}")
            new_rows = [*rows[:row_indx], new_row, *rows[row_indx+1:]]

            new_cols = []
            for j in range(len(new_rows[0])):
                col_str = ''
                for i in range(len(new_rows)):
                    col_str += new_rows[i][j]
                new_cols.append(col_str)

            # print(f"NEW R: {new_rows}")
            # print(f"NEW C: {new_cols}")
            new_ttl, line_pos = find_line(new_rows, new_cols, orig_pos)
            if new_ttl and line_pos != orig_pos:
                # print('HERE', new_ttl)
                new_ttl_found = new_ttl
                break
        if new_ttl_found:
            break

    # ttl += find_line(rows, cols)
    ttl += new_ttl_found
print(f"{ttl=}")