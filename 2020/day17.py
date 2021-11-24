import numpy as np
from scipy import ndimage

with open(r"data/2020/day17_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]


def create_cube(puzzle_input, border_size, hypercube=False):
    """
    Parse the puzzle input to the conway cube
    :param puzzle_input:
    :param border_size: border of zeros
    :param hypercube: bool, if cube is 4 dimensional
    :return:
    """
    grid = []
    for line in puzzle_input:
        line = line.replace(".", "0")
        line = line.replace("#", "1")
        row = [int(x) for x in line]
        grid.append(row)
    grid = np.array(grid)
    if hypercube:
        cube = np.zeros((grid.shape[0], grid.shape[1], max(grid.shape), max(grid.shape)))
        cube[:, :, int(max(grid.shape) / 2), int(max(grid.shape) / 2)] = grid
        cube = np.pad(cube, pad_width=border_size, mode='constant', constant_values=0)
    else:
        cube = np.zeros((grid.shape[0], grid.shape[1], max(grid.shape)))
        cube[:, :, int(max(grid.shape)/2)] = grid
        cube = np.pad(cube, pad_width=border_size, mode='constant', constant_values=0)
    return cube

def evolve(cube):
    """
    Evolve the cube according to the defined neighbourhood rules
    :param cube: nd array
    :return: nd array
    """
    # create kernel 'neighbourhood'
    in_shp = np.shape(cube)

    # Create the kernel
    kernel = np.ones(tuple([3] * len(in_shp)))
    np.put(kernel, kernel.size // 2, 0)

    # Convolve kernel to create a num_neighbours array
    neighbourhood = ndimage.convolve(cube, kernel, mode="constant", cval=0.0)

    # initialise empty grid
    new_state = np.zeros_like(cube)

    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
    new_state[np.where(((neighbourhood == 3) | (neighbourhood == 2)) & (cube == 1))] = 1
    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active
    new_state[np.where((neighbourhood == 3) & (cube == 0))] = 1

    return new_state

# Part1
cube = create_cube(puzzle_input, 10)
for cycle in range(6):
    cube = evolve(cube)
print(np.sum(np.sum(cube)))

# Part2
cube = create_cube(puzzle_input, 10, hypercube=True)
for cycle in range(6):
    cube = evolve(cube)
print(np.sum(np.sum(np.sum(cube))))

