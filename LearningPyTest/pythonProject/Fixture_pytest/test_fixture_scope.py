# import pytest
#
#
# @pytest.fixture(autouse=True,scope = "-----anything-----")
# def setup_and_teardown():
#     print("Open browser")
#     print("Open App url")
#     yield
#     print("Logout from App")
#     print("Close Browser")


#------anything------
# function : (By default)Works on function level. The fixture code runs after every test function.
# session : The fixture code run only once ,and then all testCases are executed.
# class :
# package:
# model: