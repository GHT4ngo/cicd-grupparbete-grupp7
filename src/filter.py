def rensa_bort_skräp(avgångar):
    return [
        avgång
        for avgång in avgångar
        if avgång.get("state") != "CANCELLED"
        and avgång.get("minuter", 0) >= 0
    ]