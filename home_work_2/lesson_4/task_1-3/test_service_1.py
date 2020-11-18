import pytest

from core.rest import get_obj_from_uri, check_json_schema


class TestDogApi:

    def setup_class(self):
        self.api_uri = 'https://dog.ceo/api'

    def test_list_all_breeds(self):
        status, content = get_obj_from_uri(self.api_uri + '/breeds/list/all')
        assert status == 200

        assert check_json_schema(content, 'data/service_1/schema_list_all_breeds.json')

    @pytest.mark.parametrize(('img_num_uri', 'img_num'), [('0', 1), ('1', 1), ('3', 3), ('49', 49), ('50', 50),
                                                          ('51', 50), ('test', 1)])
    def test_random_image(self, img_num_uri, img_num):
        status, content = get_obj_from_uri(self.api_uri + '/breeds/image/random' + '/' + img_num_uri)
        assert status == 200

        assert check_json_schema(content, 'data/service_1/schema_random_image.json')
        assert len(content['message']) == img_num

    def test_images_by_breed(self):
        status, content = get_obj_from_uri(self.api_uri + '/breed/hound/images')
        assert status == 200

        assert check_json_schema(content, 'data/service_1/schema_images_by_breed.json')

    def test_list_sub_breeds(self):
        status, content = get_obj_from_uri(self.api_uri + '/breed/hound/list')
        assert status == 200

    @pytest.mark.parametrize(('breed', 'status_code', 'message'),
                             [('', 404, 'No route found for \"GET /api/breed//images/random\" with code: 0'),
                              ('terrier', 200, ''),
                              ('овчарка', 404, 'Breed not found (master breed does not exist)')])
    def test_random_image_by_breed(self, breed, status_code, message):
        status, content = get_obj_from_uri(self.api_uri + '/breed/{}/images/random'.format(breed))
        assert status == status_code

        assert check_json_schema(content, 'data/service_1/schema_random_image_by_breed.json')

        if status == 404:
            assert content['message'] == message
