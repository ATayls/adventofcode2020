puzzle_input = [8, 13, 1, 0, 18, 9]


def memory_game(starting_numbers, total_turns):
    """
    Memory game

    Consider the previous number in the list.
    If that was the first time the number has been spoken, the current player says 0.
    Otherwise, append how many turns apart the number is from when it was previously spoken.
    So, after the starting numbers, each turn results in that player speaking aloud either 0 (if the last number is new)
     or an age (if the last number is a repeat).
    """
    last_num = starting_numbers[-1]
    starting_numbers = {num: x + 1 for x, num in enumerate(starting_numbers[:-1])}
    for turn in range(len(starting_numbers) + 2, total_turns + 1):
        if last_num not in starting_numbers:
            new_num = 0
        else:
            turn_spoken = starting_numbers[last_num]
            new_num = (turn - 1) - turn_spoken
        starting_numbers[last_num] = turn - 1
        last_num = new_num
    print(f"Turn {turn}, number spoken {new_num}")


# Part 1
memory_game(puzzle_input, 2020)

# Part 2
memory_game(puzzle_input, 30000000)
