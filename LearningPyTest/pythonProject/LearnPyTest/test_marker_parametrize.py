# parametrize markers are use to provide different parameters to the same test case, so that the test case can be resused.
import pytest


@pytest.mark.parametrize("username,password",[("aniket","123"),("arun","213"),("ajay","223")])
def test_samplefunc(username,password):
    print("Username :"+username)
    print("Password :"+password)
