import random
from brain_games.cli import welcome_user

def is_even(number):
    """Checks if a number is even."""
    return number % 2 == 0

def main():
    """
    Runs the "Even" game.
    """
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_to_win = 3
    for _ in range(rounds_to_win):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

        print("Correct!")

    print(f"Congratulations, {user_name}!")
