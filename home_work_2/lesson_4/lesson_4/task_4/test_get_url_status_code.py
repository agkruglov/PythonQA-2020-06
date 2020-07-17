import requests


def test_get_url_status_code(get_options):
    url, status_code = get_options
    response = requests.get(url)
    assert status_code == response.status_code
