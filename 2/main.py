import re
import operator
import functools
with open('games.txt') as rf:
    games = rf.readlines()

# 12 red cubes, 13 green cubes, and 14 blue cubes
available_cubes = {'red': 12, 'green': 13, 'blue': 14}

sum_of_powers = 0
sum_of_ids = 0
for game in games:
    # Game 2: 2 green, 3 blue; 11 red; 2 green, 5 red, 1 blue
    game_num = re.search(r'Game (\d+)', game).groups()[0]
    print(f"{game_num=}")
    rounds = [r.strip() for r in game.split(':')[1].split(';')]
    game_is_possible = True
    minimum_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for rnd in rounds:
        cubes = rnd.split(', ') if ',' in rnd else [rnd]
        print(f"{cubes=}")
        for cube_num, cube_color in [c.split() for c in cubes]:
            print(f"{cube_color=} {cube_num=}")
            if int(cube_num) > minimum_cubes[cube_color]:
                minimum_cubes[cube_color] = int(cube_num)

            if int(cube_num) > available_cubes[cube_color]:
                game_is_possible = False

    print(f"{minimum_cubes=}")
    print(functools.reduce(operator.mul, minimum_cubes.values(), 1))
    sum_of_powers += functools.reduce(operator.mul, minimum_cubes.values(), 1)

    sum_of_ids += int(game_num) if game_is_possible else 0
    print(f"{game=}")
    print(f"{rounds=}")

print(f"{sum_of_ids=}")
print(f"{sum_of_powers=}")

