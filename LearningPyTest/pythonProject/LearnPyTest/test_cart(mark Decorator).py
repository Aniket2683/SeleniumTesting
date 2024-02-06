import pytest


def testlogin():
    print("Item Added Successfully!")


@pytest.mark.sanity
def testlogout():
    print("Item Removed!")

