from collections.abc import Callable
from pathlib import Path
from typing import Any

import requests

from elf.config import get_cache_input_file, get_session_token
from elf.exceptions import InputFetchError
from elf.utils import parse_input

# 🎁 Elf Magic Input Fetcher 🎁 #


def get_input(year: int, day: int, session_token: str | None = None) -> str:
    """
    Fetch the Advent of Code puzzle input for a specific year and day.

    🎄 The elves are gathering the puzzle input from Santa's workshop!

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
        session_token (Optional[str]): Your Advent of Code session token. If not provided,
            it will be retrieved from the environment variable 'AOC_SESSION_COOKIE'.

    Returns:
        str: The puzzle input for the specified day.

    Raises:
        InputFetchError: If there is an issue fetching the puzzle input.
        ValueError: If the session token is not provided and not found in the environment.
    """
    session_token = get_session_token(session_token)

    cache_file = get_cache_input_file(year, day)

    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8").rstrip()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_token}",
        "User-Agent": "cak (+https://github.com/cak)",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        input_data = response.text.rstrip()

        # Ensure the cache directory exists
        cache_file.parent.mkdir(parents=True, exist_ok=True)

        # Save the input data to cache
        cache_file.write_text(input_data, encoding="utf-8")

        return input_data
    except requests.exceptions.RequestException as e:
        raise InputFetchError(
            f"🛑 Uh-oh! An error occurred while fetching the puzzle input: {e} ❄️"
        ) from e


def read_input_file(
    filename: str | Path, parser: Callable[[str], Any] = parse_input
) -> Any:
    """Reads and parses the input file from the given filename.

    🎁 Unwrapping the puzzle input from the specified file! 🎄

    Args:
        filename (Union[str, Path]): The path to the input file.
        parser (Callable[[str], Any]): A function that takes the file content as a string and returns the parsed data.
            Defaults to `parse_input`.

    Returns:
        Any: The parsed data as returned by the parser function.

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    filepath = Path(filename)
    if not filepath.exists():
        raise FileNotFoundError(
            f"❗ {filepath} not found. 🎄 The elves must have misplaced it! 🎁"
        )
    return parser(filepath.read_text())
