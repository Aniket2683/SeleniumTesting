# Hooks are used to do the exactly same function as that of Fixture function
# setup_function(function): After every Function
# teardown_function(function): After every Function
# setup_module(module): Run only once
# teardown_module(module): Run only once

# Note :Do not chmage the name of the functions or else it wont work.

def setup_function(function):
    print("Launch App")


def teardown_function(function):
    print("Close App")


def test_one():
    print("Test One")


def test_two():
    print("Test two")


def test_three():
    print("Test three")


def test_four():
    print("Test four")