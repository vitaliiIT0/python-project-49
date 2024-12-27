from brain_games.cli import welcome_user
from brain_games.games.prime import generate_question
from brain_games.game_logic import start_game


def main():
    user_name = welcome_user()
    start_game(
        "Answer \"yes\" if the given number is prime. Otherwise answer \"no\".",
        generate_question,
        user_name
    )


if __name__ == "__main__":
    main()
