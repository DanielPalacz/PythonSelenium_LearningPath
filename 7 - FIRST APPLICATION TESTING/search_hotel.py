from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def initiate_session(www_name):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(www_name)
    return driver


#
#
# Choosing the city in search-box:
#
def choose_the_city(general_driver, city="Dubai"):
    general_driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
    general_driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys(city)
    general_driver.find_element_by_xpath(f"//span[text()='{city}']").click()

#
# Setting Checking \ Checkout dates
#
#
# Option 1
#
# driver.find_element_by_name("checkin").send_keys("16/12/2020")
# driver.find_element_by_name("checkout").send_keys("17/12/2020")


def set_dates(general_driver, checkin_date, checkout_date):
    general_driver.find_element_by_name("checkin").send_keys(checkin_date)
    general_driver.find_element_by_name("checkout").send_keys(checkout_date)
#
# Option 2 (by using calendar)
#
# driver.find_element_by_name("checkin").click()
# driver.find_element_by_xpath("//td[@class='day ' and text()='20']").click()
# driver.find_element_by_name("checkout").click()
# for element in driver.find_elements_by_xpath("//td[@class='day ' and text()='23']"):
#    if element.is_displayed():
#        element.click()
#        break


#
# Setting number of travelers:
#
# driver.find_element_by_id("travellersInput").click()
# driver.find_element_by_id("adultInput").clear()
# driver.find_element_by_id("adultInput").send_keys("4")
# driver.find_element_by_id("childInput").clear()
# driver.find_element_by_id("childInput").send_keys("4")

def setup_amount_of_children_adults(general_driver, adults=1, children=1):
    general_driver.find_element_by_id("travellersInput").click()
    general_driver.find_element_by_id("adultInput").clear()
    general_driver.find_element_by_id("adultInput").send_keys(adults)
    general_driver.find_element_by_id("childInput").clear()
    general_driver.find_element_by_id("childInput").send_keys(children)


def click_search(general_driver):
    general_driver.find_element_by_xpath("//button[text()=' Search']").click()


# Taking hotel names:
# hotels = driver.find_elements_by_xpath("//h4[contains(@class, 'list_title')]//b")
# hotel_names = [e.get_attribute("textContent") for e in hotels]
# for hotel_name in hotel_names:
#    print(f"Hotel name: {hotel_name}")


def get_hotel_names(general_driver):
    hotels = general_driver.find_elements_by_xpath("//h4[contains(@class, 'list_title')]//b")
    hotel_names = [e.get_attribute("textContent") for e in hotels]
    return hotel_names


# Taking hotel prices:
# prices = driver.find_elements_by_xpath("//div[contains(@class, 'price_tab')]//b")
# price_values = [p.get_attribute("textContent") for p in prices]
# for price in price_values:
#    print(f"Price value: {price}")


def get_hotel_prices(general_driver):
    prices = general_driver.find_elements_by_xpath("//div[contains(@class, 'price_tab')]//b")
    price_values = [p.get_attribute("textContent") for p in prices]
    return price_values


#
# assert hotel_names[0] == "Jumeirah Beach Hotel"
# assert hotel_names[1] == "Oasis Beach Tower"
# assert hotel_names[2] == "Rose Rayhaan Rotana"
# assert hotel_names[3] == "Hyatt Regency Perth"

# assert price_values[0] == 22
# assert price_values[1] == 50
# assert price_values[2] == 80
# assert price_values[3] == 150


if __name__ == '__main__':
    d = initiate_session("http://www.kurs-selenium.pl/demo/")
    choose_the_city(d, "Dubai")
    set_dates(d, "16/12/2020", "17/12/2020")
    setup_amount_of_children_adults(d, 5, 5)
    click_search(d)
    hotels = get_hotel_names(d)
    prices = get_hotel_prices(d)
    print("")
    for hotel_in, hotel_val in enumerate(hotels):
        print(f"Hotel {hotel_in}: {hotel_val}")
    print("")
    for price_in, price_val in enumerate(prices):
        print(f"Hotel {price_in}: {price_val}")
