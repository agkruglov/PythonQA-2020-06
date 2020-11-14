import pytest

from core.rest import get_obj_from_uri, check_json_schema


class TestOpenBreweryDb:

    def setup_class(self):
        self.api_uri = 'https://api.openbrewerydb.org/breweries'

    def test_breweries_list(self):
        status, content = get_obj_from_uri(self.api_uri)
        assert status == 200

        assert check_json_schema(content, 'data/service_2/schema_breweries_list.json')

        assert len(content) == 20

    @pytest.mark.parametrize(('per_page', 'breweries_num'), [('', 20), ('0', 0), ('test', 20), ('1', 1), ('49', 49),
                                                             ('50', 50), ('51', 50)])
    def test_breweries_per_page(self, per_page, breweries_num):
        status, content = get_obj_from_uri(self.api_uri, params={'per_page': per_page})
        assert status == 200

        assert check_json_schema(content, 'data/service_2/schema_breweries_list.json')

        assert len(content) == breweries_num

    def test_breweries_sorting(self):
        # Простейшая проверка сортировки пивоварен по id
        status, content = get_obj_from_uri(self.api_uri, params={'per_page': 50, 'sort': 'id'})
        assert status == 200

        for i in range(len(content) - 1):
            assert content[i + 1]['id'] > content[i]['id']

    @pytest.mark.parametrize(('brewery_id', 'status_code'), [('0', 404), ('test', 404), ('1', 200)])
    def test_brewery_by_id(self, brewery_id, status_code):
        status, content = get_obj_from_uri(self.api_uri + '/' + brewery_id)
        assert status == status_code

        if status == 200:
            assert check_json_schema(content, 'data/service_2/schema_brewery.json')
        elif status == 404:
            assert content['message'] == 'Couldn\'t find Brewery with \'id\'={}'.format(brewery_id)

    @pytest.mark.parametrize(('query', 'length'), [('', 0), ('dog', 15)])
    def test_breweries_autocomlete(self, query, length):
        status, content = get_obj_from_uri(self.api_uri + '/autocomplete', {'query': query})
        assert status == 200

        assert check_json_schema(content, 'data/service_2/schema_breweries_autocomlete.json')

        assert len(content) == length
