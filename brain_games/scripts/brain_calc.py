#!/usr/bin/env python3
from random import randint, choice

from .utils import play_game

OPERATORS = ('*', '+', '-')


def main() -> None:
    play_game(_print_rules, _get_expression_for_question, _get_right_answer)


def _print_rules() -> None:
    """Print rules for user."""
    return print("What is the result of the expression?")


def _get_expression_for_question() -> str:
    """Get random string expression"""
    return f'{randint(1, 100)} {choice(OPERATORS)} {randint(1, 100)}'


def _get_right_answer(expression: str) -> int:
    """Calculate right answer for expression."""
    return str(eval(expression))


if __name__ == '__main__':
    main()
