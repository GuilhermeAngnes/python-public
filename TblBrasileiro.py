from requests_html import HTMLSession

session = HTMLSession()

requisition = session.get(
    "https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/"
    )

nome_times = requisition.html.find(".table__team")

pontos = requisition.html.find(".table__stats")

#print(nome_times[1].text)

#print(pontos[9].text)

for item in range(20):
    print(nome_times[item + 1].text + " " + pontos[item + 9].text)

