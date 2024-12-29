from brain_games.games.gcd import generate_question
from brain_games.game_logic import start_game


def main():
    start_game(
        "Find the greatest common divisor of given numbers.",
        generate_question
        )


if __name__ == "__main__":
    main()
