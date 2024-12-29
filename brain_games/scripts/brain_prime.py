from brain_games.games.prime import generate_question
from brain_games.game_logic import start_game


def main():
    start_game(
        "Answer \"yes\" if given number is prime. Otherwise answer \"no\".",
        generate_question
    )


if __name__ == "__main__":
    main()
