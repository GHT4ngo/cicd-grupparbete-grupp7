_LINJEFARGER = {
    "Tunnelbanans gröna linje": "#148541",
    "Tunnelbanans röda linje": "#d71d24",
    "Tunnelbanans blå linje": "#007db8",
}

STANDARDFARG = "#9aa4b2"

def hamta_farg(linjegrupp):
    return _LINJEFARGER.get(linjegrupp, STANDARDFARG)
