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

> **Frågetecken att ta med läraren.** Uppgiften säger "länka till gruppens
> gemensamma **publika** repo". Vårt repo är privat, och det har vi gjort
> avsiktligt. Fråga läraren vad som gäller innan du lämnar in. Alternativen är
> att repot görs publikt vid inlämning, att läraren bjuds in som medlem, eller
> att du bifogar skärmdumpar. Uppgiften nämner själv att skärmdumpar är
> välkomna.

***

## Del 1, begrepp, krav för G

Förklara med egna ord och **koppla varje svar till något konkret hos oss**. Det
är kopplingen som bedöms, inte definitionen.

| Nr | Fråga | Var du hittar exempel hos oss |
|---|---|---|
| 1.1 | Vad är DevOps, vilket problem löser vårt projekt, minst två delar av kedjan | `README.md` och `SUGGESTION.md` beskriver problemet |
| 1.2 | Vad är CI, vad är CD, hur skiljer de sig, vilket använde vi | Vi har båda. CI är `.github/workflows/ci.yml`, CD är Cloudflare Pages som publicerar om vid varje merge till `main` |
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
  fel, se PR #47 om `?expand=true`
- En committad datafil som inte följde datakontraktet och togs bort igen, se
  PR #46
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

## Var vi står, ögonblicksbild 2026-08-27

Kolla din rad. Ett kryss betyder att det redan finns spår i repot att länka
till, ett streck betyder att du behöver göra något innan gruppen är klar.

| GitHub | Egna commits | Egen PR | 2.3 granskat andra | 2.4 fått granskning |
|---|---|---|---|---|
| `GHT4ngo` | ja | #39, #40, #41, #51 | ja, #42, #44, #45, #46, #47 | ja, #41 |
| `somrar99` | ja | #42, #45, #47 | ja, #44, #46 | ja, #42, #45, #47 |
| `Yearofthedragon24` | ja | #44, #46, #50 | tunt, se nedan | ja, #46, #50 |
| `nibir03` | nej | nej | nej | nej |
| ej ifylld | nej | nej | nej | nej |
| ej ifylld | nej | nej | nej | nej |

**Yearofthedragon24**, din granskning på #47 är en Approve med texten "Ser bra
ut enligt mig". Det går att länka till, men det finns inget att skriva om i
rapporten. Lämna en kommentar till som säger något konkret, så har du ett
riktigt svar på 2.3.

**nibir03**, du har uppgift 7 och 8 tilldelade men ingen commit ännu. Utan en
egen branch, en egen pull request och en grön CI-körning går varken grupparbetet
eller den här rapporten att bli godkänd.

**Två rader i `README.md` är fortfarande tomma.** Uppgift 28 innebär att var och
en fyller i sin egen, i sin egen branch.
