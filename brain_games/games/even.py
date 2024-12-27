import random

MIN_NUMBER = 1
MAX_NUMBER = 100
ROUNDS_TO_WIN = 3


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_even(number) else "no"
    question = str(number)
    return question, correct_answer
