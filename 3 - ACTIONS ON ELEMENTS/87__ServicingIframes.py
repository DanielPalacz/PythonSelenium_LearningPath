from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")
driver.maximize_window()

# 86__SwitchingToNewlyOpenedWebbrowserWindow
driver.find_element_by_id("newPage").click()
# next, to check where / on which page we are:
print(driver.title)
# ok - we are here in the parent page

# checking what is our current window name
parent_windows_name = driver.current_window_handle
# get all window names available for teh Webdriver
window_names = driver.window_handles

for window in window_names:
    if window != parent_windows_name:
        child_window = window
        driver.switch_to.window(window)
        break

print(driver.title)
# ok - we are here in the child page

#######################################################################################################################
#
# handling 'Initial Google disclaimer' - "Zanim przejdziesz dalej"
#
child_windows = driver.window_handles
print("Parent Window \t\t\t - " + parent_windows_name)
print("Child Window \t\t\t - " + child_window)
print("Available Windows\t\t - " + str(child_windows))
print("Current Window  \t\t - " + driver.current_window_handle)
print("----------------------------------------------------------")

# print(driver.find_element_by_xpath("//span/span.RveJvd.snByac"))
# print(driver.find_elements_by_xpath("//div/span/span"))
# html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span


print("Current page title is: ", driver.title)
print("Switching to iframe ...")
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
print("And current page title is: ", driver.find_element_by_tag_name("h1").text)
print("Available Windows\t\t - " + str(driver.window_handles))
# to switch back to Child www:
# ---> driver.switch_to.default_content()
# ---> driver.close()

print("----------------------------------------------------------")
driver.find_element_by_xpath("//span/span[text()='Zgadzam się']").click()

time.sleep(1)
driver.quit()
