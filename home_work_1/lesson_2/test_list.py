import pytest


class TestList:

    def setup_method(self):
        self.my_list = [1, 'Alex', 55.567, 'Alex', ('Gregory', 25)]

    def test_append(self):
        self.my_list.append(5)
        assert [1, 'Alex', 55.567, 'Alex', ('Gregory', 25), 5] == self.my_list

    def test_count(self):
        assert 2 == self.my_list.count('Alex')

    def test_remove(self):
        self.my_list.remove('Alex')
        assert [1, 55.567, 'Alex', ('Gregory', 25)] == self.my_list

    def test_reverse(self):
        self.my_list.reverse()
        assert [('Gregory', 25), 'Alex', 55.567, 'Alex', 1] == self.my_list

    @pytest.mark.parametrize(['index', 'value'], [(-1, ('Gregory', 25)), (0, 1), (1, 'Alex')])
    def test_get_by_index(self, index, value):
        assert value == self.my_list[index]
