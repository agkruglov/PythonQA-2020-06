import pytest

from core.rest import *


class TestJsonPlaceholder:

    def setup_class(self):
        self.api_uri = 'https://jsonplaceholder.typicode.com'
        self.data_path = 'data/service_3'

    @pytest.mark.parametrize(('uri', 'quantity', 'schema'), [('posts', 100, 'schema_posts.json'),
                                                             ('users', 10, 'schema_users.json'),
                                                             ('comments', 500, 'schema_comments.json'),
                                                             ('albums', 100, 'schema_albums.json'),
                                                             ('photos', 5000, 'schema_photos.json'),
                                                             ('todos', 200, 'schema_todos.json')])
    def test_get_resources(self, uri, quantity, schema):
        status, content = get_obj_from_uri(self.api_uri + '/' + uri)
        assert status == 200

        assert check_json_schema(content, self.data_path + '/' + schema)

        assert len(content) == quantity

    @pytest.mark.parametrize(('user_id', 'status_code'), [('0', 404), ('1', 200), ('10', 200), ('11', 404),
                                                          ('test', 404)])
    def test_get_user_by_id(self, user_id, status_code):
        status, content = get_obj_from_uri(self.api_uri + '/users/' + user_id)
        assert status == status_code

        if status == 200:
            assert check_json_schema(content, self.data_path + '/schema_user.json')

    def test_user_create(self):
        with open(self.data_path + '/template_user.json', 'r') as f:
            body = json.load(f)

        status, content = post_obj_from_uri(self.api_uri + '/users', body)
        assert status == 201

    def test_user_patch(self):
        user_name = 'Alexandr Kruglov'
        status, content = patch_obj_from_uri(self.api_uri + '/users/5', {'name': user_name})
        assert status == 200

        assert check_json_schema(content, self.data_path + '/schema_user.json')

        assert content['id'] == 5 and content['name'] == user_name

    def test_user_delete(self):
        status, content = delete_obj_from_uri(self.api_uri + '/users/5')
        assert status == 200
