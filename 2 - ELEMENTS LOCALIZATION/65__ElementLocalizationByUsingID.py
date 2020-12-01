from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# chromedriver fizycznie dołączony do projektu
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")

# Two ways how you can localize the element by ID:

# 1 way

element_name = "fname123"
try:
    driver.find_element(By.ID, element_name)
except NoSuchElementException as e:
    print(f"There is no {element_name}.\nException content: \n" + str(e))

# 2 way
# driver.find_element_by_id(element_name)

driver.quit()
