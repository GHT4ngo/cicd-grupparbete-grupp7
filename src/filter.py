from datetime import datetime


def rensa_bort_skrap(avgangar):
    """Rensar SL:s råsvar innan det plattas ut.

    Körs på svar["departures"], alltså före utplattningen, eftersom fältet
    state bara finns i rådatan och inte i vårt eget datakontrakt.
    """
    nu = datetime.now()  # noqa: DTZ005
    filtrerade = []

    for avgang in avgangar:
        if avgang.get("state") == "CANCELLED":
            continue

        # Turer som redan har gått ligger kvar i svaret en stund. Efter
        # utplattningen syns de inte, för rakna_minuter klampar dem till noll.
        if datetime.fromisoformat(avgang["expected"]) < nu:
            continue

        filtrerade.append(avgang)

    return filtrerade
