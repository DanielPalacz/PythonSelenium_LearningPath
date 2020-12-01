from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# chromedriver fizycznie dołączony do projektu
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")


# CSS Selectors one of the most powerful technics for localization objects on Page (just after XPath)
driver.find_element_by_css_selector("a")
driver.find_element_by_css_selector("img#smileImage")
driver.find_element_by_css_selector("p.topSecret")
driver.find_element_by_css_selector("p.topSecret")
print(driver.find_element_by_css_selector("th:first-child").text)
