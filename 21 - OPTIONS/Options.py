from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time


chrome_options1 = Options()
chrome_options1.add_argument("--incognito")
chrome_options1.add_argument("--disable-gpu")
chrome_options1.add_argument("--window-size=1800,1200")

# more:
# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

# chrome_options1.add_argument("--auto-open-devtools-for-tabs")
# chrome_options1.add_argument("--headless")
# chrome_options1.add_experimental_option("excludeSwitches", extset)
# chrome_options1.add_experimental_option("useAutomationExtension", False)
# chrome_options1.add_experimental_option('mobileEmulation', mobile)
# chrome_options1.add_experimental_option("prefs", {ignore_image: 2})

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# d = DesiredCapabilities.CHROME
# d["loggingPrefs"] = {"browser": "ALL"}

driver = webdriver.Chrome(options=options, desired_capabilities=d)



def run_driver_check(x_options):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=x_options)
    time.sleep(2)
    www_address = "http://www.ringpolska.pl/"
    driver.get(www_address)
    #driver.maximize_window()
    decline_cookies_xpath = "/html/body/div[2]/div[1]/a[1][text()='Odrzuć wszystkie cookies']"
    time.sleep(1)
    driver.find_element_by_xpath(decline_cookies_xpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(decline_cookies_xpath).click()

    driver.quit()


run_driver_check(chrome_options1)
