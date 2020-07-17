import pytest


class TestDictionary:

    def setup_method(self):
        self.my_dict = dict([('name', 'Alex'),
                             ('surname', 'Kruglov'),
                             ('age', 42), ('birth', {'place': 'Moscow', 'date': '23.10.1977'})])

    def test_del(self):
        del self.my_dict['name']
        assert 'name' not in self.my_dict

    def test_get(self):
        assert 'Kruglov' == self.my_dict.get('surname', '')

    @pytest.mark.parametrize(['key', 'result'], [('name', True), ('age', True), ('marital status', False)])
    def test_key_in_dict(self, key, result):
        assert result == (key in self.my_dict)

    def test_pop(self):
        value = self.my_dict.pop('name')
        assert value == 'Alex' and 'name' not in self.my_dict

    def test_update(self):
        self.my_dict.update({'age': 43})
        assert 43 == self.my_dict['age']
