from requests_html import HTMLSession
import pandas as pd
import requests


session = HTMLSession()

requisition = session.get(
    "https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/"
)

nome_times = requisition.html.find(".table__team")

pontos = requisition.html.find(".table__stats")

titulo_time = requisition.html.find(".table__team")
titulo_pontos = requisition.html.find(".table__stats")

print(titulo_time[0].text + " " + titulo_pontos[0].text)

for item in range(20):
    dados = (nome_times[item + 1].text + " " + pontos[item + 9].text)
    print(dados)
    # dados.to_excel('dados.xls')
