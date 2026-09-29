"""Meet leesbaarheid en stijlregels van de lopende tekst in lectures/*.md.

Gebruik:
    uv run python tools/prose_stats.py                      # tabel voor alle lectures
    uv run python tools/prose_stats.py lectures/02_08_capm.md
    uv run python tools/prose_stats.py --check lectures/02_08_capm.md   # PASS/FAIL per drempel
    uv run python tools/prose_stats.py --where lectures/02_08_capm.md   # vindplaatsen van calques e.d.
    uv run python tools/prose_stats.py --selftest           # controleert de regexen

Code-cellen, tabellen, kopjes en directive-regels worden weggelaten; inline-wiskunde telt als
één woord. Een zin die over een display-vergelijking heen loopt, telt als één zin. De drempels
staan in THRESHOLDS en horen bij plannen/verbeterplan-didactiek.md §8 en STYLE.md §11.
Besluiten eigenaar 2026-09-28: notes/onderzoek-A..E.
"""
import collections
import glob
import re
import statistics
import sys

# metriek: (minimum, maximum); None = geen grens. Alle drempels staan hier.
THRESHOLDS = {
    "words": (None, 6000),     # lopende tekst, excl. code/wiskunde/tabellen
    "sent_mean": (15, 20),     # gemiddelde zinslengte in woorden
    "sent_p90": (None, 28),    # 90e percentiel zinslengte
    "sent_gt40": (None, 2),    # zinnen langer dan 40 woorden
    "para_mean": (None, 60),   # gemiddelde alinealengte in woorden (zonder lijstitems)
    "dash": (None, 10),        # gedachtestreepjes (—)
    "semicol": (None, 15),     # puntkomma's in lopende tekst
    "motief": (None, 0),       # "motief 1/2/3": projectjargon
    "Lnum": (None, 0),         # "L4", "L26": projectjargon
    "deel": (None, 0),         # "Deel V": projectjargon
    "u_form": (None, 0),       # aanspreekvorm "u"
    "je_form": (None, 0),      # aanspreekvorm "je/jij/jouw"
    "taboo": (None, 0),        # verrassend, eenvoudigweg, zoals bekend, triviaal
    "stopw": (None, 6),        # ruwweg, inderdaad, in feite, letterlijk
    "calque": (None, 0),       # vertaald Engels, zie CALQUES
    "engquote": (None, 5),     # aanhalingen van 25+ tekens (meestal Engelse citaten)
    "colon_mid": (None, 8),    # dubbele punt + kleine letter, per 1000 woorden (labels niet)
    "para_one": (None, 12),    # % alinea's van één zin (geen lijstitem, geen celaankondiging)
    "telegram": (None, 0),     # zin zonder persoonsvorm: "Eerst de data."
    "tmpl": (None, 2),         # hoogste aantal van één soort sjabloonzin, zie TEMPLATES
    "wie_open": (None, 4),     # zinnen die met "Wie " beginnen
    "connect": (20, None),     # % zinnen met een verbindingswoord, zie CONNECT
    "repeat": (None, 0),       # letterlijk herhaalde zinnen van 10+ woorden
}

