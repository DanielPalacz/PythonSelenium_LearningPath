from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
<<<<<<< HEAD
import time

# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")
=======
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
>>>>>>> dd084932f7d39cf7f45ded0a8fb90aee3439ccf7
driver.maximize_window()

# for text input field - how to check if it is enabled
# if the field is disabled then input is not possible
# <input disabled type="text" name="fname" id="fname">

first_name_input = driver.find_element_by_name("fname")

if first_name_input.is_enabled():
    print("IS ENABLED")
    first_name_input.send_keys("John")
    # driver.save_screenshot("JohnScreenshoot.png")
    time.sleep(1)
else:
    print("DISABLED")

# driver.quit()
