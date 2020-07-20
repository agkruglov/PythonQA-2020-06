from shapes.square import Square


class Rectangle(Square):
    _name = 'Прямоугольник'

    def __init__(self, a, b):
        super().__init__(a)
        self.__b = b

    @property
    def area(self):
        return self._a * self.__b

    @property
    def perimeter(self):
        return (self._a + self.__b) << 1
