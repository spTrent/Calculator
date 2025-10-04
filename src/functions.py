import re

import exceptions


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
        raise exceptions.InvalidInput('Скобка открывается, но не закрывается')
    if opened_cnt < closed_cnt:
        raise exceptions.InvalidInput('Скобка закрывается, но не открывается')
    for _ in range(opened_cnt):
        opened: int = stdin.rfind('(')
        closed: int = stdin.find(')', opened)
        current_staples = stdin[opened + 1 : closed]
        try:
            current_tokens = tokenize(current_staples)
            current_rpn = str(do_rpn(current_tokens))
            stdin = stdin[:opened] + current_rpn + stdin[closed + 1 :]
        except exceptions.CalculatorError as message:
            print(f'{type(message).__name__}: {message}')
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


def division(token1: float | int, token2: float | int) -> float:
    if token2 == 0:
        raise exceptions.ZeroDivisionError(f'Деление на 0. {token1} / 0')
    if token1 % token2 == 0:
        return int(token1 / token2)
    return token1 / token2


def int_division(token1: int | float, token2: int | float) -> int:
    if token1.is_integer() and token2.is_integer() and token2 != 0:
        return int(token1 // token2)
    if token2 == 0:
        raise exceptions.ZeroDivisionError(f'Деление на 0. {token1} // 0')
    raise exceptions.TypeError(f'// только для целых. {token1} // {token2}')


def remainder(token1: int | float, token2: int | float) -> int:
    if token1.is_integer() and token2.is_integer() and token2 != 0:
        return int(token1 % token2)
    if token2 == 0:
        raise exceptions.ZeroDivisionError(f'Деление на 0. {token1} % 0')
    raise exceptions.TypeError(f'% только для целых. {token1} % {token2}')


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x**y,
    '/': division,
    '//': int_division,
    '%': remainder,
}


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
        r'([+-]?\d+(\.\d+)?(e[+-]?\d+)?|[+-]?\d+(\.\d+)?|[+-]|\*\*|//|%|[*/])'
    )
    tokens: list[str | int | float] = []
    for token_group in re.finditer(PATTERN, s):
        token = token_group.group()
        if token in operations:
            tokens += [token]
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
            raise exceptions.InvalidInput(
                f"""Неверное количество операций и чисел:
             Количество чисел перед операцией({token}): {len(stack)}"""
            )
        else:
            num_token: float | int = int_or_float(str(token))
            stack.append(num_token)
    if len(stack) == 1:
        return stack[0]
    raise exceptions.InvalidInput(
        f"""Неверное количество операций и чисел:
             Операции закончились, количество оставшихся чисел: {len(stack)}"""
    )
