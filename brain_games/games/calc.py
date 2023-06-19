from random import randint, choice
from operator import add, sub, mul
from typing import Callable

from brain_games import game_engine as engine

OPERATOR_FUNCTIONS = {'*': mul, '+': add, '-': sub}

RULES = "What is the result of the expression?"

MIN_VALUE = 1
MAX_VALUE = 100


def _get_expression_and_answer() -> tuple:
    """Get random string expression"""
    num1 = randint(MIN_VALUE, MAX_VALUE)
    num2 = randint(MIN_VALUE, MAX_VALUE)
    operator = choice(tuple(OPERATOR_FUNCTIONS.keys()))
    expression = f'{num1} {operator} {num2}'
    right_answer = _calculate(num1, num2, OPERATOR_FUNCTIONS[operator])
    return expression, str(right_answer)


def _calculate(num1: int, num2: int, action: Callable) -> int:
    """Calculate right answer for the give numbers and operator."""
    return action(num1, num2)


def play_calc() -> None:
    """Start prime_game"""
    engine.play_game(_get_expression_and_answer, RULES)
