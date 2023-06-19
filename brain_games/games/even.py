from random import randint

from brain_games import game_engine as engine


RULES = (
    f'Answer "{engine.CORRECT}" if the number is even, '
    f'otherwise answer "{engine.WRONG}".'
)
MIN_VALUE = 1
MAX_VALUE = 100


def _get_question_and_answer() -> tuple:
    """Get random integer as question and answer for the question."""
    digit = randint(MIN_VALUE, MAX_VALUE)
    answer = engine.CORRECT if _is_even(digit) else engine.WRONG
    return digit, answer


def _is_even(digit: int) -> bool:
    """Return True if digit is even"""
    return digit % 2 == 0


def play_even() -> None:
    """Start prime_game"""
    engine.play_game(_get_question_and_answer, RULES)
