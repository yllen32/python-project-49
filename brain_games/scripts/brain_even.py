#!/usr/bin/env python3
from random import randint

from .utils import Answer,  play_game


def main() -> None:
    play_game(_print_rules, _get_digit_for_question, _get_right_answer)


def _print_rules() -> None:
    """Print rules for user."""
    return print(
            f'Answer "{Answer.CORRECT.value}" if the number is even, '
            f'otherwise answer "{Answer.WRONG.value}".'
        )


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
