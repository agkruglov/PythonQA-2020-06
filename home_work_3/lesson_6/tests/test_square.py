import pytest

from shapes.shape import NotShapeException, Shape
from shapes.square import Square


class TestSquare:

    def setup_class(self):
        self.square = Square(5)

    def test_name(self):
        rectangle = Square(1)
        assert rectangle.name == 'Квадрат_2'

    def test_area(self):
        assert self.square.area == 5 * 5

    def test_angles(self):
        assert self.square.angles == 4

    def test_perimeter(self):
        assert self.square.perimeter == 4 * 5

    def test_add_square(self):
        circle = Square(1)
        assert self.square.add_square(circle) == 25 + 1

    def test_add_square_neg(self):
        with pytest.raises(TypeError):
            not_shape = Shape()
            assert self.square.add_square(not_shape) == 25
