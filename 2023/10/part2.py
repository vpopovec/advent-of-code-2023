with open('input.txt') as rf:
    squares = [ln.strip() for ln in rf.readlines()]


def find_fields():
    def find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    grounds = []
    for row_indx, row in enumerate(squares[1:-1]):
        row_indx += 1
        row_grounds = [x for x in find(row, '.') if x not in [0, len(row)-1]]
        for x in row_grounds:
            grounds.append((x, row_indx))
    print(grounds)

    # Get fields of connected grounds
    fields = []
    for g_x, g_y in grounds:
        if f"({g_x, g_y})" in str(fields):
            continue
        field_found = False
        print(f"GROUND {g_x} {g_y}")
        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_x, new_y = g_x + x, g_y + y
            if (new_x < 0 or new_x >= len(squares[0])) or new_y < 0 or new_y >= len(squares):
                continue
            for field in fields:
                if (new_x, new_y) in field:
                    field.append((g_x, g_y))
                    field_found = True

        if not fields or not field_found:
            fields.append([(g_x, g_y)])

    for field in fields:
        print(f"{field=}")

# Determine if all grounds in a field are within borders
