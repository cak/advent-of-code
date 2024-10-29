# 🎄 Elf Package Initialization 🎄 #

from .answer import submit_answer
from .exceptions import InputFetchError, SubmissionError
from .input import get_input, read_input_file
from .testing import check_part1_solution, check_part2_solution
from .utils import parse_input, timer

# Define the public API of the elf package
__all__ = [
    "get_input",
    "read_input_file",
    "parse_input",
    "timer",
    "check_part1_solution",
    "check_part2_solution",
    "InputFetchError",
    "SubmissionError",
    "submit_answer",
]
