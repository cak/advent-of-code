from itertools import product
from pathlib import Path

import elf
from elf.templates.args import args

# 🎄 Welcome to Advent of Code! 🎄
# Let's solve today's challenge with a festive coding spirit! 🎅


def evaluate_expression(numbers: list[int], operators: list[str]) -> int:
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            result += numbers[i + 1]
        elif operator == "*":
            result *= numbers[i + 1]
    return result


def validate_calibrations(test_value: int, *args: int) -> bool:
    operators = product(["+", "*"], repeat=len(args) - 1)
    for operator in operators:
        if evaluate_expression(list(args), list(operator)) == test_value:
            return True
    return False


@elf.timer()
def part1(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    calibrations = [
        (int(y[0]), [int(z) for z in y[1].split()])
        for x in data
        for y in [x.split(":")]
    ]

    valid_calibrations = [
        x[0] for x in calibrations if validate_calibrations(x[0], *x[1])
    ]

    return sum(valid_calibrations)


def evaluate_expression_part_two(numbers: list[int], operators: list[str]) -> int:
    result = numbers[0]

    i = 0
    while i < len(operators):
        next_num = numbers[i + 1]
        operator = operators[i]
        if operator == "+":
            result += next_num
        elif operator == "*":
            result *= next_num
        elif operator == "||":
            result = int(f"{result}{next_num}")
        i += 1
    return result


def validate_calibrations_part_two(test_value: int, *args: int) -> bool:
    operators = product(["+", "*", "||"], repeat=len(args) - 1)
    for operator in operators:
        if evaluate_expression_part_two(list(args), list(operator)) == test_value:
            return True
    return False


@elf.timer()
def part2(data: list[str]) -> int | str:
    """🎅 Solve Part 1 of the puzzle 🎅"""
    calibrations = [
        (int(y[0]), [int(z) for z in y[1].split()])
        for x in data
        for y in [x.split(":")]
    ]

    valid_calibrations = [
        x[0] for x in calibrations if validate_calibrations_part_two(x[0], *x[1])
    ]

    return sum(valid_calibrations)


if __name__ == "__main__":
    base_dir = Path(__file__).parent

    # Run the arguments handler to test, fetch input, and/or submit answers
    args(part1=part1, part2=part2, base_dir=base_dir)
