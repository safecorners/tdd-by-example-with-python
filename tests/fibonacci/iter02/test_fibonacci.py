from fibonacci.iter02.fibonacci import fib


def test_fibonacci() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
