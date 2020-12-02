from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# chromedriver fizycznie dołączony do projektu
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")


# CSS Selectors one of the most powerful technics for localization objects on Page (just after XPath)

# it will find the first elemenet with tag 'a'
driver.find_element_by_css_selector("a")

# it will find the first element with tag 'img' with id = 'smileImage':
driver.find_element_by_css_selector("img#smileImage")

# it will find the first element with tag 'p' with class = 'topSecret':
driver.find_element_by_css_selector("p.topSecret")

# the below technic will find the first tag 'th' that is the first child of parent-tag
print(driver.find_element_by_css_selector("th:first-child").text)


# if all matching elements should be found then use: driver.find_elements_by_css_selector()
