with open(r'data/2020/day1_in.txt', 'r') as f:
    input_list = [int(x.strip()) for x in f.readlines()]


def mul(list_in: list):
    total = 1
    for i in list_in:
        total *= i
    return total


def find_pair(list_in: list, val: int):
    for i, ii in enumerate(list_in):
        for jj in list_in[i + 1:]:
            c = ii + jj
            if c == val:
                return [ii, jj]
    return None


def find_general(list_in: list, val: int, num: int):
    if num == 2:
        return find_pair(list_in, val)
    else:
        for a, aa in enumerate(list_in):
            remainder = val - aa
            if remainder < 0:
                continue
            matches = find_general(list_in[a + 1:], remainder, num - 1)
            if matches:
                matches.append(aa)
                return matches


# Part 1
answer1 = find_general(input_list, 2020, 2)
print(answer1, mul(answer1))
answer2 = find_general(input_list, 2020, 3)
print(answer2, mul(answer2))
