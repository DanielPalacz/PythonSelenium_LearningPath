import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# pytest.fixture decorator allows to execute "some code" before and after test method
#
# we will create fixture method for creating www instance at the beginning, before test method and closing after


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(r"D:\SeleniumPythonCourse\Test.html")
    driver.maximize_window()
    #
    # above code will be executed before test method
    # below code will be executed after test method
    yield
    driver.quit()


@pytest.mark.skipif
def test_method(test_setup):
    assert driver.title == "Strona testowa", "Assertion failed"


def test_method2(test_setup):
    assert driver.title == "Strona testowa", "Assertion failed"
