"""Konfiguration för pipelinen.

Värdena läses ur .env om filen finns. Alla har standardvärden, eftersom CI kör
utan .env och bygget annars skulle falla för hela gruppen.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Config:
    site_id: str
    site_name: str
    transport_mode: str
    forecast_minutes: int
    output_path: str
    stationer_path: str


def las_config() -> Config:
    """Läser .env och returnerar konfigurationen."""
    load_dotenv()
    return Config(
        site_id=os.getenv("SITE_ID", "9192"),
        site_name=os.getenv("SITE_NAME", "Slussen"),
        transport_mode=os.getenv("TRANSPORT_MODE", "METRO"),
        forecast_minutes=int(os.getenv("FORECAST_MINUTES", "60")),
        output_path=os.getenv("OUTPUT_PATH", "docs/data/avgangar.json"),
        stationer_path=os.getenv("STATIONER_PATH", "docs/data/hallplatser.json"),
    )
