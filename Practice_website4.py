import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.find_element(By.XPATH,"//input[@type='checkbox' and @value ='option2']").click()
# to find multiple elements we have to use find_elements
a = driver.find_elements(By.XPATH,"//input[@type='checkbox']")


print(len(a))
for i in range(len(a)):
    # we have to user get_attribute("property name") and it will fetch the element whose property with "value" tag matches the text we specify in condition
    if a[i].get_attribute("value") =="option1":
        a[i].click()
        if a[i].is_selected():
            print(True)
        break

a=driver.find_elements(By.XPATH,"//input[@type='radio' ]")
for i in range(len(a)):
    if a[i].get_attribute("value")=="radio2":
        a[i].click()
        assert a[i].is_selected()

driver.find_element(By.XPATH,'//*[@id="hide-textbox"]').click()
time.sleep(3)
# in case of assert not it will ensure the condition returns false
assert not driver.find_element(By.XPATH,'//*[@id="displayed-text"]').is_displayed()

driver.find_element(By.ID,"name").send_keys("John")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()
#assert driver.find_element(By.XPATH,'//*[@id="displayed-text"]').is_displayed()

time.sleep(3)
driver.quit()