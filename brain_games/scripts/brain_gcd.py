#!/usr/bin/env python3
from random import randint

from .utils import play_game

RULES = "Find the greatest common divisor of given numbers."


def main() -> None:
    play_game(_get_question_and_answer, RULES)


def _get_question_and_answer() -> tuple:
    """Get random integer from 1 to 100 range"""
    a, b = randint(1, 100), randint(1, 100)
    print(_get_right_answer(a, b))
    return f'{a} {b}', _get_right_answer(a, b)


def _get_right_answer(a: int, b: int) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    while b != 0:
        a, b = b, a % b
    return str(a)


if __name__ == '__main__':
    main()
