import re

grid_len = 2500
with open('input.txt') as rf:
    moves = rf.read().split('\n')
print(moves)

grid = ['.' * grid_len for i in range(grid_len)]
grid[0] = f'#{"." * (grid_len - 1)}'
pos = (0, 0)
for move in moves:
    direction, length, color = move.split()
    length = int(length)
    if direction == 'R':
        go_right = min(len(grid)-1, pos[0]+length)
        old = grid[pos[1]]
        grid[pos[1]] = f"{old[:pos[0]+1]}{'#'*length}{old[pos[0]+1+length:][:len(grid)]}"
        pos = (go_right, pos[1])
    elif direction == 'L':
        go_left = max(0, pos[0]-length)
        old = grid[pos[1]]
        grid[pos[1]] = f"{old[:pos[0]-length]}{'#' * length}{old[pos[0]:]}"
        pos = (go_left, pos[1])
    elif direction == 'U':
        go_up = max(pos[1]-length, 0)
        for y in range(go_up, pos[1]):
            grid[y] = f"{grid[y][:pos[0]]}#{grid[y][pos[0]+1:]}"
        pos = (pos[0], go_up)
    elif direction == 'D':
        go_down = min(pos[1] + length + 1, len(grid)-1)
        print(go_down, pos)
        for y in range(pos[1]+1, go_down):
            grid[y] = f"{grid[y][:pos[0]]}#{grid[y][pos[0]+1:]}"
        pos = (pos[0], go_down - 1)


ttl = 0
for x in grid:
    if '#' in x:
        wall_from = x.index('#')
        wall_to = len(x) - x[::-1].index('#')
        print(x)
        ttl += wall_to-wall_from

print(ttl)
