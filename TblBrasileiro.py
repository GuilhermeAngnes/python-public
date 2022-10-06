import pandas as pd
import requests
from bs4 import BeautifulSoup

# pagina que vamos trabalhar
url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

nomes_times = soup.find_all('span', class_='hidden-xs')
pontos_times = soup.find_all('th', scope='row')

# print(nomes_times[0].text)
# print(pontos_times[0].text)


for item in range(20):
    dados = (nomes_times[item].text + " " + pontos_times[item].text)
    print(dados)
    # dados.to_excel('dados.xls')
