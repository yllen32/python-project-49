#!/usr/bin/env python3
from random import randint

from .utils import play_game

RULES = "What number is missing in the progression?"


def main() -> None:
    play_game(_get_question_and_answer, RULES)


def _get_question_and_answer() -> tuple:
    """Get random integer from 1 to 100 range"""
    progression = _generate_progression()
    right_answer = _remove_elem(progression)
    return _tostring(progression), right_answer


def _generate_progression() -> list[str]:
    """Generate list with random progression."""
    start, progress = randint(0, 20), randint(1, 6)
    progression = [start]
    for _ in range(9):
        start += progress
        progression.append(start)
    return progression


def _remove_elem(progression) -> str:
    """Remove random elem in progression put ".." instead, return removed
    elem."""
    index_for_remove = randint(0, 9)
    right_answer = str(progression[index_for_remove])
    progression[index_for_remove] = '..'
    return right_answer


def _tostring(progression: list) -> str:
    """Convert list to string.

    >>> _tostring([1, 2, 3, 4])
    '1 2 3 4'
    """
    return ' '.join(map(str, progression))


if __name__ == '__main__':
    main()
