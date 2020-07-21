from shapes.shape import Shape


class SquareNotValidException(Exception):
    pass


class Square(Shape):
    _name = 'Квадрат'

    def __init__(self, a):
        super().__init__()

        if a <= 0:
            raise SquareNotValidException('Квадрат со стороной {} не может существовать'.format(a))

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
