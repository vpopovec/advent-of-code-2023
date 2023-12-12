import re
# row = '#.??#????. 1,5,1'
# row = '.???.??????? 1,1,2,1'
row = '?###???????? 3,2,1'
row, nums = row.split()
# 1. Simplify row
nums = [int(i) for i in nums.split(',')]
print(nums)


def collect(wanted_char):
    groups = {}
    prev = ''
    for indx, char in enumerate(row):
        if indx + 1 == len(row):
            if prev:
                groups[indx-1] = prev
        if char == wanted_char:
            prev += wanted_char
        else:
            if prev:
                groups[indx-1] = prev
            prev = ''
    return groups


def try_options(s, nums, indx, full_str=''):
    if not full_str:
        full_str = s
    if not s:
        print(f"CHECK FINAL STRING: {full_str}")
        groups = [len(x) for x in re.findall('#+', full_str)]
        print(groups, nums)
        return

    if s[0] == '?':
        for char in ['.', '#']:
            try_options(s[1:], nums, indx+1, f"{full_str[:indx]}{char}{full_str[indx+1:]}")
    else:
        try_options(s[1:], nums, indx+1, full_str)



broken_g = collect('#')
unknown_g = collect('?')
print(f"{broken_g=}")
print(f"{unknown_g=}")
try_options(row, nums, 0)
# Get groups of ?
# short_row = ''

"""
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#"""


