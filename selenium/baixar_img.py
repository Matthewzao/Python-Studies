# from selenium import webdriver
# import requests
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.keys import Keys

# chromedrive = ("C:\\Users\\Up Agency 2\\OneDrive\\Área de Trabalho\\estudo python\\selenium\\chromedriver.exe")

# driver = webdriver.Chrome(chromedrive)
# driver.maximize_window()
# driver.get('https://www.lenzme.com.br/admin')

import requests

with open('pato.jpg', 'wb') as imagem:
  resposta = requests.get("https://i.imgur.com/EyDTdcy.jpg", stream=True)

  if not resposta.ok:
    print("Ocorreu um erro, status:" , resposta.status_code)
  else:
    for dado in resposta.iter_content(1024):
      if not dado:
          break

      imagem.write(dado)

    print("Imagem salva! =)")