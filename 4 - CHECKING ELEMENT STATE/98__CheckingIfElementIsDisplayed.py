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

driver.get(r"C:\SeleniumPythonCourse\Test.html")
driver.maximize_window()

# for text input field - how to check if it is enabled
# if the field is disabled then input is not possible
# <input disabled type="text" name="fname" id="fname">

checked_element = driver.find_element_by_tag_name("p")

if checked_element.is_displayed():
    print("IS DISPLAYED")
    print(checked_element.text)
    # driver.save_screenshot("test.png")
    time.sleep(1)
else:
    print("This element is hidden.")
    print(checked_element.get_attribute("textContent"))
# driver.quit()
