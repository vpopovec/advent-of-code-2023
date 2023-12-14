import re
import time
from functools import cache
with open('input.txt') as rf:
    rows = [ln.strip() for ln in rf.readlines()]

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


def try_options(full_str, nums):

    @cache
    def dp(indx, n, res=0):
        # indx = index of full_str we're currently on
        # n = index of group of '#' we're currently on
        if indx == len(full_str):
            print(f'returning {n=} {len(nums)=}')
            return n == len(nums)

        if full_str[indx] in ['.', '?']:
            res += dp(indx + 1, n)

        try:
            indx_to = indx + nums[n]
            if '.' not in full_str[indx:indx_to] and '#' not in full_str[indx_to]:
                res += dp(indx_to + 1, n + 1)
        except:
            pass

        return res

    return dp(0, 0)

ttl = 0
t = time.time()
for row in rows:
    full_str, nums = row.split()
    full_str = f"{full_str}?" * 5
    nums = eval(nums)*5
    res = try_options(full_str, nums)
    ttl += res
    print(res)
print(f"{ttl=}")
print(round(time.time()-t, 4), 'sec')
