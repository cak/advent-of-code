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

    def rotate(direction: str, facing: int):
        if direction == "R":
            facing = (facing + 1) % 4
        elif direction == "L":
            facing = (facing - 1) % 4
        return facing

    direction = ["N", "E", "S", "W"]
    north_south = 0
    east_west = 0

    facing = 0
    coordinates: list[list[str]] = [d.split(", ") for d in data]
    flattened_coordinates = [item for sublist in coordinates for item in sublist]

    for move in flattened_coordinates:
        turn_direction = move[0]
        steps = int(move[1:])
        facing = rotate(turn_direction, facing)

        if direction[facing] == "N":
            north_south += steps
        elif direction[facing] == "S":
            north_south -= steps
        elif direction[facing] == "E":
            east_west += steps
        elif direction[facing] == "W":
            east_west -= steps

    print(north_south, east_west)
    return abs(north_south + east_west)


@elf.timer()
def part2(data: list[str]) -> int:
    """🎅 Solve Part 2 of the puzzle 🎅

    Sprinkle some extra magic for Part 2! ✨

    Args:
        data (List[str]): The puzzle input data as a list of strings.

    Returns:
        int: The result for Part 2.
    """

    def rotate(direction: str, facing: int):
        if direction == "R":
            facing = (facing + 1) % 4
        elif direction == "L":
            facing = (facing - 1) % 4
        return facing

    direction = ["N", "E", "S", "W"]
    north_south = 0
    east_west = 0

    facing = 0
    coordinates: list[list[str]] = [d.split(", ") for d in data]
    flattened_coordinates = [item for sublist in coordinates for item in sublist]

    visited_coordinates = []

    for move in flattened_coordinates:
        turn_direction = move[0]
        steps = int(move[1:])
        facing = rotate(turn_direction, facing)

        for _ in range(steps):
            if direction[facing] == "N":
                north_south += 1
            elif direction[facing] == "S":
                north_south -= 1
            elif direction[facing] == "E":
                east_west += 1
            elif direction[facing] == "W":
                east_west -= 1

            if (east_west, north_south) in visited_coordinates:
                return abs(north_south) + abs(east_west)

            visited_coordinates.append((east_west, north_south))

    return len(data)


if __name__ == "__main__":
    # Inline test data
    test_input = """
    R8, R4, R4, R8
    """.strip().split("\n")

    expected_part1 = 12  # Replace with the expected result for Part 1
    expected_part2 = 4  # Replace with the expected result for Part 2

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
