import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f"Response body is {r.json().encode('utf-8')}")
    print(f"Response Status Code is {r.status_code}")
    print(f"Response Headers is {r.headers}")

