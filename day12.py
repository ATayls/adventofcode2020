with open(r"data/day12_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

def navigate_part1(instructions: list):
    N = 0
    E = 0
    dir = 90
    for line in instructions:
        action = line[0]
        value = int(line[1:])
        if action == "N" or (dir == 0 and action == "F"):
            N += value
        elif action == "E" or (dir == 90 and action == "F"):
            E += value
        elif action == "S" or (dir == 180 and action == "F"):
            N -= value
        elif action == "W" or (dir == 270 and action == "F"):
            E -= value
        elif action == "R":
            dir = (dir+value)%360
        elif action == "L":
            dir = (dir-value)%360
    return N, E


def navigate_part2(instructions: list):
    wp = (1, 10)
    ship = (0, 0)
    for line in instructions:
        action = line[0]
        value = int(line[1:])
        if action == "N":
            wp[0] += value
        elif action == "E":
            wp[1] += value
        elif action == "S":
            wp[0] -= value
        elif action == "W":
            wp[1] -= value


# Part 1
loc = navigate_part1(puzzle_input)
print(abs(loc[0])+abs(loc[1]))

# Part 2
loc = navigate_part2(puzzle_input)
print(abs(loc[0])+abs(loc[1]))