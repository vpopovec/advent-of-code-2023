with open('input.txt') as rf:
    lns = [ln.strip() for ln in rf.readlines()]


total = 0
total2 = 0
for ln in lns:
    seqs = [[int(v) for v in ln.split()]]
    for i in range(300):
        next_seq = [seqs[-1][i+1] - seqs[-1][i] for i in range(len(seqs[-1]) - 1)]
        seqs.append(next_seq)
        if not any(next_seq):  # [0, 0, 0]
            break

    first_seq_last_n = 0
    for seq in seqs[::-1]:
        first_seq_last_n += seq[-1]
    # print(f"{first_seq_last_n=}")
    total += first_seq_last_n

    prev_seq = []
    for seq in seqs[::-1]:
        first_num = seq[0] - prev_seq[0] if prev_seq else 0
        seq.insert(0, first_num)
        print(f"{seq=}")
        prev_seq = seq
    total2 += prev_seq[0]
    print('prev_seq', prev_seq)


print('p1', total)
print('p2', total2)
