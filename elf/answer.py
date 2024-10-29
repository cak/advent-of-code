import requests
from bs4 import BeautifulSoup

from elf.config import get_session_token
from elf.exceptions import SubmissionError
from elf.messages import (
    get_already_completed_message,
    get_answer_too_high_message,
    get_answer_too_low_message,
    get_correct_answer_message,
    get_incorrect_answer_message,
    get_recent_submission_message,
    get_unexpected_response_message,
)

# 🎄 Elf Answer Submission 🎄 #


def submit_answer(
    year: int, day: int, level: int, answer: str, session_token: str | None = None
) -> str:
    """
    Submit an answer for a specific year, day, and level (part) to Advent of Code.

    🎁 Let the elves deliver your answer to Santa's server! 🎅

    Args:
        year (int): The year of the Advent of Code challenge.
        day (int): The day of the Advent of Code challenge.
        level (int): The level of the challenge (1 for Part 1, 2 for Part 2).
        answer (str): Your answer to submit.
        session_token (Optional[str]): Your Advent of Code session token. If not provided,
            it will be retrieved from the environment variable 'AOC_SESSION_COOKIE'.

    Returns:
        str: A festive message based on the response from the server.

    Raises:
        SubmissionError: If there is an issue submitting the answer.
        ValueError: If the session token is not provided and not found in the environment.
    """
    session_token = get_session_token(session_token)

    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    headers = {
        "Cookie": f"session={session_token}",
        "User-Agent": "elf-package/1.0 (+https://github.com/cak/elf)",
    }
    data = {"level": str(level), "answer": answer}

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()

        # Parse the response HTML to extract the message
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find("article")
        if article:
            message = article.text.strip()

            match message:
                case msg if "That's the right answer" in msg:
                    return get_correct_answer_message()
                case msg if "too high" in msg:
                    return get_answer_too_high_message()
                case msg if "too low" in msg:
                    return get_answer_too_low_message()
                case msg if "You gave an answer too recently" in msg:
                    return get_recent_submission_message()
                case msg if "Did you already complete it" in msg:
                    return get_already_completed_message()
                case msg if "That's not the right answer" in msg:
                    return get_incorrect_answer_message()
                case _:
                    return get_unexpected_response_message()
        else:
            return "🎄 Answer submitted, but no response message was found. Check your submission on the Advent of Code website."

    except requests.exceptions.RequestException as e:
        raise SubmissionError(
            f"🛑 Uh-oh! An error occurred while submitting your answer: {e} 🎁"
        ) from e
