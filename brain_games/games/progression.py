from random import randint

from brain_games import game_engine as engine

RULES = "What number is missing in the progression?"
MIN_START_VALUE = 0
MAX_START_VALUE = 20
MIN_PROGRESS_VALUE = 1
MAX_PROGRESS_VALUE = 6
PROGRESSION_LENGTH = 10


def _get_question_and_answer() -> tuple:
    """Get random integer from 1 to 100 range"""
    progression = _generate_progression()
    right_answer = _remove_elem(progression)
    return _tostring(progression), right_answer


def _generate_progression() -> list[str]:
    """Generate list with random progression."""
    start = randint(MIN_START_VALUE, MAX_START_VALUE)
    progress = randint(MIN_PROGRESS_VALUE, MAX_PROGRESS_VALUE)
    progression = [start]
    for _ in range(PROGRESSION_LENGTH - 1):
        start += progress
        progression.append(start)
    return progression


def _remove_elem(progression) -> str:
    """Remove random elem in progression put ".." instead, return removed
    elem."""
    index_for_remove = randint(0, PROGRESSION_LENGTH - 1)
    right_answer = str(progression[index_for_remove])
    progression[index_for_remove] = '..'
    return right_answer


def _tostring(progression: list) -> str:
    """Convert list to string.

    >>> _tostring([1, 2, 3, 4])
    '1 2 3 4'
    """
    return ' '.join(map(str, progression))


def play_progression() -> None:
    """Start progression_game"""
    engine.play_game(_get_question_and_answer, RULES)
