import re

with open(r"day4_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

validkeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optionalkeys = ["cid"]

def pass_list_to_dict(pass_list):
    pass_str = " ".join(pass_list)
    pass_dict = {x.split(':')[0]: x.split(':')[1] for x in pass_str.split(" ")}
    return pass_dict

def has_valid_keys(pass_dict):
    if set(pass_dict) == set(validkeys + optionalkeys):
        return True
    elif set(pass_dict) == set(validkeys):
        return True
    else:
        return False

def has_valid_values(pass_dict):
    # Check birth year
    if not (1920 <= int(pass_dict["byr"]) <= 2002):
        return False
    # Check Issue
    elif not (2010 <= int(pass_dict["iyr"]) <= 2020):
        return False
    # Check expiration
    elif not (2020 <= int(pass_dict["eyr"]) <= 2030):
        return False
    # Check height
    elif not (pass_dict["hgt"].endswith("cm") or pass_dict["hgt"].endswith("in")):
        return False
    elif pass_dict["hgt"].endswith("cm") and not (150 <= int(pass_dict["hgt"][:-2]) <= 193):
        return False
    elif pass_dict["hgt"].endswith("in") and not (59 <= int(pass_dict["hgt"][:-2]) <= 76):
        return False
    # Check hair colour
    elif not pass_dict["hcl"].startswith("#"):
        return False
    elif not len(pass_dict["hcl"]) < 8:
        return False
    elif bool(re.compile(r'[^a-f0-9]').search(pass_dict["hcl"][1:])):
        return False
    # Check eye colour
    elif pass_dict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    # Check pid
    elif not (len(pass_dict["pid"]) == 9 and pass_dict["pid"].isnumeric()):
        return False
    else:
        return True


def check_all(batch_input):
    individual_pass_list = []
    valid_keys = []
    valid_values = []
    for line in batch_input:
        if line:
            individual_pass_list.append(line)
        else:
            pass_dict = pass_list_to_dict(individual_pass_list)


            if has_valid_keys(pass_dict):
                valid_keys.append(True)
                valid_values.append(has_valid_values(pass_dict))
            else:
                valid_keys.append(False)
                valid_values.append(False)

            individual_pass_list = []

    # Check for remaining passports
    if individual_pass_list:
        passport_str = " ".join(individual_pass_list)
        valid_keys.append(has_valid_keys(passport_str))

    return valid_keys, valid_values

# Part 1
valid_keys, valid_values = check_all(puzzle_input)
print(sum(valid_keys))

# Part 2
print(sum(valid_values))