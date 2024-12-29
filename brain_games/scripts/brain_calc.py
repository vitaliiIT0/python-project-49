from brain_games.games.calc import generate_calculation
from brain_games.game_logic import start_game


def main():
    start_game(
        "What is the result of the expression?",
        generate_calculation
        )


if __name__ == "__main__":
    main()
