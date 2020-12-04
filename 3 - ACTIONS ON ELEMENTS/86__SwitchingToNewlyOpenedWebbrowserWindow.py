from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


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
print("----------------------------------------------------------")
print("Parent Window \t\t\t\t\t - " + parent_windows_name)
print("Child Window \t\t\t\t\t - " + child_window)
print("Available Windows\t - " + str(child_windows))
print("Current Window  \t\t\t\t - " + driver.current_window_handle)
print("----------------------------------------------------------")

# quitting from both parent and child windows
#driver.quit()
#print("Quitted with success from both: parent and child windows.")
