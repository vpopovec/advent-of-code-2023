from collections import defaultdict
with open('input.txt') as rf:
    grid = rf.read().split('\n')
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)

moves = {
    (1, 0): {  # going Right
        '.': [(1, 0)],
        '-': [(1, 0)],
        '|': [(0, 1), (0, -1)],
        '\\': [(0, 1)],
        '/': [(0, -1)]
    },
    (-1, 0): {  # going left
        '.': [(-1, 0)],
        '-': [(-1, 0)],
        '|': [(0, 1), (0, -1)],
        '\\': [(0, -1)],
        '/': [(0, 1)]
    },
    (0, -1): {  # going Up
        '.': [(0, -1)],
        '-': [(1, 0), (-1, 0)],
        '|': [(0, -1)],
        '\\': [(-1, 0)],
        '/': [(1, 0)]
    },
    (0, 1): {  # going down
        '.': [(0, 1)],
        '-': [(1, 0), (-1, 0)],
        '|': [(0, 1)],
        '\\': [(1, 0)],
        '/': [(-1, 0)]
    },

}
energized = defaultdict(list)


def get_next_dirs(beam_dir, beam_pos):
    # beam_dir, beam_pos = beam
    if beam_pos[0] < 0 or beam_pos[1] < 0:
        return
    if beam_pos in energized and beam_dir in energized[beam_pos]:
        return # Already traversed
    # next_tile = (beam_pos[0] + beam_dir[0], beam_pos[1] + beam_dir[1])
    # print(f"{next_tile=}")
    # energized[next_tile] = ''
    try:
        next_tile = grid[beam_pos[1]][beam_pos[0]]
    except IndexError:
        return
    energized[beam_pos].append(beam_dir)
    return moves[beam_dir][next_tile]
    # print(f"{beam_dir=} {beam_pos=} {next_tile=}")
    # for next_dir in moves[beam_dir][next_tile]:
    #     next_pos = beam_pos[0] + next_dir[0], beam_pos[1] +  next_dir[1]
    #     get_next_dirs(next_dir, next_pos)


def traverse_beam(beam_dir, beam_pos, identifier=0):
    idnt = identifier + 1
    for i in range(len(grid) ** 2):
        next_dirs = get_next_dirs(beam_dir, beam_pos)
        if not next_dirs:
            return
        if len(next_dirs) == 2:
            next_dir = next_dirs[1]
            next_pos = beam_pos[0] + next_dir[0], beam_pos[1] + next_dir[1]
            traverse_beam(next_dir, next_pos, idnt)
            idnt == 1

        beam_dir = next_dirs[0]
        beam_pos = beam_pos[0] + beam_dir[0], beam_pos[1] + beam_dir[1]

    return

# beam = [(1, 0), (0, 0)]
beam_dir = (1, 0)
beam_pos = (0, 0)

all_options = []
for i in range(len(grid[0])):
    # FROM TOP
    beam_dir = (0, 1)
    beam_pos = (i, 0)
    all_options.append((beam_dir, beam_pos))
    # FROM BOTTOM
    beam_dir = (0, -1)
    beam_pos = (i, len(grid))
    all_options.append((beam_dir, beam_pos))

for i in range(len(grid)):
    # FROM LEFT
    beam_dir = (1, 0)
    beam_pos = (0, i)
    all_options.append((beam_dir, beam_pos))
    # FROM Right
    beam_dir = (-1, 0)
    beam_pos = (len(grid[0]), i)
    all_options.append((beam_dir, beam_pos))

max_energy = 0
for beam_dir, beam_pos in all_options:
    energized.clear()
    traverse_beam(beam_dir, beam_pos)
    if len(energized) > max_energy:
        max_energy = len(energized)
    print(beam_dir, beam_pos, 'PRODUCES', len(energized))
print(max_energy)
# for i in range(10000):
#     next_dirs, beam_pos = get_next_dirs(beam_dir, beam_pos)
#     for next_dir in next_dirs:
#         next_pos = beam_pos[0] + next_dir[0], beam_pos[1] + next_dir[1]
print(len(energized), energized)
