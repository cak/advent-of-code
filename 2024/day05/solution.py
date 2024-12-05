from collections import defaultdict
from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""

    rules_parse, updates_parse = (
        [x.split(sep="|") for x in data if "|" in x and x],
        [x.split(sep=",") for x in data if "|" not in x and x],
    )
    rules_int = [map(int, x) for x in rules_parse]

    rules = defaultdict(list)
    for k, v in rules_int:
        rules[k].append(v)

    updates = [list(map(int, x)) for x in updates_parse]

    right_order_updates = []

    for update in updates:
        correct_update = True
        update_copy = update.copy()
        for page in update:
            update_copy.remove(page)
            rule = sorted(rules[page])
            if update_copy:
                if not all(item in rule for item in update_copy):
                    correct_update = False
                    break
        if correct_update is True:
            right_order_updates.append(update)

    middle_numbers_sum = sum([lst[len(lst) // 2] for lst in right_order_updates])

    return middle_numbers_sum


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 2 of the puzzle 🎅"""
    rules_parse, updates_parse = (
        [x.split(sep="|") for x in data if "|" in x and x],
        [x.split(sep=",") for x in data if "|" not in x and x],
    )
    rules_int = [map(int, x) for x in rules_parse]

    rules = defaultdict(list)
    for k, v in rules_int:
        rules[k].append(v)

    updates = [list(map(int, x)) for x in updates_parse]

    wrong_order_updates = []

    correct_order_updates = []
    for update in updates:
        correct_update = True
        update_copy = update.copy()
        for page in update:
            update_copy.remove(page)
            rule = sorted(rules[page])
            if update_copy:
                if not all(item in rule for item in update_copy):
                    correct_update = False
                    break
        if correct_update is False:
            wrong_order_updates.append(update)

    for wrong_update in wrong_order_updates:
        filtered_rules = {
            key: value for key, value in rules.items() if key in wrong_update
        }

        primary_sort = sorted(
            wrong_update,
            key=lambda x: 0
            if any(x in value for value in filtered_rules.values())
            else 1,
        )

        sorted_numbers = sorted(
            primary_sort,
            key=lambda x: (
                next((k for k, v in filtered_rules.items() if x in v), float("inf")),
                x,
            ),
            reverse=True,
        )

        correct_order_updates.append(sorted_numbers)

    middle_numbers_sum = sum([lst[len(lst) // 2] for lst in correct_order_updates])

    return middle_numbers_sum


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
