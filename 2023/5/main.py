from collections import defaultdict
import time

with open('input.txt') as rf:
    lns = rf.readlines()

all_seeds = [int(s) for s in lns[0].split('seeds: ')[1].split()]
print(f"{all_seeds=}")

# seeds = set()
# for seed_indx in range(0, len(all_seeds), 2):
#     range_start = all_seeds[seed_indx]
#     range_len = all_seeds[seed_indx + 1]
#     seeds.update(range(range_start, range_start + range_len))
# print(f"{seeds=}")

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

locations = []
# for source_range in seeds:
# ? range(977035576, 1177785526)
# seeds={range(104847962, 108431794): '', range(1212568077, 1327462358): '', range(3890048781, 4223500386): '', range(1520059863, 1737421853): '', range(310308287, 323093897): '', range(3492562455, 3785530504): '', range(1901414562, 2417565423): '', range(2474299950, 2627167098): '', range(3394639029, 3454329439): '', range(862612782, 1038740979): ''}
# seeds={range(1520059863, 1737421853): ''}
seeds={range(2243422648 - 13, 2243422648): ''}
for seed_range in seeds.keys():
    # sqrt_of_range = int((seed_range[-1] - seed_range[0]) ** 0.5)
    sqrt_of_range = 1
    print(f"{sqrt_of_range=}")
    for source_num in range(seed_range[0], seed_range[-1], sqrt_of_range):
    #     initial_num = source_num
    # for source_num in range(seed_range[0], seed_range[-1]):
        initial_num = source_num
        source_tp = 'seed'
        for i in range(7):
            source_dest_key = [k for k in converter.keys() if k[0] == source_tp][0]
            # print(f"{source_dest_key=}")
            for source_rng, dest_rng in converter[source_dest_key].items():
                if source_num in source_rng:
                    # print(f"FOUND RANGE, {source_num=} {source_rng=} {dest_rng=}")
                    num_difference = source_num - source_rng[0]
                    dest_num = dest_rng[0] + int(num_difference)
                    source_num = dest_num
                    break

            source_tp = source_dest_key[1]
            # print(f"{source_tp=} {dest_num=}")
            if source_tp == 'location':
                if source_num < 2008785:
                    print(f"FOUND: {initial_num=}", source_num, seed_range, )
                    time.sleep(1)
                locations.append(source_num)

print(f"{len(locations)=} {min(locations)=}")

# break

"""
seed-to-soil map:
50 98 2
52 50 48"""
