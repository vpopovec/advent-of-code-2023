import math

input = """
Time:        46     68     98     66
Distance:   358   1054   1807   1080
"""
races = {46: 358, 68: 1054, 98: 1807, 66: 1080}
races = {46689866: 358105418071080}

total_ways_to_win = []
for race_time, race_distance in races.items():
    race_wins = []
    for speed in range(1, race_time):
        remain_time = race_time - speed
        travel_distance = remain_time * speed
        if travel_distance > race_distance:
            race_wins.append(speed)
    total_ways_to_win.append(len(race_wins))

print(f"{total_ways_to_win=}")
print(f"{math.prod(total_ways_to_win)}")