import pytest

from src.validera import validera_post

GILTIG_POST = {
    "linje": "14",
    "linjegrupp": None,
    "transportmedel": "METRO",
    "riktning_kod": 2,
    "riktning": "Fruängen",
    "destination": "Liljeholmen",
    "avgar_klocka": "13:22",
    "minuter": 3,
    "farg": "#5a6472",
    "visning": "3 min",
}


def test_giltig_post():
    validera_post(GILTIG_POST)


def test_saknat_falt():
    post = GILTIG_POST.copy()
    del post["destination"]

    with pytest.raises(ValueError):
        validera_post(post)


def test_fel_riktning_kod():
    post = GILTIG_POST.copy()
    post["riktning_kod"] = 3

    with pytest.raises(ValueError):
        validera_post(post)


def test_negativa_minuter():
    post = GILTIG_POST.copy()
    post["minuter"] = -2

    with pytest.raises(ValueError):
        validera_post(post)
