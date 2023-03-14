
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector

ser_obj = Service("/Users/ujjwalsingh/Downloads/msedgedriver")
driver = webdriver.Edge(service=ser_obj)
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

driver.find_element(By.ID,"select2-reasondummy-container").click()
options = driver.find_elements()
time.sleep(5)