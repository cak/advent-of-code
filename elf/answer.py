import csv
import os
import re
from datetime import datetime
from pathlib import Path

import requests

from elf.config import get_cache_guess_file, get_session_token
from elf.exceptions import SubmissionError
from elf.messages import (
    get_already_completed_message,
    get_answer_too_high_message,
    get_answer_too_low_message,
    get_cached_duplicate_message,
    get_cached_high_message,
    get_cached_low_message,
    get_correct_answer_message,
    get_incorrect_answer_message,
    get_recent_submission_message,
    get_unexpected_response_message,
)
from elf.models import CachedGuessCheck, Guess, SubmissionResult, SubmissionStatus

# 🎄 Elf Answer Submission 🎄 #


def submit_answer(
    year: int, day: int, level: int, answer: int, session_token: str | None = None
) -> SubmissionResult:
    """
    Submit an answer for a specific year, day, and level (part) to Advent of Code.

    🎁 Let the elves deliver your answer to Santa's server! 🎅

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the challenge (1–25).
        level (int): The level of the challenge (1 for Part 1, 2 for Part 2).
        answer (int): Your answer to submit.
        session_token (Optional[str]): Your session token. If not provided,
            it will be retrieved from the environment variable 'AOC_SESSION_COOKIE'.

    Returns:
        SubmissionResult: An object containing the result, message, guess, status, and cache info.

    Raises:
        SubmissionError: If there is an issue submitting the answer.
    """
    cache_file: Path = get_cache_guess_file(year, day)

    # Ensure the cache directory exists
    cache_file.parent.mkdir(parents=True, exist_ok=True)

    if cache_file.exists():
        cached_guess = check_cached_guesses(year, day, level, answer)
        if cached_guess.status != SubmissionStatus.UNKNOWN:
            return SubmissionResult(
                guess=answer,
                result=cached_guess.status,
                message=cached_guess.message,
                is_correct=(cached_guess.status == SubmissionStatus.CORRECT),
                is_cached=True,  # Indicate the result is from cache
            )

    return submit_to_aoc(year, day, level, answer, session_token)


def submit_to_aoc(
    year: int, day: int, level: int, answer: int, session_token: str | None = None
) -> SubmissionResult:
    """
    Submit an answer for a specific year, day, and level (part) to Advent of Code.

    🎁 Let the elves deliver your answer to Santa's server! 🎅

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the challenge (1–25).
        level (int): The level of the challenge (1 for Part 1, 2 for Part 2).
        answer (int): Your answer to submit.
        session_token (Optional[str]): Your session token. If not provided,
            it will be retrieved from the environment variable 'AOC_SESSION_COOKIE'.

    Returns:
        SubmissionResult: An object containing the result, message, guess, status, and cache info.

    Raises:
        SubmissionError: If there is an issue submitting the answer.
    """
    session_token = get_session_token(session_token)

    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    headers = {
        "Cookie": f"session={session_token}",
        "User-Agent": "elf-package/1.0 (+https://github.com/cak/elf)",
    }
    data = {"level": str(level), "answer": str(answer)}

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()

        # Use regex to extract content inside <article> tags
        match = re.search(r"<article[^>]*>(.*?)</article>", response.text, re.DOTALL)
        if match:
            message_content = match.group(1).strip()

            # Match the message to known responses
            if "That's the right answer" in message_content:
                message = get_correct_answer_message(answer=answer)
                status = SubmissionStatus.CORRECT
            elif "too high" in message_content:
                message = get_answer_too_high_message(answer=answer)
                status = SubmissionStatus.TOO_HIGH
            elif "too low" in message_content:
                message = get_answer_too_low_message(answer=answer)
                status = SubmissionStatus.TOO_LOW
            elif "You gave an answer too recently" in message_content:
                message = get_recent_submission_message()
                status = SubmissionStatus.WAIT
            elif "Did you already complete it" in message_content:
                message = get_already_completed_message()
                status = SubmissionStatus.COMPLETED
            elif "That's not the right answer" in message_content:
                message = get_incorrect_answer_message(answer=answer)
                status = SubmissionStatus.INCORRECT
            else:
                message = get_unexpected_response_message()
                status = SubmissionStatus.UNKNOWN
        else:
            message = (
                "🎄 Answer submitted, but no response message was found. "
                "Check your submission on the Advent of Code website."
            )
            status = SubmissionStatus.UNKNOWN

        # Write the guess to cache with the status, except for 'wait' and 'completed'
        if status not in (SubmissionStatus.WAIT, SubmissionStatus.COMPLETED):
            write_guess_cache(year, day, level, answer, status)

        return SubmissionResult(
            guess=answer,
            result=status,
            message=message,
            is_correct=(status == SubmissionStatus.CORRECT),
            is_cached=False,
        )

    except requests.exceptions.RequestException as e:
        raise SubmissionError(
            f"🛑 Uh-oh! An error occurred while submitting your answer: {e} 🎁"
        ) from e


