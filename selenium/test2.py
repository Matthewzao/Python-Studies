from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")

driver = webdriver.Chrome(chromedrive)
driver.maximize_window()
driver.get('https://www.lenzme.com.br')

categoria1 = driver.find_element_by_xpath('//*[@id="topo"]/div[3]/div/nav/ul/li[5]/a/span')
print(categoria1.text)
