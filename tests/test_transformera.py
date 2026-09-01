from src.transformera import platta_ut_avgangar

SVAR = {
    "departures": [
        {
            "direction_code": 1,
            "direction": "Mot norr",
            "destination": "Mörby centrum",
            "expected": "2099-01-01T13:22:00",
            "line": {
                "designation": "14",
                "transport_mode": "METRO",
                "group_of_lines": "Tunnelbanans röda linje",
            },
        }
    ]
}


def test_alla_atta_falt_finns():
    poster = platta_ut_avgangar(SVAR)
    post = poster[0]

    assert set(post.keys()) == {
        "linje",
        "linjegrupp",
        "transportmedel",
        "riktning_kod",
        "riktning",
        "destination",
        "avgar_klocka",
        "minuter",
    }