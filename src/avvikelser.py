def hamta_avvikelser(svar):
    """Plockar ut störningsmeddelanden ur SL:s råsvar.

    Två fält innehåller dem. stop_deviations gäller hela hållplatsen, till
    exempel en avstängd hiss, och deviations gäller en enskild avgång. Båda
    kan saknas helt, därför .get med tom lista som standardvärde.
    """
    meddelanden = []

    for avvikelse in svar.get("stop_deviations", []):
        text = avvikelse.get("message")
        # Samma meddelande ligger ofta på flera avgångar, till exempel
        # Inställd på varje inställd tur. Vi vill bara ha det en gång.
        if text and text not in meddelanden:
            meddelanden.append(text)

    for avgang in svar.get("departures", []):
        for avvikelse in avgang.get("deviations", []):
            text = avvikelse.get("message")
            if text and text not in meddelanden:
                meddelanden.append(text)

    return meddelanden
