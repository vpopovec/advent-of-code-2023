with open('input.txt') as rf:
    words = rf.read().strip()

# ttl = 0
boxes = {i: [] for i in range(256)}
for word in words.split(','):
    # The result of running the HASH algorithm on the label indicates the correct box for that step.
    print(word)
    vl = 0
    label = word.split('-')[0].split('=')[0]
    for char in label:
        vl += ord(char)
        vl = (vl * 17) % 256
    if '-' in word:
        boxes[vl] = [x for x in boxes[vl] if label != x.split()[0]]
        # move any remaining lenses as far forward in the box as they can go without changing their order?
    if '=' in word:
        focal_len = word[-1]
        lens_in_box = [x for x in boxes[vl] if label == x.split()[0]]
        if lens_in_box:
            indx = boxes[vl].index(lens_in_box[0])
            boxes[vl][indx] = f"{label} {focal_len}"
        else:
            boxes[vl].append(f"{label} {focal_len}")
    print(boxes)
    # ttl += vl
# print(ttl)
print(boxes)
ttl = 0
for box_num, values in boxes.items():
    for lens_indx, vl in enumerate(values):
        ttl += (box_num+1) * (lens_indx+1) * (int(vl[-1]))
print('p2', ttl)
