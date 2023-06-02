#!/usr/bin/env python3
from random import randint, choice

from .utils import play_game

OPERATORS = ('*', '+', '-')

RULES = "What is the result of the expression?"


def main() -> None:
    play_game(_get_expression_and_answer, RULES)


def _get_expression_and_answer() -> tuple:
    """Get random string expression"""
    expression = f'{randint(1, 100)} {choice(OPERATORS)} {randint(1, 100)}'
    return expression, _get_right_answer(expression)


def _get_right_answer(expression: str) -> int:
    """Calculate right answer for expression."""
    return str(eval(expression))


if __name__ == '__main__':
    main()
