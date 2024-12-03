import argparse
import sys
from collections.abc import Callable
from pathlib import Path

import elf
from elf.models import TestResult
from elf.utils import read_expected_output, read_test_input


# 🎅 Festive Argument Handling for Advent of Code 🎅 #
def args(
    part1: Callable[[list[str]], int | str],
    part2: Callable[[list[str]], int | str],
    base_dir: Path,
) -> None:
    """
    Handles command-line arguments for Advent of Code solutions.

    Parameters:
        part1 (Callable[[list[str]], int | str]): Function to solve Part 1 of the puzzle.
        part2 (Callable[[list[str]], int | str]): Function to solve Part 2 of the puzzle.
        base_dir (Path): Path to the directory containing puzzle input and output files.
    """
    parser = argparse.ArgumentParser(
        description="Advent of Code Solution Runner",
        epilog="🎄 Happy Coding! 🎄",
    )
    parser.add_argument(
        "--part",
        choices=["1", "2", "both"],
        default="both",
        help="Specify which part to run.",
    )
    parser.add_argument(
        "--submit",
        action="store_true",
        help="Submit the answer to Advent of Code (requires session token).",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run tests using test_input.txt and expected_output.txt. 🎁",
    )
    args = parser.parse_args()

    # Extract day and year from the directory structure
    day = int(base_dir.name.strip("day"))
    year = int(base_dir.parent.name)

    # Define file path for input
    input_file = base_dir / "input.txt"

    # Run tests if --test is specified
    if args.test:
        print("🔍 Running tests... Let's see if the elves approve!")

        try:
            test_input = read_test_input(base_dir)
            expected_output = read_expected_output(base_dir)

            if args.part in ("1", "both"):
                part1_result: TestResult = elf.check_part1_solution(
                    part1_func=part1,
                    test_input=test_input,
                    expected_output=expected_output,
                )
                print(part1_result.message)
                if not part1_result.passed:
                    print("❌ Part 1 Test Failed.")
                    sys.exit(1)

            if args.part in ("2", "both"):
                part2_result: TestResult = elf.check_part2_solution(
                    part2_func=part2,
                    test_input=test_input,
                    expected_output=expected_output,
                )
                print(part2_result.message)
                if not part2_result.passed:
                    print("❌ Part 2 Test Failed.")
                    sys.exit(1)

            print("✅ All tests completed. The elves are dancing with joy! 🎉")

        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

    else:
        # Read or fetch input data
        if input_file.exists():
            data = elf.read_input_file(input_file)
            print("🎁 Input data found and ready for use!")
        else:
            # Try to fetch the input
            print("📥 Input file not found. The elves are fetching it for you...")
            try:
                input_text = elf.get_input(year, day)
                input_file.write_text(input_text)
                data = elf.parse_input(input_text)
                print("✅ Input fetched, saved, and ready to use!")
            except elf.InputFetchError as e:
                print(f"❌ Failed to fetch input: {e}")
                data = []
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")
                data = []

        if data:
            # Run the specified parts
            if args.part in ("1", "both"):
                result_part1 = part1(data)
                print(f"🎄 Part 1 Result: {result_part1}")
                if args.submit:
                    try:
                        print("📤 Submitting Part 1 answer to Santa’s server...")
                        submission_result = elf.submit_answer(
                            year, day, 1, result_part1
                        )
                        print(submission_result.message)
                    except elf.SubmissionError as e:
                        print(f"❌ Submission failed: {e}")

            if args.part in ("2", "both"):
                result_part2 = part2(data)
                print(f"🎄 Part 2 Result: {result_part2}")
                if args.submit:
                    try:
                        print("📤 Submitting Part 2 answer to Santa’s server...")
                        submission_result = elf.submit_answer(
                            year, day, 2, result_part2
                        )
                        print(submission_result.message)
                    except elf.SubmissionError as e:
                        print(f"❌ Submission failed: {e}")
        else:
            print("🛑 No input data available. Please check the setup and try again.")
