from typing import Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl.workbook.workbook import Workbook

import time

chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")
arquivo = Workbook()    
planilha = arquivo.worksheets[0]

driver = webdriver.Chrome(chromedrive)
driver.maximize_window()
driver.get("https://doceellastore.com.br/index.php/de309/catalog_category/index/key/5f263ebea799c97f073da552e81786d3/")

username = driver.find_element_by_xpath('//*[@id="username"]')
username.click()
username.send_keys('user')
time.sleep(0.5)
senha = driver.find_element_by_xpath('//*[@id="login"]')
senha.click()
senha.send_keys('adp4oeild')
time.sleep(0.5)
enter = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/input')
enter.click()
time.sleep(0.5)
desconto1 = driver.find_element_by_xpath('//*[@id="extdd-26"]')
desconto1.click()
time.sleep(1)
produtos = driver.find_element_by_xpath('//*[@id="category_info_tabs_products"]/span')
produtos.click()
time.sleep(1)
scroll = driver.find_element_by_xpath('//*[@id="catalog_category_products"]/table/tbody/tr/td[1]/select')
scroll.click()
#trocar o for pra 200



for n in range(1,200):
  driver.execute_script('window.scrollBy(0, 100)')
  time.sleep(1)
  calca = driver.find_element_by_xpath('//*[@id="catalog_category_products_table"]/tbody/tr[{}]/td[4]'.format(n))
  print(calca.text)
#   planilha['A{}'.format(n+1)] = nome.text
#   planilha['B{}'.format(n+1)] =  "10"
#   arquivo.save("\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\excel with python\\DESCONTOS.xlsx")