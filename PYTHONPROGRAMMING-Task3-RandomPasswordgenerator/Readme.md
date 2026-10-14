# Random Password Generator

A simple command-line password generator written in Python. You choose the password length and which character types to include, and the program builds a random password for you.

## Features

- Custom password length (minimum 8 characters)
- Choose from four character types:
  1. Uppercase letters (A-Z)
  2. Lowercase letters (a-z)
  3. Numbers (0-9)
  4. Symbols (`!@#$%^&*` and other punctuation)
- Requires at least 2 character types for a stronger password
- Input validation for length, character choices and yes/no prompts
- Generate as many passwords as you like in one session

## Requirements

- Python 3.6 or newer
- No external packages needed (uses only the standard `random` and `string` modules)

## Usage

Run the script (replace `main.py` with your file name):

```bash
python main.py
```

### Example session

```
Random Password Generator

Enter password length (minimum 8): 12

Choose character types to include:
1. Uppercase letters (A-Z)
2. Lowercase letters (a-z)
3. Numbers (0-9)
4. Symbols (!@#$%^&*)
Enter your choices separated by commas (example: 1,2,3,4): 1,2,3

Your generated password is:
aK7pQ2mXz9Lb

Generate another password? (y/n): n

Thank you for using the Password Generator!
```

## How It Works

1. Asks for a length and rejects anything below 8 or non-numeric input.
2. Asks for character types as comma-separated numbers, validates them, removes duplicates and requires at least two.
3. Builds a pool of characters from the selected types using the `string` module.
4. Picks `length` random characters from the pool with `random.choice()` and joins them into the password.
5. Asks whether to generate another password; `y` repeats, `n` exits.

## Limitations and Ideas for Improvement

- **Not cryptographically secure:** `random` is fine for learning, but for real passwords use the `secrets` module (`secrets.choice()`).
- **Type guarantee:** the password may occasionally miss one of the selected types. You could pick one character from each chosen type first, then fill the rest and shuffle.
- Add an option to exclude look-alike characters (`O`, `0`, `l`, `1`)
- Copy the password to the clipboard automatically
- Show a password strength indicator
- Build a GUI version with Tkinter

## License

This project is free to use and modify for personal and educational purposes.