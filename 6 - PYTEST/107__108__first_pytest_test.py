import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


def test_method():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 2, but was " + str(x+y)


