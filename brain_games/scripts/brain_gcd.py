#!/usr/bin/env python3
from random import randint

from .utils import play_game


def main() -> None:
    play_game(_print_rules, _get_question, _get_right_answer)


def _print_rules() -> None:
    """Print rules for user."""
    return print("Find the greatest common divisor of given numbers.")


def _get_question() -> tuple:
    """Get random integer from 1 to 100 range"""
    return randint(1, 100), randint(1, 100)


def _get_right_answer(digits: tuple) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    a, b = digits
    while b != 0:
        a, b = b, a % b
    return str(a)


if __name__ == '__main__':
    main()
