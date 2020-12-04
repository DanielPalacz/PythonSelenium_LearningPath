from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
driver.maximize_window()
time.sleep(2)
# Accept cookies
driver.find_element_by_id("onetrust-accept-btn-handler").click()
time.sleep(2)
#
draggable = driver.find_element_by_id("draggable")
drop_target = driver.find_element_by_id("droptarget")
#
webdriver.ActionChains(driver).drag_and_drop(draggable, drop_target).perform()
