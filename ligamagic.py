import requests
from bs4 import BeautifulSoup
import codecs

def main():
    url = "http://www.ligamagic.com.br/"


    with open('cards.txt') as f:


        content = f.readlines()

        for line in content:
            file = codecs.open("newfile.txt", "a","utf-8")


            querystring = {"view": "cards/search", "card": line}
            response = requests.request("GET", url, params=querystring)
            soup = BeautifulSoup(response.content, "lxml")
            try:
                card = soup.find('p', class_='subtitulo-card').getText()
                print(card)
                card = card+'\n'
                file.write(card)
            except:
                print("NOME ERRADO - ",line.replace('\n', ''))
                error="NOME ERRADO - "+line
                file.write(error)

            file.close()


main()