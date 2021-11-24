import copy

with open(r"data/2020/day8_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

def create_data_structure(puzzle_input):
    boot_list = []
    for line in puzzle_input:
        cmd, value = line.split(" ")
        boot_list.append({"command": cmd, "value": int(value), "accessed": False})
    return boot_list

def run_boot(boot_list):
    boot_list = copy.deepcopy(boot_list)
    accumulator = 0
    pos = 0
    complete = False
    while True:

        if pos >= len(boot_list):
            print(f"Completed with accumulator at {accumulator}")
            complete = True
            break

        cmd = boot_list[pos]["command"]
        val = boot_list[pos]["value"]
        accessed = boot_list[pos]["accessed"]

        if accessed:
            print(f"Entered infinite loop, Exiting with accumulator at {accumulator}")
            break
        else:
            boot_list[pos]["accessed"] = True

        if cmd == "nop":
            pos += 1
        elif cmd == "acc":
            accumulator += val
            pos += 1
        elif cmd == "jmp":
            pos += val
        else:
            raise ValueError("Command unrecognised")

    return complete, accumulator

def brute_force_fix(boot_list):

    for i, item in enumerate(boot_list):
        if item["command"] == "jmp":
            new_boot_list = copy.deepcopy(boot_list)
            new_boot_list[i]["command"] = "nop"
            complete, accumulator = run_boot(new_boot_list)
            if complete:
                return new_boot_list, accumulator
        elif item["command"] == "nop":
            new_boot_list = copy.deepcopy(boot_list)
            new_boot_list[i]["command"] = "jmp"
            complete, accumulator = run_boot(new_boot_list)
            if complete:
                return new_boot_list, accumulator


boot_list = create_data_structure(puzzle_input)

# Part 1
run_boot(boot_list)

# Part 2
brute_force_fix(boot_list)
