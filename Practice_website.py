import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)
driver.find_element(By.NAME, "name").send_keys("new user")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("abcxyz@mailinator.com")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("abcxyz123")
driver.find_element(By.ID, "exampleCheck1").click()
# driver.find_element(By.XPATH,"//select//option[2]").click()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(3)

driver.find_element(By.ID, "inlineRadio2").click()
time.sleep(3)
driver.find_element(By.NAME, "bday").send_keys(12 / 12 / 1993)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("abcdef")
driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/form/input").click()
time.sleep(3)
a = driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div").text
assert "×\nSuccess! The Form has been submitted successfully!." in a

driver.quit()
