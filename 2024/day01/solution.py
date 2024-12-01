from collections import Counter
from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    locations_id = [x.split("   ") for x in data]
    locations_one = [int(x[0]) for x in locations_id]
    locations_two = [int(x[1]) for x in locations_id]
    locations_one.sort()
    locations_two.sort()

    total_distance = 0
    for i in range(len(locations_one)):
        loc = abs(locations_one[i] - locations_two[i])
        total_distance += loc

    return total_distance


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""
    locations_id = [x.split("   ") for x in data]
    locations_one = [int(x[0]) for x in locations_id]
    locations_two = [int(x[1]) for x in locations_id]
    loc_counts = Counter(locations_two)

    total = 0
    for loc in locations_one:
        sim_score = loc * loc_counts[loc]
        total += sim_score

    return total


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
