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
driver.get("https://www.atheleco.com.br/")

clicar = driver.find_element_by_xpath('//*[@id="container"]/section[1]/div/button')
clicar.click()
clicar2 = driver.find_element_by_xpath ('//*[@id="topo"]/div[3]/div/nav/ul/li[2]/a/span')
clicar2.click()
clicar_aba = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[3]/label')
clicar_aba.click()
categoria = driver.find_element_by_xpath('//*[@id="conteudo"]/div/h1/span')  
planilha['A1'] = categoria.text

for n in range(1,10):
    time.sleep(1)
    nome = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(n))
    preço = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[2]/a/div[1]/div[1]/ins'.format(n))
    tamanho = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[3]/div/ul'.format(n))
    planilha['A{}'.format(n+1)] = nome.text
    planilha['B{}'.format(n+1)] = preço.text
    planilha['C{}'.format(n+1)] = tamanho.text
    arquivo.save("C:\\Users\\Up Agency 2\\oneDrive\\Documentos\\drive\\meuarquivo5.xlsx")
    
      
time.sleep(1)
categoria2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[3]/label') 
planilha['E1'] = categoria2.text
# categoria2.click()
 

for x in range(1,10):
    time.sleep(1)
    nome2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(x))
    preço2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[2]/a/div[1]/div[1]/ins'.format(x))
    tamanho2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[3]/div/ul'.format(x))
    planilha['E{}'.format(x+1)] = nome2.text
    planilha['F{}'.format(x+1)] = preço2.text
    planilha['G{}'.format(x+1)] = tamanho2.text
    arquivo.save("C:\\Users\\Up Agency 2\\oneDrive\\Documentos\\drive\\meuarquivo5.xlsx")



    categoria3 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[4]/label')
    planilha['I1'] = categoria3.text


for z in range(1,10):
    nome3 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(z))
    preço3 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[2]/a/div[1]'.format(z))
    tamanho3 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[3]/div/ul'.format(z))
    planilha['I{}'.format(z+1)] = nome3.text    
    planilha['j{}'.format(z+1)] = preço3.text
    planilha['K{}'.format(z+1)] = tamanho3.text
    arquivo.save("C:\\Users\\Up Agency 2\\oneDrive\\Documentos\\drive\\meuarquivo5.xlsx")
