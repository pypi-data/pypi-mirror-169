from enum import Enum


class Color(tuple, Enum):
    """Color enum"""

    def __new__(cls, bgr):
        obj = tuple.__new__(cls, bgr)
        return obj

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    YELLOW = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    CYAN = (255, 255, 0)

    def __add__(self, other):
        return tuple(int((a[0] + a[1] + 1) / 2) for a in zip(self, other))

    def __str__(self):
        return f'{self.name} {self.value}'
