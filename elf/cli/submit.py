import elf


def main(year: int, day: int, part: str, answer: str):
    try:
        result = elf.submit_answer(year, day, int(part), answer)
        print(result.message)
    except elf.SubmissionError as e:
        print(f"❌ Submission failed: {e}")
