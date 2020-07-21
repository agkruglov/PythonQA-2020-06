from shapes.square import Square


class RectangleNotValidException(Exception):
    pass


class Rectangle(Square):
    _name = 'Прямоугольник'

    def __init__(self, a, b):
        super().__init__(a)

        if a <= 0 or b <= 0:
            raise RectangleNotValidException('Прямоугольник со сторонами {} и {} не может существовать'.format(a, b))

        self.__b = b

    @property
    def area(self):
        return self._a * self.__b

    @property
    def perimeter(self):
        return (self._a + self.__b) << 1
