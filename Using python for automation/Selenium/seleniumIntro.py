from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#webdriver is initialized
driver=webdriver.Chrome()
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
#the input form is searched using its css selector
messageForm = driver.find_element(By.CSS_SELECTOR,'#user-message')
#a message is sent as a string
messageForm.send_keys('Hello,world')
#the show  message button is found and clicked
showButton=driver.find_element(By.CSS_SELECTOR,'#get-input > button')
showButton.click()
#now input forms for a and b are found
inputA=driver.find_element(By.CSS_SELECTOR,'#value1')
inputB=driver.find_element(By.CSS_SELECTOR,'#value2')
#a value is sent to A and B
inputA.send_keys('9')
inputB.send_keys('1')
#the button is found and clicked
getTotalButton=driver.find_element(By.CSS_SELECTOR,'#gettotal > button')
getTotalButton.click()
#the program is paused to see the operations happen in the browser window
time.sleep(5)

