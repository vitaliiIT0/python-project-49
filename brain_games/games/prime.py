import random

MIN_NUMBER = 1
MAX_NUMBER = 100
PRIME_MIN = 2


def is_prime(number):
    if number < PRIME_MIN:
        return False
    for i in range(PRIME_MIN, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(number) else "no"
    question = str(number)
    return question, correct_answer
