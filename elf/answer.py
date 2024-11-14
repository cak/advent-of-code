import csv
import logging
from datetime import datetime
from enum import Enum, auto
from html.parser import HTMLParser
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
from elf.models import (
    CachedGuessCheck,
    Guess,
    SubmissionResult,
    SubmissionStatus,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🎄 Elf Answer Submission 🎄 #


def submit_answer(
    year: int, day: int, level: int, answer: int | str, session_token: str | None = None
) -> SubmissionResult:
    """
    Submit an answer for a specific year, day, and level (part) to Advent of Code.

    🎁 Let the elves deliver your answer to Santa's server! 🎅

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the challenge (1–25).
        level (int): The level of the challenge (1 for Part 1, 2 for Part 2).
        answer (int | str): Your answer to submit.
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


class AocResponseParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_article = False
        self.article_content = ""

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.in_article = True

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False

    def handle_data(self, data):
        if self.in_article:
            self.article_content += data


class AocMessageType(Enum):
    EMPTY = auto()
    CORRECT = auto()
    TOO_HIGH = auto()
    TOO_LOW = auto()
    RECENT_SUBMISSION = auto()
    ALREADY_COMPLETED = auto()
    INCORRECT = auto()
    UNEXPECTED = auto()


def classify_message(content: str) -> AocMessageType:
    if not content:
        return AocMessageType.EMPTY
    elif "That's the right answer" in content:
        return AocMessageType.CORRECT
    elif "too high" in content:
        return AocMessageType.TOO_HIGH
    elif "too low" in content:
        return AocMessageType.TOO_LOW
    elif "You gave an answer too recently" in content:
        return AocMessageType.RECENT_SUBMISSION
    elif "Did you already complete it" in content:
        return AocMessageType.ALREADY_COMPLETED
    elif "That's not the right answer" in content:
        return AocMessageType.INCORRECT
    else:
        return AocMessageType.UNEXPECTED


def submit_to_aoc(
    year: int, day: int, level: int, answer: int | str, session_token: str | None = None
) -> SubmissionResult:
    """
    Submit an answer for a specific year, day, and level (part) to Advent of Code.

    🎁 Let the elves deliver your answer to Santa's server! 🎅

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the challenge (1–25).
        level (int): The level of the challenge (1 for Part 1, 2 for Part 2).
        answer (int | str): Your answer to submit.
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

        # Use the AocResponseParser to extract content inside <article> tags
        parser = AocResponseParser()
        parser.feed(response.text)
        message_content = parser.article_content.strip()

        # Classify the message
        message_type = classify_message(message_content)
        match message_type:
            case AocMessageType.EMPTY:
                message = (
                    "🎄 Answer submitted, but no response message was found. "
                    "Check your submission on the Advent of Code website."
                )
                status = SubmissionStatus.UNKNOWN
            case AocMessageType.CORRECT:
                message = get_correct_answer_message(answer=answer)
                status = SubmissionStatus.CORRECT
            case AocMessageType.TOO_HIGH:
                message = get_answer_too_high_message(answer=answer)
                status = SubmissionStatus.TOO_HIGH
            case AocMessageType.TOO_LOW:
                message = get_answer_too_low_message(answer=answer)
                status = SubmissionStatus.TOO_LOW
            case AocMessageType.RECENT_SUBMISSION:
                message = get_recent_submission_message()
                status = SubmissionStatus.WAIT
            case AocMessageType.ALREADY_COMPLETED:
                message = get_already_completed_message()
                status = SubmissionStatus.COMPLETED
            case AocMessageType.INCORRECT:
                message = get_incorrect_answer_message(answer=answer)
                status = SubmissionStatus.INCORRECT
            case AocMessageType.UNEXPECTED:
                message = get_unexpected_response_message()
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
        logger.error(f"Request exception occurred: {e}")
        raise SubmissionError(
            f"🛑 Uh-oh! An error occurred while submitting your answer: {e} 🎁"
        ) from e


def write_guess_cache(
    year: int, day: int, part: int, guess: int | str, status: SubmissionStatus
) -> None:
    """Write the user's guess to the cache file."""
    cache_file = get_cache_guess_file(year, day)

    # Get the current timestamp in ISO 8601 format
    timestamp = datetime.utcnow().isoformat()

    # Define the header
    fieldnames = ["timestamp", "part", "guess", "status"]

    try:
        # Determine if the file exists to decide on writing the header
        file_exists = cache_file.exists()

        # Open the CSV file in append mode using pathlib
        with cache_file.open("a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header if the file is new
            if not file_exists:
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
    except OSError as e:
        logger.error(f"OS error while writing to {cache_file}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error while writing to {cache_file}: {e}")


def read_guesses(year: int, day: int) -> list[Guess]:
    cache_file: Path = get_cache_guess_file(year, day)
    guesses = []

    if not cache_file.exists():
        return guesses

    try:
        with cache_file.open("r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    status = SubmissionStatus[row["status"]]
                except KeyError:
                    logger.warning(f"Unknown status '{row['status']}' in cache.")
                    status = SubmissionStatus.UNKNOWN

                guess_value = row["guess"]
                # Try to convert to int if possible
                try:
                    guess_value = int(guess_value)
                except ValueError:
                    pass  # Keep as str if not an int

                try:
                    timestamp = datetime.fromisoformat(row["timestamp"])
                except ValueError:
                    logger.warning(f"Invalid timestamp format: {row['timestamp']}")
                    timestamp = datetime.utcnow()

                guess = Guess(
                    timestamp=timestamp,
                    part=int(row["part"]),
                    guess=guess_value,
                    status=status,
                )
                guesses.append(guess)
    except OSError as e:
        logger.error(f"OS error while reading {cache_file}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error while reading {cache_file}: {e}")

    return guesses


def check_cached_guesses(
    year: int, day: int, level: int, answer: int | str
) -> CachedGuessCheck:
    """Check the cache for previous guesses and return a CachedGuessCheck instance."""
    guesses = read_guesses(year, day)
    highest_low_guess: Guess | None = None
    lowest_high_guess: Guess | None = None

    for guess in guesses:
        if guess.part != level:
            continue

        match guess:
            case Guess(guess=ans, status=SubmissionStatus.CORRECT) if ans == answer:
                return CachedGuessCheck(
                    guess=answer,
                    previous_guess=guess.guess,
                    previous_timestamp=guess.timestamp,
                    status=guess.status,
                    message=get_cached_duplicate_message(
                        answer=answer, previous_guess=guess
                    ),
                )
            case Guess(guess=ans, status=SubmissionStatus.TOO_LOW) if isinstance(
                ans, int
            ) and isinstance(answer, int):
                # Ensure highest_low_guess.guess is int before comparison
                if not highest_low_guess or (
                    isinstance(highest_low_guess.guess, int)
                    and ans > highest_low_guess.guess
                ):
                    highest_low_guess = guess
            case Guess(guess=ans, status=SubmissionStatus.TOO_HIGH) if isinstance(
                ans, int
            ) and isinstance(answer, int):
                # Ensure lowest_high_guess.guess is int before comparison
                if not lowest_high_guess or (
                    isinstance(lowest_high_guess.guess, int)
                    and ans < lowest_high_guess.guess
                ):
                    lowest_high_guess = guess
            case _:
                continue

    if isinstance(answer, int):
        match (highest_low_guess, lowest_high_guess):
            case (h_low, _) if h_low and isinstance(
                h_low.guess, int
            ) and answer <= h_low.guess:
                return CachedGuessCheck(
                    guess=answer,
                    previous_guess=h_low.guess,
                    previous_timestamp=h_low.timestamp,
                    status=SubmissionStatus.TOO_LOW,
                    message=get_cached_low_message(
                        answer=answer, highest_low_guess=h_low
                    ),
                )
            case (_, l_high) if l_high and isinstance(
                l_high.guess, int
            ) and answer >= l_high.guess:
                return CachedGuessCheck(
                    guess=answer,
                    previous_guess=l_high.guess,
                    previous_timestamp=l_high.timestamp,
                    status=SubmissionStatus.TOO_HIGH,
                    message=get_cached_high_message(
                        answer=answer, lowest_high_guess=l_high
                    ),
                )

    # Return unknown if no bounds could be inferred
    return CachedGuessCheck(
        guess=answer,
        previous_guess=None,
        previous_timestamp=None,
        status=SubmissionStatus.UNKNOWN,
        message="This is a unique guess.",
    )
