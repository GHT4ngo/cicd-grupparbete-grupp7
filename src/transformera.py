from collections import defaultdict
from datetime import datetime


def rakna_minuter(expected_tid_str):
    expected_tid = datetime.fromisoformat(expected_tid_str)

    nu = datetime.now()  # noqa: DTZ005

    differens = expected_tid - nu

    minuter = round(differens.total_seconds() / 60)

    return max(0, minuter)


def platta_ut_avgangar(svar):
    resultat = []
    for x in svar["departures"]:
        avgang = {
            "riktning_kod": x["direction_code"],
            "riktning": x["direction"],
            "destination": x["destination"],
            "avgar_klocka": x["expected"][11:16],
            "linje": x["line"]["designation"],
            "transportmedel": x["line"]["transport_mode"],
            "linjegrupp": x["line"].get("group_of_lines"),
            "minuter": rakna_minuter(x["expected"]),
        }
        resultat.append(avgang)
    return resultat


def gruppera_per_riktning(poster):
    grupper = defaultdict(lambda: defaultdict(list))

    for post in poster:
        grupper[post["linjegrupp"]][post["riktning_kod"]].append(post)

    return grupper
