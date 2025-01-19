
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.github.com"
driver.get(url)

time.sleep(2)
print(driver.title)

driver.maximize_window()
driver.save_screenshot("github-savescreenshot.png")


url2 = "https://www.github.com/ibrahimkus"
driver.get(url2)
time.sleep(2)

driver.back()


time.sleep(2)
driver.close()