import json

FALT = {"linje", "linjegrupp", "transportmedel", "riktning_kod", "riktning", "destination", "avgar_klocka", "minuter"}

def test_filen_foljer_kontraktet():
    with open("docs/data/avgangar.json", encoding="utf-8") as fil:
        data = json.load(fil)
        
    assert set(data) == {"station", "station_id", "uppdaterad", "avgangar"}
    
    for avgang in data["avgangar"]:
        assert set(avgang) == FALT
