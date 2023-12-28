import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

'''
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
# time.sleep(3)
a = driver.find_elements(By.XPATH, "//div[@class='products']//div[@class ='product']//button")
driver.implicitly_wait(10)
for i in range(len(a)):
    a[i].click()
time.sleep(3)
list2 = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
vegetable = driver.find_elements(By.XPATH, "//div[@class='products']//div//h4[@class='product-name']")
count = len(vegetable)
print(type(vegetable))
for i in range(count):
    if vegetable[i].text == list2[i]:
        print("Quantity matched")

assert vegetable == list2
# assert vegetable == list2
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/a[4]/img').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
time.sleep(3)
s = 0
a = driver.find_elements(By.XPATH, '//*[@id="productCartTables"]/tbody/tr/td[5]/p')
for i in range(len(a)):
    ab = int(a[i].text)
    s = s + ab
print(float(s - s / 10))
a = driver.find_element(By.XPATH, "//span[@class = 'discountAmt']").text
totalamount = int(driver.find_element(By.XPATH, "//span[@class = 'totAmt']").text)
# time.sleep(5)
print(totalamount)
# here we define wait the CSS Selector is loaded or not
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, '//button[@class="promoBtn"]').click()
discounted_amount = int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(discounted_amount)
assert totalamount == discounted_amount
time.sleep(10)
# wait = WebDriverWait(driver, 20)
# wait.until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, ".promoInfo"), "Code applied ..!"))
# print(driver.find_element(By.CLASS_NAME, ".promoInfo").text)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()
time.sleep(5)
# a = Select(driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]"))
# a.select_by_value("India")

# driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/input').click()
# time.sleep(10)
# driver.find_element(By.LINK_TEXT,'Proceed').click()
# wait1 = WebDriverWait(driver, 30)
# wait1.until(expected_conditions.visibility_of_element_located(By.XPATH('//*[@id="root"]/div/div/div/div/button')))
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "//input[@type='text']")))
# driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()
#  time.sleep(5)
driver.quit()
'''

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()

list22 = []
list2 = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    list22.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    button.click()
print(list22)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in veggies:
    list2.append(veg.text)

print(list2)
assert list22 == list2
originalAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

assert float(discountAmount) < int(originalAmount)

print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)  # 32+48+60

print(sum)

totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == totalAmount
