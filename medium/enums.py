from enum import Enum


class Color(str, Enum):
    ORANGE = "Orange"
    BLUE = "Blue"
    GREEN = "Green"


color = Color.GREEN

if color == color.BLUE:
    print(f'color is {color.value}')
else:
    print([color.value for color in Color])