#!/usr/bin/env python3
from random import randint

import prompt

from .utils import (
    greeting_user, Answer, CORRECT_STATUS, say_user_wrong_answer, cheer_up,
    congratulations_user,
)

MAX_ATTEMPTS = 3


def main() -> None:
    user = greeting_user()
    _read_rules()
    _play_game(user)


def _read_rules() -> None:
    """Print rules for user."""
    return print(
            f'Answer "{Answer.CORRECT.value}" if the number is even, '
            f'otherwise answer "{Answer.WRONG.value}".'
        )


def _play_game(user_name: str) -> None:
    """Play a game with the user, prompting them with a digit
    and checking their answer."""
    attempts = 0
    while attempts != MAX_ATTEMPTS:
        digit = _get_digit_for_question()
        user_answer = prompt.string(f'Question: {digit} ')
        print(f'Your answer: {user_answer}')
        right_answer = _get_right_answer(digit)
        if user_answer == right_answer:
            print(CORRECT_STATUS)
        else:
            say_user_wrong_answer(user_answer, right_answer)
            return cheer_up(user_name)
        attempts += 1
    return congratulations_user(user_name)


def _get_digit_for_question() -> str:
    """Get random integer from 1 to 100 range"""
    return randint(1, 100)


def _get_right_answer(digit: int) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    if digit % 2 == 0:
        return Answer.CORRECT.value
    return Answer.WRONG.value


if __name__ == '__main__':
    main()
