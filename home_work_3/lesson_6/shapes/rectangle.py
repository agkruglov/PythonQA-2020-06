from shapes.shape import Shape


class Rectangle(Shape):
    _instance_count = 0
    _name = 'Прямоугольник'

    def __init__(self, a, b):
        super().__init__()

        if a <= 0 or b <= 0:
            raise ValueError('{} со сторонами {} и {} не может существовать'.format(Rectangle._name, a, b))

        self._a = a
        self._b = b

    @property
    def area(self):
        return self._a * self._b

    @property
    def angles(self):
        return 4

    @property
    def perimeter(self):
        return (self._a + self._b) << 1
