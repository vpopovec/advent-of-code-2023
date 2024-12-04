import math
with open('input.txt') as rf:
    grid = rf.read().split('\n')

print(grid)
# GO 15 steps then go back and try different 15 steps
# to see which has smaller heat loss
steps = []
grid_pos = (0, 0)
end_pos = (len(grid[0])-1, len(grid)-1)
reverse = {1: -1, -1: 1, 0: 0}


def get_all_steps(steps, num=0, grid_pos=(0, 0), depth=0, heat=0):
    # for i in range(steps_num):
    if depth == num:
        print(f"FINISHED {steps} {heat} {grid_pos}, {math.dist(grid_pos, end_pos)}")
        return
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    if grid_pos[0] == 0:
        directions.remove((-1, 0))
    elif grid_pos[0] + 1 >= len(grid[0]):
        directions.remove((1, 0))
    if grid_pos[1] == 0:
        directions.remove((0, -1))
    elif grid_pos[1] + 1 >= len(grid):
        directions.remove((0, 1))
    for drct in directions:
        opposite_dir = reverse[drct[0]], reverse[drct[1]]
        if steps and steps[-1] == opposite_dir:
            continue
        if len(steps) >= 3 and all([i==drct for i in steps[-3:]]):
            continue
        new_pos = grid_pos[0] + drct[0], grid_pos[1] + drct[1]
        add_heat = int(grid[new_pos[1]][new_pos[0]])
        new_steps = [*steps, drct]
        get_all_steps(new_steps, num, new_pos, depth+1, heat+add_heat)


get_all_steps([], 10, grid_pos)
