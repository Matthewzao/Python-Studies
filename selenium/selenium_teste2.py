from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")

driver = webdriver.Chrome(chromedrive)
driver.maximize_window()
driver.get("https://www.mercadolivre.com.br/")

pesquisa = driver.find_element_by_xpath ('/html/body/header/div/form/input')
pesquisa.send_keys("celular")
botao =  driver.find_element_by_xpath('/html/body/header/div/form/button/div')
botao.click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="newCookieDisclaimerButton"]').click()
time.sleep(1)

for n in range(5,10):   
    findcelular = driver.find_element_by_xpath('//*[@id="root-app"]/div/div[1]/section/ol/li[{}]/div/div/div[2]/div[2]/a[1]/h2'.format(n))
    print(findcelular.text)




#window.scrollBy(0,500)



#for i in range(1, 2):
    #nome = driver.find_element_by_xpath('//*[@id="root-app"]/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[{}]/section/div[2]/div/ul'.format(i))
    #print(nome.text)

# botao = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section[3]/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/a')
# botao.click()
# achar = driver.find_element_by_xpath('//*[@id="root-app"]/div/div[3]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/h1')
#achar2 = driver.fid_element_by_xpath('//*[@id="root-app"]/div/div[3]/div/div[2]/div[2]/div[3]/div/p')
# print(achar.text)
#print(achar2.text)





#for i in range(1, 5):
    #nome2 = driver.find_element_by_xpath('//*[@id="acabaramDeChegar"]/div[2]/div[1]/div/div/div/div[{}]/div/div/a/div/h2'.format(i))
    #print(nome2.text)








#achar2 = driver.find_element_by_xpath('//*[@id="__next"]/main/article/section/div[2]/h1')
#print(achar2.text)
#preco = driver.find_element_by_xpath('//*[@id="blocoValores"]/div[2]/div/h4')
#print(preco.text)