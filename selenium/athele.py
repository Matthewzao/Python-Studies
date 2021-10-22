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
clicar_aba = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[3]/label')
clicar_aba.click()
categoria = driver.find_element_by_xpath('//*[@id="conteudo"]/div/h1/span')  
print(categoria.text)

for n in range(1,9):
    time.sleep(1)
    driver.execute_script('window.scrollBy(0, 100)')
    nome = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(n))
    preço = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[2]/a/div[1]/div[1]/ins'.format(n))
    parcela = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[2]/a/div[2]/div[2]'.format(n))    
    tamanho = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[3]/div/ul'.format(n))
    print(nome.text)
    # print(preço.text)
    # print(parcela.text)
    # print(tamanho.text)
    

# driver.execute_script('window.scrollTo(0, -800)')
# categoria2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/section/div[1]/ul/li[3]/label')
# categoria2.click()
# print(categoria2.text)  

# for x in range(1,9):
#     time.sleep(1)
#     driver.execute_script('window.scrollBy(0, 100)')
#     nome2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[1]/a/div[3]'.format(x))
#     preço2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[2]/a/div[1]/div[1]/ins'.format(x))
#     parcela2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[2]/a/div[2]/div[2]'.format(x))
#     tamanho2 = driver.find_element_by_xpath('//*[@id="conteudo"]/div/div/section/div[1]/div/ul/li[{}]/div/section[3]/div/ul'.format(x))

#     print(nome2.text)
#     # print(preço2.text)
#     # print(parcela2.text)
#     # print(tamanho2.text)