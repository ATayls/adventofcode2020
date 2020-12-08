import numpy as np

with open(r"data/day5_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]


def get_seat_position(seat_str: str, num_rows: int, num_cols: int) -> tuple:
    """Parse seat position string to row and column"""
    row_str = seat_str[0:7]
    col_str = seat_str[7:]

    # Find row
    rows = list(range(0, num_rows))
    for char in row_str:
        if char == "F":
            rows = [x for x in rows if x < (len(rows) / 2) + min(rows)]
        elif char == "B":
            rows = [x for x in rows if x >= (len(rows) / 2) + min(rows)]

    # Find column
    cols = list(range(0, num_cols))
    for char in col_str:
        if char == "L":
            cols = [x for x in cols if x < (len(cols) / 2) + min(cols)]
        elif char == "R":
            cols = [x for x in cols if x >= (len(cols) / 2) + min(cols)]

    return rows[0], cols[0]


def get_seat_ids(boarding_passes):
    output = []
    for seat_str in boarding_passes:
        position = get_seat_position(seat_str, 128, 8)
        seat_id = position[0] * 8 + position[1]
        output.append(seat_id)
    return output


def find_my_seat(seat_ids):
    # Order all seat ids and get difference to next item.
    seat_ids = sorted(seat_ids)
    diff = list(np.diff(seat_ids))
    # Get seat index with space next to it
    seat_index = list(diff).index(2)
    # return my seat
    return seat_ids[seat_index] + 1


all_ids = get_seat_ids(puzzle_input)

# Part 1
print(max(all_ids))

# Part 2
print(find_my_seat(all_ids))
