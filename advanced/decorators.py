import random
import time
from functools import wraps
from typing import Callable


def testing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is running...")
        func(*args, **kwargs)
        print(f"Function {func.__name__} has finished.")

    return wrapper


def multiplier(*, repeats: int):
    def decorator(function: Callable):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(repeats):
                function(*args, **kwargs)

        return wrapper

    return decorator


def report_in_slack(function: Callable):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as error:
            print(f"Raises Slack message with error: {error}")

    return wrapper


def execution_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print(
            f"\n --> Function {function.__name__} took {round(end - start, 5)} seconds"
        )
        return result

    return wrapper


@testing_decorator
@multiplier(repeats=2)
def do_something() -> None:
    """This function does something."""
    time.sleep(random.randint(1, 5))
    print("Done!")


@report_in_slack
def do_something_with_error():
    """Do something and raises error"""
    time.sleep(2)
    raise random.choice(
        [
            ValueError("Pailas"),
            EnvironmentError("Ojo con eso"),
            ZeroDivisionError("ceroo"),
        ]
    )


if __name__ == "__main__":
    # do_something()
    do_something_with_error()
