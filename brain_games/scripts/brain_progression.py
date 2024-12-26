import random
from brain_games.game_logic import start_game


def generate_progression():

    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer


def main():
    description = "What number is missing in the progression?"
    start_game(description, generate_progression)
