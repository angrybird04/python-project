import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
list = []
list2 = []
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(4)
count =len(driver.find_elements(By.XPATH,"//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    list.append(button.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies =driver.find_elements(By.CSS_SELECTOR,"p.product-name")
for veg in veggies:
    list2.append(veg.text)

print(list2)
assert list == list2
originalAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
discountAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text

assert float(discountAmount) < int(originalAmount)

print(driver.find_element(By.CSS_SELECTOR,"span.promoInfo").text)

amounts = driver.find_elements(By.XPATH,"//tr/td[5]/p")
summ = 0
for amount in amounts:
    summ = summ + int(amount.text) #32+48+60

print(summ)

totalAmount = int(driver.find_element(By.CLASS_NAME,"totAmt").text)

assert summ == totalAmount
