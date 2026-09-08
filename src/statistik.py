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

def skriv_statistik(avgangar):
    """Skriver ut statistiken i terminalen.

    Låg tidigare direkt under if __name__ == "__main__". Då kunde pipelinen
    inte anropa den, utan modulen gick bara att köra för hand.
    """
    antal = len(avgangar)
    print(f"\nTotalt antal avgångar: {antal}")

    print("\nLinjer")
    print("-" * 30)

    linjer = rakna_linjer(avgangar)
    for linje, antal_linje in linjer.items():
        print(f"Linje {linje:>3}: {antal_linje:>2} avgångar")

    print(f"Summa: {sum(linjer.values()):>2}")
    print("Kontroll OK" if sum(linjer.values()) == antal else "Kontroll misslyckades")

    print("\nRiktningar")
    print("-" * 30)

    riktningar = rakna_riktningar(avgangar)
    for riktning, antal_riktning in riktningar.items():
        print(f"{riktning:<20} {antal_riktning:>2} avgångar")

    print(f"Summa: {sum(riktningar.values()):>2}")
    print("Kontroll OK" if sum(riktningar.values()) == antal else "Kontroll misslyckades")

    if riktningar:
        vanligaste, antal_vanligaste = riktningar.most_common(1)[0]
        print(f"\nVanligaste riktning: {vanligaste} ({antal_vanligaste} avgångar)")

if __name__ == "__main__":
    skriv_statistik(las_avgangar())
