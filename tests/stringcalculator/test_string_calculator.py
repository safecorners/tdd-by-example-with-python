import pytest
from stringcalculator import StringCalculator


@pytest.fixture(scope="function")
def calc() -> StringCalculator:
    return StringCalculator()


def test_empty_string_should_be_0(calc: StringCalculator) -> None:
    assert calc.add("") == 0


def test_one_should_be_1(calc: StringCalculator) -> None:
    assert calc.add("1") == 1


def test_new_line_delimiter(calc: StringCalculator) -> None:
    assert calc.add("1\n2,3") == 6


def test_one_and_two_should_be_3(calc: StringCalculator) -> None:
    assert calc.add("1,2") == 3


def test_handle_an_unknown_amount_of_numbers(calc: StringCalculator) -> None:
    assert calc.add("1,100,2000") == 2101


def test_support_delimiters(calc: StringCalculator) -> None:
    assert calc.add("//,\n1,2,3") == 6


def test_throw_exception_when_passed_negative_number(calc: StringCalculator) -> None:
    with pytest.raises(Exception) as excinfo:
        calc.add("1,2,-3")
    assert str(excinfo.value) == "negatives not allowed - [-3]"


def test_throw_exception_when_passed_negative_numbers(calc: StringCalculator) -> None:
    with pytest.raises(Exception) as excinfo:
        calc.add("1,-22,-3")
    assert str(excinfo.value) == "negatives not allowed - [-22, -3]"
