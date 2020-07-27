import json

import jsonschema
import pytest
import requests


class TestDogApi:

    def setup_class(self):
        self.url = 'https://dog.ceo/api'

    def test_list_all_breeds(self):
        response = requests.get(self.url + '/breeds/list/all')

        assert response.status_code == 200

        with open('data/service_1/schema_list_all_breeds.json', 'r') as f:
            schema = json.load(f)
        jsonschema.validate(response.json(), schema)

    def test_random_image(self):
        response = requests.get(self.url + '/breeds/image/random')

        assert response.status_code == 200

        content = response.json()

        with open('data/service_1/schema_random_image.json', 'r') as f:
            schema = json.load(f)
        jsonschema.validate(content, schema)

    def test_images_by_breed(self):
        response = requests.get(self.url + '/breed/hound/images')

        assert response.status_code == 200

    def test_list_sub_breeds(self):
        response = requests.get(self.url + '/breed/hound/list')

        assert response.status_code == 200

    @pytest.mark.parametrize(('breed', 'status_code'), [('', 404), ('terrier', 200), ('овчарка', 404)])
    def test_random_image_by_breed(self, breed, status_code):
        response = requests.get(self.url + '/breed/{}/images/random'.format(breed))

        assert response.status_code == status_code
