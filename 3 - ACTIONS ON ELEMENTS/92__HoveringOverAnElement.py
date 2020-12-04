from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get("https://www.w3schools.com")
driver.maximize_window()
time.sleep(2)
# Accept cookies
driver.find_element_by_xpath("/html/body/div[9]/div/div/div/div[3]/div[2]/div[2][@id='accept-choices']").click()

# there is TUTORIALS Drop-Down menu on https://www.w3schools.com/ (id="navbtn_tutorials")
tutorials_webelement = driver.find_element_by_id("navbtn_tutorials")
time.sleep(3)
#
# hovering TUTORIALS Drop-Down
webdriver.ActionChains(driver).move_to_element(tutorials_webelement).perform()
time.sleep(2)
exercises_webelement = driver.find_element_by_id("navbtn_exercises")
webdriver.ActionChains(driver).move_to_element(exercises_webelement).perform()
