from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_widow()
time.sleep(5)


