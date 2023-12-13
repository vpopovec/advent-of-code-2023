import re
import time
from functools import cache
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


def old_try_options(s, nums, indx=0, full_str=''):
    global ttl_p1
    if not full_str:
        full_str = s
    if not s:
        groups = [len(x) for x in re.findall('#+', full_str)]
        if ','.join([str(x) for x in groups]) == str(nums):
            # print(f"CHECK FINAL STRING: {full_str} {nums=}")
            ttl_p1 += 1
        return full_str

    if s[0] == '?':
        for char in ['.', '#']:
            return old_try_options(s[1:], nums, indx+1, f"{full_str[:indx]}{char}{full_str[indx+1:]}")
    else:
        return old_try_options(s[1:], nums, indx+1, full_str)


# @cache
# def try_options(full_str, nums, indx=0):
#     global ttl_p1
#     if indx == len(full_str):
#         groups = [len(x) for x in re.findall('#+', full_str)]
#         if ','.join([str(x) for x in groups]) == nums:
#             # print(f"CHECK FINAL STRING: {full_str} {nums=}")
#             ttl_p1 += 1
#         # print(f"CHECK FINAL STRING: {full_str} {groups=} {nums=}")
#         return full_str, nums, indx
#
#     if full_str[indx] == '?':
#         for char in ['.', '#']:
#             try_options(f"{full_str[:indx]}{char}{full_str[indx+1:]}", nums, indx+1)
#     else:
#         return try_options(full_str, nums, indx+1)


# ChatGPT
# @cache
# def try_options(full_str, nums, indx=0):
#     # Note: Avoid using global variables, as they might affect caching behavior
#
#     if indx == len(full_str):
#         groups = [len(x) for x in re.findall('#+', full_str)]
#         if ','.join(map(str, groups)) == nums:
#             return full_str, nums, indx
#         return None  # Returning None when conditions are not met
#
#     if full_str[indx] == '?':
#         results = []
#         for char in ['.', '#']:
#             result = try_options(f"{full_str[:indx]}{char}{full_str[indx+1:]}", nums, indx+1)
#             if result:
#                 results.append(result)
#         return results
#     else:
#         return try_options(full_str, nums, indx+1)


# ChatGPT #2
# @cache
# def try_options(full_str, nums, indx=0, ttl_p1=0):
#     if indx == len(full_str):
#         groups = [len(x) for x in re.findall('#+', full_str)]
#         if ','.join(map(str, groups)) == nums:
#             return ttl_p1 + 1
#         return ttl_p1
#
#     if full_str[indx] == '?':
#         for char in ['.', '#']:
#             ttl_p1 = try_options(f"{full_str[:indx]}{char}{full_str[indx+1:]}", nums, indx+1, ttl_p1)
#     else:
#         ttl_p1 = try_options(full_str, nums, indx+1, ttl_p1)
#
#     return ttl_p1


@cache
def try_options(full_str, nums, indx=0, ttl_p1=0, ttl_hashes=0):
    if indx == len(full_str):
        groups = [len(x) for x in re.findall(r'#+', full_str)]
        if ','.join(map(str, groups)) == nums:
            return ttl_p1 + 1
        return ttl_p1

    if full_str[indx] == '?':
        for char in ['.', '#']:
            new_str = f"{full_str[:indx]}{char}{full_str[indx+1:]}"
            ttl_p1 = try_options(new_str, nums, indx+1, ttl_p1)

    else:
        ttl_p1 = try_options(full_str, nums, indx+1, ttl_p1)

    return ttl_p1

ttl = 0
t = time.time()
for row in rows:
    row, nums = row.split()
    # row = '?'.join([row]*5)
    # nums = ','.join([nums]*5)
    print(f"{row=} {nums=}")
    res = try_options(row, nums, 0, 0)
    ttl += res
    print(res)
print(f"{ttl=}")
print(round(time.time()-t, 4), 'sec')

[[[[[[[[[('.###....##.#', '3,2,1', 12)]]]], [[[[('.###...##..#', '3,2,1', 12)], [('.###...##.#.', '3,2,1', 12)]]]]], [[[[[('.###..##...#', '3,2,1', 12)], [('.###..##..#.', '3,2,1', 12)]], [[('.###..##.#..', '3,2,1', 12)]]]]]], [[[[[[('.###.##....#', '3,2,1', 12)], [('.###.##...#.', '3,2,1', 12)]], [[('.###.##..#..', '3,2,1', 12)]]], [[[('.###.##.#...', '3,2,1', 12)]]]]]]]]]
