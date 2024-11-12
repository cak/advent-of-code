# 🎄 Elf Exception Handling 🎄 #


class ElfError(Exception):
    """Base exception for elf package errors."""

    def __init__(self, message=None):
        super().__init__(message)
        self.add_note("🎅 The elves have encountered a hitch in their work! 🚨")


class InputFetchError(ElfError):
    def __init__(self, message=None):
        super().__init__(message)
        self.add_note(
            "🎅 The elves are working hard to fetch the input. Please check your network connection or session token. 🚨"
        )


class SubmissionError(ElfError):
    """Raised when there is an issue submitting the answer."""

    def __init__(self, message=None):
        super().__init__(message)
        self.add_note("🎅 Santa couldn't deliver your answer! 🚨")


class MissingSessionTokenError(ValueError):
    """Exception raised when the session token is missing."""

    def __init__(self, env_var: str):
        super().__init__(
            f"🎅 Oh no! Santa's session cookie is missing. Please set the '{env_var}' "
            "environment variable or pass the session token explicitly. 🎄"
        )
