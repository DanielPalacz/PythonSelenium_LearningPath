from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


# chromedriver file directly attached to the script

driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")
driver.maximize_window()

driver.find_element_by_id("clickOnMe").click()
driver.switch_to.alert.accept()

# here, the alert will appear
# an exception will happen if it is not handled
driver.switch_to.alert.accept()

driver.find_element_by_id("clickOnMe").click()
driver.switch_to.alert.dismiss()

# how to provide values to text field
driver.find_element_by_id("fname").send_keys("John123")

# how to simulate Enter Clicking
driver.find_element_by_name("password").send_keys(Keys.ENTER)
