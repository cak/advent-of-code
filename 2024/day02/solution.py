from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    levels = [[int(y) for y in x.split(" ")] for x in data]
    safe_levels = 0
    for level in levels:
        if level != sorted(level) and level != sorted(level, reverse=True):
            continue
        safe = True
        for i, l in enumerate(level):
            if i + 1 < len(level):
                if l == level[i + 1] or abs(l - level[i + 1]) > 3:
                    safe = False
                    break
        if safe:
            safe_levels += 1
    return safe_levels


def safe_level(level: list[int]) -> bool:
    if level != sorted(level) and level != sorted(level, reverse=True):
        return False
    for index, current_level in enumerate(level):
        if index + 1 < len(level):
            if (
                current_level == level[index + 1]
                or abs(current_level - level[index + 1]) > 3
            ):
                return False
    return True


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""
    levels = [[int(y) for y in x.split(" ")] for x in data]
    safe_levels = 0
    for level in levels:
        for index, _ in enumerate(levels):
            level_check = [value for i, value in enumerate(level) if i != index]
            if safe_level(level_check):
                safe_levels += 1
                break

    return safe_levels


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
