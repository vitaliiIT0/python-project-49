import random

MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = ["+", "-", "*"]


def generate_calculation():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"

    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return question, correct_answer
