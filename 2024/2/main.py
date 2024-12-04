with open('input.txt') as rf:
    txt = rf.read()


def check_report(levels):
    drctn = 1 if levels[0] < levels[1] else -1
    report_success = 1
    for indx in range(len(levels) - 1):
        check_vals = levels[indx] + drctn, levels[indx] + max_diff * drctn
        if levels[indx + 1] not in range(min(check_vals), max(check_vals) + 1):
            # print('Not succeeded', report, 'on', levels[indx], range(min(check_vals), max(check_vals)))
            report_success = 0

    return report_success

good = 0
max_diff = 3
# 3, 6 (6 <= 5
# 6, 3 (6 - 4 <= 3)
for report in txt.split('\n'):
    levels = [int(i) for i in report.split(' ')]
    drctn = 1 if levels[0] < levels[1] else -1
    report_success = 1
    for indx in range(len(levels) - 1):
        check_vals = levels[indx] + drctn, levels[indx] + max_diff*drctn
        if levels[indx+1] not in range(min(check_vals), max(check_vals) + 1):
            # print('Not succeeded', report, 'on', levels[indx], range(min(check_vals), max(check_vals)))
            report_success = 0

    # part 2
    if not report_success:
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i+1:]
            report_success = check_report(new_levels)
            if report_success:
                break

    if report_success:
        print(report)
    good += report_success

print(good)