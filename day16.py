import numpy as np

with open(r"data/day16_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]


def parse_puzzle_in(puzzle_input):
    limits = {}
    your_ticket = None
    nearby_tickets = []
    section = 0
    for line in puzzle_input:
        if line == "":
            section += 1
        elif section == 0:
            field, rules = line.split(":")
            rule1, rule2 = rules.split("or")
            limits[field] = list(
                range(
                    int(rule1.split("-")[0].strip()),
                    int(rule1.split("-")[1].strip()) + 1,
                )
            ) + list(
                range(
                    int(rule2.split("-")[0].strip()),
                    int(rule2.split("-")[1].strip()) + 1,
                )
            )
        elif section == 1:
            if ":" not in line:
                your_ticket = [int(x) for x in line.split(",")]
        elif section == 2:
            if ":" not in line:
                nearby_tickets.append([int(x) for x in line.split(",")])

    return your_ticket, nearby_tickets, limits


your_ticket, nearby_tickets, limits = parse_puzzle_in(puzzle_input)

# Part 1
all_valid_values = []
for rule in limits.values():
    all_valid_values += rule
all_valid_values = list(set(all_valid_values))

invalid_ticket_values = []
valid_tickets = []
for ticket in nearby_tickets:
    valid = True
    for value in ticket:
        if value not in all_valid_values:
            invalid_ticket_values.append(value)
            valid = False
    if valid:
        valid_tickets.append(ticket)
print("Ticket scanning error rate ", sum(invalid_ticket_values))

# Part2
valid_array = np.array(valid_tickets)
position_results = {}
for position in range(len(your_ticket)):
    valid_fields = dict(limits)
    field_valid_values = valid_array[:, position]
    for value in field_valid_values:
        fields_to_drop = []
        for field, rule in valid_fields.items():
            if value not in rule:
                fields_to_drop.append(field)
        for field in fields_to_drop:
            del valid_fields[field]
    possible_fields = list(valid_fields.keys())
    print(f"Position {position}, valid sections: {valid_fields.keys()}")
    position_results[position] = possible_fields

final_results = {}
while len(final_results) < 20:
    found_fields = []
    for position, possible_fields in position_results.items():
        if possible_fields and len(possible_fields) == 1:
            found_fields.append(possible_fields[0])
            final_results[position] = possible_fields[0]
    for field in found_fields:
        for position, possible_fields in position_results.items():
            if field in possible_fields:
                position_results[position].remove(field)

answer = 1
for pos, field in final_results.items():
    if field.startswith("departure"):
        answer *= your_ticket[pos]

print(answer)
