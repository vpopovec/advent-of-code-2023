from concurrent.futures import ProcessPoolExecutor

with open('input.txt') as rf:
    lns = rf.readlines()

all_seeds = [int(s) for s in lns[0].split('seeds: ')[1].split()]
print(f"{all_seeds=}")

# seeds = set()
seeds = {}
for seed_indx in range(0, len(all_seeds), 2):
    range_start = all_seeds[seed_indx]
    range_len = all_seeds[seed_indx + 1]
    # seeds.update(range(range_start, range_start + range_len))
    seeds[range(range_start, range_start + range_len, 1)] = ''
print(f"{seeds=}")

types = 'seed soil fertilizer water light temperature humidity location'.split()
converter = {}
print(f"{converter=}")

map_from, map_to = '', ''
for ln in lns:
    if ' map' in ln:
        map_from, map_to = ln.split()[0].split('-to-')
        converter[(map_from, map_to)] = {}
        print(map_from, map_to)
        continue

    if not map_from or not map_to or not ln.strip():
        continue

    dest_start, source_start, range_len = [int(i) for i in ln.split()]
    converter[(map_from, map_to)][range(source_start, source_start+range_len, 1)] = range(dest_start, dest_start+range_len, 1)

print(converter)


# Try starting from Humidity
dest_tp = 'light'
start_from_num = 0
prev_range = ''
for i in range(4):
    source_dest_key = [k for k in converter.keys() if k[1] == dest_tp][0]
    try:
        next_dest_key = [k for k in converter.keys() if k[1] == source_dest_key[0]][0]
    except IndexError:
        print("Nearing end...")
    print(f"\n{source_dest_key=} {next_dest_key=}")

    # for i in range(100):  # Iterate over all ranges
    range_starts = {}
    for source_rng, dest_rng in converter[source_dest_key].items():
        range_starts[dest_rng[0]] = (source_rng, dest_rng)
    for min_range_start in sorted(range_starts):
        min_range_src, min_range_dest = range_starts[min_range_start]
        # Check intersect_range
        if prev_range:
            x, y = prev_range, min_range_dest
            intersect_range = range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)
            if not intersect_range:
                continue

        if not prev_range or 'TODO':
            prev_range = min_range_src if not prev_range else intersect_range
            dest_tp = source_dest_key[0]
            print(f"{min_range_start=} {min_range_src=} {min_range_dest=}")
        break
        # Try to work my way back, all the way to the seed for smallest location

# Try minimum of all destination ranges
# dest_tp = 'location'
# start_from_num = 0
# prev_range = ''
# for i in range(7):
#     source_dest_key = [k for k in converter.keys() if k[1] == dest_tp][0]
#     try:
#         next_dest_key = [k for k in converter.keys() if k[1] == source_dest_key[0]][0]
#     except IndexError:
#         print("Nearing end...")
#     print(f"\n{source_dest_key=} {next_dest_key=}")
#
#     # for i in range(100):  # Iterate over all ranges
#     range_starts = {}
#     for source_rng, dest_rng in converter[source_dest_key].items():
#         range_starts[dest_rng[0]] = (source_rng, dest_rng)
#     for min_range_start in sorted(range_starts):
#         min_range_src, min_range_dest = range_starts[min_range_start]
#         # Check intersect_range
#         if prev_range:
#             x, y = prev_range, min_range_dest
#             intersect_range = range(max(x[0], y[0]), min(x[-1], y[-1])+1)
#             if not intersect_range:
#                 continue
#
#         if not prev_range:
#             prev_range = min_range_src if not prev_range else intersect_range
#             dest_tp = source_dest_key[0]
#             print(f"{min_range_start=} {min_range_src=} {min_range_dest=}")
#         break
#         # Try to work my way back, all the way to the seed for smallest location
#