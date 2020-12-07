from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

# chromedriver file directly attached to the script
try:
    driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
except WebDriverException:
    print("Driver could not be loaded from Phy location.")
    driver = webdriver.Chrome(ChromeDriverManager().install())

# ExplicitWait object is based on WebDriverWait - it allows for defining specific condition for which we wait
# WebDriverWait(driver, timeout, freq, IgnoredException)
wait = WebDriverWait(driver, 10, 0.5, NoSuchElementException)

driver.get(r"D:\SeleniumPythonCourse\Waits2.html")
driver.maximize_window()
driver.find_element_by_id("clickOnMe").click()
print("Clicked: ", time.time())
#
# to use previously defined ExplicitWait:
# here in method until we provide condition (importing expected_conditions module)
#
# expected_conditions - provides lot of predefinied conditions
# ----> however we can define also conditions by ourself
#
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "p")))
print(driver.find_element_by_tag_name("p").text)
print("Printed: ", time.time())

lista = [el for el in range(10) if el % 2 == 0]
print(lista)
