from selenium import webdriver
import pathmagic  # noqa Pep8 uncheck
from pages.google_home_page import GoogleHomePage
from pages.google_result_page import GoogleResultPage
# E   ImportError: attempted relative import with no known parent package
# here was question howTo manage PYTHON PATH aspect
# introduced workaround: "import pathmagic  # noqa Pep8 uncheck"

import pytest
from webdriver_manager.chrome import ChromeDriverManager


class TestGoogleSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.find_element_by_xpath("//span/span[text()='Zgadzam się']").click()
        yield
        self.driver.quit()

    def test_google_search(self, setup):
        home_page = GoogleHomePage(self.driver)
        home_page.search_in_google("Selenium")
        result_page = GoogleResultPage(self.driver)
        result_page.open_first_result()
        assert self.driver.title == "SeleniumHQ Browser Automation"

