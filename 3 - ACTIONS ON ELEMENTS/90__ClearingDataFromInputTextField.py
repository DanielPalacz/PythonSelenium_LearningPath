from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")
driver.maximize_window()

#
# How to execute JavaScript code by using Selenium?
# examples - by using JavaScript code:
# 1 - we will click on the element
# 2 - we will set value to text field
# Ad.1)
driver.execute_script("arguments[0].click();", driver.find_element_by_id("newPage"))
# Ad.2)
a1 = "text123"
driver.execute_script("arguments[0].setAttribute('value', '" + a1 + "');", driver.find_element_by_id("fname"))

# Selenium click(), sendKeys methods in some websites may not work --- then is must to use JS code

#
# Method clear()
username_input = driver.find_element_by_name("username")
username_input.clear()
username_input.send_keys("___LaLaLa")
