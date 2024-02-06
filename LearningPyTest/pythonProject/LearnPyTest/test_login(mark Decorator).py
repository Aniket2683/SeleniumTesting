import pytest


def testlogin():
    print("Login Successful!")

def testlogout():
    print("Logged Out!")


@pytest.mark.smoke
def testCalculate():
    assert 2 + 3 == 6