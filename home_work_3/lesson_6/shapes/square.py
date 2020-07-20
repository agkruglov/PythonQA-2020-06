from shapes.shape import Shape


class Square(Shape):
    _name = 'Квадрат'

    def __init__(self, a):
        super().__init__()
        self._a = a

    @property
    def area(self):
        return self._a * self._a

    @property
    def angles(self):
        return 4

    @property
    def perimeter(self):
        return self._a << 2
