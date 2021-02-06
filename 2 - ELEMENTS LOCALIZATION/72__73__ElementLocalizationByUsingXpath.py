from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# chromedriver fizycznie dołączony do projektu
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")
driver.get(r"D:\SeleniumPythonCourse\Test.html")


# CSS Selectors one of the most powerful technics for localization objects on Page (just after XPath)
driver.find_element_by_css_selector("a")
driver.find_element_by_css_selector("img#smileImage")
driver.find_element_by_css_selector("p.topSecret")
driver.find_element_by_css_selector("p.topSecret")
print(driver.find_element_by_css_selector("th:first-child").text)


# how to localize elements on the page by using XPath

# - absolute path:
# --- /html/body/table/tr/th

# - relative path
# --- //table/tr/th
# ---//th

# the below XPath selector will find: element 'th' for which text = 'Month'
# //th[text()='Month']

# the below XPath selector will find: all 'input' elements attribute 'name' (or id) = fname
# //input[@name='fname']
# //input[@id='fname']

# to go to parent-element we use '..'
# //input[@id='fname']/..

# following sibling
# //input[@id='fname']/following-sibling::table

driver.find_elements_by_xpath("/html/body/table/tbody/tr/th")
driver.find_elements_by_xpath("//tbody/th")
driver.find_elements_by_xpath("//tbody/th")
driver.find_elements_by_xpath("//th")
driver.find_elements_by_xpath("//th[text()='Month']")
driver.find_elements_by_xpath("//button[@id='clickOnMe']")
driver.find_elements_by_xpath("//input[@name='fname']/following-sibling::table")
print(len(driver.find_elements_by_xpath("//th")))

driver.find_elements_by_xpath("//*[@id='idOfYourHiddenElement' and @type='hidden']")
driver.find_element_by_xpath("//input[@type='radio'][@value='other']").click()

# Combine the conditions within the [...]
# E.g., //div[@class='xxxx' and contains(text(), 'justin')].

# the above examples will find "THE FIRST ELEMENT"
# if all matching elements should be found then use: driver.find_elements_by_xpath()
