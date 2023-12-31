import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
list23 = []
a = driver.find_elements(By.XPATH, "//div[@class='products']//div[@class ='product']//button")
driver.implicitly_wait(10)
for i in a:
    list23.append(i.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    i.click()
time.sleep(3)
print(list23)
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/a[4]/img').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
time.sleep(3)
s = 0
a = driver.find_elements(By.XPATH, '//*[@id="productCartTables"]/tbody/tr/td[5]/p')
for i in range(len(a)):
    ab = int(a[i].text)
    s = s + ab
list22 = []
veggies = driver.find_elements(By.XPATH, "//td//p[@class='product-name']")
for i in veggies:
    list22.append(i.text)
print(float(s - s / 10))
print(list22)
assert list22 == list23

a = driver.find_element(By.XPATH, "//span[@class = 'discountAmt']").text

totalamount = int(driver.find_element(By.XPATH, "//span[@class = 'totAmt']").text)

print(totalamount)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, '//button[@class="promoBtn"]').click()
discounted_amount = int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(discounted_amount)
assert totalamount == discounted_amount
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()
time.sleep(5)


driver.quit()
