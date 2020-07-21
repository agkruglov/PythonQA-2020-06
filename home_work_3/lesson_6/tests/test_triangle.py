from math import sqrt

import pytest

from shapes.shape import NotShapeException
from shapes.triangle import Triangle, TriangleNotValidException


class TestTriangle:

    def setup_class(self):
        self.triangle = Triangle(7, 10, 5)

    def test_valid(self):
        with pytest.raises(TriangleNotValidException):
            triangle = Triangle(1, 2, 3)
            assert triangle.angles == 3

    def test_name(self):
        triangle = Triangle(1, 1, 1)
        assert triangle.name == 'Треугольник_3'

    def test_area(self):
        assert self.triangle.area == sqrt(11 * 4 * 1 * 6)

    def test_angles(self):
        assert self.triangle.angles == 3

    def test_perimeter(self):
        assert self.triangle.perimeter == 7 + 10 + 5

    def test_add_square(self):
        triangle = Triangle(1, 1, 1)
        print(triangle.area)
        print(self.triangle.area)
        assert self.triangle.add_square(triangle) == sqrt(11 * 4 * 1 * 6) + sqrt(1.5 * 0.5 * 0.5 * 0.5)

    def test_add_square_neg(self):
        not_shape = 3.14
        with pytest.raises(NotShapeException):
            assert self.triangle.add_square(not_shape) == 20
