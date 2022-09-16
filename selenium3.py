from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url= "http://github.com"
driver.get(url)

searchInput= driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
driver.close()
