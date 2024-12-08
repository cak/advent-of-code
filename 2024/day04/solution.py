from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅

directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
    "up-right": (-1, 1),
    "up-left": (-1, -1),
    "down-right": (1, 1),
    "down-left": (1, -1),
}


def move_in_grid(grid, direction):
    d = directions[direction]
    count = 0
    word_length = 4
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            result = []
            for step in range(word_length):
                new_i = i + step * d[0]
                new_j = j + step * d[1]

                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                    result.append(grid[new_i][new_j])
                else:
                    break

            if "".join(result) == "XMAS":
                count += 1

    return count


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    grid = [list(x) for x in data]

    answer = 0
    for direction in directions.keys():
        ans = move_in_grid(grid, direction=direction)
        answer += ans

    return answer


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""
    # TODO: Implement the solution for Part 2
    return len(data)


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
