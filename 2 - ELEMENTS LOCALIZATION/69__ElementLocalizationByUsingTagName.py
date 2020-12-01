from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# chromedriver fizycznie dołączony do projektu
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")


# how to locate elements on the page by Tag name:
# examples of Tags in html pages:
# -- tag a (links)
# -- table
# -- select
# -- p (paragraphs)
# -- img
# -- label

driver.find_element_by_tag_name("a")
driver.find_element_by_tag_name("div")
