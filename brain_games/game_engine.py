from typing import Callable

import prompt


CORRECT = 'yes'
WRONG = 'no'
MAX_ATTEMPTS = 3


def play_game(getting_question_and_answer: Callable, rules: str) -> None:
    """Play a game with the user, prompting them with a question
    and checking their answer."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(rules)
    attempts = 0
    while attempts != MAX_ATTEMPTS:
        question, right_answer = getting_question_and_answer()
        user_answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {user_answer}')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'."
            )
            return print(f"Let's try again, {user_name}!")
        attempts += 1
    return print(f"Congratulations, {user_name}!")
