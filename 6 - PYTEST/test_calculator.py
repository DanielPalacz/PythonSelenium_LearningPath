import pytest
from calculator import Calculator
# conda env create -f py_venv.yml


@pytest.fixture
def my_calculator():
    '''Returns a Calculator session'''
    return Calculator()

@pytest.mark.dependency()
def test_setting_initial_number1(my_calculator):
    assert my_calculator.value == 1, "Initial value is not expected Zero value"


@pytest.mark.skip()
@pytest.mark.dependency(depends=["test_setting_initial_number1"])
def test_setting_initial_number2(my_calculator):
    assert my_calculator.value == None, "Initial value is not expected Zero value"


@pytest.mark.dependency()
@pytest.mark.parametrize("a, b, expected",
                         [
                             (10, 10, 20),
                             #(20, -2, 18)
                         ])
def test_adding_two_numbers(my_calculator, a, b, expected):
    my_calculator.add_two_numbers(a,b)
    assert my_calculator.value == expected, "Incorrect result"


