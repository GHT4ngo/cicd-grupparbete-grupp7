from collections import defaultdict


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
        }
        resultat.append(avgang)
    return resultat


def gruppera_per_riktning(poster):
    grupper = defaultdict(lambda: defaultdict(list))

    for post in poster:
        grupper[post["linjegrupp"]][post["riktning_kod"]].append(post)

    return grupper