# Vertaald Engels (STYLE.md §11.4, onderzoek A §P6-P8, D §5, E §1). Hoofdlettergevoelig.
CALQUES = [
    r"\bde nul\b(?!hypothese)",                 # "the null" -> de nulhypothese
    r"omvang van de toets",                     # "size of the test" -> werkelijk significantieniveau
    r"\bNoteer\b",                              # "Note that" -> weglaten of "Let wel"
    r"\bOnthoud dat\b",                         # "Remember that" -> weglaten of "Bedenk dat"
    r"\b(Twee|Drie|Vier) dingen\b",             # "Two things ..." -> "Deze tabel laat twee dingen zien"
    r"\bis de reden dat\b",                     # "is the reason that" -> "Daarom"
    r"\b(Dit|Dat|Het) is wat\b",                # "This is what X means" -> "Dat betekent X"
    r"in de taal van",                          # "in the language of" -> "in de termen van"
    r"het hart van",                            # "the heart of" -> "de kern van"
    r"\btot vandaag\b",                         # "to this day" -> "nog altijd"
    r"Leg dit naast",                           # "lay this next to" -> "Vergelijk dit met"
    r"de hele inhoud van",                      # "the whole content of" -> "meer zegt X niet"
    r"aan het eind van de dag",                 # -> "uiteindelijk"
    r"(?m)^Les:",                               # -> "Wat dit leert:"
    r"epistemisch",                             # -> "theorie of feit" (STYLE §11.3)
    r"bestaansobject|restpost|vastgeknoopt",    # bedachte of gekunstelde woorden
    r"\b[A-Z][a-z]+[bcdfgjklmnpqrtvw]'s\b",     # Cochrane's, Merton's -> Cochranes, Mertons
    r"\b[A-Z][a-z]+e's\b",                      # Sharpe's -> Sharpes (stomme e)
    r"\bhet punt van\b",                        # "the point of" -> "liet X zien"
    r"\bdoet (dat |het )?ertoe\b",              # "it matters" -> "is van belang"
    r"\bdraagt (de hele|ruim)\b",               # "carries the lecture" -> "draait om"
    r"\bin niveaus\b",                          # "in levels" -> "in euro's", "de reeks zelf"
    r"Zo komt het uit",                         # "so it turns out" -> "Dat klopt"
    r"\bRij maal kolom\b",                      # "row times column"
    r"\blang gaat? in\b",                       # "goes long in" -> "koopt"
    r"\bhangt aan\b",                           # "hangs on" -> "hangt af van"
    r"[Mm]arktruiming|\bde markt ruimt\b",      # "market clearing" -> evenwicht
    r"\bvertragingen\b",                        # "lags" -> "lags"
    r"\b(prijst|geprijsd|beprijsde?|ingeprijsde?)\b|\bWe prijzen\b",  # "to price" -> waarderen
    r"\bdefinie\w+ het tijdvak\b",              # "defines the era" -> "opent het tijdvak"
    r"\boverleeft:",                            # "survives:" -> "blijft overeind"
    r"(?m)(?:^|(?<=\. ))(?:Equal|Value)-weighted\b",  # Engels als onderwerp
    r"\bdetrend(?:en|ing)\b|\bgedemeend",       # vernederlandst Engels werkwoord
    r"\blost\b[^.]{0,60}\bin\b[.:]",            # projectjargon "inlossen"
    r"\bWerk achterwaarts\b|\béén morgen\b",    # "work backwards", "one tomorrow"
]

# Sjabloonzinnen: per soort hoogstens THRESHOLDS["tmpl"]. MOTIFS alleen in proza (geen vet kopje).
TEMPLATES = {
    "In woorden": r"In woorden:",
    "Waarom zou": r"Waarom zou dit waar zijn",
    "Wat dit leert": r"Wat dit leert",
    "intuïtie voorspeld": r"intuïtie voorspeld",
    "Wat we nu weten": r"Wat we nu weten",
    "Wat de lezer nu weet": r"Wat de lezer nu weet",
}
MOTIFS = {
    "standaardfout 2%": r"de standaardfout van 2 ?%",
    "theorie of feit": r"theorie of feit",
    "risico of alpha": r"risico of (alpha|vergissing)",
}
LABELS = r"(In woorden|Wat dit leert|Het bewijsidee|Wat we nu weten|Wat de lezer nu weet):"
CONNECT = (r"\b(maar|want|omdat|hoewel|terwijl|doordat|zodat|daarom|toch|bovendien|echter|immers|"
           r"namelijk|tenzij|mits|voordat|nadat|zodra|dus|ook al|daardoor|dan ook|juist)\b|^Al\b")
TELEGRAM = r"^(?:Eerst|Dan|Daarna|Nu|Ten slotte|Tot slot) (?:de|het|een|twee|drie|zijn|haar)\b[^.!?:,]{0,70}\.$|^Niet in de [^.]*, maar in"
# Alleen rapporteren (kolom info): Engelse vakwoorden met Nederlandse vorm (onderzoek D §6, E).
ANGLICISMS = (r"(?<![-/])\b(finance|asset pricing|paper|short|size|value-weighted|equal-weighted|"
              r"pre-ranking|toy|lecture|in-sample|horizons)\b(?![-/])")
DAT_IS = r"^(Dat|Dit) (is|zijn)\b"
LIST = r"\s*([-*+]|\d{1,2}\.)\s"  # hoogstens twee cijfers: een jaartal aan het regelbegin is geen lijstnummer


