import elf


def main(year: int, day: int):
    try:
        input_data = elf.get_input(year, day)
        print(f"📥 Input fetched:\n{input_data}")
    except elf.InputFetchError as e:
        print(f"❌ Failed to fetch input: {e}")
