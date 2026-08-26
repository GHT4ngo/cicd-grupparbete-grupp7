import json
from pathlib import Path

from src.config import las_config


def skriv_resultat(data):
    config = las_config()
    sokvag = Path(config.output_path)
    sokvag.parent.mkdir(parents=True, exist_ok=True)

    with sokvag.open("w", encoding="utf-8") as fil:
        json.dump(data, fil, ensure_ascii=False, indent=2)