# refactor the filename ,starting with test_,to run the code
# assertion messages are only printed if the assertion fails
import pytest

@pytest.mark.smoke
def test_assert1():
    a=5
    b=10
    assert a == b,"a is not equal to b"


def test_assert2():
    a=5
    b=7
    assert a<b

@pytest.mark.regression
def test_assert3():
    a="Aniket"
    b="Jaiswal"
    assert a.__eq__(b),"Aniket is not equal to Jaiswal"

