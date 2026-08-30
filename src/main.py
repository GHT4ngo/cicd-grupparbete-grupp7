from datetime import datetime

from src.config import las_config
from src.hamta import hamta_avgangar
from src.resultat import skriv_resultat
from src.transformera import platta_ut_avgangar
from src.validera import validera_post


def main():
    config = las_config()
    
    svar = hamta_avgangar() 
    avgangar = platta_ut_avgangar(svar)
    
    for avgang in avgangar:
        validera_post(avgang)
        
    riktningar = []
    sedda = set()
    for avgang in avgangar:
        nyckel = (avgang["riktning_kod"], avgang["riktning"])
        if nyckel not in sedda:
            sedda.add(nyckel)
            riktningar.append({
                "riktning_kod": avgang["riktning_kod"],
                "riktning": avgang["riktning"],
            })

    resultat = {
        "station": config.site_name,
        "station_id": config.site_id,
        "uppdaterad": datetime.now().isoformat(),  # noqa: DTZ005
        "riktningar": riktningar,
        "avgangar": avgangar,
    }

    skriv_resultat(resultat)
    print(f"Skrev {len(avgangar)} avgångar")


if __name__ == "__main__":
    main()