
class GoogleHomePage:

    def __init__(self, webdriver):
        self.driver = webdriver
        self.search_input_name = "q"
        self.search_button_name = "btnK"

    def search_in_google(self, text):
        self.driver.find_element_by_name(self.search_input_name).send_keys(text)
        self.driver.find_element_by_name(self.search_button_name).click()



