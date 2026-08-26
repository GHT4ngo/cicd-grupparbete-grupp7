<div align="center">

# Uppgiftstavlan

### Grupp 7 &nbsp;&bull;&nbsp; DevOps &nbsp;&bull;&nbsp; DE25

<p>
<img alt="Kärnan" src="https://img.shields.io/badge/K%C3%A4rnan-16%20uppgifter-0e8a16?style=for-the-badge">
<img alt="Tavla" src="https://img.shields.io/badge/Status%20finns%20i-GitHub%20Projects-8957e5?style=for-the-badge">
<img alt="Bonus" src="https://img.shields.io/badge/Bonus-14%20frivilliga-c5def5?style=for-the-badge">
<img alt="Hosting" src="https://img.shields.io/badge/Publiceras-Cloudflare%20Pages-F38020?style=for-the-badge">
</p>

<em>Ingen har en tilldelad roll. Här finns en kö av små uppgifter.<br>
Sexton stycken är kärnan. Resten är bonus.</em>

</div>

***

## Innehåll

1. [Så fungerar tavlan](#så-fungerar-tavlan)
2. [Uppgifterna](#uppgifterna)
3. [Datakontraktet](#datakontraktet)
4. [Så löser du uppgifterna](#så-löser-du-uppgifterna)
5. [När uppgifterna tar slut](#när-uppgifterna-tar-slut)
6. [Checklista för G](#checklista-för-g)

***

## Så fungerar tavlan

**Statusen bor i [projekttavlan](../../projects), inte i den här filen.** Varje uppgift är ett issue. Den här filen är bara innehållsförteckningen med beskrivningarna.

Det betyder att du **aldrig behöver redigera `TASKS.md`** för att ta en uppgift. Du drar ett kort på tavlan i stället.

**Så gör du.**

1. Öppna [projekttavlan](../../projects) och leta upp ett kort i kolumnen **Todo**.
2. Tilldela dig själv och dra kortet till **In progress**.
3. Skapa en branch som heter `task/16-linjefarger`, alltså numret plus ett kort namn.
4. Skriv `Closes #16` i beskrivningen på din pull request.

När din pull request mergas stängs issuet automatiskt och kortet flyttar sig själv till **Done**. Ingen behöver städa efteråt.

> [!TIP]
> Du får ta hur många uppgifter du vill. Vill du bara göra en enda, ta en liten ur kärnan. Vill du köra hårt, ta tre och fortsätt in i bonushögen.

> [!NOTE]
> Bakgrunden till projektet, alltså vad vi bygger och hur API:et fungerar, står i [SUGGESTION.md](SUGGESTION.md).

***

## Uppgifterna

Uppgifterna är delade i två högar. **Kärnan är projektet.** Bonus är sådant vi gör om vi hinner och har lust.

> [!IMPORTANT]
> Sexton kärnuppgifter fördelat på sex personer blir under tre var. Det räcker för att projektet ska vara klart och för att alla ska bli godkända. Ta inget ur bonushögen förrän kärnan är i hamn.

***

### Kärnan

Sexton uppgifter. Det här, och inget mer, är vad som måste bli gjort.

**Grunden.** Allt annat väntar på de fyra. Christofer tar dem.

| Nr | Uppgift | Storlek | Väntar på |
|---|---|---|---|
| [1](../../issues/9) | Mappstruktur | 5 min | inget |
| [2](../../issues/10) | CI workflow | 25 rader | 1 |
| [3](../../issues/11) | Konfiguration | 15 rader | 1 |
| [4](../../issues/12) | Datakontraktet | ingen kod | inget |

**Pipelinen.**

| Nr | Uppgift | Storlek | Väntar på |
|---|---|---|---|
| [5](../../issues/13) | Hämta från SL | 10 rader | 3 |
| [6](../../issues/14) | Spara ett exempelsvar | ingen kod | 5 |
| [7](../../issues/15) | Platta ut en avgång | 15 rader | 4, 6 |
| [8](../../issues/16) | Räkna minuter | 8 rader | 7 |
| [10](../../issues/18) | Validera posterna | 12 rader | 4 |
| [11](../../issues/19) | Skriv resultatet | 10 rader | 4 |
| [14](../../issues/22) | Kör hela kedjan | 8 rader | 5, 7, 11 |

**Sidan.**

| Nr | Uppgift | Storlek | Väntar på |
|---|---|---|---|
| [12](../../issues/20) | Avgångstavlan i webbläsaren | html | 4 |
| [29](../../issues/37) | Publicera på Cloudflare Pages | klickande | 12 |

**Tester.**

| Nr | Uppgift | Storlek | Väntar på |
|---|---|---|---|
| [22](../../issues/30) | Test för utplattningen | 2 test | 7 |
| [23](../../issues/31) | Test för minuträkningen | 3 test | 18 |

**Den här tar alla sex, var för sig.**

| Nr | Uppgift | Vem |
|---|---|---|
| [28](../../issues/36) | Lägg till dig själv i `README.md` | alla sex |

***

### Bonus

Fjorton uppgifter som är helt frivilliga. Inget här behövs för att bli godkänd, och inget här behövs för att projektet ska fungera.

De ligger kvar som issues med etiketten `bonus`, så det finns alltid något att ta för den som vill göra mer.

| Nr | Uppgift | Storlek | Väntar på |
|---|---|---|---|
| [9](../../issues/17) | Gruppera per riktning | 12 rader | 7 |
| [13](../../issues/21) | Hämta färska tider direkt från SL | 15 rader js | 12 |
| [15](../../issues/23) | Sök hållplats | 15 rader | inget |
| [16](../../issues/24) | Linjefärger | 15 rader | inget |
| [17](../../issues/25) | Avvikelser | 15 rader | inget |
| [18](../../issues/26) | Formatera tid | 10 rader | inget |
| [19](../../issues/27) | Statistik | 12 rader | inget |
| [20](../../issues/28) | Rensa bort skräp | 10 rader | inget |
| [21](../../issues/29) | Kommandoradsflaggor | 10 rader | inget |
| [24](../../issues/32) | Test för färgkartan | 2 test | 16 |
| [25](../../issues/33) | Test för avvikelser | 2 test | 17 |
| [26](../../issues/34) | Test för stationssökningen | 2 test | 15 |
| [27](../../issues/35) | Test för filtreringen | 2 test | 20 |
| [30](../../issues/48) | Test för valideringen | 3 test | 10 |

> [!NOTE]
> Uppgift 13 är den enda i bonushögen som märks utifrån. Utan den visar sidan de tider som låg i JSON filen när den senast committades. Med den blir tavlan levande. Bra att ta om någon vill göra något som syns.

***

## Datakontraktet

Så här ser en avgång ut efter att den tvättats. Åtta fält, alla platta, inga nästlade objekt.

```json
{
  "linje": "14",
  "linjegrupp": "Tunnelbanans röda linje",
  "transportmedel": "METRO",
  "riktning_kod": 2,
  "riktning": "Fruängen",
  "destination": "Liljeholmen",
  "avgar_klocka": "13:22",
  "minuter": 3
}
```

> [!IMPORTANT]
> Det här är det viktigaste i hela filen. Uppgift 7 fyller fälten, uppgift 10 kontrollerar dem, uppgift 12 visar dem. Så länge alla håller sig till kontraktet kan de tre uppgifterna göras av tre olika personer utan att de behöver prata med varandra.

### Och så här ser hela filen ut

Kontraktet ovan gäller **en avgång**. Posterna ligger i sin tur inuti ett objekt, och det är det objektet som hamnar i `docs/data/avgangar.json`.

```json
{
  "station": "Slussen",
  "station_id": "9192",
  "uppdaterad": "2026-08-25T13:22:03",
  "riktningar": {
    "1": "Mot norr",
    "2": "Mot söder"
  },
  "avgangar": [
    { "linje": "14", "linjegrupp": "Tunnelbanans röda linje", "transportmedel": "METRO", "riktning_kod": 1, "riktning": "Mörby centrum", "destination": "Mörby centrum", "avgar_klocka": "13:22", "minuter": 0 }
  ]
}
```

| Fält | Vad det är | Varifrån |
|---|---|---|
| `station` | Hållplatsens namn, används som rubrik på sidan | `SITE_NAME` ur konfigurationen |
| `station_id` | Samma id som hämtningen använde | `SITE_ID` ur konfigurationen |
| `uppdaterad` | När filen skrevs, lokal tid utan tidszon | `datetime.now().isoformat(timespec="seconds")` |
| `riktningar` | Kopplar riktningskoden till en rubrik | Skrivs för hand, `1` och `2` är de två hållen |
| `avgangar` | Listan med poster enligt kontraktet ovan | Uppgift 7 till 10 |

> [!WARNING]
> `skriv_resultat` från uppgift 11 skriver rakt av vad den får. Skickar uppgift 14 in bara listan blir filen en lista, och då hittar sidan varken `station` eller `riktningar` och renderar tomt. **Bygg hela objektet i `src/main.py` innan du skickar det vidare.**

Nycklarna i `riktningar` är strängar, inte tal, eftersom JSON bara tillåter strängar som nycklar. Posternas `riktning_kod` är däremot ett tal. Sidan gör om koden till sträng när den slår upp rubriken, så det är inget att bry sig om, men det förklarar varför de ser olika ut.

***

## Så löser du uppgifterna

<details open>
<summary><b>Kärnan: grunden, uppgift 1 till 4</b></summary>

<br>

**Task #1 · Mappstruktur** &nbsp;&bull;&nbsp; `src/`, `tests/`

Skapa mapparna `src/` och `tests/` med varsin tom `__init__.py`. Utan dem hittar inte `pytest` modulerna när testerna importerar.

*Klar när:* `python -c "import src"` går igenom utan fel.

<br>

**Task #2 · CI workflow** &nbsp;&bull;&nbsp; `.github/workflows/ci.yml`

Fyra steg: `actions/checkout@v4`, `actions/setup-python@v5`, installera från `requirements.txt`, kör `ruff check .` och `pytest -v`. Inget `env:` block behövs, SL kräver ingen nyckel.

Skicka med `tests/test_smoke.py` med ett enda `assert True` i samma pull request. `pytest` avslutar med kod 5 när noll test hittas, vilket gör CI röd för hela gruppen.

*Klar när:* en pull request visar grön bock i GitHub.

<br>

**Task #3 · Konfiguration** &nbsp;&bull;&nbsp; `src/config.py`, `.env.example`

`load_dotenv()` och sedan `os.getenv("SITE_ID", "9192")` för varje värde. Samla dem i en dataclass. Fälten är `SITE_ID`, `SITE_NAME`, `TRANSPORT_MODE`, `FORECAST_MINUTES` och `OUTPUT_PATH`.

**Varje fält måste ha ett standardvärde.** CI kör utan `.env` fil, så ett `os.environ["SITE_ID"]` fäller bygget för alla. Ta samtidigt bort `API_KEY` och `API_BASE_URL` ur `.env.example`, de kommer aldrig att användas.

*Klar när:* konfigurationen går att importera utan `.env` och ger standardvärdena.

<br>

**Task #4 · Datakontraktet** &nbsp;&bull;&nbsp; `TASKS.md`

Bestäm hur en tvättad avgång ser ut och skriv ner exemplet i avsnittet ovan. Ingen kod. Det här styr uppgift 7 till 12, så det måste finnas först.

*Klar när:* exemplet ligger i `TASKS.md` och gruppen har sett det.

</details>

<details>
<summary><b>Kärnan: pipelinen, uppgift 5 till 11 och 14</b> &nbsp;&bull;&nbsp; <i>uppgift 9 är bonus</i></summary>

<br>

**Task #5 · Hämta från SL** &nbsp;&bull;&nbsp; `src/hamta.py`

> [!NOTE]
> **somrar99 har redan gjort det här arbetet** under det gamla rollissuet. Öppna en pull request med den koden i stället för att börja om.

`requests.get` mot `https://transport.integration.sl.se/v1/sites/{SITE_ID}/departures`, med `transport` och `forecast` som parametrar. Sätt `timeout=10` så programmet inte hänger sig om SL är nere. Anropa `response.raise_for_status()` och returnera `response.json()`.

*Klar när:* du får tillbaka en dictionary som innehåller nyckeln `departures`.

<br>

**Task #6 · Spara ett exempelsvar** &nbsp;&bull;&nbsp; `tests/exempel/`

Kör uppgift 5 en gång och spara svaret med `json.dump` till `tests/exempel/avgangar_slussen.json`. Committa filen.

Den här lilla uppgiften låser upp tre andra. Uppgift 7, 22 och 27 behöver se hur datan faktiskt ser ut, och testerna får aldrig gå mot nätverket.

*Klar när:* filen ligger i repot och går att öppna.

<br>

**Task #7 · Platta ut en avgång** &nbsp;&bull;&nbsp; `src/transformera.py`

Loopa över `svar["departures"]` och plocka de åtta fälten ur kontraktet. Linjenumret sitter i `x["line"]["designation"]`, färggruppen i `x["line"]["group_of_lines"]`, färdmedlet i `x["line"]["transport_mode"]`. Riktning och destination ligger direkt på `x`.

**Använd `.get("group_of_lines")`, inte hakparenteser.** Nyckeln saknas helt för ungefär hälften av bussarna, verifierat mot ett live svar där 57 av 113 avgångar var utan den. Exempelfilen från uppgift 6 är bara tunnelbana, så alla poster där har fältet och felet syns inte förrän pipelinen körs på riktigt.

*Klar när:* en post ur exempelfilen ger tillbaka de åtta fälten och inget mer.

<br>

**Task #8 · Räkna minuter** &nbsp;&bull;&nbsp; `src/transformera.py`

`datetime.fromisoformat(x["expected"])` minus `datetime.now()`, dela antalet sekunder med 60 och avrunda. Klampa negativa värden till noll.

**Läs aldrig `display`.** Det fältet blandar `"Nu"`, `"3 min"` och `"13:25"` i samma svar, eftersom det växlar från minuter till klockslag efter ungefär tio minuter.

*Klar när:* en avgång tre minuter fram ger `3`.

<br>

**Task #9 · Gruppera per riktning** &nbsp;&bull;&nbsp; `src/transformera.py`

Bygg `{linjegrupp: {riktning_kod: [poster]}}`. `collections.defaultdict` gör det kortare. Riktningskoden är alltid `1` eller `2`, vilket är de två hållen linjen går.

*Klar när:* exempelfilen ger två riktningar per linje.

<br>

**Task #10 · Validera posterna** &nbsp;&bull;&nbsp; `src/validera.py`

Kontrollera att alla åtta nycklar finns, att `riktning_kod` är `1` eller `2` och att `minuter` inte är negativt. Kasta `ValueError` med ett tydligt meddelande vid fel.

*Klar när:* en trasig post ger fel och en hel post går igenom tyst.

<br>

**Task #11 · Skriv resultatet** &nbsp;&bull;&nbsp; `src/resultat.py`

Skriv till `docs/data/avgangar.json`. `json.dump` med `ensure_ascii=False` så att å, ä och ö överlever, och `indent=2` så filen går att läsa. Skapa målmappen med `Path(...).parent.mkdir(parents=True, exist_ok=True)` först, annars kraschar det första körningen.

Filen ska **committas**. Den är det sidan visar direkt vid laddning, innan den hunnit hämta färska tider.

*Klar när:* filen finns på `OUTPUT_PATH` och svenska tecken ser rätt ut.

<br>

**Task #14 · Kör hela kedjan** &nbsp;&bull;&nbsp; `src/main.py`

Anropa hämta, transformera, validera och resultat i den ordningen. Skriv ut hur många avgångar som skrevs.

**Bygg hela objektet innan du skickar det till `skriv_resultat`.** Listan med poster är bara fältet `avgangar`. Runt den ska `station`, `station_id`, `uppdaterad` och `riktningar` med, se [datakontraktet](#datakontraktet). Skickar du in bara listan renderar sidan tomt.

*Klar när:* `python -m src.main` skapar JSON filen och avgångstavlan visar den.

</details>

<details>
<summary><b>Kärnan: sidan, uppgift 12 och 29</b> &nbsp;&bull;&nbsp; <i>uppgift 13 är bonus</i></summary>

<br>

> [!IMPORTANT]
> Sidan ligger på Cloudflare Pages, som är en **statisk** webbserver. Det körs ingen Python där. Allt sidan behöver måste alltså antingen ligga committat i `docs/`, eller hämtas av webbläsaren själv.

<br>

**Task #12 · Avgångstavlan** &nbsp;&bull;&nbsp; `docs/index.html`

En enda självbärande fil. Inget byggsteg, inga externa bibliotek. `fetch('data/avgangar.json')`, loopa över linjerna och bygg raderna. Två kolumner för de två riktningarna med CSS grid.

Bygg mot en **handskriven** exempelfil som följer kontraktet. Då går uppgiften att bli klar med långt innan uppgift 7 finns.

*Klar när:* `cd docs && python -m http.server 8000` visar avgångar i två kolumner.

<br>

**Task #13 · Färska tider** &nbsp;&bull;&nbsp; `docs/index.html`

Den committade JSON filen blir gammal direkt. Den här uppgiften är det som gör sidan till en riktig avgångstavla.

Anropa SL direkt från webbläsaren när sidan laddas, och sedan om var trettionde sekund med `setInterval`. Det fungerar utan proxy och utan nyckel eftersom API:et skickar `access-control-allow-origin: *`.

**Sidan måste fungera även om anropet misslyckas.** Visa den committade filen då, tillsammans med en tydlig text om att tiderna inte är färska. Visa alltid en stämpel med senast uppdaterad.

*Klar när:* tiderna räknar ner utan att sidan laddas om, och sidan visar något vettigt även med nätverket avstängt.

<br>

**Task #29 · Publicera** &nbsp;&bull;&nbsp; Cloudflare

Ingen kod, bara klickande. Bra första uppgift om du känner dig osäker.

1. Logga in på Cloudflare och välj **Workers and Pages**, sedan **Create**, sedan **Pages**, sedan **Connect to Git**.
2. Välj det här repot. Privata repon fungerar, det ingår i gratisplanen.
3. Lämna **Build command** tomt. Sätt **Build output directory** till `docs`.
4. Under **Custom domains**, lägg till `sl.t4ngo.com`. Domänen ligger redan i Cloudflare, så det är bara att välja den i listan.

Varje push till `main` publicerar om sidan automatiskt. Inget behöver köras på någons dator.

*Klar när:* `sl.t4ngo.com` visar avgångstavlan i mobilen.

</details>

<details>
<summary><b>Bonus: fristående, uppgift 15 till 21</b></summary>

<br>

Rena funktioner i egna filer. De kan omöjligt krocka med någon annans arbete, och de väntar inte på någon.

<br>

**Task #15 · Sök hållplats** &nbsp;&bull;&nbsp; `src/stationer.py`

Hämta `https://transport.integration.sl.se/v1/sites` och filtrera på `namn.lower() in site["name"].lower()`. Returnera id och namn för träffarna.

Nyttan är konkret: svaret innehåller **6511 hållplatser och väger 1,35 MB**, så att leta upp ett id för hand är projektets segaste moment. Det finns dessutom två Slussen, `9192` och `9208`, och sökningen ska visa båda.

**Sätt inte `?expand=true`.** Det lägger bara till fältet `stop_areas` som vi inte använder, och mätt tre gånger tar anropet 5 till 8,6 sekunder med flaggan mot 1,3 utan. Med `timeout=10` ligger den varianten obehagligt nära att falla på en trög dag.

Dela funktionen i två, en som hämtar listan och en som filtrerar den. Då kan uppgift 26 testa sökningen mot en handskriven lista i stället för att gå ut på nätet.

*Klar när:* `"slussen"` ger fyra träffar, alltså båda Slussen plus Stadsgården och Södermalmstorg.

<br>

**Task #16 · Linjefärger** &nbsp;&bull;&nbsp; `src/linjer.py`

En dictionary från `group_of_lines` till hexfärg. Grön `#148541`, röd `#d71d24`, blå `#007db8`.

Fällan: **`group_of_lines` saknas helt för de flesta bussar**, verifierat mot riktig data. Använd `.get(nyckel, standardfarg)` så att en buss utan fältet ändå får en färg.

*Klar när:* en känd linje ger rätt färg och en okänd ger standardfärgen.

<br>

**Task #17 · Avvikelser** &nbsp;&bull;&nbsp; `src/avvikelser.py`

Svaret har två fält som pipelinen slänger bort idag: `deviations` på varje avgång, och `stop_deviations` på svaret som helhet. Plocka ut båda och platta ihop dem till en lista med meddelanden.

*Klar när:* ett svar utan störningar ger en tom lista, inte ett fel.

<br>

**Task #18 · Formatera tid** &nbsp;&bull;&nbsp; `src/tid.py`

Ta ett antal minuter och returnera `"Nu"` vid noll, annars `"3 min"`. Lägg en andra funktion som plockar klockslaget ur `expected` med strängsnittet `[11:16]`.

*Klar när:* 0, 3 och 45 ger rätt sträng.

<br>

**Task #19 · Statistik** &nbsp;&bull;&nbsp; `src/statistik.py`

`collections.Counter` över linje och riktning. Svara på hur många avgångar varje linje har och vilken riktning som går oftast.

*Klar när:* summan av räknaren stämmer med antalet avgångar.

<br>

**Task #20 · Rensa bort skräp** &nbsp;&bull;&nbsp; `src/filter.py`

Behåll bara poster där `state` inte är `CANCELLED` och `minuter` inte är negativt. Turer som redan har gått ligger kvar i svaret en stund.

*Klar när:* en inställd tur försvinner ur listan.

<br>

**Task #21 · Kommandoradsflaggor** &nbsp;&bull;&nbsp; `src/main.py`

`argparse` med `--station` och `--transport` som skriver över konfigurationen.

*Klar när:* `python -m src.main --station 9001` hämtar T-Centralen i stället.

</details>

<details>
<summary><b>Tester, uppgift 22 till 27 och 30</b> &nbsp;&bull;&nbsp; <i>22 och 23 är kärna, resten bonus</i></summary>

<br>

Samma mönster i allihop: skriv en liten handskriven dictionary överst i testfilen, anropa funktionen, kontrollera svaret.

> [!WARNING]
> **Inget test får gå mot nätverket.** Då blir CI rött för hela gruppen den dagen SL har problem, och felet har ingenting med vår kod att göra.

| Nr | Fil | Ska täcka |
|---|---|---|
| [22](../../issues/30) | `tests/test_transformera.py` | att alla åtta fält kommer med |
| [23](../../issues/31) | `tests/test_tid.py` | noll, positivt, och att negativt klampas till noll |
| [24](../../issues/32) | `tests/test_linjer.py` | känd linjegrupp, och buss där fältet saknas |
| [25](../../issues/33) | `tests/test_avvikelser.py` | både tomt och ifyllt svar |
| [26](../../issues/34) | `tests/test_stationer.py` | skiftlägesokänslig, hittar delsträngar |
| [27](../../issues/35) | `tests/test_filter.py` | inställd tur, och tur som redan gått |
| [30](../../issues/48) | `tests/test_validera.py` | saknat fält, fel riktningskod, negativa minuter |

**En fälla i uppgift 23.** Tidsstämplarna från SL saknar tidszon och är svensk lokaltid, medan CI kör i UTC. Ett test som räknar mot `datetime.now()` går igenom på din dator och fallerar i CI. Lås en fast tidpunkt i testet i stället.

</details>

<details>
<summary><b>Kärnan: den här tar alla sex, uppgift 28</b></summary>

<br>

**Task #28 · Lägg till dig själv** &nbsp;&bull;&nbsp; `README.md`

Fyll i din rad i tabellen `Gruppmedlemmar`, i din egen branch.

Uppgiften tas av **alla sex, var för sig**. Det är avsiktligt. Bedömningen kräver att var och en hanterar en merge konflikt, och om alla arbetar i varsin fil uppstår aldrig någon. Sex parallella branches som rör samma tabell ger garanterade konflikter, och de är ofarliga att lösa eftersom facit alltid är att behålla båda raderna.

*Klar när:* din rad står i tabellen på `main` och du har löst minst en konflikt på vägen.

</details>

***

## När uppgifterna tar slut

Först finns [bonushögen](#bonus) med tretton uppgifter. Tar även den slut skriver vi fler och lägger upp dem som nya kort. Här är råmaterialet.

| Idé | Vad det ger |
|---|---|
| Flera hållplatser i samma körning | En tavla för hela resan, inte bara ett stopp |
| Mörkt läge på sidan | Går att ha uppe på en skärm i hallen |
| Dölj avgångar som går om mindre än tre minuter | Visar bara det du faktiskt hinner med |
| Cachea `/v1/sites` lokalt | Slipper ladda 1,6 MB vid varje sökning |
| Jämför `expected` mot `scheduled` | Räknar ut hur ofta SL faktiskt är sen |
| Spara varje körning och jämför över tid | Historik, och underlag för statistik |
| Loggning i stället för `print` | Går att felsöka när något går fel i CI |
| `ruff format --check` som eget steg | Slut på diskussioner om kodstil |

***

## Checklista för G

Det här är det som faktiskt bedöms. Uppgifterna ovan är bara vägen dit.

| Krav | Hur du visar det |
|---|---|
| Egen feature branch | Din branch syns i historiken |
| Genomfört din del | Dina commits på din branch |
| Mergad via granskad pull request | Någon i gruppen har godkänt din PR |
| Hanterat en merge konflikt | Uppgift 28 ger dig en garanterad |
| Deltagit i `.gitignore` och `.env` | Antingen skrivit dem eller förstått hur uppgift 3 löstes |
| Grön CI på din pull request | Grön bock på PR sidan |

> [!NOTE]
> Det räcker med **en** uppgift för att uppfylla allt i tabellen, så länge du gör den i egen branch och mergar via en granskad pull request. Resten är för att projektet ska bli klart.

<div align="center">
<sub>DevOps DE25 &nbsp;&bull;&nbsp; Grupp 7 &nbsp;&bull;&nbsp; Ta ett kort på tavlan</sub>
</div>
