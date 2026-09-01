# Individuell examination

Utöver grupparbetet gör **var och en en egen skriftlig rapport**. Den här filen
är en checklista så att ingen upptäcker för sent att något saknas.

Rapporten skriver du själv. Den här filen ersätter den inte, den hjälper dig
bara hitta det du ska länka till.

| | |
|---|---|
| Omfattning | 4 till 6 sidor |
| Betyg | IG, G eller VG |
| Format | PDF, Word eller Markdown |
| Innehåll | Ditt namn, gruppnummer, länk till repot, rapporten |

Rubriknumreringen 1.1, 1.2 och så vidare ska följas, så att läraren ser vad som
besvarar vad. Rapporten ska gå att läsa av någon som aldrig sett vårt projekt.

Du får diskutera med gruppen, men texten ska vara din egen. Kopierade
definitioner utan egen förklaring ger inte godkänt.

***

## Läs det här först

Två saker i uppgiften **går inte att fixa i efterhand**. De kräver att du gör
något i repot medan gruppen fortfarande arbetar.

**Punkt 2.3 kräver att du har granskat någon annans pull request.** Alltså en
skriven kommentar med innehåll. Att bara klicka Approve utan text räcker inte,
det finns inget att skriva om i rapporten då.

**Punkt 2.4 kräver att du har fått en granskning.** Det förutsätter att du
öppnat en pull request och att någon annan hunnit skriva på den.

Är tavlan tom och alla PR:er mergade när du börjar skriva, då är det för sent.
Kolla din rad i tabellen längst ner i den här filen redan nu.

> **Om att repot är privat.** Uppgiften säger "länka till gruppens gemensamma
> **publika** repo". Vårt repo är privat, och det har vi gjort avsiktligt.
>
> Läraren, `LindaLiBogardi`, är redan medlem i repot och ser därför allt du
> länkar till. Det löser problemet i praktiken. Nämn det ändå i en mening i
> rapporten, så att ingen tror att en länk är trasig. Behöver du visa något för
> någon utanför repot fungerar skärmdumpar, uppgiften nämner själv att de är
> välkomna.

***

## Del 1, begrepp, krav för G

Förklara med egna ord och **koppla varje svar till något konkret hos oss**. Det
är kopplingen som bedöms, inte definitionen.

| Nr | Fråga | Var du hittar exempel hos oss |
|---|---|---|
| 1.1 | Vad är DevOps, vilket problem löser vårt projekt, minst två delar av kedjan | `README.md` och `SUGGESTION.md` beskriver problemet |
| 1.2 | Vad är CI, vad är CD, hur skiljer de sig, vilket använde vi | Vi har båda. CI är `.github/workflows/ci.yml`, CD är Cloudflare som bygger om `docs/` vid varje merge till `main`, styrt av `wrangler.jsonc` |
| 1.3 | Vad är en pipeline, förklara vår build pipeline | Två att välja på, se nedan |
| 1.4 | Hur gruppen arbetade | `TASKS.md`, uppgiftstavlan, en uppgift per branch och pull request |
| 1.5 | Syftet med kodgranskning | Använd ett verkligt exempel från våra PR:er |

Om 1.3, vi har egentligen **två** pipelines och det är värt en poäng att se det:

1. **CI-pipelinen.** Push eller pull request startar `ci.yml`, som hämtar koden,
   sätter upp Python, installerar från `requirements.txt`, kör `ruff check .`
   och sedan `pytest -v`.
2. **Datapipelinen.** `python -m src.main` hämtar från SL, plattar ut, validerar
   och skriver `docs/data/avgangar.json`.

Blanda inte ihop dem. Skriv vilken du beskriver.

***

## Del 2, ditt eget arbete, krav för G

Här krävs **spårbara länkar**. Påståenden om eget arbete utan länk ger IG.

- [ ] **2.1 Ditt bidrag.** Vad du byggde, länk till din feature branch och till
      minst **tre** av dina commits
