from src import linjer


def test_bla_linje():
    linjegrupp = "Tunnelbanans blå linje"

    assert linjer.hamta_farg(linjegrupp) == "#007db8"

def test_gron_linje():
    linjegrupp = "Tunnelbanans gröna linje"

    assert linjer.hamta_farg(linjegrupp) == "#148541"

def test_rod_linje():
    linjegrupp = "Tunnelbanans röda linje"

    assert linjer.hamta_farg(linjegrupp) == "#d71d24"

def test_annan_linje():
    linjegrupp = "Annan linje"

    assert linjer.hamta_farg(linjegrupp) == "#9aa4b2"

def test_ingen_linje():
    linjegrupp = None

    assert linjer.hamta_farg(linjegrupp) == "#9aa4b2"
