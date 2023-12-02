import re
import operator
import functools
with open('games.txt') as rf:
    games = rf.readlines()

available_cubes = {'red': 12, 'green': 13, 'blue': 14}

sum_of_powers = 0
sum_of_ids = 0
for game in games:
    game_num = re.search(r'Game (\d+)', game).groups()[0]
    rounds = [r.strip() for r in game.split(':')[1].split(';')]

    game_is_possible = True
    minimum_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for rnd in rounds:
        cubes = rnd.split(', ') if ',' in rnd else [rnd]

        for cube_num, cube_color in [c.split() for c in cubes]:
            if int(cube_num) > minimum_cubes[cube_color]:
                minimum_cubes[cube_color] = int(cube_num)

            if int(cube_num) > available_cubes[cube_color]:
                game_is_possible = False

    sum_of_powers += functools.reduce(operator.mul, minimum_cubes.values(), 1)
    sum_of_ids += int(game_num) if game_is_possible else 0

print(f"{sum_of_ids=}")
print(f"{sum_of_powers=}")

