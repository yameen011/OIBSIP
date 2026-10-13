import random
import string

print("Random Password Generator")

while True:

    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length < 8:
                print("Password must be at least 8 characters long.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Ask which character types to include
    print("\nChoose character types to include:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$%^&*)")

    while True:
        choices = input(
            "Enter your choices separated by commas (example: 1,2,3,4): "
        )

        choices = choices.replace(" ", "").split(",")

        # Check that choices are valid
        if not all(choice in ["1", "2", "3", "4"] for choice in choices):
            print("Invalid choice. Please select only 1, 2, 3, or 4.")
            continue

        # Remove duplicates
        choices = list(set(choices))

        # At least 2 types must be selected
        if len(choices) < 2:
            print("Please select at least 2 character types.")
            continue

        break

    # Build the character pool
    characters = ""

    if "1" in choices:
        characters += string.ascii_uppercase

    if "2" in choices:
        characters += string.ascii_lowercase

    if "3" in choices:
        characters += string.digits

    if "4" in choices:
        characters += string.punctuation

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nYour generated password is:")
    print(password)

    # Ask whether to generate another
    while True:
        again = input("\nGenerate another password? (y/n): ").lower()

        if again == "y":
            break
        elif again == "n":
            print("\nThank you for using the Password Generator!")
            exit()
        else:
            print("Please enter y or n.")