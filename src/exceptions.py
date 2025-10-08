class CalculatorError(Exception):
    """Базовое исключение для калькулятора"""

    pass


class FloatNotInt(CalculatorError):
    """
    Ошибка неверного типа данных:
    // и % только для целых.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class IncorrectInput(CalculatorError):
    """
    Ошибка неверного ввода:
    неправильное количество чисел, операций или скобок.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ZeroDivision(CalculatorError):
    """Деление на 0"""

    def __init__(self, message: str) -> None:
        super().__init__(message)
