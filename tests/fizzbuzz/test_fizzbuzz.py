from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_1() -> None:
    assert fizzbuzz(1) == 1


def test_fizzbuzz_2() -> None:
    assert fizzbuzz(2) == 2


def test_fizzbuzz_3() -> None:
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_4() -> None:
    assert fizzbuzz(4) == 4


def test_fizzbuzz_5() -> None:
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz_6() -> None:
    assert fizzbuzz(6) == "Fizz"


def test_fizzbuzz_15() -> None:
    assert fizzbuzz(15) == "FizzBuzz"
