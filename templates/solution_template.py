import sys
from pathlib import Path

# 🎄 Define the base directory (two levels up from the script location) 🎄
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Add the project root to sys.path if not installing elf as a package
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

import elf  # Import elf after modifying sys.path  # noqa: E402
from utils import args  # Import utils after modifying sys.path  # noqa: E402

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


@elf.timer()
def part1(data: list[str]) -> int:
    """🎅 Solve Part 1 of the puzzle 🎅

    The elves are eager to see your solution! 🎁

    Args:
        data (List[str]): The puzzle input data as a list of strings.

    Returns:
        int: The result for Part 1.
    """
    # TODO: Implement the solution for Part 1
    return len(data)


@elf.timer()
def part2(data: list[str]) -> int:
    """🎅 Solve Part 2 of the puzzle 🎅

    Sprinkle some extra magic for Part 2! ✨

    Args:
        data (List[str]): The puzzle input data as a list of strings.

    Returns:
        int: The result for Part 2.
    """
    # TODO: Implement the solution for Part 2
    return len(data)


if __name__ == "__main__":
    # Inline test data
    test_input = """
    # Add your test input data here, for example:
    Line 1 of test input
    Line 2 of test input
    """.strip().split("\n")

    expected_part1 = 42  # Replace with the expected result for Part 1
    expected_part2 = 84  # Replace with the expected result for Part 2

    # Determine the base directory (current script's directory)
    base_dir = Path(__file__).parent

    args(
        part1=part1,
        part2=part2,
        expected_part1=expected_part1,
        expected_part2=expected_part2,
        test_input=list(test_input),
        base_dir=base_dir,
    )
