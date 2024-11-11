import os
import platform
from pathlib import Path
from typing import Optional

# 🎄 Elf Configuration 🎄 #


def get_session_token(session_token: Optional[str] = None) -> str:
    """
    Retrieve the Advent of Code session token.

    🎅 Santa's magic session cookie helps the elves access the workshop!

    Args:
        session_token (Optional[str]): The session token to use. If None,
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
        raise ValueError(
            f"🎅 Oh no! Santa's session cookie is missing. Please set the '{env_var}' "
            "environment variable or pass the session token explicitly. 🎄"
        )


def get_cache_dir() -> Path:
    """Return the appropriate cache directory based on the OS."""
    if platform.system() == "Windows":
        return (
            Path(os.getenv("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "elf"
        )
    else:
        return Path(os.getenv("XDG_CACHE_HOME", Path.home() / ".cache")) / "elf"


def get_cache_guess_file(year: int, day: int) -> Path:
    cache_dir = get_cache_dir()
    cache_file = cache_dir / f"{year:04d}" / f"{day:02d}" / "guesses.csv"
    return cache_file


def get_cache_input_file(year: int, day: int) -> Path:
    cache_dir = get_cache_dir()
    cache_file = cache_dir / f"{year:04d}" / f"{day:02d}" / "input.txt"
    return cache_file
