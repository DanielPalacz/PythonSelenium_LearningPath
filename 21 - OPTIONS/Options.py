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


# chrome_options.add_argument("--lang=pl")

# chrome_options1.add_argument("--auto-open-devtools-for-tabs")
######################################################################################################################
#
# chrome_options1.add_argument("--headless")
######################################################################################################################
# chrome_options1.add_experimental_option("excludeSwitches", extset)
# chrome_options1.add_experimental_option("useAutomationExtension", False)
# chrome_options1.add_experimental_option('mobileEmulation', mobile)
# chrome_options1.add_experimental_option("prefs", {ignore_image: 2})

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# d = DesiredCapabilities.CHROME
# d["loggingPrefs"] = {"browser": "ALL"}

# driver = webdriver.Chrome(options=options, desired_capabilities=d)


# "preferences are not supported in headless mode ?
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)


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
    time.sleep(2)
    driver.execute_script("document.body.style.zoom='350%'")
    time.sleep(2)

    driver.quit()


# run_driver_check(chrome_options1)


#
# Other Options-arguments:
#
# chrome_options1.add_argument("--start-maximized")
# chrome_options1.add_argument("--ignore-certificate-errors")   --- ignore SSL certifications

#
# below userAgent concept allows simulation of "other-country behaviour"
#
# ua = UserAgent()
# userAgent = ua.random
# options.add_argument(f"user-agent={userAgent}")