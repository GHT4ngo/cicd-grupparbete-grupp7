from datetime import datetime

from src.config import las_config
from src.filter import rensa_bort_skrap
from src.hamta import hamta_avgangar
from src.resultat import skriv_resultat
from src.transformera import platta_ut_avgangar
from src.validera import validera_post


def main():
    config = las_config()

    svar = hamta_avgangar()

    # Rensa inställda och redan avgångna turer medan state och expected
    # fortfarande finns kvar i rådatan.
    svar["departures"] = rensa_bort_skrap(svar["departures"])

    avgangar = platta_ut_avgangar(svar)

    for avgang in avgangar:
        validera_post(avgang)

    resultat = {
        "station": config.site_name,
        "station_id": config.site_id,
        "uppdaterad": datetime.now().isoformat(),  # noqa: DTZ005
        "avgangar": avgangar,
    }

    skriv_resultat(resultat)
    print(f"Skrev {len(avgangar)} avgångar")


if __name__ == "__main__":
    main()
