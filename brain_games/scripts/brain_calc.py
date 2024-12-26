import random
from brain_games.game_logic import start_game


def generate_calculation():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(operations)
    question = f"{num1} {operation} {num2}"

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return question, correct_answer


def main():
    start_game("What is the result of the expression?", generate_calculation)
