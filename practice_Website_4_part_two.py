import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("/Users/ujjwalsingh/Downloads/geckodriver")
driver = webdriver.Firefox(service=serv_obj)

# driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# the first approach to scroll is by providing pixel as argument in execute_Script
# driver.execute_script("window.scrollBy(0,1000)","")

# the second approach is to scroll till the element is not found
a = driver.find_element(By.ID, "mousehover")
driver.execute_script("arguments[0].scrollIntoView();",a)

# the third approach is used to scroll to the end of the page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
action = ActionChains(driver)
# html = driver.find_element(By.TAG_NAME, 'html')
# html.send_keys(Keys.END)
element = driver.find_element(By.ID, "mousehover")
time.sleep(3)

# action.scroll_to_element(element).perform()
action.move_to_element(element)
action.perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top"))
action.perform()
time.sleep(5)
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click()
action.perform()
time.sleep(3)

driver.quit()
