from abc import ABC, abstractmethod
from enum import StrEnum, auto
import random


class FruitSizes(StrEnum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    HUGE = auto()


class Fruit:
    def __init__(self, name: str, *, color: str, size: FruitSizes = FruitSizes.SMALL) -> None:
        self._color = color  # protected
        self.__size = size  # private
        self.nombre = name  # public

    def __str__(self) -> str:
        return (
            f"{self.nombre.title()[:-1]}ita"
            if self.nombre.upper() == "PERA"
            else self.nombre.title()
        )

    @property
    def name(self):
        return self.nombre

    @name.setter
    def name(self, value: str):
        self.nombre = value
        return f"name changed to: {value}"

    @property
    def size(self):
        return self.__size.value

    @size.setter
    def size(self, value: FruitSizes):
        self.__size = value
        return f"size changed to: {value}"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value
        return f"color changed to: {value}"

    def __repr__(self) -> str:
        return f"Fruit(name={self.nombre}, color={self.color}, size={self.size})"

    def __eq__(self, other):
        return (
            self.nombre == other.name
            and self.color == other.color
            and self.size == other.size
        )

    @staticmethod
    def validate_size(size: FruitSizes) -> bool:
        return size in FruitSizes


class TropicalFruit(Fruit):
    def __init__(self, name: str, *, color: str, size: FruitSizes, origin: str) -> None:
        super().__init__(name, color=color, size=size)
        self.__origin = origin

    def __str__(self) -> str:
        return f"{super().__str__()} from {self.origin}"

    def __guess_origin(self) -> str:
        if (
            self.nombre.lower() in ["banana", "mango"]
            and self.color.lower() == "yellow"
        ):
            return "Can be Mango from Mexico or Banana from Ecuador"
        if self.size == FruitSizes.HUGE:
            return "Piña from Costa Rica"
        return "I don't know the origin of this fruit"

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, value: str):
        self.__origin = value
        return f"origin changed to: {value}"

    @property
    def guess_origin(self):
        return self.__guess_origin()

    @classmethod
    def from_string(cls, fruit: str):
        """Create a new instance of TropicalFruit from a string like 'banana-Yellow-Small-Ecuador'"""
        name, color, size, origin = fruit.split("-")
        return cls(name, color=color, size=FruitSizes(size), origin=origin)


class Phone(ABC):
    def __init__(self, number: str) -> None:
        self.__number = number

    @abstractmethod
    def call(self, number: str) -> None: ...


class CellPhone(Phone):
    def __init__(self, number: str, brand: str) -> None:
        super().__init__(number)
        self.brand = brand

    # def call(self, number: str) -> None:
    #     print(f"Calling {number} from {self.__number}...")


class Vehicle:
    def __new__(cls, wheels: int) -> None:
        if wheels == 2:
            return Motorbike()
        if wheels == 4:
            return Car()
        else:
            return super().__new__(cls)

    def __init__(self, wheels: int) -> None:
        self.wheels = wheels
        print(f"Vehicle with {self.wheels} wheels")


class Motorbike:
    def __init__(self) -> None:
        print("I'm a Motorbike")


class Car:
    def __init__(self) -> None:
        print("I'm a Car")


if __name__ == "__main__":
    fruit_1: Fruit = Fruit("pera", color="Green", size=FruitSizes.SMALL)
    print(f"{str(fruit_1)}")
    print(f"{fruit_1.color=}")
    print(f"{fruit_1.size=}")
    print(f"{fruit_1=}")
    if Fruit.validate_size("Small"):
        print("Size is valid")
        fruit_2: TropicalFruit = TropicalFruit(
            "banana", color="Yellow", size=FruitSizes.SMALL, origin="Ecuador"
        )
    print(fruit_2.guess_origin)
    print(f"{fruit_2=}")
    print(f"{str(fruit_2)=}")
    print(fruit_2.__repr__())
    try:
        print("\nprint(fruit_2.__origin)", end="--> ")
        print(fruit_2.__origin)
    except AttributeError as error:
        print(f"This error was generated to apreciate encapsulation: {error}\n")
    fruit_3: Fruit = TropicalFruit.from_string("banana-Yellow-Small-Ecuador")
    print(f"{fruit_3=}")

    try:
        phone = Phone("123456789")
    except TypeError as error:
        print(f"this error was generated to apreciate abstraction: {error}")

    Vehicle(random.randint(1, 5))

"""
WHEN SHOULD USE FUNCTIONS AND WHEN SHOULD USE CLASSES

Use clases when your program is state focus
Use functions when your program is action focus
"""
