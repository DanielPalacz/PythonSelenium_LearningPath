from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# first of all is needed to attach 'Dedicated Webdriver' (here chromedriver) to the project


# Option1:
# chromedriver is physically copied to disc space and mapped to the appropriate object:
driver = webdriver.Chrome(r"C:\Users\danie\OneDrive\Pulpit\PythonProjects\Selenium_Kurs\drivers\chromedriver.exe")

# Option2:
# chromedriver is attached to the project via webdriver manager (pip install webdriver_manager)
# driver = webdriver.Chrome(ChromeDriverManager().install())
