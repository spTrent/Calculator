from src import operations


def test_division() -> None:
    """Тест деления"""
    tests: list[tuple] = [
        ([5, 1], 5),
        ([5, 2], 2.5),
        ([2.2, 1], 2.2),
        ([2.2, 2], 1.1),
        ([2.2, 1.1], 2),
        ([10, 0.1], 100),
        ([-5, 2], -2.5),
        ([5, -2], -2.5),
        ([-5, -2], 2.5),
    ]
    for stdin, res in tests:
        assert operations.division(*stdin) == res


def test_int_division() -> None:
    """Тест целочисленного деления"""
    tests: list[tuple] = [
        ([5, 1], 5),
        ([5, 2], 2),
        ([-5, 2], -3),
        ([5, -2], -3),
    ]
    for stdin, res in tests:
        assert operations.int_division(*stdin) == res


def test_power() -> None:
    """Тест возведения в степень"""
    tests: list[tuple] = [
        ([5, 1], 5),
        ([5, 2], 25),
        ([1, 100_000_000], 1),
        ([0.99999, 100_000_000], 0),
        ([-0.99999, 100_000_000], 0),
    ]
    for stdin, res in tests:
        assert operations.power(*stdin) == res


def test_remainder() -> None:
    """Тест остатка от деления"""
    tests: list[tuple] = [
        ([15, 2], 1),
        ([16, 2], 0),
        ([-15, 6], 3),
        ([15, -6], -3),
    ]
    for stdin, res in tests:
        assert operations.remainder(*stdin) == res
