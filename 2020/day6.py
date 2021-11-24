with open(r"data/2020/day6_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

def get_groups(all_answers: list) -> list:
    """ Use blank space lines to group together passenger groups"""
    group = []
    grouped = []
    for line in all_answers:
        if line:
            group.append(line)
        else:
            grouped.append(group)
            group = []

    if group:
        grouped.append(group)

    return grouped

def get_count_any(group: list) -> int:
    """ Get counts that any group member answered yes"""
    all_answers = "".join(group)
    return len(set(all_answers))

def get_count_all(group: list) -> int:
    """ Get counts where all group members answered yes"""
    group = [set(x) for x in group]
    return len(set.intersection(*group))

def get_counts(puzzle_input, all=False):
    """ Main function to return list of all counts for each group"""
    grouped_input = get_groups(puzzle_input)
    counts = []
    for group in grouped_input:
        if all:
            counts.append(get_count_all(group))
        else:
            counts.append(get_count_any(group))
    return counts

counts = get_counts(puzzle_input)
counts_all = get_counts(puzzle_input, True)

# Part 1
print(sum(counts))

# Part 2
print(sum(counts_all))