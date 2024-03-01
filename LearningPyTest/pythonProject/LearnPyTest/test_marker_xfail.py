# markers Expected fail and Expected pass , xfail is an  inbuilt in pytest for it
import pytest


@pytest.mark.xfail
def test_func1():
    assert 2 == 2
    print("Expected to Pass")


def test_func_pass():
    print("It will pass")


@pytest.mark.xfail
def test_func2():
    print("Expected to Fail")
    assert 5 > 7


def test_func_fail():
    print("It wil be failed")
    assert False
