from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")

driver = webdriver.Chrome(chromedrive)
driver.maximize_window()
driver.get("https://www.atheleco.com.br/")
clicar = driver.find_element_by_xpath('//*[@id="container"]/section[1]/div/button')
clicar.click()
clicar2 = driver.find_element_by_xpath ('//*[@id="topo"]/div[3]/div/nav/ul/li[2]/a/span')
clicar2.click()


for n in range(1,9):   
    nome = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(n))
    print(nome.text)