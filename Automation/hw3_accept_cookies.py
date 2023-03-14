
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector

ser_obj = Service("/Users/ujjwalsingh/Downloads/msedgedriver")
driver = webdriver.Edge(service=ser_obj)
driver.maximize_window()
driver.get("https://stackoverflow.com/questions/43612340/chromedriver-closing-after-test")
driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/button[1]").click()
time.sleep(5)