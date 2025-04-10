import requests 
from bs4 import BeautifulSoup

print("\nConectando ao site")

url = "http://www.uol.com.br"

resposta = requests.get(url)
if resposta.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print("Conexão mal-sucedida!. Código do erro: ", resposta.status_code)
    exit()
    
print("\nAnalisando a estrutura do site!")

soup = BeautifulSoup(resposta.text, "html.parser")

pageTitle = soup.title.string
print(f"exibindo o título da página: {pageTitle}")

print("\nProcurando os títulos das notícias")
titles = soup.find_all(["h2", "h3"])

keywords = ["acidente", "inteligência artificial", "doméstico"]
filteredtitles = []


print("\n=========titulos enumerados=========")
# for i, titles in enumerate(titles, 1):
#     print(f"{i}.{titles.get_text(strip = True)}")
for title in titles:
    texto = title.get_text(strip = True)
    
    if any(palavra.lower() in texto.lower() for palavra in keywords):
        linkTag = title.find('a')
        link = linkTag['href'] if linkTag and linkTag.has_attr('href') else 'link indisponivel'
        filteredtitles.append((texto,link))

for i, (texto, link) in enumerate(filteredtitles, 1):
    print(f"{i}.{texto}\n {link}")