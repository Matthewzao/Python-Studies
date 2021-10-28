import requests
import json
from requests.models import HTTPBasicAuth

                                #     GET
# nome = requests.get('https://teste-67f75-default-rtdb.firebaseio.com/.json')
# nomeJson = nome.json()
# print(nome.json())

                                    #  POST
token = '5b7e6001408c9e949cd547f014ffaf9a'
key = 'ec74c389ef4a070869602a5c4b1f1fae'
url_site = 'http://www.yaraoficial.com.br/api/variacoes/adicionar'

cor = {

    "pai_id": "0",

    "ativo": "1",

    "nome": "Nome da Variação"

}

requisicao = requests.post(url=url_site,auth=HTTPBasicAuth(token,key),json=cor)
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
