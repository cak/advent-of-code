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
        data (list[str]): The puzzle input data as a list of strings.

    Returns:
        int: The result for Part 1.
    """
    parse_data = [list(map(int, line.split())) for line in data]

    valid_triangles = 0

    for sides in parse_data:
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            valid_triangles += 1

    return valid_triangles


@elf.timer()
def part2(data: list[str]) -> int:
    """🎅 Solve Part 2 of the puzzle 🎅

    Sprinkle some extra magic for Part 2! ✨

    Args:
        data (list[str]): The puzzle input data as a list of strings.

    Returns:
        int: The result for Part 2.
    """
    parse_data: list[list[int]] = [list(map(int, line.split())) for line in data]

    valid_triangles = 0

    col_one = [x[0] for x in parse_data]
    col_two = [x[1] for x in parse_data]
    col_three = [x[2] for x in parse_data]

    # Interleave rows to form vertical triangles
    combined_rows = [col_one, col_two, col_three]

    for columns in combined_rows:
        groups = [columns[i : i + 3] for i in range(0, len(columns), 3)]
        for a, b, c in groups:
            sides = [a, b, c]
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                valid_triangles += 1
    return valid_triangles


if __name__ == "__main__":
    # Inline test data
    test_input = """
    101 301 501
    102 302 502
    103 303 503
    201 401 601
    202 402 602
    203 403 603
    """.strip()

    expected_part1 = 42  # Replace with the expected result for Part 1
    expected_part2 = 84  # Replace with the expected result for Part 2

    # Combine expected outputs into a single string, each on a new line
    expected_output = f"{expected_part1}\n{expected_part2}"

    # Determine the base directory (current script's directory)
    base_dir = Path(__file__).parent

    args(
        part1=part1,
        part2=part2,
        expected_output=expected_output,
        test_input=test_input,
        base_dir=base_dir,
    )
