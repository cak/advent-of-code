import os
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
