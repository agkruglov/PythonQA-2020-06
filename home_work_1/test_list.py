import pytest


class TestList:

    def test_append(self):
        my_list = [1, 'Alex', 55.567, 'Alex']
        my_list.append(('Gregory', 25))
        assert [1, 'Alex', 55.567, 'Alex', ('Gregory', 25)] == my_list

    def test_count(self):
        my_list = [1, 'Alex', 55.567, 'Alex', ('Gregory', 25)]
        assert 2 == my_list.count('Alex')

    def test_remove(self):
        my_list = [1, 'Alex', 55.567, 'Alex', ('Gregory', 25)]
        my_list.remove('Alex')
        assert [1, 55.567, 'Alex', ('Gregory', 25)] == my_list

    def test_reverse(self):
        my_list = [1, 'Alex', 55.567, ('Gregory', 25)]
        my_list.reverse()
        assert [('Gregory', 25), 55.567, 'Alex', 1] == my_list

    def test_zfill(self):
        pass
