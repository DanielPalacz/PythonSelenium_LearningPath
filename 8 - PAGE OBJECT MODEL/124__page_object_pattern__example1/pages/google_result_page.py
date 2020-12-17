
class GoogleResultPage:

    def __init__(self, webdriver):
        self.driver = webdriver
        self.search_results_xpath = "//h3[@class='LC20lb DKV0Md']"

    def open_first_result(self):
        self.driver.find_elements_by_xpath(self.search_results_xpath)[0].click()
