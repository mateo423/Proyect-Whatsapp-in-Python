import requests
from bs4 import BeautifulSoup

url = "https://www.frasess.net/frases-romanticas-para-enamorar-71.html"

pagina = requests.get(url)

bs = BeautifulSoup(pagina.content, 'html.parser')


mensaje = bs.find_all('div', class_='quote_text')

texto = open('mensaje.txt', 'w')

for i in mensaje:
    texto.write(i.text)

texto.close()
