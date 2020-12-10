import copy

with open(r"data/day9_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

def get_sums(list_of_ints):
    """ Get all possible sums from using two values in a list of ints """
    sums = []
    rotating_list = copy.deepcopy(list_of_ints)
    for i in range(len(list_of_ints)):
        rotating_list.append(rotating_list.pop(0))
        sums += [sum(list(x)) for x in zip(list_of_ints, rotating_list)]

    return list(set(sums))


def validity_check(puzzle_input, preamble_len):
    """ Check for input validity, return first invalid value"""
    for i in range(preamble_len, len(puzzle_input)-1):
        available_set = puzzle_input[i-preamble_len:i]
        valid_values = get_sums(available_set)
        value = puzzle_input[i]
        if value not in valid_values:
            return value

def find_contiguous_set(puzzle_input, value, min_size):
    """ find the contiguous set that sums to the input value"""
    for i in range(len(puzzle_input)):
        contiguous_set = []
        for j in range(i, len(puzzle_input)):
            contiguous_set.append(puzzle_input[j])
            if len(contiguous_set) < min_size:
                continue
            elif sum(contiguous_set) > value:
                break
            elif sum(contiguous_set) == value:
                return contiguous_set
            else:
                continue


puzzle_input = [int(x) for x in puzzle_input]

# Part 1
invalid_value = validity_check(puzzle_input, 25)
print(invalid_value)

# Part 2
contiguous_set = find_contiguous_set(puzzle_input, invalid_value, 2)
print(min(contiguous_set) + max(contiguous_set))