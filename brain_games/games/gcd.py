from random import randint

from brain_games import game_engine as engine

RULES = "Find the greatest common divisor of given numbers."
MIN_VALUE = 1
MAX_VALUE = 100


def _get_question_and_answer() -> tuple:
    """Get random integer from 1 to 100 range"""
    a = randint(MIN_VALUE, MAX_VALUE)
    b = randint(MIN_VALUE, MAX_VALUE)
    print(_get_right_answer(a, b))
    return f'{a} {b}', _get_right_answer(a, b)


def _get_right_answer(a: int, b: int) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    while b != 0:
        a, b = b, a % b
    return str(a)


def play_gcd() -> None:
    """Start gcd game"""
    engine.play_game(_get_question_and_answer, RULES)
