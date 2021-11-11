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
driver.get("https://analytics.google.com/analytics/web/#/report-home/a203518459w281100907p248059955")
login = driver.find_element_by_xpath('//*[@id="identifierId"]')
login.send_keys('suporte@upagencybrasil.com.br')
proximo = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
proximo.click()
time.sleep(1)
senha = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
senha.send_keys('@VoaUpagency2020!')    
proximo2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
proximo2.click()
time.sleep(5)
pagina = driver.find_element_by_xxpath('//*[@id="1"]/div/div/h2')
print(pagina.text)






# for n in range(0,10):
#     paginaCarrinho = driver.find_element_by_xpath('//*[@id="ID-explorer-table-dataTable-key-0-{}"]/div/div[1]'.format(n)) 
#     rejeição = driver.find_element_by_xpath('//*[@id="ID-rowTable"]/tbody/tr[{}]/td[8]/div'.format(n+1))

#     print(paginaCarrinho.text)
#     print(rejeição.text)
