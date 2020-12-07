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
# Option 1 - 105)
# Below method until should take as parameter other method (which returns False if New condition is not Passed)
# -- in the example this method will be lambda
# -- web_driver = driver (web_driver is local variable in lambda namespace)
wait.until(lambda web_driver: len(web_driver.find_elements_by_tag_name("p")) == 1)
print(driver.find_element_by_tag_name("p").text)