- [ ] **2.2 Din pull request.** Vad ändringen gjorde, hur du testade den innan
      du öppnade den, vem som granskade och vad de sa, samt länk till
      CI-körningen
- [ ] **2.3 Granskning du gjort.** Länk till minst en kommentar du lämnat på
      någon **annans** PR, och vad du reagerade på
- [ ] **2.4 Granskning du fått.** Länk till en kommentar du fått, och vad du
      ändrade, eller varför du inte ändrade
- [ ] **2.5 Versionshantering kopplad till uppgifter.** Hur vi höll ihop
      planering och kod
- [ ] **2.6 Konfiguration och secrets.** Hur vi hanterade `.gitignore` och
      `.env`, och varför det behövs

Om 2.5, vårt svar är att varje kort i `TASKS.md` har en issue, varje issue en
egen branch, och varje pull request skriver `Closes #20` så att issuen stängs
automatiskt vid merge.

Om 2.6, vår situation är ovanlig och värd att förklara. **SL Transport kräver
ingen API-nyckel**, så `.env` innehåller inställningar som `SITE_ID` och
`OUTPUT_PATH`, inte hemligheter. Rutinen är ändå på plats: `.env` ligger i
`.gitignore` och committas aldrig, medan `.env.example` ligger i repot med
standardvärden så att alla kan komma igång. Alla fält har standardvärden i
`src/config.py`, eftersom CI kör helt utan `.env` och bygget annars hade fallit
för hela gruppen.

Konfigurerade du det inte själv, beskriv hur gruppen gjorde och vad du förstått.
Det står uttryckligen att det räcker.

***

## Del 3, fördjupning, krav för VG

Bedöms bara om Del 1 och 2 är godkända.

- [ ] **3.1 En konkret händelse.** Något som gick fel eller blev svårare än
      väntat. Vad som hände och varför, hur ni löste det, och vad ni kunnat
      göra annorlunda. Länka till spåren i repot
- [ ] **3.2 Planering av källkodshantering.** Vilka regler du skulle sätta upp
      från dag ett om projektet startade om, och varför

Skillnaden mot G är enkel att missa. **G svarar på vad och hur. VG svarar på
varför just så.** Du ska väga alternativ mot varandra och redovisa nackdelar i
båda riktningarna. Att beskriva fler saker gör inte texten till VG.

Ett exempel på skillnaden, om branch protection i 3.2:

> G: "Vi skulle satt på branch protection på `main`."
>
> VG: "Jag skulle satt på branch protection med krav på en granskare. Nackdelen
> är att arbetet stannar när bara en person är aktiv, vilket hände oss. Jag
> skulle ändå gjort det, eftersom risken att någon pushar direkt till `main`
> och förstör för fem andra är värre än att vänta en dag på en granskning."

Händelser hos oss som fungerar för 3.1:

- Uppgift 28, där alla sex fyller i samma tabell i `README.md` och får merge
  konflikter på riktigt
- En pull request där uppgiftstexten i `TASKS.md` var fel och ledde utvecklaren
  fel, se PR #47 om `?expand=true`, rättat i PR #63
- En committad datafil som inte följde datakontraktet och togs bort igen, se
  PR #46
- En riktig merge konflikt i `src/transformera.py` mellan uppgift 8 och 9, som
  löstes av båda parter i tur och ordning, se PR #61
- Cloudflare slutade publicera helt när tjänsten bytte från Pages till Workers.
  Bygget föll på `Missing entry-point to Worker script or to assets directory`
  och löstes med `wrangler.jsonc` i repotroten, se PR #57
- Ett fält i datakontraktet som visade sig omöjligt att räkna fram. `riktningar`
  skulle koppla riktningskoden till en rubrik, men SL har inget riktningsnamn
  per hållplats. Fältet togs bort och sidan bygger rubriken själv, se PR #63
- Att gruppen kom igång sent, och att rollfördelningen byttes mot en
  uppgiftstavla för att ingen skulle blockeras av någon annan

***

## Så hittar du dina länkar

