import logging


class SearchResultsPage:

    def __init__(self, webdriver):
        self.logger = logging.getLogger(__name__)
        self.driver = webdriver
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"

    def get_hotel_names(self):
        hotels = self.driver.find_elements_by_xpath(self.hotel_names_xpath)
        hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Available hotels:")
        for hotel_name in hotel_names:
            self.logger.info(hotel_name)
        return hotel_names

    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Hotels prices:")
        for hotel_price in hotel_prices:
            self.logger.info(hotel_price)
        return hotel_prices
