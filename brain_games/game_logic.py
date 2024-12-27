def start_game(description, question_func, name):
    print(description)

    rounds_to_win = 3
    for _ in range(rounds_to_win):
        question, correct_answer = question_func()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer != str(correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
