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
    first_number = randint(MIN_VALUE, MAX_VALUE)
    second_number = randint(MIN_VALUE, MAX_VALUE)
    operator = choice(OPERATOR_FUNCTIONS)
    expression = f'{first_number} {operator} {second_number}'
    right_answer = _get_right_answer(
        first_number,
        second_number,
        OPERATOR_FUNCTIONS[operator]
    )
    return expression, right_answer


def _get_right_answer(num1: int, num2: int, action: Callable) -> int:
    """Calculate right answer for the give numbers and operator."""
    return action(num1, num2)


def play_calc() -> None:
    """Start prime_game"""
    engine.play_game(_get_expression_and_answer, RULES)
