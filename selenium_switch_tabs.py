# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:26:17 2021
Selenium Open and Switch Tabs
@author: lux
"""
from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")
driver.get("http://www.google.com/")

driver.execute_script("window.open("");")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

driver.get("http://www.duckduckgo.com")
time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

driver.close()
driver.close()













