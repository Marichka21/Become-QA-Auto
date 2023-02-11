import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()

    assert body['name'] =="Chris Wanth"
    assert r.status_code == 200
    print(f"Response Headers is {r.headers}")

