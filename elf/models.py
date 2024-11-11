from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

# 🎁 Elf Models 🎁 #


class SubmissionStatus(Enum):
    CORRECT = auto()
    INCORRECT = auto()
    TOO_HIGH = auto()
    TOO_LOW = auto()
    WAIT = auto()
    COMPLETED = auto()
    UNKNOWN = auto()


@dataclass
class SubmissionResult:
    guess: int
    result: SubmissionStatus
    message: str
    is_correct: bool


@dataclass
class Guess:
    timestamp: datetime
    part: int
    guess: int
    status: SubmissionStatus

    def is_too_low(self, answer: int) -> bool:
        return self.guess < answer and self.status == SubmissionStatus.TOO_LOW

    def is_too_high(self, answer: int) -> bool:
        return self.guess > answer and self.status == SubmissionStatus.TOO_HIGH


@dataclass
class CachedGuessCheck:
    guess: int
    previous_guess: int | None
    previous_timestamp: datetime | None
    status: SubmissionStatus
    message: str
