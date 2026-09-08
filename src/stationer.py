import json
import sys
from pathlib import Path

import requests

from src.config import las_config


def hamta_hallplatser():
    # expand=true behövs för fältet stop_areas, som spara_hallplatser
    # använder för att skilja hållplatser med samma namn åt.
    url = "https://transport.integration.sl.se/v1/sites?expand=true"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def sok_hallplats(namn, hallplatser=None):
    if hallplatser is None:
        hallplatser = hamta_hallplatser()

    traffar = []
    for site in hallplatser:
        if namn.lower() in site["name"].lower():
            traffar.append({"id": site["id"], "name": site["name"]})
    return traffar


# SL:s egna namn på lägestyper, översatta till samma färdmedelsnamn som
# resten av kedjan använder. Sidan färglägger och namnger dem sedan själv.
FARDMEDEL_PER_TYP = {
    "METROSTN": "METRO",
    "BUSTERM": "BUS",
    "TRAMSTN": "TRAM",
    "RAILWSTN": "TRAIN",
    "SHIPBER": "SHIP",
    "FERRYBER": "SHIP",
}


def hamta_lagestyper():
    """Ger en uppslagning från lägets id till färdmedel.

    Hållplatslistan säger bara vilka lägen en hållplats har, inte vad de är
    för sorts lägen. Den uppgiften ligger i stop-points.
    """
    url = "https://transport.integration.sl.se/v1/stop-points"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    typer = {}
    for lage in response.json():
        omrade = lage.get("stop_area", {})
        fardmedel = FARDMEDEL_PER_TYP.get(omrade.get("type"))
        if fardmedel:
            typer[omrade["id"]] = fardmedel
    return typer


def namn_for_id(site_id):
    """Slår upp hållplatsens namn i den sparade listan.

    Används av flaggan --station, så att tavlan visar rätt namn och inte
    det som råkar stå i .env. Saknas filen får id:t duga som namn.
    """
    sokvag = Path(las_config().stationer_path)
    if not sokvag.exists():
        return str(site_id)

    with sokvag.open(encoding="utf-8") as fil:
        for hallplats in json.load(fil):
            if str(hallplats["id"]) == str(site_id):
                return hallplats["namn"]

    return str(site_id)


def spara_hallplatser(hallplatser=None, lagestyper=None):
    """Skriver alla hållplatser till en fil som sökrutan på sidan läser."""
    if hallplatser is None:
        hallplatser = hamta_hallplatser()

    if lagestyper is None:
        lagestyper = hamta_lagestyper()

    # Flera hållplatser delar namn, till exempel tre stycken som heter
    # Västertorp. stop_areas säger hur många lägen hållplatsen har, och den
    # riktiga knutpunkten har alltid flest. Sökrutan sorterar på det.
    trimmade = []
    for site in hallplatser:
        omraden = site.get("stop_areas", [])

        # Samma hållplats kan ha både tunnelbana och buss. Sorterat, så att
        # ordningen på sidan blir densamma varje gång filen skrivs om.
        fardmedel = set()
        for omrade in omraden:
            if omrade in lagestyper:
                fardmedel.add(lagestyper[omrade])

        trimmade.append({
            "id": site["id"],
            "namn": site["name"],
            "storlek": len(omraden),
            "fardmedel": sorted(fardmedel),
        })

    sokvag = Path(las_config().stationer_path)
    sokvag.parent.mkdir(parents=True, exist_ok=True)

    # Utan indent, eftersom filen har 6512 poster och laddas av webbläsaren.
    with sokvag.open("w", encoding="utf-8") as fil:
        json.dump(trimmade, fil, ensure_ascii=False)

    return trimmade


if __name__ == "__main__":
    # Med ett sökord letar den upp hållplatsen, till exempel för att hitta
    # ett SITE_ID att lägga i .env. Utan sökord skrivs hela listan till fil.
    if len(sys.argv) > 1:
        for traff in sok_hallplats(sys.argv[1]):
            print(f"{traff['id']:>6}  {traff['name']}")
    else:
        sparade = spara_hallplatser()
        print(f"Skrev {len(sparade)} hållplatser till {las_config().stationer_path}")
