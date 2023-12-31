import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
windows_opened = driver.window_handles
print(windows_opened)
time.sleep(3)
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.XPATH,"//h3").text)
time.sleep(5)
driver.close()
driver.switch_to.window(windows_opened[0])

print(driver.find_element(By.XPATH,"//h3").text)

time.sleep(3)
driver.quit()