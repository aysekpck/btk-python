from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window() #ekranı büyütür
driver.save_screenshot("github.com-homepage.png") #anasayfanın resmini siteden alır

url = "http://github.com/sadikturan"
driver.get(url)

print(driver.title)
if "sadikturan" in driver.title:
     driver.save_screenshot("github-sadikturan.png")


time.sleep(2)

driver.back() #sayfayı geriye alma
driver.forward() #ileri alma

time.sleep(2)

driver.close()


