import requests


def baixar_arquivo (url, endereco)
    resposta = requests.get(url)
    with open('teste.png', 'wb')