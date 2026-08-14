from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select
import time
import sys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://letcode.in/file')

driver.maximize_window()
driver.implicitly_wait(10)
actions = ActionChains(driver)
driver.find_element(By.ID,"resume").send_keys("C:\\Users\\Sarves\\PycharmProjects\\PythonProject\\info.txt")
# frame = driver.find_element(By.ID,'root')
# driver.switch_to.frame(1)
el = driver.find_element(By.XPATH ,"//table[@id='shopping']//tr[0]//td[0]")
# for row in el:
    # print(row.text)
# print(el.text)
time.sleep(2)
driver.close()
