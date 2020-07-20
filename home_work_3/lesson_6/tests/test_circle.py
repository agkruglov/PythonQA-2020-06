from math import pi

import pytest

from shapes.circle import Circle
from shapes.shape import NotShapeException

epsilon = 0.00000001


class TestCircle:

    def setup_class(self):
        self.circle = Circle(11)

    def test_name(self):
        circle = Circle(1)
        assert circle.name == 'Окружность_2'

    def test_area(self):
        assert self.circle.area == pi * 11 * 11

    def test_angles(self):
        assert self.circle.angles == 0

    def test_perimeter(self):
        assert self.circle.perimeter == 2 * pi * 11

    def test_add_square(self):
        circle = Circle(5)
        assert self.circle.add_square(circle) == pi * (121 + 25)

    def test_add_square_neg(self):
        not_shape = 5
        with pytest.raises(NotShapeException):
            assert self.circle.add_square(not_shape) == pi * (121 + 25)
