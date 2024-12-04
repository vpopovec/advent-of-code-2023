import copy
import re
from collections import defaultdict

with open('input.txt') as rf:
    txt = rf.readlines()

is_a_part = lambda ch: ch not in ['.'] and not ch.isdigit()

total_lines = len(txt)
all_nums = {}
# Collect numbers
for ln_indx, ln in enumerate(txt):
    numbers = defaultdict(str)
    num_start = 0
    for indx, char in enumerate(ln):
        if char.isdigit():
            numbers[num_start] += char
        else:
            num_start = indx + 1
    all_nums[ln_indx] = copy.deepcopy(numbers)

total_sum = []
for ln_indx, ln in enumerate(txt):
    gears = [indx for indx, ch in enumerate(ln) if ch == '*']

    print(f"ROW {ln_indx + 1} {gears=}")
    last_line, first_line = ln_indx == total_lines - 1, ln_indx == 0

    prev_line = all_nums[ln_indx - 1] if not first_line else ''
    this_line = all_nums[ln_indx] if not first_line else ''
    next_line = all_nums[ln_indx + 1] if not last_line else ''

    # Check left and right
    for gear_indx in gears:
        print(f"{gear_indx=}")
        adjacent_nums = []
        number_is_valid = False
        if gear_indx > 0:  # check left
            if ln[gear_indx - 1].isdigit():
                # Get number on left
                for i in range(1, 100):
                    if gear_indx - i in this_line:
                        adjacent_nums.append(this_line[gear_indx - i])
                        break

        if gear_indx + 1 < len(ln):  # check right
            if ln[gear_indx + 1].isdigit():
                adjacent_nums.append(this_line[gear_indx + 1])

        left_indx = max(gear_indx - 1, 0)
        right_indx = min(gear_indx + 2, len(ln) - 1)  # upper index
        for check_indx in range(left_indx, right_indx):
            # check top
            # if gear_indx == 3:
            #     print(f"{check_indx=}")
            #     print(prev_line)
            #     print(next_line)
            if txt[ln_indx - 1][check_indx].isdigit() and prev_line:
                for i in range(0, 100):
                    if check_indx - i in prev_line:
                        if prev_line[check_indx - i] in adjacent_nums:  # Number already added, logic a bit flawed
                            break
                        adjacent_nums.append(prev_line[check_indx - i])
                        break

            if txt[ln_indx + 1][check_indx].isdigit() and next_line:
                for i in range(0, 100):
                    if check_indx - i in next_line:
                        if next_line[check_indx - i] in adjacent_nums:  # Number already added, logic a bit flawed
                            break
                        adjacent_nums.append(next_line[check_indx - i])
                        break
            # if check_indx in prev_line:
            #     adjacent_nums.append(prev_line[check_indx])
            # if check_indx in next_line:
            #     print('found in next line')
            #     adjacent_nums.append(next_line[check_indx])

        print(f"{adjacent_nums=}")
        if len(adjacent_nums) == 2:
            total_sum.append(int(adjacent_nums[0]) * int(adjacent_nums[1]))
print(f"{total_sum=}")
print(f"{sum(total_sum)=}")  # 4361

