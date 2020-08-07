from shapes.rectangle import Rectangle


class Square(Rectangle):
    _instance_count = 0
    _name = 'Квадрат'

    def __init__(self, a):
        super().__init__(a, a)
