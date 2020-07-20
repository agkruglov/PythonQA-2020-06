import pytest

from shapes.rectangle import Rectangle
from shapes.shape import NotShapeException


class TestRectangle:

    def setup_class(self):
        self.rectangle = Rectangle(5, 4)

    def test_name(self):
        rectangle = Rectangle(1, 1)
        assert rectangle.name == 'Прямоугольник_2'

    def test_area(self):
        assert self.rectangle.area == 5 * 4

    def test_angles(self):
        assert self.rectangle.angles == 4

    def test_perimeter(self):
        assert self.rectangle.perimeter == 2 * (5 + 4)

    def test_add_square(self):
        circle = Rectangle(1, 1)
        assert self.rectangle.add_square(circle) == 20 + 1

    def test_add_square_neg(self):
        not_shape = 'not_shape'
        with pytest.raises(NotShapeException):
            assert self.rectangle.add_square(not_shape) == 20
