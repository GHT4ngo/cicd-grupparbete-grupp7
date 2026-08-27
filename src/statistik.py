import json
from collections import Counter

with open("docs/data/avgangar.json", "r", encoding="utf-8") as f:
    data = json.load(f)

avgangar = data["avgangar"]
avgangar_antal_json = len(avgangar)

linjer_statistik = Counter(a["linje"] for a in avgangar)
riktningar_statistik = Counter(a["riktning"] for a in avgangar)
print(f"\nTotalt antal avgångar i JSON: {avgangar_antal_json}")

#Count departures by line
print("\nLinjer statistik")
print("-" * 30)

avgangar_antal_linje = 0
for linje, antal in linjer_statistik.items():
    avgangar_antal_linje += antal
    print(f"Linje {linje:>3}: {antal:>2} avgångar")

print(f"Totalt antal avgångar per linje: {avgangar_antal_linje:>2} avgångar")
if avgangar_antal_json == avgangar_antal_linje:
    print("Kontroll OK")
else:
    print("Kontroll misslyckades")

#Count departures by direction
print("\n\nRiktningar statistik")
print("-" * 30)

avgangar_antal_riktning = 0
for riktning, antal in riktningar_statistik.items():
    avgangar_antal_riktning += antal
    print(f"{riktning:<20} {antal:>2} avgångar")

print(f"Totalt antal avgångar per riktning: {avgangar_antal_riktning:>2} avgångar")
if avgangar_antal_json == avgangar_antal_riktning:
    print("Kontroll OK")
else:
    print("Kontroll misslyckades")

#Find the most common direction
vanligaste_riktning, antal = riktningar_statistik.most_common(1)[0]

print(
    f"\nVanligaste riktning: {vanligaste_riktning} "
    f"({antal} avgångar)"
)    

print()