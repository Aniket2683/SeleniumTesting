# fixture is referred to the setup that is to be done before and after the test case is executed

import pytest
@pytest.fixture()
def setup_and_teardown():
    print("Open browser")
    print("Open App url")
    yield
    print("Logout from App")
    print("Close Browser")

def test_LoginWithValidCred(setup_and_teardown):
    print("Testing test_LoginWithValidCred")

def test_LoginWithValidEmail(setup_and_teardown):
    print("Testing test_LoginWithValidEmail")