import re
from collections import defaultdict

with open('input.txt') as rf:
    txt = rf.readlines()

is_a_part = lambda ch: ch not in ['.'] and not ch.isdigit()

total_lines = len(txt)
total_sum = []
for ln_indx, ln in enumerate(txt):
    numbers = defaultdict(str)

    num_start = 0
    for indx, char in enumerate(ln):
        if char.isdigit():
            numbers[num_start] += char
        else:
            num_start = indx + 1

    print(f"ROW {ln_indx+1}")

    # Check left and right
    for n_indx, n in numbers.items():
        number_is_valid = False
        if n_indx > 0:  # check left
            if is_a_part(ln[n_indx-1]):
                number_is_valid = True

        if n_indx + len(n) < len(ln):
            if is_a_part(ln[n_indx + len(n)]):
                number_is_valid = True

        last_line, first_line = ln_indx == total_lines - 1, ln_indx == 0
        left_indx = max(n_indx - 1, 0)
        right_indx = min(n_indx + len(n) + 1, len(ln) - 1)  # upper index
        # print(f"{left_indx=} {right_indx=}")

        if not last_line:  # check bottom
            for ch in txt[ln_indx + 1][left_indx:right_indx]:
                if is_a_part(ch):
                    number_is_valid = True

        if not first_line:  # check top
            for ch in txt[ln_indx - 1][left_indx:right_indx]:
                if is_a_part(ch):
                    number_is_valid = True

        total_sum.append(int(n) if number_is_valid else 0)

print(f"{total_sum=}")
print(f"{sum(total_sum)=}")  # 4361

