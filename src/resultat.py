import json
from pathlib import Path


def skriv_resultat(data, output_path="docs/data/avgangar.json"):
    sokvag = Path(output_path)
    sokvag.parent.mkdir(parents=True, exist_ok=True)

    with sokvag.open("w", encoding="utf-8") as fil:
        json.dump(data, fil, ensure_ascii=False, indent=2)