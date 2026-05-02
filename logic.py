import random


def get_level_choice():
    while True:
        print(
            "Please select the difficulty level:\n\t"
            "1. Easy (10 chances)\n\t"
            "2. Medium (5 chances)\n\t"
            "3. Hard (3 chances)\n"
        )
        choice = input("Enter your choice: ")

        if choice in ("1", "2", "3"):
            return int(choice)

        print("Invalid choice! Please choose between 1 and 3.")


def get_chances(level):
    levels = {
        1: [10, "Great! You have selected the Easy difficulty level."],
        2: [5, "Great! You have selected the Medium difficulty level."],
        3: [3, "Great! You have selected the Medium difficulty level."]
    }
    return (levels[level][0], levels[level][1])


def evaluate_guess(guess, target):
    if guess == target:
        return "correct"
    elif guess > target:
        return "high"
    else:
        return "low"


def play_game(chances, target):
    attempts = 0

    while chances > 0:
        user_input = input("\nEnter your guess: ")

        if not user_input.isdigit():
            print("Invalid input! Enter a number between 1 and 100.")
            continue

        guess = int(user_input)
        attempts += 1

        result = evaluate_guess(guess, target)

        if result == "correct":
            print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts!")
            return

        chances -= 1

        if result == "high":
            print(f"Incorrect! The number is less than {guess}.")
        else:
            print(f"Incorrect! The number is greater than {guess}.")

        print(f"Remaining chances: {chances}")

    print(f"💀 Game over! The number was {target}")

