import logging


class SearchHotelPage:

    def __init__(self, webdriver):
        self.logger = logging.getLogger(__name__)
        self.driver = webdriver
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.location_match_xpath = "//span[text()='Dubai']"
        self.checkin_input_name = "checkin"
        self.checkout_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.children_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"

    def set_city(self, city="Dubai"):
        self.logger.info(f"Setting city {city}.")
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpath).click()

    def set_date_range(self, checkin, checkout):
        self.logger.info(f"Setting check in/out dates: {checkin}, {checkout}.")
        self.driver.find_element_by_name(self.checkin_input_name).send_keys(checkin)
        self.driver.find_element_by_name(self.checkout_input_name).send_keys(checkout)

    def set_travellers(self, adults, child):
        self.logger.info(f"Setting travellers adults/children quantity: {adults}, {child}.")
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adults)
        self.driver.find_element_by_id(self.children_input_id).clear()
        self.driver.find_element_by_id(self.children_input_id).send_keys(child)

    def perform_search(self):
        self.logger.info("Performing search.")
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
