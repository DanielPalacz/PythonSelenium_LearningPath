from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time

# chromedriver file directly attached to the script
try:
    driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
except WebDriverException:
    print("Driver could not be loaded from Phy location.")
    driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(r"C:\SeleniumPythonCourse\Test.html")
driver.maximize_window()

# How to check state of Checkbox element? (it is marked)
searched_element = driver.find_element_by_xpath("//input[@type='checkbox']")
#
time.sleep(1)
searched_element.click()
#
if searched_element.is_selected():
    print("Checkbox is selected, so we will untick it.")
    time.sleep(1)
    searched_element.click()
