import pytest


class TestString:

    def setup_method(self):
        self.my_str = 'Alex Kruglov'

    def test_center(self):
        assert '----Alex Kruglov----' == self.my_str.center(20, '-')

    @pytest.mark.parametrize(['value', 'result'], [('ov', True), ('av', False), (' Kruglov', True)])
    def test_endswith(self, value, result):
        assert result == self.my_str.endswith(value)

    def test_isalpha(self):
        assert not self.my_str.isalpha()

    def test_split(self):
        assert ['Alex', 'Kruglov'] == self.my_str.split()

    def test_swap_case(self):
        assert 'aLEX kRUGLOV' == self.my_str.swapcase()
