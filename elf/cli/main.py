import argparse
import sys

from elf.cli import create_day, fetch_input, run, submit, test


def main():
    parser = argparse.ArgumentParser(
        description="Elf CLI - A Festive Helper for Advent of Code 🎄",
        epilog="🎅 Happy Coding and Merry Christmas! 🎅",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: create-day
    create_day_parser = subparsers.add_parser(
        "create-day", help="Create a new day folder with solution template."
    )
    create_day_parser.add_argument("year", type=int, help="Year (e.g., 2024)")
    create_day_parser.add_argument("day", type=int, help="Day number (1-25)")

    # Subcommand: fetch-input
    fetch_input_parser = subparsers.add_parser(
        "fetch-input", help="Fetch the input data for a specific day."
    )
    fetch_input_parser.add_argument("year", type=int, help="Year (e.g., 2024)")
    fetch_input_parser.add_argument("day", type=int, help="Day number (1-25)")

    # Subcommand: run
    run_parser = subparsers.add_parser(
        "run", help="Run the solution for a specific day and part."
    )
    run_parser.add_argument("year", type=int, help="Year (e.g., 2024)")
    run_parser.add_argument("day", type=int, help="Day number (1-25)")
    run_parser.add_argument(
        "--part",
        choices=["1", "2", "both"],
        default="both",
        help="Specify which part to run.",
    )

    # Subcommand: submit
    submit_parser = subparsers.add_parser(
        "submit", help="Submit your answer to Advent of Code."
    )
    submit_parser.add_argument("year", type=int, help="Year (e.g., 2024)")
    submit_parser.add_argument("day", type=int, help="Day number (1-25)")
    submit_parser.add_argument(
        "part", choices=["1", "2"], help="Part of the challenge (1 or 2)"
    )
    submit_parser.add_argument("answer", help="Your answer to submit")

    # Subcommand: test
    test_parser = subparsers.add_parser("test", help="Run tests for a specific day.")
    test_parser.add_argument("year", type=int, help="Year (e.g., 2024)")
    test_parser.add_argument("day", type=int, help="Day number (1-25)")

    args = parser.parse_args()

    # Dispatch to the appropriate subcommand handler
    if args.command == "create-day":
        create_day.main(args.year, args.day)
    elif args.command == "fetch-input":
        fetch_input.main(args.year, args.day)
    elif args.command == "run":
        run.main(args.year, args.day, args.part)
    elif args.command == "submit":
        submit.main(args.year, args.day, args.part, args.answer)
    elif args.command == "test":
        test.main(args.year, args.day)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
