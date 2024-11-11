from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

# 🎁 Elf Models 🎁 #


@dataclass
class TestResult:
    part: int
    passed: bool
    expected: str
    actual: str
    message: str

    def __str__(self):
        return (
            f"SubmissionResult(\n"
            f"  part={self.part},\n"
            f"  passed={self.passed},\n"
            f"  expected='{self.expected}',\n"
            f"  actual={self.actual},\n"
            f"  message={self.message}\n"
            f")"
        )


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
    is_cached: bool

    def __str__(self):
        return (
            f"SubmissionResult(\n"
            f"  guess={self.guess},\n"
            f"  result={self.result.name},\n"
            f"  is_correct={self.is_correct},\n"
            f"  is_cached={self.is_cached}\n"
            f"  message='{self.message}',\n"
            f")"
        )


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
