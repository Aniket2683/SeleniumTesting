# the py file should also be named after test_filename.py, to run the code
# Methods starting with test_ will only be executed.
import pytest


@pytest.mark.smoke
def test_sample_one():
    print("Inside sample one")

# skip is an inbuilt method
@pytest.mark.skip
def sample_two():
    print("Inside sample two")
