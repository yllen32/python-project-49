#!/usr/bin/env python3
from random import randint

from .utils import Answer,  play_game


RULES = (
            f'Answer "{Answer.CORRECT.value}" if the number is even, '
            f'Otherwise answer "{Answer.WRONG.value}".'
        )


def main() -> None:
    play_game(_get_question_and_answer)


def _get_question_and_answer() -> str:
    """Get random integer from 1 to 100 range"""
    digit = randint(1, 100)
    return digit, _get_right_answer(digit)


def _get_right_answer(number: int) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return Answer.WRONG.value
    return Answer.CORRECT.value


if __name__ == '__main__':
    main()
