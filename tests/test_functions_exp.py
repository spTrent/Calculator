import pytest

import src.exceptions
from src.functions import check_accuracy, do_rpn, remove_staples


def test_check_accuracy() -> None:
    """Тест ошибки ввода с лишними символами"""
    with pytest.raises(src.exceptions.IncorrectInput) as exp_info:
        check_accuracy('55 55 aaa +')
    assert 'Неизвестный символ' in str(exp_info.value)


def test_do_rpn_exp_digits() -> None:
    """Тест ошибки ввода с неверным количеством операций"""
    with pytest.raises(src.exceptions.IncorrectInput) as exp_info:
        do_rpn([1, '+'])
    assert 'Количество чисел перед операцией' in str(exp_info.value)


def test_do_rpn_exp_operations() -> None:
    """Тест ошибки ввода с неверным количеством чисел"""
    with pytest.raises(src.exceptions.IncorrectInput) as exp_info:
        do_rpn([1, 1, 1, '-'])
    assert 'Операции закончились' in str(exp_info.value)


def test_remove_staples_open() -> None:
    """Тест ошибки ввода с открывающейся, но не закрывающейся скобкой"""
    with pytest.raises(src.exceptions.IncorrectInput) as exp_info:
        remove_staples('(55 55 +')
    assert 'Скобка открывается, но не закрывается' in str(exp_info.value)


def test_remove_staples_close() -> None:
    """Тест ошибки ввода с закрывающейся, но не открывающейся скобкой"""
    with pytest.raises(src.exceptions.IncorrectInput) as exp_info:
        remove_staples('55 55 +)')
    assert 'Скобка закрывается, но не открывается' in str(exp_info.value)


def test_remove_staples_open_close() -> None:
    """Тест ошибки ввода со скобками в разные стороны"""
    with pytest.raises(src.exceptions.IncorrectInput) as exp_info:
        remove_staples(')55 55 +(')
    assert 'Скобка открывается, но не закрывается' in str(exp_info.value)
