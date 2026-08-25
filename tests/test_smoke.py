"""Tillfälligt test så att CI har något att köra.

pytest avslutar med kod 5 när noll test hittas, och då blir CI röd trots att
ingenting är fel. Den här filen kan tas bort när uppgift 22 och 23 är inne.
"""


def test_ci_kor_tester():
    assert True
