from brain_games.games.even import generate_question
from brain_games.game_logic import start_game


def main():
    start_game(
        "Answer \"yes\" if the number is even, otherwise answer \"no\".",
        generate_question
        )


if __name__ == "__main__":
    main()
