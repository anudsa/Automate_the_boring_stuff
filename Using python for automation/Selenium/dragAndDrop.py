from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
#webdriver is initialized
driver=webdriver.Chrome()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()
#source and destination are selected
stockholm=driver.find_element(By.CSS_SELECTOR,'#box2')
sweden=driver.find_element(By.CSS_SELECTOR,'#box102')
#an object is created for the drag and drop action
dAndD=ActionChains(driver)
#the source and destination are given
dAndD.drag_and_drop(stockholm,sweden)
#the action is then performed
dAndD.perform()
time.sleep(5)