import pytest

import src.exceptions
from src.operations import division, int_division, power, remainder


def test_division_zero() -> None:
    with pytest.raises(src.exceptions.ZeroDivisionError) as exp_info:
        division(5, 0)
        assert '5 / 0' in str(exp_info.value)


def test_int_division_zero() -> None:
    with pytest.raises(src.exceptions.ZeroDivisionError) as exp_info:
        int_division(5, 0)
        assert '5 // 0' in str(exp_info.value)


def test_remainder_zero() -> None:
    with pytest.raises(src.exceptions.ZeroDivisionError) as exp_info:
        remainder(5, 0)
        assert '5 % 0' in str(exp_info.value)


def test_power_inf() -> None:
    with pytest.raises(src.exceptions.CalculatorError) as exp_info:
        power(2, 100_000_000)
        assert 'inf' in str(exp_info.value)


def test_power_minus_inf0() -> None:
    with pytest.raises(src.exceptions.CalculatorError) as exp_info:
        power(-2, 100_000_000)
        assert 'inf' in str(exp_info.value)


def test_power_minus_inf1() -> None:
    with pytest.raises(src.exceptions.CalculatorError) as exp_info:
        power(-2, 99_999_999)
        assert '-inf' in str(exp_info.value)
