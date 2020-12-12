import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.mark.skip
def test_method1():
    x = 5
    y = 2
    assert x + y == 2, "Assertion failed, Expected 2, but was " + str(x+y)


@pytest.mark.skip
def test_method2():
    x = 5
    y = 2
    assert x + y == 2, "Assertion failed, Expected 2, but was " + str(x+y)


def test_method3():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7, but was " + str(x+y)


@pytest.mark.xfail
def test_method4():
    x = 5
    y = 2
    assert x + y == 2, "Assertion failed, Expected 2, but was " + str(x+y)


# skipping tests:
# @pytest.mark.skip

# marking tests as failing (known issues)
# @pytest.mark.xfail
