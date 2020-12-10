with open(r"data/day7_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]


def parse_rule(rule: str) -> dict:
    """Function to parse a single rule"""
    colour = rule.split("bags")[0].strip()
    inner_bags = [" ".join(x.strip().split(" ")[:-1]) for x in rule.split("contain")[1].split(",")]
    if inner_bags[0] == "no other":
        output = {colour: None}
    else:
        inner_bag_dict = {" ".join(x.split(" ")[1:]): int(x.split(" ")[0]) for x in inner_bags}
        output = {colour: inner_bag_dict}
    return output


def create_data_structure(puzzle_input):
    """ create dict structure to hold puzzle input info"""
    rule_dict = {}
    for rule_line in puzzle_input:
        rule = parse_rule(rule_line)
        rule_dict = {**rule_dict, **rule}
    return rule_dict


def find_colour(bag_colour, search_colour, rule_dict):
    """ Traverse rules to find a search_colour in your bag, recursion"""
    if rule_dict[bag_colour] is None:
        return False
    elif search_colour in rule_dict[bag_colour].keys():
        return True
    else:
        child_searches = [find_colour(child_colour, search_colour, rule_dict) for child_colour in rule_dict[bag_colour].keys()]
        if any(child_searches):
            return True
        else:
            return False

def count_bags(bag_colour, rule_dict):
    """ Count bags within your bag, recursion"""
    if rule_dict[bag_colour] is None:
        return 0
    else:
        child_counts = [(1+count_bags(child_colour, rule_dict))*count for child_colour, count in rule_dict[bag_colour].items()]
        return sum(child_counts)


rule_dict = create_data_structure(puzzle_input)

# Part 1
count = 0
for bag_colour in rule_dict.keys():
    if find_colour(bag_colour, "shiny gold", rule_dict):
        count+=1
print(count)

# Part 2
print(count_bags("shiny gold", rule_dict))
