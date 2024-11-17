import string
from collections import Counter
from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""

    answer = 0
    for line in data:
        room = line.split("[")[0]
        check_sum = line.split("[")[1].split("]")[0]
        sector_id = int(room.split("-")[-1])

        letter_counts = Counter(
            char for char in room if char.isalpha() and char.islower()
        )
        sorted_letter_counts = sorted(
            letter_counts.items(), key=lambda item: (-item[1], item[0])
        )

        if len(sorted_letter_counts) < len(check_sum):
            print("not enough letters", sorted_letter_counts)
            continue

        to_check = "".join([x[0] for x in (sorted_letter_counts[: len(check_sum)])])

        if to_check == check_sum:
            answer += sector_id

    return answer


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""

    letters = list(string.ascii_lowercase)

    for line in data:
        room = line.split("[")[0]
        # check_sum = line.split("[")[1].split("]")[0]
        sector_id = int(room.split("-")[-1])

        decrypted = ""
        for char in room:
            if char.isalpha() and char.islower():
                index = letters.index(char)
                new_letter = letters[(index + sector_id) % len(letters)]
                decrypted += new_letter
            elif char == "-":
                decrypted += " "

        if "north" in decrypted:
            print(decrypted, sector_id)
            return sector_id

    return 0


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
