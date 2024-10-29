# 🎄 Elf Exception Handling 🎄 #


class ElfError(Exception):
    """Base exception for elf package errors.

    🎅 The elves have encountered a hitch in their work! 🚨
    """

    pass


class InputFetchError(ElfError):
    """Raised when there is an issue fetching the puzzle input.

    🎅 Oh no! The elves couldn't fetch the input! 🚨
    """

    pass


class SubmissionError(ElfError):
    """Raised when there is an issue submitting the answer.

    🎅 Santa couldn't deliver your answer! 🚨
    """

    pass
