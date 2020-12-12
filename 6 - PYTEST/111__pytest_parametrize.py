import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# how to use pytest.mark.parametrize decorator for running test method with different parameter values?

# @pytest.mark.parametrize("name1,name21", [(name1_val1,arg_name2_val1),(name1_val2,arg_name2_val2)])
# -- first names of arguments
# -- later list with tuples of values for those arguments


@pytest.mark.parametrize("value1, value_sum", [(1, 3), (2, 6), (3, 8)])
def test_summing(value1, value_sum):
    # the given parameters from 'parametrize' decorator have to be dded to test method declaration
    assert value1 * 3 == value_sum, "Error, the results it should be " + str(value1 * 3) + " not " + str(value_sum)
