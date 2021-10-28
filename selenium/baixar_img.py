# from selenium import webdriver
# import requests
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.keys import Keys

# chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")

# driver = webdriver.Chrome(chromedrive)
# driver.maximize_window()
# driver.get('https://www.lenzme.com.br/admin')

import requests

with open('imagem_baixada.jpg', 'wb') as imagem:
  resposta = requests.get("https://static3.tcdn.com.br/img/img_prod/460977/pre_venda_action_figure_miles_morales_homem_aranha_no_aranhaverso_spider_man_into_the_spider_verse_e_55999_1_20201211173135.png", stream=True)

  if not resposta.ok:
    print("Ocorreu um erro, status:" , resposta.status_code)
  else:
    for dado in resposta.iter_content(1024):
      if not dado:
          break

      imagem.write(dado)

    print("Imagem salva! =)")