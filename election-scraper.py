import csv
from bs4 import BeautifulSoup
import requests
import pandas



webovky = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

r = requests.get(webovky, headers=headers)
html = r.text
soup = BeautifulSoup(html, "html.parser")

obce_odkazy = soup.select('.center a')
# print(obce_odkazy[0])

###tohle vytvoří první odkaz
# odkazy = [obec['href'] for obec in obce_odkazy]
# print(odkazy[0])


###TOTO VYTVOŘÍ ODKAZY NA DALŠÍ STRÁNKY
odkazy = ['https://volby.cz/pls/ps2017nss/' + obec['href'] for obec in obce_odkazy]
# print(odkazy[0])


obce_jmeno = []
obalky = []
volici_v_seznamu = []
platne_hlasy = []

for odkaz in odkazy[0:4]:
    r = requests.get(odkaz, headers=headers)
    html = r.text
    obce_soup = BeautifulSoup(html, 'html.parser')

    pandas.read_html(webovky, encoding="utf-8")[
        0].to_csv("vysledek0.csv")
    tabulka0 = pandas.read_csv("vysledek0.csv", encoding="utf-8")
    tabulka0 = tabulka0.loc[:, 'Obec':'Obec.1']
    tabulka0 = tabulka0.drop(0)
    pandas.read_html(webovky, encoding="utf-8")[
        1].to_csv("vysledek1.csv")
    tabulka1 = pandas.read_csv("vysledek1.csv", encoding="utf-8")
    tabulka1 = tabulka1.loc[:, 'Obec':'Obec.1']
    tabulka1 = tabulka1.drop(0)

    pandas.read_html(webovky, encoding="utf-8")[
        2].to_csv("vysledek2.csv")
    tabulka2 = pandas.read_csv("vysledek2.csv", encoding="utf-8")
    tabulka2 = tabulka2.loc[:, 'Obec':'Obec.1']
    tabulka2 = tabulka2.drop(0)
    # print(tabulka, tabulka1, tabulka2)

    vsechny_obce = pandas.concat([tabulka0, tabulka1, tabulka2], ignore_index=True)
    #print(vsechny_obce)
    vsechny_obce.to_csv("vsechny_obce.csv", encoding="utf-8")


    obce_jmeno = []

    obce_jmeno = obce_soup.select("h3")[2]
    for obec_jmeno in obce_jmeno:
        obce_jmeno.append(obec_jmeno)
        # obce_jmeno = str(obce_jmeno)
        # obec_jmeno = obec_jmeno.strip("\nObec:")
        # print(obce_jmeno)

    volici_v_seznamu = obce_soup.find_all(headers="sa2")
    for volic in volici_v_seznamu:
        volici_v_seznamu = volic.text.strip()
        #print(volici_v_seznamu)

    obalky = obce_soup.find_all(headers="sa3")
    for obalka in obalky:
        obalky = obalka.text.strip()
        # print(obalky)

    platne_hlasy = obce_soup.find_all(headers="sa6")
    for p in platne_hlasy:
        platne_hlasy = p.text.strip()
        # print(platne_hlasy)

    pocet_hlasu = obce_soup.find_all(headers="t1sa2 t1sb3")
    pocet_hlasu2 = obce_soup.find_all(headers="t2sa2 t2sb3")
    pocet_hlasu.extend(pocet_hlasu2)


    for hlas in pocet_hlasu:
        pocet_hlasu = hlas.text.strip()
        # print(pocet_hlasu)

    strany = obce_soup.find_all(headers="t1sa1 t1sb2")
    strany2 = obce_soup.find_all(headers="t2sa1 t2sb2")
    strany.extend(strany2)

    list_stran = []

    for strana in strany:
        list_stran.append(strana.text.strip())
        # print(list_stran)

    vysledky_stran_list = []

    vysledky_stran = obce_soup.find_all(headers="t1sa2 t1sb3")
    vysledky_stran2 = obce_soup.find_all(headers="t2sa2 t2sb3")
    vysledky_stran.extend(vysledky_stran2)
    # print(vysledky_stran)

    for s in vysledky_stran:
        vysledky_stran_list.append(s.text.strip())
        # print(vysledky_stran_list)



    with open("volby.csv", mode='w', newline='', encoding="utf-8") as f:
        f_writer = csv.writer(f)
        f_writer.writerow(list_stran)
        f_writer.writerows([vysledky_stran_list])
        f.close()


