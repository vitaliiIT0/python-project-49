from brain_games.cli import welcome_user
from brain_games.games.calc import generate_calculation
from brain_games.game_logic import start_game


def main():
    user_name = welcome_user()
    start_game(
        "What is the result of the expression?",
        generate_calculation,
        user_name)


if __name__ == "__main__":
    main()
