class CalculatorError(Exception):
    """Базовое исключение для калькулятора"""

    pass


class TypeError(CalculatorError):
    """
    Ошибка неверного типа данных:
    // и % только для целых.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class SyntaxError(CalculatorError):
    """
    Ошибка неверного ввода:
    неправильное количество чисел и операций.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ZeroDivisionError(CalculatorError):
    """Деление на 0"""

    def __init__(self, message: str) -> None:
        super().__init__(message)
