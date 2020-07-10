import pytest


class TestSet:

    def test_eliminate_duplication(self):
        pass

    def test_check_membership(self):
        pass

    def test_difference(self):
        pass

    @pytest.mark.parametrize('params', [({1, 2}, {2, 3}, {2}), ([])])
    def test_intersection(self, params):
        assert params[0] & params[1] == params[2]
        pass

    def test_union(self):
        pass
