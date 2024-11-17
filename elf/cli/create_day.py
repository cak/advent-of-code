import os
import shutil
from datetime import datetime
from pathlib import Path

import elf

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = Path(os.getenv("ELF_TEMPLATE_DIR", BASE_DIR / "templates"))
template_file = Path(
    os.getenv("ELF_TEMPLATE_FILE", TEMPLATE_DIR / "solution_template.py")
)


def create_directory(path: Path) -> None:
    """Create a directory if it doesn't already exist."""
    try:
        path.mkdir(parents=True, exist_ok=False)
        print(f"✨ Created directory at {path}. 🎄")
    except FileExistsError:
        print(f"🎁 Directory already exists at {path}. Time to open the presents!")


def copy_template(template_path: Path, destination_path: Path) -> None:
    """Copy the solution template to the new day's folder."""
    if template_path.exists():
        shutil.copy(template_path, destination_path)
        print(f"🎅 Solution template copied to {destination_path}.")
    else:
        raise FileNotFoundError(f"⛄ Template not found at {template_path}!")


def format_day_number(day: int) -> str:
    """Format the day number as a two-digit string."""
    return f"{day:02d}"


def create_test_files(day_dir: Path) -> None:
    """Create test_input.txt and expected_output.txt with default content."""
    test_input_file = day_dir / "test_input.txt"
    expected_output_file = day_dir / "expected_output.txt"

    if not test_input_file.exists():
        test_input_file.write_text("# Add your test input data here\n")
        print("📝 Created test_input.txt with default content.")

    if not expected_output_file.exists():
        expected_output_file.write_text(
            "# Add your expected output here (Part 1 and Part 2 on separate lines)\n"
        )
        print("📝 Created expected_output.txt with default content.")


def fetch_input_file(year: int, day: int, input_file: Path) -> None:
    """Fetch the puzzle input and save it to input.txt."""
    if not input_file.exists():
        try:
            print(f"📡 Fetching input for Year {year}, Day {day}...")
            input_text = elf.get_input(year, day)
            input_file.write_text(input_text)
            print(
                f"🎉 Input for Day {format_day_number(day)} fetched and saved to input.txt! The elves are dancing! 🕺"
            )
        except elf.InputFetchError as e:
            print(f"🎅❌ Oh no! The elves couldn't fetch the input: {e}")
            print(
                "🚨 Please ensure your session cookie is set correctly to help the elves."
            )
        except Exception as e:
            print(f"🎄❌ An unexpected error occurred: {e}")
    else:
        print("🎁 input.txt already exists. The gift has already been unwrapped! 🎁")


def create_new_day(year: int, day: int, output_dir: str) -> None:
    """Create the folder structure and solution file for the given year and day."""
    # Resolve the output path, defaulting to the current working directory
    output_path = Path(output_dir).resolve() if output_dir else Path.cwd()
    day_str = f"{day:02d}"

    # Paths
    year_dir = output_path / str(year)
    day_dir = year_dir / f"day{day_str}"
    new_solution_file = day_dir / "solution.py"
    input_file = day_dir / "input.txt"

    current_year = datetime.now().year
    # Validate year and day
    if not (2015 <= year <= current_year):
        raise ValueError(
            f"Invalid year: {year}. Year must be between 2015 and {current_year}."
        )
    if not (1 <= day <= 25):
        raise ValueError(f"Invalid day: {day}. Day must be between 1 and 25.")

    # Check if the template file exists
    if not template_file.exists():
        raise FileNotFoundError(f"Template file not found at {template_file}")

    # Create directories if they don't exist
    create_directory(year_dir)
    create_directory(day_dir)

    # Fetch input.txt
    fetch_input_file(year, day, input_file)

    # Copy the solution template
    copy_template(template_file, new_solution_file)

    # Create test_input.txt and expected_output.txt
    create_test_files(day_dir)

    print(f"🎄 Day {day_str} in {year} is ready! Time to code by the fireplace. 🔥")


def main(year: int, day: int, output_dir: str = "") -> None:
    output_dir = output_dir or str(Path.cwd())  # Default to current working directory
    print(f"🎄 Creating day structure for {year}, Day {day} in {output_dir}...")
    create_new_day(year, day, output_dir)
