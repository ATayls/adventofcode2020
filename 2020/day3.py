with open(r"data/2020/day3_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]


def traverse(tree_map, across, down):
    pos = (0, 0)
    max_y = len(tree_map)
    encounters = {"#": 0, ".": 0}
    while pos[1] < max_y:
        # Get row
        row = tree_map[pos[1]]
        # Get current location
        location = row[pos[0]]
        # Store location
        encounters[location] += 1
        # Move
        pos = ((pos[0] + across) % len(row), pos[1] + down)
    print(f"You hit {encounters['#']} Trees!")
    return encounters["#"]


# Part 1
answer1 = traverse(puzzle_input, 3, 1)

# Part 2
answer2 = (
    traverse(puzzle_input, 1, 1)
    * traverse(puzzle_input, 3, 1)
    * traverse(puzzle_input, 5, 1)
    * traverse(puzzle_input, 7, 1)
    * traverse(puzzle_input, 1, 2)
)

print(f"Part1 Answer {answer1}")
print(f"Part2 Answer {answer2}")
