import pytest


@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Open browser")
    print("Open App url")
    yield
    print("Logout from App")
    print("Close Browser")
