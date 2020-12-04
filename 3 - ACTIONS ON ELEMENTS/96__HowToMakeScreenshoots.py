from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import os

# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\FileUpload.html")
driver.maximize_window()
time.sleep(2)

# our element:
# <input type="file" id="myFile">
choose_file = driver.find_element_by_id("myFile")
#
# Uploading files is surprisingly easy:
driver.save_screenshot("screenshoots/before_upload.png")
file_path = os.path.abspath("uploadMe.txt")
choose_file.send_keys(file_path)

#
# How to make screenshoots?
#
driver.save_screenshot("screenshoots/after_upload.png")
time.sleep(1)
driver.quit()
