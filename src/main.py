from datetime import datetime

from src.avvikelser import hamta_avvikelser
from src.config import las_config
from src.filter import rensa_bort_skrap
from src.hamta import hamta_avgangar
from src.resultat import skriv_resultat
from src.statistik import skriv_statistik
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
        # Hämtas efter filtret, så att meddelandena hör ihop med de
        # avgångar som faktiskt visas på tavlan.
        "avvikelser": hamta_avvikelser(svar),
    }

    skriv_resultat(resultat)
    print(f"Skrev {len(avgangar)} avgångar")

    skriv_statistik(avgangar)


if __name__ == "__main__":
    main()
