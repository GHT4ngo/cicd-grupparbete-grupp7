from src.stationer import sok_hallplats

HALLPLATSER = [
    {"id": 9192, "name": "Slussen"},
    {"id": 9001, "name": "T-Centralen"},
    {"id": 9117, "name": "Odenplan"},
]


def test_sokning_ar_skiftlagesokanslig():
    traffar = sok_hallplats("SLUSSEN", HALLPLATSER)

    assert traffar == [{"id": 9192, "name": "Slussen"}]


def test_sokning_hittar_delstrang():
    traffar = sok_hallplats("central", HALLPLATSER)

    assert traffar == [{"id": 9001, "name": "T-Centralen"}]
