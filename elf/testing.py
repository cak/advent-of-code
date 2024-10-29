from pathlib import Path
from typing import Any, Callable

from elf.input import parse_input, read_input_file
from elf.messages import get_negative_message, get_positive_message

# 🎄 Elf Testing Laboratory 🎄 #


def read_expected_output(expected_output: str | Path) -> list[str]:
    """Reads or parses the expected output for Part 1 and Part 2.

    🎁 Reading the expected outcomes! ✨

    Args:
        expected_output (str | Path): The expected output as a direct string or file path.

    Returns:
        list[str]: A list containing the expected outputs for part 1 and part 2.
    """
    if isinstance(expected_output, Path) or Path(expected_output).exists():
        filepath = Path(expected_output)
        if not filepath.exists():
            print(
                f"🎁 Warning: {filepath} not found. The elves must have missed this one! 🎅"
            )
            return ["", ""]
        output_data = filepath.read_text().strip()
    else:
        output_data = expected_output

    # Ensure the list has at least two elements
    output_lines = output_data.strip().splitlines()
    while len(output_lines) < 2:
        output_lines.append("")
    return output_lines


def check_part1_solution(
    part1_func: Callable[[list[str]], Any],
    test_input: str | Path,
    expected_output: str | Path,
) -> None:
    """Checks the test input against the expected output for Part 1.

    🎄 Time to test your Part 1 solution with elf magic! 🎅

    Args:
        part1_func (Callable[[list[str]], Any]): The function solving part 1.
        test_input (str | Path): The test input as a direct string or file path.
        expected_output (str | Path): The expected output as a direct string or file path.
    """
    test_data = (
        parse_input(test_input)
        if isinstance(test_input, str)
        else read_input_file(test_input)
    )
    expected_output_lines = read_expected_output(expected_output)

    if expected_output_lines[0]:
        result = part1_func(test_data)
        if str(result) == expected_output_lines[0]:
            print(f"🎅 Part 1 test passed! {get_positive_message()}")
        else:
            print(
                f"🎄 Part 1 failed: Expected {expected_output_lines[0]}, got {result}. {get_negative_message()}"
            )
    else:
        print("🎄 Part 1 expected output is missing. Please check the expected output.")


def check_part2_solution(
    part2_func: Callable[[list[str]], Any],
    test_input: str | Path,
    expected_output: str | Path,
) -> None:
    """Checks the test input against the expected output for Part 2.

    🎄 Time to test your Part 2 solution with elf magic! 🎅

    Args:
        part2_func (Callable[[list[str]], Any]): The function solving part 2.
        test_input (str | Path): The test input as a direct string or file path.
        expected_output (str | Path): The expected output as a direct string or file path.
    """
    test_data = (
        parse_input(test_input)
        if isinstance(test_input, str)
        else read_input_file(test_input)
    )
    expected_output_lines = read_expected_output(expected_output)

    if len(expected_output_lines) > 1 and expected_output_lines[1]:
        result = part2_func(test_data)
        if str(result) == expected_output_lines[1]:
            print(f"🎅 Part 2 test passed! {get_positive_message()}")
        else:
            print(
                f"🎄 Part 2 failed: Expected {expected_output_lines[1]}, got {result}. {get_negative_message()}"
            )
    else:
        print("🎄 Part 2 expected output is missing or empty. Skipping Part 2 test.")
