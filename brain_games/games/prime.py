from random import randint

from brain_games import game_engine as engine


RULES = (
    f'Answer "{engine.CORRECT}" if given number is prime, '
    f'Otherwise answer "{engine.WRONG}".'
)
MIN_VALUE = 1
MAX_VALUE = 100


def _get_question_and_answer() -> tuple:
    """Get random integer from 1 to 100 range"""
    digit = randint(MIN_VALUE, MAX_VALUE)
    return digit, _get_right_answer(digit)


def _get_right_answer(number: int) -> str:
    """Get right answer for given digit. return 'yes' if it even, 'no'
    otherwise."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return engine.WRONG
    return engine.CORRECT


def play_prime() -> None:
    """Start prime_game"""
    engine.play_game(_get_question_and_answer, RULES)
