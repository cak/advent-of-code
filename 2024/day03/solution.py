import re
from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    memory = "".join(data)
    pattern = r"mul\(\d+,\s*\d+\)"
    matches = re.findall(pattern, memory)

    answer = 0
    for match in matches:
        a, b = map(int, re.findall(r"\d+", match))
        answer += a * b

    return answer


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""
    memory = "".join(data)
    mul_pattern = r"mul\(\d+,\s*\d+\)"
    do_pattern = r"do\(\)"
    do_not_pattern = r"don\'t\(\)"
    matches = re.findall(f"{mul_pattern}|{do_pattern}|{do_not_pattern}", memory)
    answer = 0
    enabled = True

    for match in matches:
        if "do()" in match:
            enabled = True
        elif "don't()" in match:
            enabled = False
        else:
            if enabled:
                a, b = map(int, re.findall(r"\d+", match))
                answer += a * b

    return answer


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
