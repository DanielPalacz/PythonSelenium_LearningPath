from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# chromedriver fizycznie dołączony do projektu
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")


# how to locate links to different pages ('tag a'), for example:
# <a href="https://www.w3schools.com">Visit W3Schools.com!</a>
link_text = "Visit W3Schools.com!"
partial_link_text = "Visit W3Schools"

# 1 way
driver.find_elements_by_link_text(link_text)
# 2 way
driver.find_element_by_partial_link_text(partial_link_text)
