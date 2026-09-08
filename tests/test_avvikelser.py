import json

from src.avvikelser import hamta_avvikelser

EXEMPEL = "tests/exempel/avgangar_slussen.json"


def las_exempel():
    with open(EXEMPEL, encoding="utf-8") as fil:
        return json.load(fil)


def test_tomt_svar_ger_tom_lista():
    assert hamta_avvikelser({}) == []


def test_svar_utan_storningar_ger_tom_lista():
    svar = {"departures": [{"destination": "Mörby centrum"}], "stop_deviations": []}

    assert hamta_avvikelser(svar) == []


def test_meddelande_pa_avgang_kommer_med():
    avvikelser = hamta_avvikelser(las_exempel())

    assert "Inställd" in avvikelser


def test_samma_meddelande_raknas_en_gang():
    # Exempelfilen har tre avgångar som alla säger Inställd.
    avvikelser = hamta_avvikelser(las_exempel())

    assert avvikelser.count("Inställd") == 1


def test_hela_hallplatsen_kommer_forst():
    svar = {
        "stop_deviations": [{"message": "Hissen är avstängd"}],
        "departures": [{"deviations": [{"message": "Inställd"}]}],
    }

    assert hamta_avvikelser(svar) == ["Hissen är avstängd", "Inställd"]
