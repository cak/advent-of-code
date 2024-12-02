# 🎄 Advent of Code 🎄

Welcome to my festive repository, where code meets Christmas cheer! This collection holds my solutions for the [Advent of Code](https://adventofcode.com/) puzzles across multiple years. Join me as we unwrap new challenges each day of December, guided by the merry elves and sprinkled with holiday magic! ✨

## 📅 Advent of Code 2024 Progress (Goal: 20 Stars ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐)

### ⭐ Progress: 4/50 ⭐

| Day                                        | Stars | Solution                                                                           |
| ------------------------------------------ | ----- | ---------------------------------------------------------------------------------- |
| [01](https://adventofcode.com/2024/day/1)  | ⭐⭐  | [Solution](https://github.com/cak/advent-of-code/blob/main/2024/day01/solution.py) |
| [02](https://adventofcode.com/2024/day/2)  | ⭐⭐  | [Solution](https://github.com/cak/advent-of-code/blob/main/2024/day02/solution.py) |
| [03](https://adventofcode.com/2024/day/3)  |       |                                                                                    |
| [04](https://adventofcode.com/2024/day/4)  |       |                                                                                    |
| [05](https://adventofcode.com/2024/day/5)  |       |                                                                                    |
| [06](https://adventofcode.com/2024/day/6)  |       |                                                                                    |
| [07](https://adventofcode.com/2024/day/7)  |       |                                                                                    |
| [08](https://adventofcode.com/2024/day/8)  |       |                                                                                    |
| [09](https://adventofcode.com/2024/day/9)  |       |                                                                                    |
| [10](https://adventofcode.com/2024/day/10) |       |                                                                                    |
| [11](https://adventofcode.com/2024/day/11) |       |                                                                                    |
| [12](https://adventofcode.com/2024/day/12) |       |                                                                                    |
| [13](https://adventofcode.com/2024/day/13) |       |                                                                                    |
| [14](https://adventofcode.com/2024/day/14) |       |                                                                                    |
| [15](https://adventofcode.com/2024/day/15) |       |                                                                                    |
| [16](https://adventofcode.com/2024/day/16) |       |                                                                                    |
| [17](https://adventofcode.com/2024/day/17) |       |                                                                                    |
| [18](https://adventofcode.com/2024/day/18) |       |                                                                                    |
| [19](https://adventofcode.com/2024/day/19) |       |                                                                                    |
| [20](https://adventofcode.com/2024/day/20) |       |                                                                                    |
| [21](https://adventofcode.com/2024/day/21) |       |                                                                                    |
| [22](https://adventofcode.com/2024/day/22) |       |                                                                                    |
| [23](https://adventofcode.com/2024/day/23) |       |                                                                                    |
| [24](https://adventofcode.com/2024/day/24) |       |                                                                                    |
| [25](https://adventofcode.com/2024/day/25) |       |                                                                                    |

---

### 🎯 Goal Tracker: Earn 20 Stars

| Milestone       | Stars Earned | Status         |
| --------------- | ------------ | -------------- |
| 1-10 Stars      | 4/10         | 🟩 On Track    |
| 11-20 Stars     | 0/10         | 🟦 Not Started |
| Full Completion | 4/50         | ⬜             |

## 🎄 Folder Structure

Our repository is structured like a well-organized Christmas workshop! Each year contains folders for individual days, and the `elf` package houses utilities for puzzle-solving and automation:

```bash
advent-of-code/
├── 2016/
│   ├── day01/
│       ├── solution.py              # 🎁 Your main solution script for the day
│       ├── input.txt                # 📜 The puzzle input for the day
│       ├── test_input.txt           # 🧪 Example input for testing your solution
│       ├── expected_output.txt      # ✅ The expected output for test input
├── elf/                             # 🧝‍♂️ The elves' magical helpers!
│   ├── cli/                         # 🎅 Command-line interface for automation
│       ├── create_day.py            # 🏗️ Script to create new day folders
│       ├── fetch_input.py           # 🔄 Script to fetch puzzle inputs
│       ├── run.py                   # 🚀 Script to run a day's solution
│       ├── submit.py                # 🎯 Script to submit answers to Advent of Code
│       ├── test.py                  # 🧪 Script to test solutions for correctness
│   ├── templates/                   # ✨ Templates for new solution files
│       ├── args.py                  # ⚙️ Argument parsing template for solutions
│       ├── solution_template.py     # 📝 Template for daily solution scripts
│   ├── utils.py                     # 🧰 General utility functions for helpers
│   ├── input.py                     # 🔄 Functions to fetch and cache puzzle inputs
│   ├── config.py                    # ⚙️ Configuration settings for the project
│   ├── testing.py                   # 🧪 Tools for testing solutions
│   ├── answer.py                    # 🎯 Helpers for answer validation and submission
│   └── exceptions.py                # 🚨 Custom exception handling for the CLI
├── README.md                        # 📖 Documentation (you're here!)
├── LICENSE                          # 📜 Open source license
├── pyproject.toml                   # 📦 Project dependencies and settings
├── uv.lock                          # 🔒 Dependency lockfile
```

## 🛠️ Automating Tasks with the Elf CLI

The `elf` CLI is your all-in-one tool to manage Advent of Code puzzles. From creating folders to running tests, it makes solving puzzles joyful!

### Installing Dependencies

Before you start, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Commands Overview

Run the CLI by executing:

```bash
python -m elf.cli.main <command> [options]
```

Available commands:

- **`create-day`**: Create a new folder for a specific day.
- **`fetch-input`**: Fetch puzzle input for a specific day.
- **`run`**: Run the solution for a specific day and part.
- **`test`**: Test the solution using provided test inputs.
- **`submit`**: Submit your solution to Advent of Code.

### Command Details

#### 1. Create a New Day Folder

Set up a new folder for a day, complete with templates and input files:

```bash
python -m elf.cli.main create-day <year> <day> --output-dir <directory>
```

Example:

```bash
python -m elf.cli.main create-day 2016 5
```

#### 2. Fetch Puzzle Input

Fetch your personalized input for a day:

```bash
python -m elf.cli.main fetch-input <year> <day>
```

Example:

```bash
python -m elf.cli.main fetch-input 2016 5
```

#### 3. Run a Solution

Run your solution for a specific day and part:

```bash
python -m elf.cli.main run <year> <day> --part <1|2|both>
```

Examples:

```bash
python -m elf.cli.main run 2016 4 --part 1
python -m elf.cli.main run 2016 4 --part both
```

#### 4. Test Your Solution

Run tests using `test_input.txt` and `expected_output.txt`:

```bash
python -m elf.cli.main test <year> <day>
```

Example:

```bash
python -m elf.cli.main test 2016 4
```

#### 5. Submit Your Answer

Submit your solution directly to Advent of Code:

```bash
python -m elf.cli.main submit <year> <day> <part> <answer>
```

Example:

```bash
python -m elf.cli.main submit 2016 4 1 12345
```

### Setting Up Your Session Token

To fetch inputs and submit answers, you'll need your Advent of Code session token:

1. Log in to [Advent of Code](https://adventofcode.com/) and copy your session token from the browser cookies.
2. Save it as an environment variable:
   ```bash
   export AOC_SESSION_COOKIE='your_session_token_here'
   ```

**Note**: Keep your token secret to prevent unauthorized access.

## ✨ Features of the `elf` Package

The `elf` package simplifies common tasks:

- **Input Handling**: Automatically fetch and cache puzzle inputs.
- **Testing Utilities**: Compare your output with expected results.
- **Template Management**: Quickly create new solution files.
- **Error Handling**: Gracefully manage exceptions.

Example usage in a solution:

```python
from elf import input, utils

def part1(data):
    return sum(map(int, data.split()))

if __name__ == "__main__":
    data = input.read_input_file("input.txt")
    print("Part 1:", part1(data))
```

---

**May your Advent of Code journey be merry and bright! Happy coding! 🎅**
