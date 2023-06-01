from enum import Enum

import prompt


class Answer(Enum):
    CORRECT = 'yes'
    WRONG = 'no'


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
