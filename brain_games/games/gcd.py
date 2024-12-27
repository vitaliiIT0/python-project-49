import random
from math import gcd

MIN_NUMBER = 1
MAX_NUMBER = 100
ROUNDS_TO_WIN = 3


def generate_question():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number1} {number2}"

    correct_answer = gcd(number1, number2)
    return question, correct_answer
