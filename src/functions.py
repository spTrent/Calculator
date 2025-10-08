import re
from math import e, pi

import src.exceptions
from src.operations import operations


def check_accuracy(stdin: str) -> None:
    for el in stdin:
        if el not in '+-~$0123456789Eπ. ()*/%':
            raise src.exceptions.IncorrectInput(f'Неизвестный символ: {el}')


def remove_staples(stdin: str) -> str:
    """
    Меняет выражение в скобках в stdin на их значение

    Находит самую правую открывающуюся и соответсвующую ей закрывающуюся,
    считает выражение внутри них и записывает вместо него значение

    Args:
        stdin(str): строка с выражениями в скобках

    Returns:
        stdin(str): строка без выражений в скобках. Заменены на значения
    """
    opened_cnt: int = stdin.count('(')
    closed_cnt: int = stdin.count(')')
    if opened_cnt > closed_cnt:
        raise src.exceptions.IncorrectInput(
            'Скобка открывается, но не закрывается'
        )
    if opened_cnt < closed_cnt:
        raise src.exceptions.IncorrectInput(
            'Скобка закрывается, но не открывается'
        )
    for _ in range(opened_cnt):
        opened: int = stdin.rfind('(')
        closed: int = stdin.find(')', opened)
        if closed == -1:
            raise src.exceptions.IncorrectInput(
                'Скобка открывается, но не закрывается'
            )
        current_staples = stdin[opened + 1 : closed]
        current_tokens = tokenize(current_staples)
        current_rpn = str(do_rpn(current_tokens))
        stdin = stdin[:opened] + current_rpn + stdin[closed + 1 :]
    return stdin


def int_or_float(digit: str) -> float | int:
    """
    Переводит число в правильный тип

    Args:
        digit(str): строка с определяемым числом

    Returns:
        digit(float | int): число в правильном типе
    """
    if float(digit).is_integer():
        return int(float(digit))
    return float(digit)


def tokenize(stdin: str) -> list[str | float | int]:
    """
    Разбивает строку stdin на список токенов.

    Находит в строке числа, в том числе с унарными +/- ($/~),
                    и знаки операций.
    Приводит числа к типу float/int и собирает итоговый список токенов.

    Args:
        stdin(str): строка, которую нужно разбить на токены.

    Returns:
        tokens(list): список токенов.
    """
    s: str = stdin.replace('~', '-').replace('$', '')
    PATTERN = re.compile(
        r'([+-]?\d+(\.\d+)?(e[+-]?\d+)?|E|π|[+-]?\d+(\.\d+)?|[+-]|\*\*|//|%|[*/])'
    )
    tokens: list[str | int | float] = []
    for token_group in re.finditer(PATTERN, s):
        token = token_group.group()
        if token in operations:
            tokens += [token]
        elif token == 'E':
            tokens += [e]
        elif token == 'π':
            tokens += [pi]
        else:
            tokens += [int_or_float(token)]
    return tokens


def do_rpn(tokens: list[float | int | str]) -> float | int:
    """
    Считает результат операций в списке токенов.

    По очереди берет токены и добавляет числа в стек,
    пока не встретит знак операции.
    Достает последние два числа из стека, применяет операцию
    и кладет результат в стек

    Args:
        tokens(list): список токенов

    Returns:
        float: результат операций
    """
    stack: list[float | int] = []
    for token in tokens:
        if token in operations and len(stack) >= 2:
            item2, item1 = stack.pop(), stack.pop()
            operator: str = str(token)
            new_token: float | int = operations[operator](item1, item2)
            stack.append(new_token)
        elif token in operations and len(stack) < 2:
            raise src.exceptions.IncorrectInput(
                f"""Неверное количество операций и чисел:
             Количество чисел перед операцией({token}): {len(stack)}"""
            )
        else:
            num_token: float | int = int_or_float(str(token))
            stack.append(num_token)
    if len(stack) == 1:
        return stack[0]
    raise src.exceptions.IncorrectInput(
        f"""Неверное количество операций и чисел:
             Операции закончились, количество оставшихся чисел: {len(stack)}"""
    )
