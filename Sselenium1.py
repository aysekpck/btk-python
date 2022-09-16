#SELENİUM

"""import os
print(os.system("pip install selenium"))
"""

from selenium import webdriver

driver = webdriver.Chrome()

url ="http://youtube.com"  #youtube u açar
driver.get(url)
