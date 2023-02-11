import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists():
    api = GitHub
