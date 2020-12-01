from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# chromedriver fizycznie dołączony do projektu
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")


# how to locate elements on the page by using Class name:
# <p hidden="" class="topSecret">This paragraph should be hidden.</p>
class_name = "topSecret"
# 1 way
driver.find_element_by_class_name(class_name)

# class atribute can have more than 1 parameters
# <p hidden="" class="topSecret second_class third_class fourth_class ">This paragraph should be hidden.</p>
