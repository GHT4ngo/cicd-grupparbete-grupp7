# Färgerna är samma hexvärden som CSS-variablerna i docs/index.html, så att
# tavlan och datafilen aldrig visar två olika färger för samma linje.
_LINJEFARGER = {
    "Tunnelbanans gröna linje": "#148541",
    "Tunnelbanans röda linje": "#d71d24",
    "Tunnelbanans blå linje": "#007db8",
    "Blåbuss": "#005aa3",
    "Pendeltåg": "#f0677f",
    "Pendelbåt": "#00a5b5",
}

STANDARDFARG = "#5a6472"


def hamta_farg(linjegrupp):
    # group_of_lines saknas helt för de flesta bussar, därför .get med default.
    return _LINJEFARGER.get(linjegrupp, STANDARDFARG)
