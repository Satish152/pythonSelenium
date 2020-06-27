from selenium import  webdriver
from pathlib import Path
import os.path

driver=webdriver.Chrome("./../drivers/chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window();
driver.find_element_by_name("q").send_keys("run")
driver.close()
