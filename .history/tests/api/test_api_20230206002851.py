import pytest


class User:

    def __init__(self) -> None:
        self.name = 'Sergii'
        self.second_name = 'Butenko'


@pytest.fixture
def user():
    yield User()


def test_change_name():
    user = User()
    user.create()
    
    assert user.name == 'Sergii'
    user.remove()

def test_change_second_name():
    user = User()
    user.create()
    
    assert user.second_name == 'Butenko'
    user.remove()
