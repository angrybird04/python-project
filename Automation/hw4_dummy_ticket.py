
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector

ser_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=ser_obj)
driver.maximize_window()

driver.get("https://www.dummyticket.com/")

driver.find_element(By.ID,"menu-item-574").click()
# time.sleep(2)
driver.find_element(By.ID,"product_551").click()
# time.sleep(2)
driver.find_element(By.ID,"travname").send_keys("Abc")
# time.sleep(2)
driver.find_element(By.ID,"travlastname").send_keys("Xyz")
# time.sleep(2)
driver.find_element(By.ID,"dob").click()
# time.sleep(2)


month = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
month.select_by_visible_text("Sep")

year = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
year.select_by_visible_text("1995")

a = driver.find_elements(By.XPATH,"//a[@class='ui-state-default']")
for i in a:
    if i.text=="17":
        i.click()
        break
# time.sleep(2)

# month= Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
# month.select_by_visible_text("Jun")

# time.sleep(3)
# year = Select(driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
# year.select_by_visible_text('1995')

driver.find_element(By.XPATH,"//*[@id='sex_1']").click()
driver.find_element(By.ID,"addmorepax").click()
driver.find_element(By.ID,"traveltype_1").click()
driver.find_element(By.ID,"fromcity").send_keys("Delhi")
driver.find_element(By.ID,"tocity").send_keys("New York")

driver.find_element(By.XPATH,"//*[@id='departon']").click()
month = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
month.select_by_visible_text("Sep")

year = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
year.select_by_visible_text("2023")

a = driver.find_elements(By.XPATH,"//a[@class='ui-state-default']")
for i in a:
    if i.text=="17":
        i.click()
        break

driver.find_element(By.ID,"notes").send_keys("Book the ticket")

time.sleep(3)
driver.find_element(By.ID,"select2-reasondummy-container").click()

countries = driver.find_elements(By.XPATH,"//span[@class='select2-results']//li") 
time.sleep(2)
print(len(countries))
for i in countries:
    if i.text=="Visa extension":
        i.click()
        break
time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='appoinmentdate']").click()
# driver.find_element(By.CSS_SELECTOR,"#appoinmentdate").click()


driver.find_element(By.XPATH,"//label[@for='deliverymethod_1']").click()
time.sleep(2)

driver.find_element(By.ID,"billname").send_keys("Ujjwal")
driver.find_element(By.ID,"billing_phone").send_keys(1234567890)
driver.find_element(By.ID,"billing_email").send_keys("abc@xyz.com")
time.sleep(5)
# month = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
# month.select_by_visible_text("Sep")

# year = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
# year.select_by_visible_text("1995")

# a = driver.find_elements(By.XPATH,"//a[@class='ui-state-default']")
# for i in a:
#     if i.text=="17":
#         i.click()
#         break
driver.find_element(By.ID,"select2-billing_country-container").click()
# time.sleep(3)
countries = driver.find_elements(By.XPATH,"//*[@id='select2-billing_country-results']/li")   
time.sleep(2)
print(len(countries))
for i in countries:
    if i.text=="Australia":
        i.click()
        break

driver.find_element(By.ID,"billing_address_1").send_keys("H-165")
driver.find_element(By.XPATH,"//*[@id='billing_address_2']").send_keys("Gurgaon")
driver.find_element(By.ID,"billing_city").send_keys("Haryana")

driver.find_element(By.ID,"select2-billing_state-container").click()

state = driver.find_elements(By.XPATH,"//*[@class='select2-results__options']//li")
for i in state:
    if i.text=="Haryana":
        i.click()

driver.find_element(By.ID,"billing_postcode").send_keys(275101)

a = driver.find_element(By.XPATH,"//*[@id='order_review']/div[1]/table/tfoot/tr[2]/td/strong/span/text()").text
if a=="1,450":
    print("Ticket value correct")
else:
    print("Ticket value not correct")

driver.find_element(By.ID,"place_order").click()


time.sleep(5)