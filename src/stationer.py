import json
from pathlib import Path

import requests

from src.config import las_config


def hamta_hallplatser():
    url = "https://transport.integration.sl.se/v1/sites"
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

    trimmade = []
    for site in hallplatser:
        trimmade.append({"id": site["id"], "namn": site["name"]})

    sokvag = Path(las_config().stationer_path)
    sokvag.parent.mkdir(parents=True, exist_ok=True)

    # Utan indent, eftersom filen har 6511 poster och laddas av webbläsaren.
    with sokvag.open("w", encoding="utf-8") as fil:
        json.dump(trimmade, fil, ensure_ascii=False)

    return trimmade


if __name__ == "__main__":
    sparade = spara_hallplatser()
    print(f"Skrev {len(sparade)} hållplatser till {las_config().stationer_path}")
