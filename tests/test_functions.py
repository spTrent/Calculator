from math import e, pi

from src.functions import do_rpn, int_or_float, remove_staples, tokenize


def test_int_or_float() -> None:
    """Тест проверки на тип числа"""
    tests: list[tuple] = [
        (5, 5),
        (5.1, 5.1),
        (5.0, 5),
        (-5, -5),
        (-5.1, -5.1),
        (-5.0, -5),
    ]
    for digit, res in tests:
        assert int_or_float(digit) == res


def test_tokenize() -> None:
    """Тест токенизации"""
    tests: list[tuple] = [
        ('5 5 +', [5, 5, '+']),
        ('5e2 5.0 **', [500, 5, '**']),
        ('5.1 E **', [5.1, e, '**']),
        ('π ~6.2 //', [pi, -6.2, '//']),
        ('$5 3.14 % 6 +', [5, 3.14, '%', 6, '+']),
        ('1e-2', [0.01]),
    ]
    for stdin, res in tests:
        assert tokenize(stdin) == res


def test_do_rpn() -> None:
    """Тест подсчета токенов"""
    tests: list[tuple] = [
        ([5, 5, '+'], 10),
        ([500, 5, '**'], 31250000000000),
        ([5.1, e, '**'], 83.82530688265744),
        ([0.01], 0.01),
        ([1, 6, '*', 5, '-'], 1),
        ([5, 5, '+'], 10),
    ]
    for tokens, res in tests:
        assert do_rpn(tokens) == res


def test_remove_staples() -> None:
    """Тест подсчета выражений в скобках и их заменой"""
    tests: list[tuple] = [
        ('(((555)))', '555'),
        ('(((555 100 +)))', '655'),
        ('((555 100 +) 100 -)', '555'),
        ('((555 100 +) (12 88 +) -)', '555'),
        ('(5) 5 +', '5 5 +'),
        ('(5 6 +) 5 -', '11 5 -'),
    ]
    for stdin, res in tests:
        assert remove_staples(stdin) == res
