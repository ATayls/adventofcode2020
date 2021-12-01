import os
from pathlib import Path
from dotenv import load_dotenv

AOC_URL = r'https://adventofcode.com'

BASE_DIR = Path(__file__).parent.absolute()

load_dotenv(dotenv_path=BASE_DIR.joinpath('config.env'))
SESSION = os.environ.get("AOC_SESSION")

DATA_DIR = BASE_DIR.joinpath("data")