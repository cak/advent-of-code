import time
from functools import wraps
from typing import Any, Callable

from elf.messages import get_timer_message

# 🎁 Elf Utility Functions 🎁 #


def parse_input(input_str: str) -> list[str]:
    """Parses the input string into a list of lines.

    🎄 Splitting the input into delightful pieces! 🎁

    Args:
        input_str (str): The raw input string.

    Returns:
        list[str]: A list of input lines.
    """
    return input_str.strip().splitlines()


def timer(enabled: bool = True) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator to measure the execution time of functions.

    🕒 Timing the magic of your functions! ✨

    Args:
        enabled (bool): Whether to enable timing.

    Returns:
        Callable: The decorated function.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = 0  # Initialize start_time to avoid unbound variable issues
            if enabled:
                start_time = time.perf_counter()
            result = func(*args, **kwargs)
            if enabled:
                end_time = time.perf_counter()
                print(
                    f"⏱️ Function '{func.__name__}' took {end_time - start_time:.6f}s to complete. {get_timer_message()}"
                )
            return result

        return wrapper

    return decorator
