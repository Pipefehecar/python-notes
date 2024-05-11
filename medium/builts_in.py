import random
import sys as system

from oop import Fruit, Motorbike


def is_odd(number: int) -> bool:
    return number % 2 == 1


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_string(obj: object) -> bool:
    return isinstance(obj, str)


def make_square(number: int) -> int:
    return number**2


if __name__ == "__main__":
    moto: Motorbike = Motorbike()
    if isinstance(moto, Motorbike):
        print("Motorbike instance")
    odds: list = list(range(1, 20, 2))
    print(f"{system.getsizeof(odds)=}")
    print(f"{system.getsizeof(range(1, 20, 2))=}")
    print(f"{system.getsizeof(range(20**20))=}")
    print(f"{system.getsizeof([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])=}")
    randoms: list = random.choices(range(1, 51), k=10)
    is_odd_list: bool = all(i % 2 == 1 for i in odds)
    print(f"{is_odd_list=}")
    is_any_odd: bool = any(i > 40 for i in randoms)
    print(f"{is_any_odd=}")

    # explicit any and all
    print(f"{any([True, False, False])=}")
    print(f"{any([False, False, False])=}")
    print(f"{all([True, False, False])=}")
    print(f"{all([False, False, False])=}")
    print(f"{any([])=}")
    callable_obj = random.choice([odds, randoms, moto, Motorbike, print])
    print(f"{callable_obj=}")
    print(f"{callable(callable_obj)=}")

    another_odd_list: list = list(filter(is_odd, randoms))
    print(f"{another_odd_list=}")

    even_list: list = list(map(lambda x: x + 1, odds))
    print(f"{even_list=}")

    squares_list: list = list(map(make_square, range(1, 11)))
    print(f"{squares_list=}")

    fruits = [
        Fruit("apple", color="green"),
        Fruit("banana",color="yellow"),
        Fruit("orange", color="orange"),
    ]
    sorted_fruits = sorted(fruits, key=lambda fruit: fruit.color, reverse=True)
    sorted_fruits = sorted(fruits, key=str, reverse=False)
    print(f"{sorted_fruits=}")