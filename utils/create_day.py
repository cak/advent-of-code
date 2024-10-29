import argparse
import shutil
import sys
from pathlib import Path

# 🎄 Define the base directory (one level up from the script location) 🎄
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the project root to sys.path if not installing elf as a package
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

import elf  # Import elf after modifying sys.path  # noqa: E402

# 🎄 Cozy Christmas Utility Functions 🎄 #


def create_directory(path: Path) -> None:
    """
    Create a directory if it doesn't already exist.

    🎁 Let's create a warm and cozy place for our code to live! 🎁

    Args:
        path (Path): The directory path to create.
    """
    try:
        path.mkdir(parents=True, exist_ok=False)
        print(
            f"✨ Created directory at {path}. It's like decorating a fresh Christmas tree! 🎄"
        )
    except FileExistsError:
        print(
            f"🎄 Directory already exists at {path}. Time to open the presents inside! 🎁"
        )


def copy_template(template_path: Path, destination_path: Path) -> None:
    """
    Copy the solution template to the new day's folder.

    🎁 This will be our coding gift for the day! 🎁

    Args:
        template_path (Path): The path to the template file.
        destination_path (Path): The destination path for the copied template.
    """
    if template_path.exists():
        shutil.copy(template_path, destination_path)
        print(
            f"🎅 Solution template copied to {destination_path}. Let the coding magic begin! ✨"
        )
    else:
        print("⛄ Template not found! The elves must have hidden it! 🔎")


def format_day_number(day: int) -> str:
    """
    Format the day number as a two-digit string.

    🎅 Make sure our day is festive and formatted! 🎅

    Args:
        day (int): The day number.

    Returns:
        str: The formatted day string.
    """
    return f"{day:02d}"


# 🎄 Let's Create a New Day of Advent Code Magic! 🎄 #


def create_new_day(year: int, day: int) -> None:
    """
    Create the folder structure and solution file for the given year and day.

    🎅 Setting up your coding winter wonderland! 🎅

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
    """
    day_str = format_day_number(day)

    # Paths
    year_dir = BASE_DIR / str(year)
    day_dir = year_dir / f"day{day_str}"
    template_file = BASE_DIR / "templates" / "solution_template.py"
    new_solution_file = day_dir / f"day{day_str}.py"

    # Validate year and day
    if not (1000 <= year <= 9999):
        raise ValueError(f"Invalid year: {year}. Year must be a 4-digit number.")
    if not (1 <= day <= 25):
        raise ValueError(f"Invalid day: {day}. Day must be between 1 and 25.")

    # Check if the template file exists
    if not template_file.exists():
        raise FileNotFoundError(f"Template file not found at {template_file}")

    # Create directories if they don't exist
    create_directory(year_dir)
    create_directory(day_dir)

    # Create input.txt and fetch the puzzle input
    input_file = day_dir / "input.txt"
    if not input_file.exists():
        try:
            print(f"📡 Fetching input for Year {year}, Day {day}...")
            input_text = elf.get_input(year, day)
            input_file.write_text(input_text)
            print(
                f"🎉 Input for Day {day_str} fetched and saved to input.txt! The elves are dancing! 🕺"
            )
        except elf.InputFetchError as e:
            print(f"🎅❌ Oh no! The elves couldn't fetch the input: {e}")
            print(
                "🚨 Please ensure your session cookie is set correctly to help the elves."
            )
        except Exception as e:
            print(f"🎄❌ An unexpected error occurred: {e}")
    else:
        print(
            f"🎁 input.txt already exists in {day_dir}. The gift has already been unwrapped! 🎁"
        )

    # Copy the solution template (our daily gift to you!)
    copy_template(template_file, new_solution_file)

    print(f"🎄 Day {day_str} in {year} is ready! Time to code by the fireplace. 🔥")


# 🎁 Main Script to Create the Year and Day Structure 🎁 #
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create Advent of Code day folder and files.",
        epilog="🎄 Happy Coding! 🎄",
    )
    parser.add_argument("year", type=int, help="Year (e.g., 2022)")
    parser.add_argument("day", type=int, help="Day number (1-25)")

    args = parser.parse_args()

    try:
        print(
            f"✨ Preparing Advent of Code {args.year}, Day {args.day}. Let's make some coding magic! 🎄"
        )
        create_new_day(args.year, args.day)
    except (ValueError, FileNotFoundError) as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
