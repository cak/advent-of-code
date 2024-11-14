import importlib
from pathlib import Path

import elf


def main(year: int, day: int):
    day_dir = Path(f"{year}/day{day:02d}")
    test_input_file = day_dir / "test_input.txt"
    expected_output_file = day_dir / "expected_output.txt"

    if not test_input_file.exists() or not expected_output_file.exists():
        print("❌ Test files are missing.")
        return

    # Import the solution module using importlib.import_module
    module_name = f"{year}.day{day:02d}.day{day:02d}"
    try:
        module = importlib.import_module(module_name)
        part1_func = getattr(module, "part1", None)
        part2_func = getattr(module, "part2", None)
    except ModuleNotFoundError as e:
        print(f"❌ Solution module not found: {e}")
        return

    if not part1_func or not part2_func:
        print("❌ Solution functions part1 or part2 not found.")
        return

    # Read test input and expected output
    test_input = test_input_file.read_text().strip()
    expected_output = expected_output_file.read_text().strip()

    # Run tests using the run_tests function from elf.testing
    elf.testing.run_tests(part1_func, part2_func, day_dir, test_input, expected_output)
