import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
# time.sleep(3)
a = driver.find_elements(By.XPATH, "//div[@class='products']//div[@class ='product']//button")
driver.implicitly_wait(5)
for i in range(len(a)):
    a[i].click()
# time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/a[4]/img').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
# time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rohitshettyacademy")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()
# driver.find_element(By.XPATH,"//input[@type='text']").click()
#  time.sleep(5)
driver.quit()
