import requests
import json
from requests.models import HTTPBasicAuth

                                #     GET
# nome = requests.get('https://teste-67f75-default-rtdb.firebaseio.com/.json')
# nomeJson = nome.json()
# print(nome.json())

                                    #  POST
token = '4423f2d8922cad3e3ec5a8c342992c04'   
key = '1582c527884345cd8153fda9b11c7356'
url_site = 'https://www.rushrush.com.br//api/variacoes/buscar/todos'


requisicao = requests.post(url=url_site,auth=HTTPBasicAuth(token,key))
res = requisicao.json()
print(res)






                                         #   PATCH
# informacao = '{"Nome": "Beatriz", "Sobrenome": "Santos", "idade": "20"}'
# mudanca = requests.patch('https://teste-67f75-default-rtdb.firebaseio.com/-Mn6FggheX8G27sz6aQu.json',data=informacao)
# mudaca = mudanca.json()
# print(mudanca)

                                #  DELETE

# mudanca = requests.delete('https://teste-67f75-default-rtdb.firebaseio.com/3.json')
# print(mudanca)
 

        # como especificar a informação que quero pegar
# cotacao_dolar = nome['USDBRL'] ['bid']




