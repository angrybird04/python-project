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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,"//a[@class= 'blinkingText']").click()
window_handler = driver.window_handles
time.sleep(3)

driver.switch_to.window(window_handler[1])
a= driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
driver.close()
driver.switch_to.window(window_handler[0])
driver.find_element(By.ID,"username").send_keys(a)
driver.find_element(By.ID,"password").send_keys("Password")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
#waitt = WebDriverWait(driver,10)
#waitt.until(expected_conditions.presence_of_element_located((By.XPATH,"//strong[contains(text(),'Incorrect')]")))
#print(driver.find_element(By.XPATH,"//strong[contains(text(),'Incorrect')]").text)
'''
wait = WebDriverWait(driver, 10)
message = driver.find_element(By.XPATH, "//form[@id='login-form']//strong/..")
wait.until(expected_conditions.visibility_of(message))

print(message.text)
'''
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
time.sleep(2)
driver.quit()