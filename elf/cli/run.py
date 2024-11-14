import importlib.util


def main(year: int, day: int, part: str):
    day_dir = Path(f"{year}/day{day:02d}")
    solution_file = day_dir / f"day{day:02d}.py"
    if not solution_file.exists():
        print(f"❌ Solution file not found: {solution_file}")
        return

    spec = importlib.util.spec_from_file_location("solution", solution_file)
    solution = importlib.util.module_from_spec(spec)
    sys.modules["solution"] = solution
    spec.loader.exec_module(solution)

    # Now you can call functions from the solution module
    # For example:
    if part in ("1", "both"):
        result_part1 = solution.part1()
        print(f"Part 1 result: {result_part1}")
    if part in ("2", "both"):
        result_part2 = solution.part2()
        print(f"Part 2 result: {result_part2}")
