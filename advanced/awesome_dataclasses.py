from dataclasses import dataclass

@dataclass
class Fruit:
    name: str
    price: float

class Fruit2:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price!r})"

if __name__ == "__main__":
    apple = Fruit("apple", 1.99)
    banana = Fruit2("banana", 0.99)
    print(apple)
    print(banana)