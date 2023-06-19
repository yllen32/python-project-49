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
    answer = engine.CORRECT if (
        digit > 2 and _is_prime(digit)
    ) else engine.WRONG
    return digit, answer


def _is_prime(number: int) -> bool:
    """Get right answer for given digit. return True if it prime, False
    otherwise."""
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def play_prime() -> None:
    """Start prime_game"""
    engine.play_game(_get_question_and_answer, RULES)
