from .helpers import to_integer, byteswap


class Point:
    def __init__(self, x, y):
        self.x = to_integer(x)
        self.y = to_integer(y)

    def __repr__(self):
        return f"{self.__class__}({self.__dict__})"

    def byteswapped(self):
        return self.__class__(byteswap(self.x), byteswap(self.y))
