#!/usr/bin/env python3
from random import randint

from .utils import CORRECT, WRONG, play_game


RULES = (
    f'Answer "{CORRECT}" if the number is even, '
    f'otherwise answer "{WRONG}".'
)


def main() -> None:
    play_game(_get_question_and_answer, RULES)


def _get_question_and_answer() -> tuple:
    """Get random integer from 1 to 100 range"""
    digit = randint(1, 100)
    return digit, _get_right_answer(digit)


def _get_right_answer(digit: int) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    if digit % 2 == 0:
        return CORRECT
    return WRONG


if __name__ == '__main__':
    main()
