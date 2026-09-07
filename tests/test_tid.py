from datetime import datetime

from src import transformera


class FastDatetime(datetime):
    @classmethod
    def now(cls):
        return cls(2026, 9, 3, 12, 0, 0)


def test_noll_minuter(monkeypatch):
    monkeypatch.setattr(transformera, "datetime", FastDatetime)

    assert transformera.rakna_minuter("2026-09-03T12:00:00") == 0


def test_positiva_minuter(monkeypatch):
    monkeypatch.setattr(transformera, "datetime", FastDatetime)

    assert transformera.rakna_minuter("2026-09-03T12:03:00") == 3


def test_negativa_minuter_blir_noll(monkeypatch):
    monkeypatch.setattr(transformera, "datetime", FastDatetime)

    assert transformera.rakna_minuter("2026-09-03T11:55:00") == 0