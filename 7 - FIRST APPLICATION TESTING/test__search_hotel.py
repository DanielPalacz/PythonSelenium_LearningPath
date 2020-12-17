from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import search_hotel as app


global driver
global DUBAI_HOTELS
DUBAI_HOTELS = ["Jumeirah Beach Hotel", "Oasis Beach Tower", "Rose Rayhaan Rotana", "Hyatt Regency Perth"]


@pytest.fixture()
def test__setup():
    global driver
    driver = app.initiate_session("http://www.kurs-selenium.pl/demo/")
    yield
    driver.quit()


def test__check_number_of_hotels_in_dubai(test__setup):
    app.choose_the_city(driver, "Dubai")
    app.set_dates(driver, "16/12/2020", "17/12/2020")
    app.setup_amount_of_children_adults(driver, 5, 5)
    app.click_search(driver)
    hotels = app.get_hotel_names(driver)
    for hotel in hotels:
        assert DUBAI_HOTELS.count(hotel) == 1, "There is no hotel: " + str(hotel)


def test__check_hotel_number_in_dubai(test__setup):
    app.choose_the_city(driver, "Dubai")
    app.set_dates(driver, "16/12/2020", "17/12/2020")
    app.setup_amount_of_children_adults(driver, 5, 5)
    app.click_search(driver)
    hotels = app.get_hotel_names(driver)
    assert len(DUBAI_HOTELS) == len(hotels)
