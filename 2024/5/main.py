from collections import defaultdict
with open('input.txt') as rf:
    txt = rf.read()


rules_d = defaultdict(list)
rules, updates = txt.split('\n\n')
for rule in rules.split('\n'):
    n1, n2 = [int(n) for n in rule.split('|')]
    rules_d[n1].append(n2)


def update_is_correct(upd):
    for indx, n in enumerate(upd):
        for right_num in upd[indx + 1:]:
            if n in rules_d[right_num]:
                return False
    return True



def fix_update(upd):
    # 1234 - 4321 - 3421 - 2341 - 1234
    for i in range(100):
        try_again = False
        for indx, n in enumerate(upd):
            for right_indx, right_num in enumerate(upd[indx + 1:]):
                if n in rules_d[right_num]:
                    bad_num = upd.pop(right_indx+indx + 1)
                    print(f"bad_num {bad_num}")
                    upd = [bad_num, *upd]
                    try_again = True
                    break
            if try_again:
                break
        if not try_again:
            print("Fixed!", upd)
            break
        print('iter', i, 'upd', upd, '\n')
    return upd


if __name__ == '__main__':
    # fix_update([61,13,29])
    print(rules_d)
    ttl = 0
    ttl_after_correction = 0
    for update in updates.split('\n'):
        upd = [int(n) for n in update.split(',')]
        # rule_broken = False
        # for indx, n in enumerate(upd):
        #     for right_num in upd[indx+1:]:
        #         if n in rules_d[right_num]:
        #             rule_broken = True
        #             break
        #     if rule_broken:
        #         break

        good_update = update_is_correct(upd)
        if good_update:
            ttl += upd[len(upd)//2]
        else:
            upd = fix_update(upd)
            ttl_after_correction += upd[len(upd) // 2]
    print('Part 1', ttl)
    print('Part 2', ttl_after_correction)
