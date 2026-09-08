import json
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


def spara_hallplatser(hallplatser=None):
    """Skriver alla hållplatser till en fil som sökrutan på sidan läser."""
    if hallplatser is None:
        hallplatser = hamta_hallplatser()

    # Flera hållplatser delar namn, till exempel tre stycken som heter
    # Västertorp. stop_areas säger hur många lägen hållplatsen har, och den
    # riktiga knutpunkten har alltid flest. Sökrutan sorterar på det.
    trimmade = []
    for site in hallplatser:
        trimmade.append({
            "id": site["id"],
            "namn": site["name"],
            "storlek": len(site.get("stop_areas", [])),
        })

    sokvag = Path(las_config().stationer_path)
    sokvag.parent.mkdir(parents=True, exist_ok=True)

    # Utan indent, eftersom filen har 6512 poster och laddas av webbläsaren.
    with sokvag.open("w", encoding="utf-8") as fil:
        json.dump(trimmade, fil, ensure_ascii=False)

    return trimmade


if __name__ == "__main__":
    sparade = spara_hallplatser()
    print(f"Skrev {len(sparade)} hållplatser till {las_config().stationer_path}")
