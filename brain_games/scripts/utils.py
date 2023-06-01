from enum import Enum
from typing import Callable

import prompt


class Answer(Enum):
    CORRECT = 'yes'
    WRONG = 'no'


MAX_ATTEMPTS = 3
CORRECT_STATUS = 'Correct!'


def greeting_user() -> str:
    """Print grettings in to console and ask user_name, return username"""
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def say_user_wrong_answer(
        user_answer: str | int,
        right_answer: str | int,
        ) -> None:
    """Print user answer and correct answer."""
    return print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'."
            )


def cheer_up(user_name: str) -> None:
    """Print cheer_up if user lost."""
    print(f"Let's try again, {user_name}!")


def congratulations_user(user_name: str) -> None:
    """Print a congratulations message."""
    print(f"Congratulations, {user_name}!")


def play_game(
        print_rules: Callable,
        getting_question: Callable,
        get_right_answer: Callable,
        ) -> None:
    """Play a game with the user, prompting them with a question
    and checking their answer."""
    user_name = greeting_user()
    print_rules()
    attempts = 0
    while attempts != MAX_ATTEMPTS:
        question = getting_question()
        user_answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {user_answer}')
        right_answer = get_right_answer(question)
        if user_answer == right_answer:
            print(CORRECT_STATUS)
        else:
            say_user_wrong_answer(user_answer, right_answer)
            return cheer_up(user_name)
        attempts += 1
    return congratulations_user(user_name)
