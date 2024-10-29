# 🎄 Advent of Code 🎄

Welcome to my festive repository, where code meets Christmas cheer! This collection holds my solutions for the [Advent of Code](https://adventofcode.com/) puzzles across multiple years. Join me as we unwrap new challenges each day of December, guided by the merry elves and sprinkled with holiday magic! ✨

## 📅 Years and Progress

- **[2016](2015/README.md)**: Progress: 1/25
- **[2015](2015/README.md)**: Progress: 0/25

## 🎄 Folder Structure

Our repository is neatly organized, just like gifts under the Christmas tree. Each folder represents a year, and inside, you'll find daily presents waiting to be opened:

```bash
advent_of_code/
├── 2015/
│   ├── day01/
│   │   ├── day01.py                  # 🎁 Solution script for Day 01
│   │   ├── input.txt                 # 📜 Puzzle input for Day 01
│   │   └── README.md                 # 📘 Notes and reflections
├── utils/
│   ├── __init__.py                   # 🛠️ Makes it a Python package
│   └── create_day.py                 # 🎅 Script to create new day folders
├── templates/
│   └── solution_template.py          # ✨ Template for daily solutions
└── elf/                              # 🧝‍♂️ The elves' magical helpers!
    ├── __init__.py
    ├── config.py
    ├── input.py                      # 🔄 Fetching and caching puzzle inputs
    ├── utils.py                      # 🧰 Utility functions
    ├── testing.py                    # 🧪 Testing helpers
    └── exceptions.py                 # 🚨 Custom exceptions
```

## 🎅 Automating Day Folder Creation

The elves have been busy crafting a script to help you set up your daily challenges with ease!

### Step 1: Create a New Day Folder

Run the `create_day.py` script with the desired year and day:

```bash
python utils/create_day.py <year> <day>
```

For example, to create the `day01` folder for 2015:

```bash
python utils/create_day.py 2015 1
```

This magical script will:

- Create the necessary folders.
- Copy the solution template.
- Fetch your puzzle input and save it to `input.txt` (more on this below).
- Create `test_input.txt` and `expected_test_output.txt` for your testing needs.

Your folder will look like this:

```bash
advent_of_code/
├── 2015/
│   ├── day01/
│   │   ├── day01.py
│   │   ├── input.txt
│   │   ├── test_input.txt
│   │   ├── expected_test_output.txt
│   │   └── README.md
```

## 🔑 Setting Up Your Advent of Code Session Token

To fetch your personalized puzzle input, the elves need your Advent of Code session token. Don't worry; we'll keep it safe and sound!

### Step 1: Retrieve Your Session Token

1. **Log in to Advent of Code**: Visit [Advent of Code](https://adventofcode.com/) and log in using your preferred method (GitHub, Google, Twitter, etc.).
2. **Open Browser Developer Tools**:
   - Right-click anywhere on the page and select **Inspect** (Chrome) or **Inspect Element** (Firefox).
3. **Find the Session Cookie**:
   - Navigate to the **Application** (Chrome) or **Storage** (Firefox) tab in the developer tools.
   - Under **Cookies**, find `session` and copy its value.
   - **Important**: Keep this value secret; it's like the key to Santa's workshop!

### Step 2: Set the Session Token as an Environment Variable

The elves will read this environment variable to fetch your inputs.

#### On Unix/Linux/MacOS:

```bash
export AOC_SESSION_COOKIE='your_session_token_here'
```

#### On Windows Command Prompt:

```cmd
set AOC_SESSION_COOKIE=your_session_token_here
```

#### On Windows PowerShell:

```powershell
$env:AOC_SESSION_COOKIE='your_session_token_here'
```

**Note**: Replace `'your_session_token_here'` with the actual session token you copied.

### Step 3: Keep It Secret, Keep It Safe

- **Do Not Commit**: Ensure you **never** commit your session token to any repository.
- **Security First**: Treat it like a cherished gift; only you should know it!

Now, when you run `create_day.py`, the elves can fetch your puzzle input and save it to `input.txt` automatically!

## 🏃 Running the Code

Time to see the elves' magic in action! Here are the ways to run your solutions:

### Running Tests

Navigate to the day's directory and run:

```bash
python dayXX.py --test
```

This will:

- Use `test_input.txt` and `expected_test_output.txt` to verify your solution.
- Let you know if the elves approve of your code!

### Running with Actual Input

Once your code passes the tests, simply run the script without any flags to use your actual puzzle input:

```bash
python dayXX.py
```

The elves will process your actual input and provide the results for both parts (or the part you specify).

### Running a Specific Part

You can choose to run either Part 1, Part 2, or both:

```bash
python dayXX.py --part 1  # Runs only Part 1
python dayXX.py --part 2  # Runs only Part 2
python dayXX.py --part both  # Runs both parts
```

### Skipping Tests

If you want to skip running tests and go straight to the main solution, you can use:

```bash
python dayXX.py --no-test
```

### Submitting Your Answer

Once you're confident with your solution, you can submit it directly using the `--submit` flag:

```bash
python dayXX.py --submit
```

You can also submit a specific part:

```bash
python dayXX.py --part 1 --submit  # Submits only Part 1
python dayXX.py --part 2 --submit  # Submits only Part 2
```

## 🎁 Using the `elf` Package

The `elf` package is your toolbox of festive functions, crafted to make solving puzzles joyful!

### What's Inside the Elves' Workshop?

- **`input.py`**: Functions to fetch and read puzzle inputs.
- **`utils.py`**: Handy utilities like input parsing and timing decorators.
- **`testing.py`**: Tools to help you test your solutions.
- **`exceptions.py`**: Custom exceptions to handle any mishaps.
- **`config.py`**: Configuration settings (like your session token).

### Example Usage in Your Solution

```python
import elf
from pathlib import Path

def part1(data):
    # Your solution for part 1
    pass

def part2(data):
    # Your solution for part 2
    pass

if __name__ == "__main__":
    base_dir = Path(__file__).parent
    data = elf.read_input_file(base_dir / "input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
```

The elves are always there to lend a helping hand (or hoof)!

## 🛠️ Requirements

To ensure all the elf magic works smoothly, make sure to install the required packages:

```bash
pip install -r requirements.txt
```

The elves recommend using a virtual environment to keep things tidy.

## 🎉 Contributing and Sharing the Joy

Found a better way to solve a puzzle or want to share some holiday cheer? Feel free to open an issue or submit a pull request. Let's make this repository as magical as the season itself!

## ✨ License

This project is licensed under the MIT License. Spread the joy, but remember to give credit where it's due!

---

**May your days be merry and bright, and may your code run without a fight! Happy Holidays! 🎄🎅**

---

## ☃️ Final Notes

- **Security Reminder**: Always keep your session token private. It's like the secret recipe for Santa's cookies!
- **Community Guidelines**: Be respectful and kind. The holiday spirit is all about sharing and caring.
- **Feedback Welcome**: If you have suggestions to make this repository even more festive, let me know!

---

**Special thanks to [Eric Wastl](https://adventofcode.com/about) for creating Advent of Code and bringing joy to the coding community every December!** 🎉

---

**Enjoy your coding adventure, and may the elves guide you to success!**