def _display(m):
    """Display-wiskunde: alinea-einde als de zin ervoor al af is, anders loopt de zin door."""
    before = m.string[:m.start()].rstrip()
    after = m.string[m.end():m.end() + 1]
    if not before or before[-1] in ".!?":
        return "\n\n"
    return " X " if after.islower() or m.group(0).rstrip().rstrip("`$").rstrip().endswith(",") else " X.\n\n"


def prose_of(t):
    t = re.sub(r"^---.*?---", "", t, count=1, flags=re.S)
    t = re.sub(r"```\{code-cell\}.*?```", "\n\nCODECELL\n\n", t, flags=re.S)
    t = re.sub(r"\s*(```\{math\}.*?```|\$\$.*?\$\$)\s*", _display, t, flags=re.S)
    dash = t.count("—")
    p = re.sub(r"\\\$", "", t)  # een geëscapete dollar (\$2 million) is geen wiskundegrens
    p = re.sub(r"\$[^$]*\$", "X", p)
    p = re.sub(r"\{cite[^}]*\}`[^`]*`", "", p)
    p = re.sub(r"\[\]\(#[^)]*\)", "REF", p)
    p = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", p)  # [tekst](url) -> tekst
    p = re.sub(r"^[:`]{3}.*$|^:[\w-]+:.*$", "", p, flags=re.M)
    p = re.sub(r"^#.*$", "", p, flags=re.M)
    p = re.sub(r"^\|.*$", "", p, flags=re.M)
    p = re.sub(r"^(" + LIST + ")", r"\n\1", p, flags=re.M)  # elk lijstitem een eigen blok
    return p, dash


def stats_for(text, name=""):
    prose, dash = prose_of(text)
    blocks = [b.strip() for b in re.split(r"\n\s*\n", prose) if b.strip()]
    paras, one, n_one = [], 0, 0
    sents = []
    for i, b in enumerate(blocks):
        if b == "CODECELL" or len(b.split()) <= 2:
            continue
        is_list = re.match(LIST, b)
        ss = [s for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý\"'(*])", re.sub(LIST, "", b).replace("\n", " "))
              if len(s.split()) > 2]
        if len(b.split()) > 8:
            sents += ss
            if not is_list:
                paras.append(b)
        announce = i + 1 < len(blocks) and blocks[i + 1] == "CODECELL"
        if not is_list and not announce:
            n_one += 1
            one += len(ss) == 1
    lens = [len(s.split()) for s in sents] or [0]
    words = sum(len(b.split()) for b in blocks if b != "CODECELL" and len(b.split()) > 8)
    flat = "\n\n".join(" ".join(b.split()) for b in blocks if b != "CODECELL")
    nobold = re.sub(r"\*\*[^*]+\*\*", "", flat)
    tmpl = {k: len(re.findall(r, flat)) for k, r in TEMPLATES.items()}
    if "00_0" not in name:  # setup en rendementen definiëren de motieven en mogen ze vaker noemen
        tmpl.update({k: len(re.findall(r, nobold, flags=re.I)) for k, r in MOTIFS.items()})
    counts = collections.Counter(" ".join(s.split()) for s in sents if len(s.split()) >= 10)
    return {
        "words": words,
        "sent_mean": round(statistics.mean(lens), 1),
        "sent_p90": sorted(lens)[int(0.9 * (len(lens) - 1))],
        "sent_gt40": sum(n > 40 for n in lens),
        "para_mean": int(statistics.mean(len(p.split()) for p in paras)) if paras else 0,
        "dash": dash,
        "semicol": prose.count(";"),
        "motief": len(re.findall(r"\b[Mm]otief\s*\d|\d%-motief|epistemische? (status|wending)", prose)),
        "Lnum": len(re.findall(r"\bL\d{1,2}\b", prose)),
        "deel": len(re.findall(r"\bDeel [IVX0-9]+\b", prose)),
        "u_form": len(re.findall(r"\b(u|uw)\b", prose)),
        "je_form": len(re.findall(r"\b(je|jij|jouw)\b", prose)),
        "taboo": len(re.findall(r"verrassend|eenvoudigweg|zoals bekend|triviaal", prose, flags=re.I)),
        "stopw": len(re.findall(r"\b(ruwweg|inderdaad|in feite|letterlijk)\b", prose, flags=re.I)),
        "calque": sum(len(re.findall(c, flat)) for c in CALQUES),
        "engquote": len(re.findall(r'"[^"]{25,}"', prose)),
        "colon_mid": round(1000 * len(re.findall(r":\s+[a-z]", re.sub(LABELS, "", flat))) / max(words, 1), 1),
        "para_one": round(100 * one / max(n_one, 1)),
        "telegram": sum(bool(re.search(TELEGRAM, s)) for s in sents),
        "tmpl": max(tmpl.values()),
        "wie_open": sum(s.startswith("Wie ") for s in sents),
        "connect": round(100 * sum(bool(re.search(CONNECT, s, flags=re.I)) for s in sents) / max(len(sents), 1)),
        "repeat": sum(n - 1 for n in counts.values()),
        "info": f"{len(re.findall(ANGLICISMS, flat, flags=re.I))}/{sum(bool(re.match(DAT_IS, s)) for s in sents)}",
        "_tmpl": ", ".join(f"{k} {v}" for k, v in tmpl.items() if v > THRESHOLDS["tmpl"][1]),
    }


