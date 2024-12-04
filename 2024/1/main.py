with open('input.txt') as rf:
    txt = rf.read()

l1, l2 = [], []
for pair in txt.split('\n'):
    p1, p2 = pair.split('   ')
    l1.append(int(p1))
    l2.append(int(p2))

l1.sort()
l2.sort()

ttl_dst = 0
for i1, i2 in zip(l1, l2):
    ttl_dst += abs(i1 - i2)

print('1', ttl_dst)

# part 2

new_ttl = 0
for i in l1:
    new_ttl += i * l2.count(i)

print('2', new_ttl)