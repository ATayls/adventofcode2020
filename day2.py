with open(r"day2_in.txt", "r") as f:
	input_list = [x.strip() for x in f.readlines()]


def check_valid(input_line: str, policy: int) -> bool:
	limits, letter, passw = input_line.split(" ")
	limits = [int(x) for x in limits.split("-")]
	letter = letter[:-1]

	if policy == 1:
		count = passw.count(letter)
		return limits[0] <= count <= limits[1]
	elif policy == 2:
		index1 = limits[0] - 1
		index2 = limits[1] - 1
		return (passw[index1] == letter) != (passw[index2] == letter)
	else:
		raise ValueError("Policy not found")


def count_valids(list_in, policy):
	valids = [check_valid(x, policy) for x in list_in]
	return sum(valids)


# Part1
print(count_valids(input_list, 1))

# Part2
print(count_valids(input_list, 2))