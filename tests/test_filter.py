from datetime import datetime, timedelta

from src.filter import rensa_bort_skrap


def klocka(minuter):
    """Ger en tidsstämpel så många minuter fram eller bak från nu."""
    return (datetime.now() + timedelta(minutes=minuter)).isoformat()  # noqa: DTZ005


def test_installd_tur_forsvinner():
    avgangar = [
        {"state": "EXPECTED", "expected": klocka(5), "destination": "Mörby centrum"},
        {"state": "CANCELLED", "expected": klocka(7), "destination": "Fruängen"},
    ]

    kvar = rensa_bort_skrap(avgangar)

    assert len(kvar) == 1
    assert kvar[0]["destination"] == "Mörby centrum"


def test_tur_som_redan_gatt_forsvinner():
    avgangar = [
        {"state": "EXPECTED", "expected": klocka(-3), "destination": "Ropsten"},
        {"state": "EXPECTED", "expected": klocka(4), "destination": "Norsborg"},
    ]

    kvar = rensa_bort_skrap(avgangar)

    assert len(kvar) == 1
    assert kvar[0]["destination"] == "Norsborg"


def test_tom_lista_ger_tom_lista():
    assert rensa_bort_skrap([]) == []


def test_avgang_utan_state_behalls():
    # SL skickar inte alltid med state. Saknas det är turen inte inställd.
    avgangar = [{"expected": klocka(6), "destination": "Alvik"}]

    assert len(rensa_bort_skrap(avgangar)) == 1
