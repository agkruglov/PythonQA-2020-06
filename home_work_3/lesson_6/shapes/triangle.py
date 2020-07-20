from math import sqrt

from shapes.shape import Shape


class TriangleNotValidException(Exception):
    pass


class Triangle(Shape):
    _name = 'Треугольник'

    def __init__(self, a, b, c):
        super().__init__()
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise TriangleNotValidException('Тругольник со сторонами {}, {} и {} не может существовать')
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def area(self):
        p = (self.__a + self.__b + self.__c) / 2
        return sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    @property
    def angles(self):
        return 3

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c
