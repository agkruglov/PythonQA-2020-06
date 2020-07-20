from math import pi

from shapes.shape import Shape


class Circle(Shape):
    _name = 'Окружность'

    def __init__(self, r):
        super().__init__()
        self._r = r

    @property
    def area(self):
        return pi * self._r * self._r

    @property
    def angles(self):
        return 0

    @property
    def perimeter(self):
        return 2 * pi * self._r
