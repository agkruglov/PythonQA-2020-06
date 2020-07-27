from abc import ABC, abstractmethod


class NotShapeException(Exception):
    pass


class Shape(ABC):
    _instance_count = 0
    _name = 'Фигура'

    def __init__(self):
        self.__class__._instance_count += 1
        self.__name = '{}_{}'.format(self.__class__._name, self.__class__._instance_count)

    @property
    def name(self):
        return self.__name

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def angles(self) -> int:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    def add_square(self, shape):
        if isinstance(shape, Shape):
            return self.area + shape.area
        else:
            raise NotShapeException('{} не является потомком класса Shape'.format(shape))
