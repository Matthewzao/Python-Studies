from selenium import webdriver
#import requests
#from bs4 import BeautifulSoup
#page = requests.get("https://www.magazineluiza.com.br/?partner_id=974&gclid=CjwKCAjw_L6LBhBbEiwA4c46ujzJB6MA7TNVPUhR08LL6QDCqnlCAKjD0jZ3vz1OIvuyyZEUN8RvRhoC4F4QAvD_BwE&gclsrc=aw.ds")
from selenium.webdriver.common.keys import Keys

chromeDrive = "C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\PYTHON\\chromedriver.exe"
#nba = "nba"
driver = webdriver.Chrome(chromeDrive)
driver.maximize_window()

driver.get("https://www.magazineluiza.com.br/")
#driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(nba)
botao = driver.find_element_by_xpath('//*[@id="__next"]/div/main/section[1]/div[2]/header/div/div[3]/nav/ul/li[7]/div[1]/a')
botao.click()
botao2 = driver.find_element_by_xpath('//*[@id="showcase"]/ul[1]/a[1]')
botao2.click()
driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div[2]/h1')
achar = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div[2]/h1')
print(achar.text)
  



#//*[@id="showcase"]/div[3]/div/div/ul/li[1]/a/div[3]/h3

#import requests
#from bs4 import BeautifulSoup

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
#page = requests.get("https://www.magazineluiza.com.br/?partner_id=974&gclid=CjwKCAjw_L6LBhBbEiwA4c46ujzJB6MA7TNVPUhR08LL6QDCqnlCAKjD0jZ3vz1OIvuyyZEUN8RvRhoC4F4QAvD_BwE&gclsrc=aw.ds")
#from selenium.webdriver.common.keys import Keys

#//*[@id="showcase"]/div[3]/div/div/ul/li[1]/a/div[3]/h3


#driver.find_element_by_name("g").send_keys(keys.return)

#//*[@id="__next"]/div/main/section[1]/div[2]/header/div/div[3]/nav/ul/li[7]/div[1]/a


# nomeProduto = driver.find_element_by_xpath(tal xpath)

#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36
