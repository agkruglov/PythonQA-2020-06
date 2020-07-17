import pytest


class TestSet:

    def setup_method(self):
        self.my_set = {1, 'Alex', 3, 'Ball', 'World', 12}

    @pytest.mark.parametrize(['value', 'result'], [(3, True), ('Alex', True), (5, False)])
    def test_check_membership(self, value, result):
        assert result == (value in self.my_set)

    def test_difference(self):
        another_set = {3, 5, 'Alex', 1, 'World'}
        assert {'Ball', 12} == self.my_set - another_set

    def test_intersection(self):
        another_set = {3, 5, 'Alex', 1, 'World'}
        assert {3, 'Alex', 1, 'World'} == self.my_set & another_set

    def test_pop(self):
        value = self.my_set.pop()
        assert value not in self.my_set

    def test_union(self):
        another_set = {3, 5, 'Alex', 1, 'World'}
        assert {1, 5, 'Alex', 3, 'Ball', 'World', 12} == self.my_set | another_set
