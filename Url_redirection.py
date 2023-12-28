# from selenium.webdriver.chrome.service import Service
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# this is the chromium for testing which can be downloaded from the link given below

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# ser_obj = Service(executable_path="/Users/ujjwalsingh/Downloads/chrome-mac-x642/Google_Chrome_for_testing")
# driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.implicitly_wait(5)
driver.get("https://www.gmail.com")
print(driver.title)
time.sleep(3)
driver.minimize_window()
driver.back()
time.sleep(3)
print(driver.title)
time.sleep(3)
driver.forward()
driver.refresh()
print(driver.title)
time.sleep(3)
driver.close()
