
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector

ser_obj = Service("/Users/ujjwalsingh/Downloads/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)

connect =mysql.connector.connect(host="127.0.0.1",port=3306,user="root",passwd="Coco@1995",database="mydb")
cursuor = connect.cursor()
cursuor.execute("select * from LOGIN")
for i in cursuor:

    driver.find_element(By.XPATH,"//input[@name='username']").send_keys(i[0])
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@name='password']").send_keys(i[1])
    time.sleep(1)

    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(5)

   
# a=driver.find_elements(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container --collapse']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[1]/div[1]/div[1]")
# driver.find_element(By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent --visited']").click

    time.sleep(3)

    if driver.current_url=="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
        print("Login Failed")
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@name='username']").clear()
        driver.find_element(By.XPATH,"//input[@name='password']").clear()

    else:
        time.sleep(3)
        driver.find_element(By.LINK_TEXT,"Admin").click()
        a = len(driver.find_elements(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div"))
        print("Number of users: ",a)

        b = driver.find_elements(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div> div:nth-child(5)")
        time.sleep(3)
        count =0
        for i in b:
            if i.text=="Enabled":
                count+=1

        print("Number of enabled users: ",count)
        print("Number of disabled users: ",a - len(b))
        time.sleep(2)
        c = driver.find_elements(By.CSS_SELECTOR,"div[class='orangehrm-container'] div div:nth-child(1) div:nth-child(3) div:nth-child(1)")
        countt =0
        for i in c:
            if i.text =="ESS":
                # d=driver.find_element(By.CSS_SELECTOR,"div[class='orangehrm-container'] div div:nth-child(1) div:nth-child(1) div:nth-child(1)").text
                # print(d)
                # print(i.text)
                countt+=1
        time.sleep(3)

print("Number of ESS Users",countt)