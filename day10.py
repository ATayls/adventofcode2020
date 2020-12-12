import numpy as np
import itertools

with open(r"data/day10_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

def get_jolt_differences(adapter_list):
    """ Get list of all jolt differences including from plug and to phone"""
    adapter_list = sorted(adapter_list)
    adapter_list.insert(0, 0)
    adapter_list.append(max(adapter_list)+3)
    return adapter_list, np.diff(adapter_list)

def get_permutations(adapter_list):
    """ Get a list of permutations given a sorted adapter_list"""
    valid_perms = []
    if len(adapter_list) <= 2:
        valid_perms.append(adapter_list)
    else:
        search_list = adapter_list[1:-1]
        perms = [list(x) for l in range(1, len(search_list)+1) for x in itertools.combinations(search_list, l)]
        for p in perms:
            p.insert(0, adapter_list[0])
            p.append(adapter_list[-1])
            if max(np.diff(p)) <= 3:
                valid_perms.append(p)
        if adapter_list[-1] - adapter_list[0] <= 3:
            valid_perms.append([adapter_list[0],adapter_list[-1]])
    return valid_perms

def get_total_permutations(adapter_list, jolt_differences):
    """ Get count of all total permutations given an adapter list and its jolt differences"""
    sublist = []
    total_perms = 1
    for i, jd in enumerate(jolt_differences):
        if jd == 3:
            sublist.append(adapter_list[i])
            perms = get_permutations(sublist)
            total_perms *= len(perms)
            sublist = []
            continue
        else:
            sublist.append(adapter_list[i])
    return total_perms

puzzle_input = [int(x) for x in puzzle_input]

sorted_adapter_list, j_diff = get_jolt_differences(puzzle_input)

# Part 1
print(list(j_diff).count(1) * list(j_diff).count(3))

# Part 2
answer = get_total_permutations(sorted_adapter_list, j_diff)
print(answer)