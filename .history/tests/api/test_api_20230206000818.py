class User:
    
    def __init__(self) -> None:
        self.name = 'Sergii'
        self.second_name = 'Butenko'


user = User()

def test_remove_name():
    user.name = 