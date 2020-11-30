from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# first of all is needed to attach 'Dedicated Webdriver' (here chromedriver) to the project


# Option1:
# chromedriver is physically copied to disc space and mapped to the appropriate object:
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")

# Option2:
# chromedriver is attached to the project via webdriver manager (pip install webdriver_manager)
# driver = webdriver.Chrome(ChromeDriverManager().install())

# By the above declaration is opened empty Chrome page. By the following line we jump to other www
driver.get("https://www.google.com")


# Changing Window Size - Setting specific Window size
driver.set_window_size(900, 300)
# Changing Window Size - maximizing Window
driver.maximize_window()


# Closing browser window

# Option1: closing only focused window (initial/parent window)
# driver.close()
# Option2: closing both Focused and Child windows
driver.quit()
