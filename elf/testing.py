from collections.abc import Callable
from pathlib import Path
from typing import Any

from elf.input import parse_input, read_input_file
from elf.messages import get_negative_message, get_positive_message
from elf.models import TestResult  # Import the TestResult dataclass

# 🎄 Elf Testing Laboratory 🎄 #


def read_expected_output(expected_output: str | Path) -> list[str]:
    """Reads or parses the expected output for Part 1 and Part 2."""
    filepath = Path(expected_output)

    if filepath.is_file():
        output_data = filepath.read_text().strip()
    else:
        output_data = str(expected_output).strip()

    output_lines = output_data.splitlines()
    return output_lines + [""] * (2 - len(output_lines))


def check_part1_solution(
    part1_func: Callable[[list[str]], Any],
    test_input: str | Path,
    expected_output: str | Path,
) -> TestResult:
    """Checks the test input against the expected output for Part 1."""
    test_data = (
        parse_input(test_input)
        if isinstance(test_input, str)
        else read_input_file(test_input)
    )
    expected_output_lines = read_expected_output(expected_output)

    if not expected_output_lines[0]:
        message = (
            "🎄 Part 1 expected output is missing. Please check the expected output."
        )
        return TestResult(part=1, passed=False, expected="", actual="", message=message)

    result = part1_func(test_data)
    actual_result = str(result)
    expected_result = expected_output_lines[0]

    if actual_result == expected_result:
        message = f"🎅 Part 1 test passed! {get_positive_message(answer=result)}"
        passed = True
    else:
        message = (
            f"🎄 Part 1 failed: Expected {expected_result}, got {actual_result}. "
            f"{get_negative_message(answer=result)}"
        )
        passed = False

    return TestResult(
        part=1,
        passed=passed,
        expected=expected_result,
        actual=actual_result,
        message=message,
    )


def check_part2_solution(
    part2_func: Callable[[list[str]], Any],
    test_input: str | Path,
    expected_output: str | Path,
) -> TestResult:
    """Checks the test input against the expected output for Part 2."""
    test_data = (
        parse_input(test_input)
        if isinstance(test_input, str)
        else read_input_file(test_input)
    )
    expected_output_lines = read_expected_output(expected_output)

    if len(expected_output_lines) < 2 or not expected_output_lines[1]:
        message = "🎄 Part 2 expected output is missing or empty. Skipping Part 2 test."
        return TestResult(part=2, passed=False, expected="", actual="", message=message)

    result = part2_func(test_data)
    actual_result = str(result)
    expected_result = expected_output_lines[1]

    if actual_result == expected_result:
        message = f"🎅 Part 2 test passed! {get_positive_message(answer=result)}"
        passed = True
    else:
        message = (
            f"🎄 Part 2 failed: Expected {expected_result}, got {actual_result}. "
            f"{get_negative_message(answer=result)}"
        )
        passed = False

    return TestResult(
        part=2,
        passed=passed,
        expected=expected_result,
        actual=actual_result,
        message=message,
    )


def run_tests(
    part1_func, part2_func, base_dir: Path, test_input: str, expected_output: str
) -> None:
    # Use test_input and expected_output in your test cases
    part1_result = part1_func(test_input.splitlines())
    part2_result = part2_func(test_input.splitlines())

    expected_output_lines = expected_output.splitlines()
    expected_part1 = expected_output_lines[0] if len(expected_output_lines) > 0 else ""
    expected_part2 = expected_output_lines[1] if len(expected_output_lines) > 1 else ""

    if str(part1_result) == expected_part1:
        print("✅ Part 1 test passed!")
    else:
        print(f"❌ Part 1 test failed: Expected {expected_part1}, got {part1_result}")

    if str(part2_result) == expected_part2:
        print("✅ Part 2 test passed!")
    else:
        print(f"❌ Part 2 test failed: Expected {expected_part2}, got {part2_result}")
