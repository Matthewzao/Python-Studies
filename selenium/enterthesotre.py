from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")

driver = webdriver.Chrome(chromedrive)
driver.maximize_window()
driver.get('https://www.lenzme.com.br/admin/produto_fotos/prod/276')

clicar = driver.find_element_by_xpath('//*[@id="container"]/section[1]/div/button')
clicar.click()
email = driver.find_element_by_xpath('//*[@id="UsuarioEmail"]')
email.click()
email.send_keys("suporte@upagencybrasil.com.br")
senha = driver.find_element_by_xpath('//*[@id="UsuarioSenha"]')
senha.click()
senha.send_keys('@VoaUpagency2021!')
entrar = driver.find_element_by_xpath('//*[@id="frm-login"]/div[4]/input')
entrar.click()
azul = driver.find_element_by_xpath('//*[@id="artigo"]/section[3]/div/table/tbody/tr[1]/td[1]/div/div[1]')
azul.click()
editar = driver.find_element_by_xpath('//*[@id="artigo"]/section[3]/div/table/tbody/tr[1]/td[1]/div/div[2]/a[1]')
editar.click()
voltar = driver.find_element_by_xpath('//*[@id="artigo"]/div/section/section/ul/li/a')
voltar.click()
sku = driver.find_element_by_xpath('//*[@id="artigo"]/section[2]/div[2]/a')
sku.click()
escrever = driver.find_element_by_xpath('//*[@id="SkuPeso"]')
escrever.clear()
escrever.send_keys('6885')















# estoque = driver.find_element_by_xpath('//*[@id="menu"]/ul[2]/li[2]/a')
# estoque.click()
# time.sleep(0.5)
# produtos = driver.find_element_by_xpath('//*[@id="menu"]/ul[2]/li[2]/ul/li[1]/a')
# produtos.click()
# vestido = driver.find_element_by_xpath('//*[@id="artigo"]/section[5]/div/table/tbody/tr[1]/td[4]/div/div[1]')
# vestido.click()
# edit_foto = driver.find_element_by_xpath('//*[@id="artigo"]/section[5]/div/table/tbody/tr[1]/td[4]/div/div[2]/a[4]')
# edit_foto.click()
# time.sleep(0.5)
# foto = driver.find_element_by_xpath('//*[@id="artigo"]/section[3]/div/table/tbody/tr[1]/td[1]/div/div[1]')
# foto.click()











#
#botao = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
#botao.click()
