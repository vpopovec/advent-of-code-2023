import re
with open('input.txt') as rf:
    rows = [ln.strip() for ln in rf.readlines()]



# def collect(wanted_char):
#     groups = {}
#     prev = ''
#     for indx, char in enumerate(row):
#         if indx + 1 == len(row):
#             if prev:
#                 groups[indx-1] = prev
#         if char == wanted_char:
#             prev += wanted_char
#         else:
#             if prev:
#                 groups[indx-1] = prev
#             prev = ''
#     return groups

ttl_p1 = 0


def try_options(s, nums, indx=0, full_str=''):
    global ttl_p1
    if not full_str:
        full_str = s
    if not s:
        groups = [len(x) for x in re.findall('#+', full_str)]
        if str(groups) == str(nums):
            # print(f"CHECK FINAL STRING: {full_str} {nums=}")
            ttl_p1 += 1
        return

    if s[0] == '?':
        for char in ['.', '#']:
            try_options(s[1:], nums, indx+1, f"{full_str[:indx]}{char}{full_str[indx+1:]}")
    else:
        try_options(s[1:], nums, indx+1, full_str)


# try_options(row, nums, 0)

for row in rows:
    row, nums = row.split()
    nums = [int(i) for i in nums.split(',')]
    try_options(row, nums, 0)
print(f"{ttl_p1=}")
