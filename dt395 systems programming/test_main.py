import pytest
import mock
import builtins
from main_program import analysis
from main_program import getint


# tests below
def main():
    test_getint()
    test_analysis1()


def test_getint():
    with mock.patch.object(builtins, 'input', lambda _: "2"):
        assert getint(
            "enter number of dice") == 2  # this uses assert funciton to test the getint function returns the correct value
    # the lines above use patch from the mock library this is used to simulate the inbuilt function input
    # for this example 2 is tested as the input for getinput
    with mock.patch.object(builtins, 'input', lambda _: "hello"):
        with mock.patch.object(builtins, 'input', lambda _: "0"):
            with mock.patch.object(builtins, 'input', lambda _: "-1"):
                with mock.patch.object(builtins, 'input', lambda _: "10"):
                    assert getint("enter number of rolls") == 10
    # these lines above simulate the users entering invalid inputs
    # first a string, then 0, then -1 and finally 10 which is then valid.


def test_analysis1():
    assert analysis([9, 10, 7, 2, 5, 5, 11, 7, 2, 7],
                    "") == "Mean:6.5\nMedian:7.0\nMode:[7]\nMaximum:11\nMinimum:2\nDeviation:3.06\n"
    assert analysis([12, 7, 10, 6, 14, 7, 9, 9, 5, 10, 9, 6],
                    "data") == "Mean:8.67\nMedian:9.0\nMode:[9]\nMaximum:14\nMinimum:5\nDeviation:2.64\n"


# this code above uses assert to test analysis function  passing thorugh a simulate list of dice roll values
# the code then checks the function outputs the correct string in correct format based on this simulated list
# the funciton is tested twice with 2 different lists

if __name__ == "__main__":
    main()
