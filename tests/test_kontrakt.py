import json

FALT = {"linje", "linjegrupp", "transportmedel", "riktning_kod", "riktning", "destination", "avgar_klocka", "minuter"}

def test_filen_foljer_kontraktet():
    with open("docs/data/avgangar.json", encoding="utf-8") as fil:
        data = json.load(fil)
        
    assert set(data) == {"station", "station_id", "uppdaterad", "avgangar"}
    
    for avgang in data["avgangar"]:
        assert set(avgang) == FALT
def test_riktning_kod_och_minuter_ar_giltiga():
    with open("docs/data/avgangar.json", encoding="utf-8") as fil:
        data = json.load(fil)
        
    for avgang in data["avgangar"]:
        assert avgang["riktning_kod"] in (1, 2)
        assert avgang["minuter"] >= 0
