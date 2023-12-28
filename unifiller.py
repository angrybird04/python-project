import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("http://qa.cms.unifiller.studiographene.xyz/")
driver.find_element(By.ID, "email").send_keys("unifiller11@mailinator.com")
driver.find_element(By.XPATH, "//button").click()
time.sleep(3)
print(driver.current_url)
driver.find_element(By.ID, "password").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.title)
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Customers").click()
print(driver.current_url)
time.sleep(3)
driver.find_element(By.XPATH, "//button").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="name"]').send_keys("rock2023")

# dropdown = Select(driver.find_element(By.ID, 'react-select-12-input'))
a = driver.find_elements(By.ID, 'lifetimeValue')
for i in range(len(a)):
    if a[i].text == "Select an option":
        a[i].click()
        dropdown = driver.find_element(By.XPATH,"//*[@id='lifetimeValue']/div/div[1]/div[1]")
        dropdown.select_by_visible_text("Premium")
# driver.find_element(By.CLASS_NAME,"css-7pg0cj-a11yText").click()
# dropdown.select_by_visible_text("Premium")
time.sleep(5)
driver.quit()
