import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT,"Register").click()

time.sleep(3)
driver.find_element(By.ID,"firstName").send_keys("Admin")
driver.find_element(By.ID,"lastName").send_keys("User")
driver.find_element(By.ID,"userEmail").send_keys("abcxyz597439@gmail.com")
driver.find_element(By.ID,'userMobile').send_keys('9876543210')
driver.find_element(By.XPATH,"//input[@value='Male']").click()

driver.find_element(By.XPATH,'//select//option[@value="1: Doctor"]').click()
driver.find_element(By.ID,"userPassword").send_keys("Abcdef@123")
driver.find_element(By.ID,"confirmPassword").send_keys("Abcdef@123")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(3)

driver.find_element(By.ID,"login").click()
time.sleep(3)

driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.CLASS_NAME,"forgot-password-link").click()
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("abcxyz597439@gmail.com")
driver.find_element(By.ID,"userPassword").send_keys("Abcdef@123")
driver.find_element(By.ID,"confirmPassword").send_keys("Abcdef@123")
time.sleep(3)

driver.quit()