import pytest


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Sergii'
        self.second_name = 'Butenko'

    def remove(self):
        self.name = ''
        self.second_name = ''


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