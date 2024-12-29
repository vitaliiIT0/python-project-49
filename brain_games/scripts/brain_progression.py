from brain_games.games.progression import generate_progression
from brain_games.game_logic import start_game


def main():
    start_game(
        "What number is missing in the progression?",
        generate_progression
        )


if __name__ == "__main__":
    main()
