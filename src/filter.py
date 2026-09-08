def rensa_bort_skrap(avgangar):
    filtrerade = []

    for avgang in avgangar:
        if avgang.get("state") != "CANCELLED":
            filtrerade.append(avgang)

    return filtrerade