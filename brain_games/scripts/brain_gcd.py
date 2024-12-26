import random
from math import gcd
from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    rounds_to_win = 3
    for _ in range(rounds_to_win):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f"Question: {number1} {number2}")

        correct_answer = gcd(number1, number2)
        user_answer = input("Your answer: ").strip()

        if not user_answer.isdigit() or int(user_answer) != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

        print("Correct!")

    print(f"Congratulations, {user_name}!")
