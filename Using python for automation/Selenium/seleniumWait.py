from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get('https://www.google.com/intl/es-419/earth/')
#explicit wait
explicitWait=WebDriverWait(driver,9)
#the program waits until the button can be clicked and then does that
button = explicitWait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a')))
button.click()
time.sleep(10)
