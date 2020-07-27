from math import pi

from shapes.shape import Shape


class Circle(Shape):
    _instance_count = 0
    _name = 'Окружность'

    def __init__(self, r):
        super().__init__()

        if r <= 0:
            raise ValueError('{} с радиусом {} не может существовать'.format(Circle._name, r))

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
