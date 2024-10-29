import os
import platform
from pathlib import Path

import requests

from elf.config import get_session_token
from elf.exceptions import InputFetchError
from elf.utils import parse_input

# 🎁 Elf Magic Input Fetcher 🎁 #


def get_cache_dir() -> Path:
    """Return the appropriate cache directory based on the OS."""
    if platform.system() == "Windows":
        return (
            Path(os.getenv("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "elf"
        )
    else:
        return Path(os.getenv("XDG_CACHE_HOME", Path.home() / ".cache")) / "elf"


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

    # Use user-specific cache directory without external dependencies
    cache_dir = get_cache_dir()
    cache_file = cache_dir / f"{year}" / f"day_{day}.txt"

    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8").rstrip()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_token}",
        "User-Agent": "elf-package/1.0 (+https://github.com/cak/elf)",
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


def read_input_file(filename: str | Path) -> list[str]:
    """Reads and parses the input file from the given filename.

    🎁 Unwrapping the puzzle input from the specified file! 🎄

    Args:
        filename (str | Path): The path to the input file.

    Returns:
        list[str]: A list of input lines.

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    filepath = Path(filename)
    if not filepath.exists():
        raise FileNotFoundError(
            f"❗ {filepath} not found. 🎄 The elves must have misplaced it! 🎁"
        )
    return parse_input(filepath.read_text())
