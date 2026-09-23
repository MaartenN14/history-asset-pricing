"""Meet leesbaarheid en stijlregels van de lopende tekst in lectures/*.md.

Gebruik:
    uv run python tools/prose_stats.py                      # tabel voor alle lectures
    uv run python tools/prose_stats.py lectures/02_08_capm.md
    uv run python tools/prose_stats.py --check lectures/02_08_capm.md   # PASS/FAIL per drempel
    uv run python tools/prose_stats.py --where lectures/02_08_capm.md   # vindplaatsen van calques

Code-cellen, math-blokken, tabellen, kopjes en directive-regels worden weggelaten;
inline-wiskunde telt als één woord. De drempels staan in THRESHOLDS en horen bij
plannen/verbeterplan-didactiek.md §8 en STYLE.md §11.
"""
import glob
import re
import statistics
import sys

# (metriek, maximum). None = alleen rapporteren.
THRESHOLDS = {
    "words": 5500,      # lopende tekst, excl. code/wiskunde/tabellen
    "sent_mean": 17,    # gemiddelde zinslengte in woorden
    "sent_p90": 28,     # 90e percentiel zinslengte
    "sent_gt40": 2,     # zinnen langer dan 40 woorden
    "para_mean": 45,    # gemiddelde alinealengte in woorden
    "dash": 10,         # gedachtestreepjes (—)
    "semicol": 15,      # puntkomma's in lopende tekst
    "motief": 0,        # "motief 1/2/3": projectjargon
    "Lnum": 0,          # "L4", "L26": projectjargon
    "deel": 0,          # "Deel V": projectjargon
    "u_form": 0,        # aanspreekvorm "u"
    "je_form": 0,       # aanspreekvorm "je/jij/jouw"
    "taboo": 0,         # verrassend, eenvoudigweg, zoals bekend, triviaal
    "stopw": 6,         # precies, ruwweg, inderdaad, in feite, letterlijk
    "calque": 0,        # vertaald Engels, zie CALQUES
    "engquote": 5,      # aanhalingen van 25+ tekens (meestal Engelse citaten)
}

# Vertaald Engels dat in de lectures voorkomt (STYLE.md §11.4). Regex, hoofdlettergevoelig
# waar dat de valse treffers beperkt.
CALQUES = [
    r"\bde nul\b(?!hypothese)",                 # "the null" -> de nulhypothese
    r"omvang van de toets",                     # "size of the test" -> werkelijk significantieniveau
    r"\bNoteer\b",                              # "Note that" -> weglaten of "Let wel"
    r"\bOnthoud dat\b",                         # "Remember that" -> weglaten of "Bedenk dat"
    r"\b(Twee|Drie|Vier) dingen\b",             # "Two things ..." -> "Deze tabel laat twee dingen zien"
    r"\b(Dit|Dat) is de reden dat\b",           # "This is the reason that" -> "Daarom"
    r"\b(Dit|Dat) is wat\b",                    # "This is what X means" -> "Dat betekent X"
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
]


def prose_of(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"^---.*?---", "", t, count=1, flags=re.S)
    t = re.sub(r"```\{code-cell\}.*?```", "", t, flags=re.S)
    t = re.sub(r"```\{math\}.*?```", "", t, flags=re.S)
    t = re.sub(r"\$\$.*?\$\$", "", t, flags=re.S)
    dash = t.count("—")
    p = re.sub(r"\$[^$]*\$", "X", t)
    p = re.sub(r"\{cite[^}]*\}`[^`]*`", "", p)
    p = re.sub(r"\[\]\(#[^)]*\)", "REF", p)
    p = re.sub(r"^[:`]{3}.*$", "", p, flags=re.M)
    p = re.sub(r"^#.*$", "", p, flags=re.M)
    p = re.sub(r"^\|.*$", "", p, flags=re.M)
    return p, dash


def stats_for(path):
    prose, dash = prose_of(path)
    paras = [p for p in re.split(r"\n\s*\n", prose) if len(p.split()) > 8]
    sents = []
    for p in paras:
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", p.replace("\n", " ")):
            n = len(s.split())
            if n > 2:
                sents.append(n)
    if not sents:
        sents = [0]
    return {
        "words": sum(len(p.split()) for p in paras),
        "sent_mean": round(statistics.mean(sents), 1),
        "sent_p90": sorted(sents)[int(0.9 * (len(sents) - 1))],
        "sent_gt40": sum(s > 40 for s in sents),
        "para_mean": int(statistics.mean(len(p.split()) for p in paras)) if paras else 0,
        "dash": dash,
        "semicol": prose.count(";"),
        "motief": len(re.findall(r"\b[Mm]otief\s*\d|\d%-motief|epistemische? (status|wending)", prose)),
        "Lnum": len(re.findall(r"\bL\d{1,2}\b", prose)),
        "deel": len(re.findall(r"\bDeel [IVX0-9]+\b", prose)),
        "u_form": len(re.findall(r"\b(u|uw)\b", prose)),
        "je_form": len(re.findall(r"\b(je|jij|jouw)\b", prose)),
        "taboo": len(re.findall(r"verrassend|eenvoudigweg|zoals bekend|triviaal", prose, flags=re.I)),
        "stopw": len(re.findall(r"\b(precies|ruwweg|inderdaad|in feite|letterlijk)\b", prose, flags=re.I)),
        "calque": sum(len(re.findall(c, prose)) for c in CALQUES),
        "engquote": len(re.findall(r'"[^"]{25,}"', prose)),
    }


def where(path):
    """Print elke calque-treffer met regelnummer, op de ruwe tekst (regelnummers kloppen dan)."""
    lines = open(path, encoding="utf-8").read().splitlines()
    for i, line in enumerate(lines, 1):
        for c in CALQUES:
            for m in re.finditer(c.replace("(?m)", ""), line):
                print(f"{path}:{i}: {m.group(0)!r}  in: {line.strip()[:100]}")


def main(argv):
    check = "--check" in argv
    files = [a for a in argv if not a.startswith("--")] or sorted(glob.glob("lectures/[0-9]*.md"))
    if "--where" in argv:
        for f in files:
            where(f)
        return 0
    hdr = list(THRESHOLDS)
    print("lecture".ljust(30), " ".join(h.rjust(9) for h in hdr))
    failed = False
    for f in files:
        c = stats_for(f)
        name = f.replace("\\", "/").split("/")[-1][:30]
        print(name.ljust(30), " ".join(str(c[h]).rjust(9) for h in hdr))
        if check:
            bad = [f"{h}={c[h]} (max {m})" for h, m in THRESHOLDS.items() if m is not None and c[h] > m]
            print("  " + ("PASS" if not bad else "FAIL: " + ", ".join(bad)))
            failed |= bool(bad)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
