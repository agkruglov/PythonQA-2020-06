import requests
import json
import jsonschema


class TestDogApi:

    def setup_class(self):
	self.url = 'https://dog.ceo/api'

    def test_list_all_breeds(self):
        response = requests.get(
	pass

    def test_random_image(self):
	pass

    def test_images_by_breed(self):
	pass

    def test_list_sub_breeds(self):
	pass

    def test_random_image_by_breed(self):
	pass
