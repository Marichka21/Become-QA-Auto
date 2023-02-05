class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None


def test_name(user):
    assert user.name == 'Sergii'


def test_second_name(user):
    assert user.second_name == 'Butenko'