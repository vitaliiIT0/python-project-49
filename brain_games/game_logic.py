from brain_games.cli import welcome_user

def start_game(description, generate_question):
    user_name = welcome_user()
    print(description)
    ROUNDS_TO_WIN = 3

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
