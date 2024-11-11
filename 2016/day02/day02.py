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
    key_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Remove all whitespace from each line
    data = ["".join(line.split()) for line in data]

    x_axis = 1
    y_axis = 1

    bathroom_code = []

    codes = [list(c) for c in data]

    for code in codes:
        for move in code:
            if move == "U":
                y_axis = max(0, y_axis - 1)
            elif move == "D":
                y_axis = min(2, y_axis + 1)
            elif move == "L":
                x_axis = max(0, x_axis - 1)
            elif move == "R":
                x_axis = min(2, x_axis + 1)
            else:
                raise ValueError(f"Invalid move: {move}")

        bathroom_code.append(key_pad[y_axis][x_axis])

    answer = int("".join(str(i) for i in bathroom_code))

    return answer


@elf.timer()
def part2(data: list[str]) -> str:
    """🎅 Solve Part 2 of the puzzle 🎅

    Sprinkle some extra magic for Part 2! ✨

    Args:
        data (List[str]): The puzzle input data as a list of strings.

    Returns:
        int: The result for Part 2.
    """
    key_pad = [
        [None, None, "1", None, None],
        [None, "2", "3", "4", None],
        ["5", "6", "7", "8", "9"],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]

    # Remove all whitespace from each line
    data = ["".join(line.split()) for line in data]

    y_axis = 2
    x_axis = 0

    bathroom_code = []

    codes = [list(c) for c in data]

    for code in codes:
        for move in code:
            if move == "U":
                move_y_axis = max(0, y_axis - 1)
                if key_pad[move_y_axis][x_axis] is not None:
                    y_axis = move_y_axis
            elif move == "D":
                move_y_axis = min(4, y_axis + 1)
                if key_pad[move_y_axis][x_axis] is not None:
                    y_axis = move_y_axis
            elif move == "L":
                move_x_axis = max(0, x_axis - 1)
                if key_pad[y_axis][move_x_axis] is not None:
                    x_axis = move_x_axis
            elif move == "R":
                move_x_axis = min(4, x_axis + 1)
                if key_pad[y_axis][move_x_axis] is not None:
                    x_axis = move_x_axis
            else:
                raise ValueError(f"Invalid move: {move}")

        bathroom_code.append(key_pad[y_axis][x_axis])

    answer = "".join(str(i) for i in bathroom_code)

    return answer


if __name__ == "__main__":
    # Inline test data
    test_input = """
    ULL
    RRDDD
    LURDL
    UUUUD
    """.strip()

    expected_part1 = 1985  # Replace with the expected result for Part 1
    expected_part2 = "5DB3"  # Replace with the expected result for Part 2

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
