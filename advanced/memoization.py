import sys
import time
from functools import wraps, cache
from typing import Callable


def memoize(function: Callable):
    cache = {}

    @wraps(function)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]

    return wrapper


@cache
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    sys.setrecursionlimit(100_000)
    while text := input(f"{28*'-'}\nEnter a number: "):
        number = int(text)
        start: float = time.perf_counter()
        print(f"{28*'-'}\n{fibonacci(number)=}")
        end: float = time.perf_counter()
        print(f"\n Time: {round(end - start, 5)} s")
    else:
        print("\nGood bye!")
