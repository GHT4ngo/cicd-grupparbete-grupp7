import json
from collections import Counter

from src.config import las_config


def las_avgangar():
    with open(las_config().output_path, encoding="utf-8") as fil:
        return json.load(fil)["avgangar"]

def rakna_linjer(avgangar):
    return Counter(a["linje"] for a in avgangar)

def rakna_riktningar(avgangar):
    return Counter(a["riktning"] for a in avgangar)

if __name__ == "__main__":
    #Read departure data from file
    avgangar = las_avgangar()
    avgangar_antal_json = len(avgangar)
    print(f"\nTotalt antal avgångar i JSON: {avgangar_antal_json}")

    #Count departures by line
    print("\nLinjer statistik")
    print("-" * 30)

    linjer_statistik = rakna_linjer(avgangar)
    for linje, antal in linjer_statistik.items():
        print(f"Linje {linje:>3}: {antal:>2} avgångar")

    avgangar_antal_linje = sum(linjer_statistik.values())
    print(f"Totalt antal avgångar: {avgangar_antal_linje:>2} avgångar")
    if avgangar_antal_json == avgangar_antal_linje:
        print("Kontroll OK")
    else:
        print("Kontroll misslyckades")

    #Count departures by direction
    print("\n\nRiktningar statistik")
    print("-" * 30)

    riktningar_statistik = rakna_riktningar(avgangar)
    for riktning, antal in riktningar_statistik.items():
        print(f"{riktning:<20} {antal:>2} avgångar")

    avgangar_antal_riktning = sum(riktningar_statistik.values())
    print(f"Totalt antal avgångar: {avgangar_antal_riktning:>2} avgångar")
    if avgangar_antal_json == avgangar_antal_riktning:
        print("Kontroll OK")
    else:
        print("Kontroll misslyckades")

    #Find the most common direction
    vanligaste_riktning, antal = riktningar_statistik.most_common(1)[0]
    print(
        f"\nVanligaste riktning: {vanligaste_riktning} "
        f"({antal} avgångar)"
    )    
    print()