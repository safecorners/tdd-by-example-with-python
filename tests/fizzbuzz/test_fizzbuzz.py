from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_1() -> None:
    assert fizzbuzz(1) == 1


def test_fizzbuzz_2() -> None:
    assert fizzbuzz(2) == 2


def test_fizzbuzz_3() -> None:
    assert fizzbuzz(3) == "Fizz"
