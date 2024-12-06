from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


def display_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def move_in_grid(grid) -> bool:
    bounds = True
    for i, row in enumerate(grid):
        # Handle "^" (moving up)
        if "^" in row:
            col = row.index("^")
            grid[i][col] = "X"
            if i - 1 >= 0:
                if grid[i - 1][col] == "#":
                    grid[i][col] = ">"
                else:
                    grid[i - 1][col] = "^"
            else:
                bounds = False

        # Handle "v" (moving down)
        elif "v" in row:
            col = row.index("v")
            grid[i][col] = "X"
            if i + 1 < len(grid):
                if grid[i + 1][col] == "#":
                    grid[i][col] = "<"
                else:
                    grid[i + 1][col] = "v"
            else:
                bounds = False

        # Handle ">" (moving right)
        elif ">" in row:
            col = row.index(">")
            grid[i][col] = "X"
            if col + 1 < len(grid[i]):
                if grid[i][col + 1] == "#":
                    grid[i][col] = "v"
                else:
                    grid[i][col + 1] = ">"
            else:
                bounds = False

        # Handle "<" (moving right)
        elif "<" in row:
            col = row.index("<")
            grid[i][col] = "X"
            if col - 1 < len(grid[i]):
                if grid[i][col - 1] == "#":
                    grid[i][col] = "^"
                else:
                    grid[i][col - 1] = "<"
            else:
                bounds = False

    return bounds


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    grid = [list(x) for x in data]
    continue_move = True
    while continue_move:
        continue_move = move_in_grid(grid)
        # display_grid(grid)

    positions = sum([row.count("X") for row in grid if "X" in row])

    return positions


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""
    # TODO: Implement the solution for Part 2
    return len(data)


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
