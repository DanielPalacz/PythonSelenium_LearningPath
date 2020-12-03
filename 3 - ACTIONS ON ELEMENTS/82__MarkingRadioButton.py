from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# chromedriver file directly attached to the script
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")
driver.maximize_window()

driver.find_element_by_id("clickOnMe").click()

# here, the alert will appear
# an exception will happen if it is not handled
driver.switch_to.alert.accept()

driver.find_element_by_id("clickOnMe").click()
driver.switch_to.alert.dismiss()

# how to provide values to text field
driver.find_element_by_id("fname").send_keys("John123")

# how to simulate Enter Clicking (it creates alert)
# driver.find_element_by_name("password").send_keys(Keys.ENTER)


# how to choose option from Select by using text / index / value:
auto_select = Select(driver.find_element_by_tag_name("select"))
# driver.find_element_by_tag_name("select") -- WebElement
auto_select.select_by_visible_text("Volvo")
auto_select.select_by_value("saab")
auto_select.select_by_index(2)  # --> Mercedes

# how to mark checkbox on page
driver.find_element_by_xpath("//input[@type='checkbox']").click()

# how to mark Radiobox on the page
driver.find_element_by_xpath("//input[@type='radio'][@value='other']").click()
