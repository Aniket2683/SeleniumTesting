# refactor the filename ,starting with test_,to run the code
import pytest


@pytest.mark.smoke
def test_sample_one():
    print("Inside sample one")

@pytest.mark.regression
def test_sample_two():
    print("Inside sample two")
    assert False

@pytest.mark.regression
def test_sample_three():
    print("Inside sample three")


# Flags
# --help or -h  : Info about all flags
#  -v : Verbose (gives more info about the output)
#  -rA : Get the output details as well
#  -k : k stands for Keyword (it will help you to run only a specific testcase)

#  We can use regular expressions to run moe than one test case
#  -k"one or two"
#  -k"not one"