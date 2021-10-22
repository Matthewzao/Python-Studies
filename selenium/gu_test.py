from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl.workbook.workbook import Workbook

import time

chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")
arquivo = Workbook()
planilha = arquivo.worksheets[0]

driver = webdriver.Chrome(chromedrive)
driver.maximize_window()
driver.get("https://www.atheleco.com.br/")

clicar = driver.find_element_by_xpath('//*[@id="container"]/section[1]/div/button')
clicar.click()
clicar2 = driver.find_element_by_xpath ('//*[@id="topo"]/div[3]/div/nav/ul/li[2]/a/span')
clicar2.click()
clicar_aba = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[3]/label')
clicar_aba.click()
categoria = driver.find_element_by_xpath('//*[@id="conteudo"]/div/h1/span')  
planilha['A1'] = categoria.text

for n in range(1,5):
    time.sleep(1)
    nome = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(n))
    planilha['A{}'.format(n+1)] = nome.text
    arquivo.save("C:\\Users\\Up Agency 2\\oneDrive\\Documentos\\drive\\meuarquivo4.xlsx")
    
      
time.sleep(1)
categoria2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[3]/label')
planilha['B1'] = categoria2.text
# categoria2.click()
 

for x in range(1,5):
    time.sleep(1)
    nome2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(x))
    planilha['B{}'.format(x+1)] = nome2.text
    arquivo.save("C:\\Users\\Up Agency 2\\oneDrive\\Documentos\\drive\\meuarquivo4.xlsx")
    

    




