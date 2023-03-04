import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service(r"C:\Users\All might\Downloads\chromedriver\chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("selenium")
# driver.find_element(By.LINK_TEXT,"selenium").click()
# driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")

# driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.ID,"datepicker").click()

# ab= driver.find_element(By.XPATH,"//div[@id='content']")
# ab.click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Selenium in").click()

driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
time.sleep(3)
driver.switch_to.alert.accept()

dropdown=driver.find_element(By.ID,"speed")

# dropdown.click()
speed = Select(dropdown)
speed.select_by_visible_text("Medium")
time.sleep(1)

file=driver.find_element(By.ID,"files")
# dropdown.click()
file = Select(file)
file.select_by_visible_text("PDF file")
time.sleep(1)

number=driver.find_element(By.ID,"number")
# dropdown.click()
number = Select(number)
number.select_by_visible_text("3")

product=driver.find_element(By.ID,"products")
# dropdown.click()
product = Select(product)
product.select_by_visible_text("Yahoo")
time.sleep(1)

animal=driver.find_element(By.ID,"animals")
# dropdown.click()
animal = Select(animal)
animal.select_by_visible_text("Baby Cat")
time.sleep(1)

driver.find_element(By.ID,"age").send_keys("28")

driver.find_element(By.LINK_TEXT,"mariusFM77").click()
print(driver.title)

# windowid = driver.window_handles
# if driver.title =="mariusFM77 Stock Image and Video Portfolio - iStock":
#     driver.close()

driver.back

time.sleep(2)
driver.switch_to.frame('frame-one1434677811')
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Abc")
time.sleep(1)

driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Xyz")
time.sleep(1)

driver.find_element(By.ID,"RESULT_TextField-3").send_keys("1234567890")
time.sleep(1)
driver.find_element(By.ID,"RESULT_TextField-4").send_keys("India")
time.sleep(1)
driver.find_element(By.ID,"RESULT_TextField-5").send_keys("Delhi")
time.sleep(1)
driver.find_element(By.ID,"RESULT_TextField-6").send_keys("abc@xyz.com")
time.sleep(1)
# driver.find_element(By.ID,"RESULT_RadioButton-7_1").click()
gender = driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-7_0']")
# print(abc.is_selected())
gender.click()
time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,"#frame-one1434677811").click()
day = driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_1']")
day.click()
time.sleep(1)
dropdown=driver.find_element(By.ID,"RESULT_RadioButton-9")
# dropdown.click()
tim = Select(dropdown)
tim.select_by_value("Radio-0")
time.sleep(1)

# driver.find_element(By.XPATH,"//*[@id='RESULT_RadioButton-9']/option[3]").click()
driver.find_element(By.ID,"FSsubmit").click()

# s=driver.find_element(By.ID,"content").text
# if s =="The result storage capacity has been reached for this form. Your result was not created. Please contact the form owner.":
#     print("\nLogin failed\n")
# else:
#     print("\n Login successful\n")
# time.sleep(3)