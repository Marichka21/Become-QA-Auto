


def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()