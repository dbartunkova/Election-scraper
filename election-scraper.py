import csv
from bs4 import BeautifulSoup
import requests
import sys


def main():
    if "https://volby.cz/pls/ps2017nss/" not in sys.argv[1]:
        print(f"Zadán špatný web.")
        sys(exit())

    else:
        output_path = sys.argv[2]
        starting_url = sys.argv[1]

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

        r = requests.get(starting_url, headers=headers)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        obce_odkazy = soup.select('.center a') and soup.select('.cislo a')

        odkazy = ['https://volby.cz/pls/ps2017nss/' + obec['href'] for obec in obce_odkazy]

        obce_jmeno = []
        obalky = []
        volici_v_seznamu = []
        platne_hlasy = []

        for odkaz in odkazy:
            r = requests.get(odkaz, headers=headers)
            html = r.text
            obce_soup = BeautifulSoup(html, 'html.parser')

            obce_jmeno = []
            obce_jmeno = obce_soup.select("h3")[2]
            for obec_jmeno in obce_jmeno:
                obce_jmeno.append(obec_jmeno)
                obec_jmeno = obec_jmeno.strip("\nObec:")

            volici_v_seznamu = obce_soup.find_all(headers="sa2")[0].text

            obalky = obce_soup.find_all(headers="sa3")[0].text

            platne_hlasy = obce_soup.find_all(headers="sa6")[0].text

            pocet_hlasu = obce_soup.find_all(headers="t1sa2 t1sb3")
            pocet_hlasu2 = obce_soup.find_all(headers="t2sa2 t2sb3")
            pocet_hlasu3 = obce_soup.find_all(headers="t1sa2 t1sb3")
            pocet_hlasu.extend(pocet_hlasu2)
            pocet_hlasu.extend(pocet_hlasu3)

            for hlas in pocet_hlasu:
                pocet_hlasu = hlas.text.strip("&nbsp;")
                #print(pocet_hlasu)

            strany = obce_soup.find_all(headers="t1sa1 t1sb2")
            strany2 = obce_soup.find_all(headers="t2sa1 t2sb2")
            strany.extend(strany2)

            list_stran = []

            for strana in strany:
                list_stran.append(strana.text.strip())

            vysledky_stran_list = []
            vysledky_stran = obce_soup.find_all(headers="t1sa2 t1sb3")
            vysledky_stran2 = obce_soup.find_all(headers="t2sa2 t2sb3")
            vysledky_stran.extend(vysledky_stran2)

            for s in vysledky_stran:
                vysledky_stran_list.append(s.text.strip())


            dohromady = {"NAZEV": obec_jmeno, "VOLICI": volici_v_seznamu, "OBALKY": obalky, "PLATNE": platne_hlasy,
                         "VYSLEDKY": vysledky_stran_list}

            with open(output_path, mode='a', newline='', encoding="utf-8") as f:
                header = ["NAZEV", "VOLICI", "OBALKY", "PLATNE", "VYSLEDKY", "{}".format(list_stran)]
                writer = csv.DictWriter(f, header)
                writer.writeheader()
                writer.writerow(
                {
                    "NAZEV": dohromady["NAZEV"],
                    "VOLICI": dohromady["VOLICI"],
                    "OBALKY": dohromady["OBALKY"],
                    "PLATNE": dohromady["PLATNE"],
                    "VYSLEDKY": dohromady["VYSLEDKY"],
                }
                )

                f.close()

if __name__ == "__main__":
    print(f"STAHUJI DATA Z VYBRANEHO URL: {sys.argv[1]}")
    print(f"UKLADAM DATA DO SOUBORU: {sys.argv[2]}")
    print(f"UKONCUJI election-scraper")

    main()
