import requests


class GitHub:

    def get_user_defunkt():
        r = requests.get('https://api.github.com/users/defunkt')
        body = str(r.json()).encode('utf-8')

        return body