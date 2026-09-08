OBLIGATORISKA_FALT = {
    "linje",
    "linjegrupp",
    "transportmedel",
    "riktning_kod",
    "riktning",
    "destination",
    "avgar_klocka",
    "minuter",
    "farg",
    "visning",
}


def validera_post(post):
    saknade_falt = OBLIGATORISKA_FALT - post.keys()

    if saknade_falt:
        raise ValueError(f"Saknade fält: {saknade_falt}")

    if post["riktning_kod"] not in (1, 2):
        raise ValueError("riktning_kod måste vara 1 eller 2")

    if post["minuter"] < 0:
        raise ValueError("minuter får inte vara negativt")