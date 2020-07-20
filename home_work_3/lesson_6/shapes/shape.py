from abc import ABC, abstractmethod


class NotShapeException(Exception):
    pass


class Shape(ABC):
    __instance_count = 0
    _name = 'Фигура'

    def __init__(self):
        self.__class__.__instance_count += 1

    def __del__(self):
        self.__class__.__instance_count -= 1

    @classmethod
    def __name(cls):
        return '{}_{}'.format(cls._name, cls.__instance_count)

    @property
    def name(self):
        return self.__name()

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
