# Formaterar minuter till text
def formatera_minuter(minuter):
    if minuter == 0:
        return "Nu"
    return f"{minuter} min"


# Hämtar klockslaget från expected
def hamta_klockslag(expected):
    return expected[11:16]
