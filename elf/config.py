import os
import platform
from pathlib import Path

from elf.exceptions import MissingSessionTokenError

# 🎄 Elf Configuration 🎄 #


def get_session_token(session_token: str | None = None) -> str:
    """
    Retrieve the Advent of Code session token.

    🎅 Santa's magic session cookie helps the elves access the workshop!

    Args:
        session_token (str | None): The session token to use. If None,
            attempts to retrieve it from the 'AOC_SESSION_COOKIE' environment variable.

    Returns:
        str: The session token.

    Raises:
        ValueError: If the session token is not provided and not found in the environment.
    """
    env_var = "AOC_SESSION_COOKIE"
    if session_token:
        return session_token
    elif session_token_env := os.getenv(env_var):
        return session_token_env
    else:
        raise MissingSessionTokenError(env_var)


def get_cache_dir() -> Path:
    """Return the appropriate cache directory based on the OS.

    Checks for the 'ELF_CACHE_DIR' environment variable. If set, uses its value.
    Otherwise, on Windows, uses 'LOCALAPPDATA' or defaults to 'AppData/Local'.
    On other systems, uses 'XDG_CACHE_HOME' or defaults to '~/.cache'.

    Returns:
        Path: The path to the cache directory.
    """
    env_cache_dir = os.getenv("ELF_CACHE_DIR")
    if env_cache_dir:
        env_cache_dir = os.path.expandvars(os.path.expanduser(env_cache_dir))
        return Path(env_cache_dir)
    elif platform.system() == "Windows":
        return (
            Path(os.getenv("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "elf"
        )
    else:
        return Path(os.getenv("XDG_CACHE_HOME", Path.home() / ".cache")) / "elf"


def get_cache_guess_file(year: int, day: int) -> Path:
    """Get the path to the cache file for storing guesses.

    Args:
        year (int): The year of the challenge.
        day (int): The day of the challenge.

    Returns:
        Path: The path to the guesses cache file.
    """
    cache_dir = get_cache_dir()
    cache_file = cache_dir / f"{year:04d}" / f"{day:02d}" / "guesses.csv"
    return cache_file


def get_cache_input_file(year: int, day: int) -> Path:
    """Get the path to the cache file for storing input data.

    Args:
        year (int): The year of the challenge.
        day (int): The day of the challenge.

    Returns:
        Path: The path to the input cache file.
    """
    cache_dir = get_cache_dir()
    cache_file = cache_dir / f"{year:04d}" / f"{day:02d}" / "input.txt"
    return cache_file
