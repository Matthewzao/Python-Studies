import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
page = requests.get("https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome..69i57j0i131i433i512l2j0i433i512j0i131i433i512j0i433i512l5.677j0j7&sourceid=chrome&ie=UTF-8",headers=headers)

#print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

#span class = DFlfde SwHCTb
atributos = {'class':'g'}

valor_dolar = soup.find_all("span",class_="DFlfde SwHCTb")[0]

print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar['data-value'])


#resposta = soup.find_all("div",attrs=atributos)
#print(resposta[0].get_text())

    