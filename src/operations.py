import exceptions


def power(token1: int | float, token2: int | float) -> float | int:
    if token2 > 1_000_000 and (-1 < token1 < 1):
        return 0
    if token2 > 1_000_000 and token1 > 1:
        raise exceptions.CalculatorError('inf')
    if token2 > 1_000_000 and token1 < -1:
        if token2 % 2 == 0:
            raise exceptions.CalculatorError('inf')
        else:
            raise exceptions.CalculatorError('-inf')
    return token1**token2


def division(token1: float | int, token2: float | int) -> float:
    if token2 == 0:
        raise exceptions.ZeroDivisionError(f'Деление на 0. {token1} / 0')
    if token1 % token2 == 0:
        return token1 // token2
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
    '**': power,
    '/': division,
    '//': int_division,
    '%': remainder,
}
