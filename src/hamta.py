import requests

from src.config import las_config


def hamta_avgangar(config=None):
    # Flaggorna i main.py kan skicka in en egen config. Utan argument
    # läses den ur .env som förut.
    if config is None:
        config = las_config()

    url = (
        f"https://transport.integration.sl.se/v1/sites/"
        f"{config.site_id}/departures"
    )

    params = {
        "transport": config.transport_mode or None,
        "forecast": config.forecast_minutes,
    }

    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()
