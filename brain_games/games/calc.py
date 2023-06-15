from random import randint, choice

from brain_games import game_engine as engine

OPERATORS = ('*', '+', '-')

RULES = "What is the result of the expression?"

MIN_VALUE = 1
MAX_VALUE = 100


def _get_expression_and_answer() -> tuple:
    """Get random string expression"""
    expression = [
        randint(MIN_VALUE, MAX_VALUE),
        choice(OPERATORS),
        randint(MIN_VALUE, MAX_VALUE),
    ]
    return ' '.join(expression), _get_right_answer(expression)


def _get_right_answer(expression: str) -> int:
    """Calculate right answer for expression."""
    return str(eval(expression))


def play_calc() -> None:
    """Start prime_game"""
    engine.play_game(_get_expression_and_answer, RULES)