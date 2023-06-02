#!/usr/bin/env python3
from random import randint

from .utils import Answer, play_game


RULES = (
        f'Answer "{Answer.CORRECT.value}" if the number is even, '
        f'otherwise answer "{Answer.WRONG.value}".'
    )


def main() -> None:
    play_game(_get_question_and_answer, RULES)


def _get_question_and_answer() -> str:
    """Get random integer from 1 to 100 range"""
    digit = randint(1, 100)
    return digit, _get_right_answer(digit)


def _get_right_answer(digit: int) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    if digit % 2 == 0:
        return Answer.CORRECT.value
    return Answer.WRONG.value


if __name__ == '__main__':
    main()