**Din branch.** Gå till repot, klicka rullgardinen som visar `main` och välj din
branch. URL:en i adressfältet är länken.

**Dina commits.** På din branch, klicka **Commits**. Klicka en commit och
kopiera URL:en. Du behöver tre. I terminalen:

```bash
git log --oneline --author="ditt-github-namn"
```

**Din pull request.** Fliken **Pull requests**, sedan filtret `Author`.

**CI-körningen.** Öppna din PR, fliken **Checks**, klicka `lint och test`, och
kopiera URL:en. I terminalen:

```bash
gh pr checks 51
```

**En granskningskommentar.** Hovra över kommentaren, klicka de tre prickarna
uppe till höger och välj **Copy link**. Den länken går direkt till kommentaren.

***

## Var vi står, ögonblicksbild 2026-09-01

Kolla din rad. Ja betyder att det redan finns spår i repot att länka till, nej
betyder att du behöver göra något innan gruppen är klar.

| GitHub | Commits på main | Egen PR | 2.3 granskat andra | 2.4 fått granskning |
|---|---|---|---|---|
| `GHT4ngo` | 39 | #39, #40, #41, #43, #49, #51, #53, #55, #56, #57, #63 | ja, #42, #44, #45, #46, #47, #58, #62 | tunt, se nedan |
| `somrar99` | 18 | #42, #45, #47, #58 | ja, #44, #46 | ja, #42, #47, #58 |
| `Yearofthedragon24` | 8 | #44, #46, #50, #61 | ja, #47, #60 | ja, #44, #46, #61 |
| `nibir03` | 12 | #59, #60, #62 | ja, #61 | ja, #60, #62 |
| `mahtotbelai` | 1 | #54 | nej | nej |
| `Haydslife` | 0 | nej | nej | nej |

Sedan förra ögonblicksbilden har mycket lossnat. Fyra av sex har nu allt de
behöver för Del 2.

**Yearofthedragon24**, anmärkningen om tunn granskning gäller inte längre. Dina
Approve på #47 och #60 har båda riktig text som säger vad du kontrollerat mot
uppgiftskortet. Det är precis vad 2.3 efterfrågar.

**nibir03**, du har gått från noll till tolv commits och tre pull requests.
Kommentaren du lämnade på #61 om merge konflikten i `transformera.py` duger som
svar på 2.3. Kvar är att slutföra #62.

**somrar99**, en varning som bara rör dig. Tio av dina arton commits är gjorda
med e-postadressen `kun.song@student.forsbergsskola.se`, som inte är kopplad
till ditt GitHub konto. De räknas därför inte i GitHubs statistik och visas utan
din profilbild. De ligger kvar i historiken och går att länka till, så det
duger för rapporten, men lägg gärna till adressen under Settings, Emails.

**mahtotbelai**, du har uppgift 18 mergad i #54, vilket täcker 2.1 och 2.2. Men
ingen granskade din PR och du har inte granskat någon annans. Både 2.3 och 2.4
saknas alltså. Ta en av de öppna PR:erna och skriv en kommentar med innehåll, så
löser det halva problemet direkt.

**Haydslife**, du har uppgift 16 tilldelad och en branch `task/16-linjefarger`,
men inga commits på den. Utan en egen branch med commits, en pull request och en
grön CI-körning går varken grupparbetet eller rapporten att bli godkänd.

**Fyra rader i `README.md` är fortfarande tomma.** Uppgift 28 innebär att var och
en fyller i sin egen, i sin egen branch. Ingen har gjort det utom Christofer.

**Christofer**, ditt eget 2.4 är svagt. Granskningarna du fått är "Tested
locally, works as expected" på #41 och #51. Det går att länka till men det finns
inget resonemang att skriva om. Be någon i gruppen granska #56 med en riktig
kommentar.

> Den sjunde medlemmen i repot, `LindaLiBogardi`, är läraren. Hon är redan
> inbjuden och ser allt, så länkarna i din rapport fungerar för henne trots att
> repot är privat.
