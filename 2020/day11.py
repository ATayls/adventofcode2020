import numpy as np
from scipy.signal import convolve2d
from math import sqrt

with open(r"data/2020/day11_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

def create_grid(puzzle_input):
    grid = []
    for line in puzzle_input:
        line = line.replace("L", "0")
        line = line.replace("#", "1")
        line = line.replace(".", "2")
        row = [int(x) for x in line]
        grid.append(row)
    grid = np.array(grid)
    mask = grid == 2
    grid[grid == 2] = 0
    mx = np.ma.masked_array(grid, mask=mask)
    return mx

def evolve_part1(grid):
    """
    Evaluate grid following rules.
    Implemented using Scipy convolutions
    :param grid: ndarray
    :return: ndarray
    """
    # create number of neighbours array 'neighbourhood'
    in_shp = np.shape(grid)
    kernal = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])
    conv_grid = convolve2d(grid,kernal,boundary='fill',fillvalue=0)
    neighbourhood = conv_grid[1:in_shp[0]+1,1:in_shp[1]+1]

    # initialise new grid
    new_state = np.ma.copy(grid)

    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    new_state[np.where((neighbourhood == 0) & (grid == 0))] = 1
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    new_state[np.where((neighbourhood >= 4) & (grid == 1))] = 0

    return new_state


def evolve_part2(grid):
    _ , cols, rows = np.shape(grid)
    for row in range(rows):
        for col in range(cols):
            print(row,col)

grid = create_grid(puzzle_input)

# Part 1
# occupied_counts = []
# while True:
#     grid = evolve_part1(grid)
#     seats_occ = np.ma.sum(grid)
#     occupied_counts.append(seats_occ)
#
#     # Check if last 10 counts are the same
#     if len(occupied_counts) > 10:
#         if all(x == occupied_counts[-10:][0] for x in occupied_counts[-10:]):
#             print(occupied_counts[-1])
#             break

# Change grid for part2
empty_seats = np.array(grid == 0)
occupied_seats = np.array(grid == 1)
no_seats = grid.mask
grid = np.array([occupied_seats,empty_seats,no_seats])
while True:
    grid = evolve_part2(grid)