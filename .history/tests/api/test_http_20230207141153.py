import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.')