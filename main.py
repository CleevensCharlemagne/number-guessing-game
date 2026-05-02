import random

from logic import get_level_choice, get_chances, play_game


def main():
    print(
        "Welcome to the Number Guessing Game!\n"
        "I'm thinking of a number between 1 and 100.\n"
    )

    level = get_level_choice()
    chances = get_chances(level)[0]
    print('\n'+ get_chances(level)[1])
    print("Let's start the game!")
    target = random.randint(1, 100)

    play_game(chances, target)


if __name__ == "__main__":
    main()