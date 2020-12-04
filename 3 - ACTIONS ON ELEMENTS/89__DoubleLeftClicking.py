from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\DoubleClick.html")
driver.maximize_window()

# For double clicking you need to use special class: 'ActionChains'
button = driver.find_element_by_id("bottom")
webdriver.ActionChains(driver).double_click(button).perform()
