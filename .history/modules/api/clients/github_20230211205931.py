import requests


class GitHub

    def get_users_request():
    r  = requests.get('https://api.github.com/users/defunkt')
    body = r.json()