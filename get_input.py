import argparse
from datetime import datetime
import requests

from settings import DATA_DIR, AOC_URL, SESSION


def make_request(year: int, day: int):
    """ Scrape input from AOC input url """
    input_url = f"{AOC_URL}/{year}/day/{day}/input"
    r = requests.get(input_url, cookies={"session": SESSION})
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.text:
            raise ValueError(r.text)
        else:
            raise(e)
    return r.text


def get_data(year: int, day: int):
    """ Get input data for given year and day. Save to data dir."""
    data_input = make_request(year, day)
    output_dir = DATA_DIR.joinpath(str(year))
    output_dir.mkdir(parents=True, exist_ok=True)
    title = f"day{day}_in.txt"
    full_path = output_dir.joinpath(title)
    if not full_path.exists():
        (output_dir / title).write_text(data_input)


def isfloat(element):
    try:
        float(element)
        assert(str(element) == str(float(element)))
        return True
    except (ValueError, AssertionError):
        return False


def isint(element):
    try:
        int(element)
        assert (str(element) == str(int(element)))
        return True
    except (ValueError, AssertionError):
        return False


def convertor(element):
    if isint(element):
        return int(element)
    elif isfloat(element):
        return float(element)
    else:
        raise ValueError


def load_data(year: int, day: int):
    """ Load input data from path. Get from url if missing"""
    data_path = DATA_DIR.joinpath(str(year), f"day{day}_in.txt")
    if data_path.exists():
        with open(data_path, 'r') as f:
            input_list = [x.strip() for x in f.readlines()]
        try:
            input_list = [convertor(x) for x in input_list]
        except ValueError:
            pass
    else:
        get_data(year, day)
        input_list = load_data(year, day)
    return input_list


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Retrieve day input file")
    parser.add_argument(
        "year", help="Advent of code year", type=int, choices=range(2015,datetime.now().year+1)
    )
    parser.add_argument("day", help="Advent of code day", type=int)
    args = parser.parse_args()

    get_data(args.year, args.day)
