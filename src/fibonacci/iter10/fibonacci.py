from typing import Any, Callable, Dict, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def memorization(func: Callable[P, R]) -> Callable[P, R]:
    __cache: Dict[Any, R] = {}

    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        if args in __cache:
            return __cache[args]
        else:
            result = func(*args, **kwargs)
            __cache.update({args: result})
            return result

    return _wrapper


@memorization
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
