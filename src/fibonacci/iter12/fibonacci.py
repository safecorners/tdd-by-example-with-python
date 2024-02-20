"""
https://peps.python.org/pep-0612/
"""

from typing import Callable, Concatenate, Dict, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")


def memorization(
    func: Callable[Concatenate[T, P], R]
) -> Callable[Concatenate[T, P], R]:
    __cache: Dict[T, R] = {}

    def _wrapper(n: T, *args: P.args, **kwargs: P.kwargs) -> R:
        if n in __cache:
            return __cache[n]
        else:
            result = func(n, *args, **kwargs)
            __cache.update({n: result})
            return result

    return _wrapper


@memorization
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)