def write_guess_cache(
    year: int, day: int, part: int, guess: int, status: SubmissionStatus
) -> None:
    """Write the user's guess to the cache file."""
    cache_file = get_cache_guess_file(year, day)

    # Get the current timestamp in ISO 8601 format
    timestamp = datetime.now().isoformat()

    # Define the header
    fieldnames = ["timestamp", "part", "guess", "status"]

    try:
        # Open the CSV file in append mode
        with open(cache_file, "a", newline="") as csvfile:
            # Create a DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # If the file is empty, write the header
            csvfile.seek(0, os.SEEK_END)
            if csvfile.tell() == 0:
                writer.writeheader()

            # Write the guess data as a new row
            writer.writerow(
                {
                    "timestamp": timestamp,
                    "part": part,
                    "guess": str(guess),
                    "status": status.name,
                }
            )
    except Exception as e:
        print(f"An error occurred while writing to {cache_file}: {e}")


def read_guesses(year: int, day: int) -> list[Guess]:
    cache_file: Path = get_cache_guess_file(year, day)
    guesses = []

    # Check if the file exists
    if not cache_file.exists():
        print(f"{cache_file} does not exist. Returning an empty list.")
        return guesses

    # Open and read the file if it exists
    with open(cache_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create a Guess object for each row
            status = SubmissionStatus[row["status"]]
            guess = Guess(
                timestamp=datetime.fromisoformat(row["timestamp"]),
                part=int(row["part"]),
                guess=int(row["guess"]),
                status=status,
            )
            guesses.append(guess)

    return guesses


def check_cached_guesses(
    year: int, day: int, level: int, answer: int
) -> CachedGuessCheck:
    """Check the cache for previous guesses and return a CachedGuessCheck instance."""
    guesses = read_guesses(year, day)
    answer = int(answer)

    highest_low_guess: Guess | None = None  # Highest 'too low' guess for this level
    lowest_high_guess: Guess | None = None  # Lowest 'too high' guess for this level

    # Loop through previous guesses to find bounds
    for guess in guesses:
        if guess.part != level:
            continue

        # If there's an exact match
        if guess.guess == answer:
            return CachedGuessCheck(
                guess=answer,
                previous_guess=guess.guess,
                previous_timestamp=guess.timestamp,
                status=guess.status,
                message=get_cached_duplicate_message(
                    answer=answer, previous_guess=guess
                ),
            )

        # Track bounds based on previous 'too low' and 'too high' guesses
        if guess.status == SubmissionStatus.TOO_LOW and guess.guess < answer:
            if highest_low_guess is None or guess.guess > highest_low_guess.guess:
                highest_low_guess = guess
        elif guess.status == SubmissionStatus.TOO_HIGH and guess.guess > answer:
            if lowest_high_guess is None or guess.guess < lowest_high_guess.guess:
                lowest_high_guess = guess

    # Check if the new guess is inferably too low or too high based on bounds
    if highest_low_guess and answer <= highest_low_guess.guess:
        return CachedGuessCheck(
            guess=answer,
            previous_guess=highest_low_guess.guess,
            previous_timestamp=highest_low_guess.timestamp,
            status=SubmissionStatus.TOO_LOW,
            message=get_cached_low_message(
                answer=answer, highest_low_guess=highest_low_guess
            ),
        )
    elif lowest_high_guess and answer >= lowest_high_guess.guess:
        return CachedGuessCheck(
            guess=answer,
            previous_guess=lowest_high_guess.guess,
            previous_timestamp=lowest_high_guess.timestamp,
            status=SubmissionStatus.TOO_HIGH,
            message=get_cached_high_message(
                answer=answer, lowest_high_guess=lowest_high_guess
            ),
        )

    # If no match and no clear bounds, it's an unknown (unique) guess
    return CachedGuessCheck(
        guess=answer,
        previous_guess=None,
        previous_timestamp=None,
        status=SubmissionStatus.UNKNOWN,
        message="This is a unique guess.",
    )
