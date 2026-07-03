import pytest

@pytest.fixture(scope="session")
def app_config():
    return {"api_url": "https://www.example.com", "timeout": 5}