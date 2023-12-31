import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
iframe = driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)
# driver.switch_to.frame("mce_0_ifr")
time.sleep(3)
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("This is a frame example.")
driver.switch_to.default_content()
a=driver.find_element(By.XPATH,"//h3").text
print(a)
time.sleep(3)
driver.quit()