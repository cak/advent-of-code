import hashlib
from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    # TODO: Implement the solution for Part 1

    door_id = data[0]

    password = ""

    hash_index = 0

    while len(password) < 8:
        door_id_hash = hashlib.md5(f"{door_id}{hash_index}".encode()).hexdigest()
        if door_id_hash.startswith("00000"):
            password += door_id_hash[5]
        hash_index += 1

    return password


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""
    # TODO: Implement the solution for Part 2
    return len(data)


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
