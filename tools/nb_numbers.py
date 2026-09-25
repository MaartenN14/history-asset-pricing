"""Meld getallen in de proza van een lecture die niet in de celuitvoer voorkomen.

Gebruik:
    uv run python tools/nb_numbers.py lectures/03_12_consumptie_capm.md

Leest de proza (buiten code-cellen) van de .md, haalt er getallen met decimalen of met
drie of meer cijfers uit (jaartallen 1600–2100 uitgezonderd) en zoekt ze, ook als
percentage (×100, ÷100) en op minder decimalen, in de uitvoer van de gekoppelde .ipynb.
Wat niet gevonden wordt, is een kandidaat voor handmatige controle: een bron, een
handberekening of een fout.
"""
import re
import subprocess
import sys
from pathlib import Path

NUM = re.compile(r"(?<![\w.])-?\d+(?:[.,]\d+)?(?![\w])")


def to_float(s):
    s = s.replace("{,}", ",")
    if re.fullmatch(r"-?\d{1,3}\.\d{3}", s):      # 4.500 = duizendtal in NL-proza
        return float(s.replace(".", ""))
    return float(s.replace(",", "."))


def prose_lines(md):
    lines, fence, is_code = [], None, False
    for i, line in enumerate(md.splitlines(), 1):
        if fence is None and line.startswith("```"):
            fence = line[: len(line) - len(line.lstrip("`"))]
            is_code = "{code-cell}" in line
            continue
        if fence is not None and line.strip() == fence:
            fence, is_code = None, False
            continue
        if not is_code:
            lines.append((i, line))
    return lines


def main(path):
    sys.stdout.reconfigure(encoding="utf-8")
    md = Path(path).read_text(encoding="utf-8").replace("{,}", ",")
    out = subprocess.run([sys.executable, str(Path(__file__).with_name("nb_outputs.py")), str(Path(path).with_suffix(".ipynb"))],
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
    out_nums = {abs(float(m)) for m in re.findall(r"-?\d+(?:\.\d+)?", out)}
    # ponytail: rondt op 0..4 decimalen af; een getal in de proza met meer decimalen dan de cel valt hierdoor niet
    keys = {round(x, d) for x in out_nums for d in range(5)} | {round(x * f, d) for x in out_nums for f in (100, 0.01) for d in range(5)}
    missing = 0
    for i, line in prose_lines(md):
        for m in NUM.finditer(line):
            s = m.group()
            if "," not in s and line[m.end():m.end() + 1] != "%":   # heel getal zonder %: breuk, pagina, jaartal
                continue
            x = abs(to_float(s))
            dec = len(s.split(",")[1]) if "," in s else 0
            if round(x, dec) not in keys:
                missing += 1
                print(f"regel {i}: {s}  |  {line.strip()[:90]}")
    print(f"\n{missing} getallen niet in de celuitvoer gevonden")


if __name__ == "__main__":
    main(sys.argv[1])
