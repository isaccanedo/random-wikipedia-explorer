"""Author Isac Canedo
Módulo para buscar páginas wiki aleatórias e pedir ao usuário para abrir uma delas

Python:
  - 3.5

Requirementos:
  - requests
  - json
  - webbrowser

Uso:
  - $python3 wiki_random.py

digite o índice do artigo que você gostaria de ver, ou 'r' para tentar novamente e 'n' para sair.
"""
import requests
import webbrowser

page_count = 10
url = (
    "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit="
    + str(page_count)
    + "&format=json"
)


def load():
    response = requests.get(url)
    if response.ok:
        jsonData = response.json()["query"]["random"]
        print("10 Random generted WIKI pages...")
        for idx, j in enumerate(jsonData):
            print(str(idx) + ": ", j["title"])
        i = input(
            "Qual página você quer ver? Digite o index que aparece na lista, (r) para tentar novamente e (n) para sair"
        ).lower()
        if i == "r":
            print("Loading randoms again...")
        elif i == "n":
            print("Auf Wiedersehen!")
            return
        else:
            try:
                jsonData[int(i)]["id"]
            except Exception:
                raise Exception("Wrong Input...")
            print("taking you to the browser...")
            webbrowser.get().open(
                "https://en.wikipedia.org/wiki?curid=" + str(jsonData[int(i)]["id"])
            )
        load()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    load()
