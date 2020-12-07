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

# this is linked to every element in the script
driver.implicitly_wait(10)
driver.get(r"D:\SeleniumPythonCourse\Waits2.html")
driver.maximize_window()
#
# if there are no elements then script will wait 10s defined in implicitly_wait
# implicitly_wait is linked to every element
driver.find_element_by_id("clickOnMe").click()
print("Here, now.")
print(driver.find_element_by_tag_name("p").text)
