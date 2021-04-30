# Election-scraper

Třetí projekt od Engeta.


## Popis projektu
Tento projekt slouží k extrahování výsledků voleb v roce 2017. Zde je odkaz k prohlédnutí daného webu: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ


## Instalace knihoven
Knihovny, které jsou v kódu použity, jsou uložené v souboru requirements.txt. Pro instalaci je vhodné použít nové virtuální prostředí a s nainstalovaným manažerem
spustit následovně: 

$ pip3 --version 

$ pip3 install -r requirements.txt


## Spuštění projektu 
Spuštění souboru election-scraper.py vyžaduje zadání dvou argumentů z příkazové řádky.
python election-scraper.py <odkaz-konkretniho-uzemniho-celku> <nazev-vysledneho-souboru-s-priponou-.csv>
Výsledky se vám uloží do vámi zvoleného názvu souboru ve formátu .csv.

## Ukázka projektu
Výsledky hlasování pro okres :

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105
2. argument: vysledky_zdarsko.csv

### Spuštění programu: 
python election-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105" "vysledky_zdarsko.csv"

### Průběh stahování: 

STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105

UKLADAM DATA DO SOUBORU: vysledky_zdarsko.csv

UKONCUJI election-scraper


