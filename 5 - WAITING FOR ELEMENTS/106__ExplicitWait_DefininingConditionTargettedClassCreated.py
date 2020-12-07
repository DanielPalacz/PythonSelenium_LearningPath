from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

# chromedriver file directly attached to the script
try:
    driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
except WebDriverException:
    print("Driver could not be loaded from Phy location.")
    driver = webdriver.Chrome(ChromeDriverManager().install())

# ExplicitWait object is based on WebDriverWait - it allows for defining specific condition for which we wait
# WebDriverWait(driver, timeout, freq, IgnoredException)
wait = WebDriverWait(driver, 10, 0.5, NoSuchElementException)

driver.get(r"D:\SeleniumPythonCourse\Waits2.html")
driver.maximize_window()
driver.find_element_by_id("clickOnMe").click()
print("Clicked: ", time.time())

#
# Defining specific condition for Wait if predefinied conditions from 'expected_conditions' are not enough for us.
#
# Option 2 - 106)
# New class with special '__call__' method:
# --- with driver as parameter
# --- and with condition inside body of __call__ method


class WaitForListSize:

    def __init__(self, element_name, expected_number_of_elements):
        self.located_element = element_name
        self.expected_size = expected_number_of_elements

    def __call__(self, driver):
        return len(driver.find_elements_by_xpath(self.located_element)) == self.expected_size


# Then to use our class / (__call__ method) -- we are passing object newly created class WaitForListSize
wait.until(WaitForListSize("//p", 1))
print("Printed: ", time.time())
print(driver.find_element_by_tag_name("p").text)
