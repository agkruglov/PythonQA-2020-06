import json

import jsonschema
import requests


class TestDogApi:

    def setup_class(self):
        self.url = 'https://dog.ceo/api'

    def test_list_all_breeds(self):
        response = requests.get(self.url + '/breeds/list/all')

        assert response.status_code == 200

        with open('./data/schema_list_all_breeds.json', 'r') as f:
            schema = json.load(f)
        jsonschema.validate(response.json(), schema)

        assert response.json()['status'] == 'success'

    def test_random_image(self):
        response = requests.get(self.url + '/breeds/image/random')

        assert response.status_code == 200

        content = response.json()

        with open('./data/schema_random_image.json', 'r') as f:
            schema = json.load(f)
        jsonschema.validate(content, schema)

        assert content['status'] == 'success'

    def test_images_by_breed(self):
        pass

    def test_list_sub_breeds(self):
        pass

    def test_random_image_by_breed(self):
        pass
