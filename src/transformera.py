from datetime import datetime

from src.linjer import hamta_farg
from src.tid import formatera_minuter, hamta_klockslag


def rakna_minuter(expected_tid_str):
    expected_tid = datetime.fromisoformat(expected_tid_str)

    nu = datetime.now()  # noqa: DTZ005

    differens = expected_tid - nu

    minuter = round(differens.total_seconds() / 60)

    return max(0, minuter)


def platta_ut_avgangar(svar):
    resultat = []
    for x in svar["departures"]:
        minuter = rakna_minuter(x["expected"])
        avgang = {
            "riktning_kod": x["direction_code"],
            "riktning": x["direction"],
            "destination": x["destination"],
            "avgar_klocka": hamta_klockslag(x["expected"]),
            "linje": x["line"]["designation"],
            "transportmedel": x["line"]["transport_mode"],
            "linjegrupp": x["line"].get("group_of_lines"),
            "farg": hamta_farg(x["line"].get("group_of_lines")),
            "minuter": minuter,
            "visning": formatera_minuter(minuter),
        }
        resultat.append(avgang)
    return resultat
