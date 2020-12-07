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

# Selenium doesnt provide a method for checking if element exist
# use 'elements'-like find methods for this
searched_element_list = driver.find_elements_by_tag_name("p11")

if not len(searched_element_list):
    print("There is no such element.")

try:
    driver.find_element_by_tag_name("p111")
except NoSuchElementException:
    print("There is no such element.")