def where(path):
    """Print calque-, sjabloon- en anglicisme-treffers met regelnummer op de ruwe tekst."""
    pats = CALQUES + list(TEMPLATES.values()) + list(MOTIFS.values()) + [ANGLICISMS]
    for i, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        for c in pats:
            for m in re.finditer(c.replace("(?m)", ""), line, flags=re.I if c == ANGLICISMS else 0):
                print(f"{path}:{i}: {m.group(0)!r}  in: {line.strip()[:100]}")


def bad_of(c):
    bad = []
    for h, (lo, hi) in THRESHOLDS.items():
        if hi is not None and c[h] > hi:
            bad.append(f"{h}={c[h]} (max {hi})" + (f" [{c['_tmpl']}]" if h == "tmpl" else ""))
        if lo is not None and c[h] < lo:
            bad.append(f"{h}={c[h]} (min {lo})")
    return bad


def selftest():
    t = """---
kernel: x
---
# Kop met In woorden: telt niet

Eerst de data en de Sharpe-ratio van de markt. Wie lang leeft, ziet veel. Wie kort leeft, ziet weinig.
De remedie is de reden dat we portefeuilles bouwen. De hedgevraag hangt aan de helling hier.
Het model verklaart dit deel van de premie: de rest blijft open voor later onderzoek.
In woorden: de prijs daalt als de rente stijgt. In woorden: nog een keer hetzelfde label.
In woorden: en een derde keer, dat is te veel. Die paper gebruikt value-weighted rendementen.
Dat is de standaardfout van 2% uit het eerste college, en die komt vaak terug in de tekst.
Dat is de standaardfout van 2% uit het eerste college, en die komt vaak terug in de tekst.

Een losse alinea van één zin met genoeg woorden erin om mee te tellen.

De prijs volgt uit de som

$$
P = \\sum_t D_t,
$$

waarbij de som over alle perioden loopt, omdat de looptijd oneindig is.

De cel hieronder rekent het na.

```{code-cell} python
x = 1
```
"""
    c = stats_for(t)
    expect = {"telegram": 1, "wie_open": 2, "tmpl": 3, "repeat": 1, "info": "2/2"}
    for k, v in expect.items():
        assert c[k] == v, (k, c[k], v)
    assert c["calque"] == 2, c["calque"]
    assert c["colon_mid"] > 0 and c["para_one"] == 67 and 0 < c["connect"] < 100, c
    # display-vergelijking midden in de zin: één zin van 1 + 17 woorden
    assert any(n > 15 for n in [len(s.split()) for s in re.split(r"(?<=[.!?])\s+", prose_of(t)[0])]), "display"
    assert "tmpl" in " ".join(bad_of(c)) and "repeat" in " ".join(bad_of(c))
    print("selftest OK")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    check = "--check" in argv
    files = [a for a in argv if not a.startswith("--")] or sorted(glob.glob("lectures/[0-9]*.md"))
    if "--where" in argv:
        for f in files:
            where(f)
        return 0
    hdr = list(THRESHOLDS) + ["info"]
    w = {h: max(len(h), 5) for h in hdr}
    print("lecture".ljust(30), " ".join(h.rjust(w[h]) for h in hdr))
    failed = False
    for f in files:
        c = stats_for(open(f, encoding="utf-8").read(), f)
        name = f.replace("\\", "/").split("/")[-1][:30]
        print(name.ljust(30), " ".join(str(c[h]).rjust(w[h]) for h in hdr))
        if check:
            bad = bad_of(c)
            print("  " + ("PASS" if not bad else "FAIL: " + ", ".join(bad)))
            failed |= bool(bad)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
