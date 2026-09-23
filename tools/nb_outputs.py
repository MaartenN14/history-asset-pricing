"""Schrijf de uitvoer van alle code-cellen in een .ipynb als platte tekst, voor een diff vóór/na.

Gebruik:
    git show HEAD:lectures/02_08_capm.ipynb > /tmp/voor.ipynb
    uv run python tools/nb_outputs.py /tmp/voor.ipynb > /tmp/voor.txt
    uv run python tools/nb_outputs.py lectures/02_08_capm.ipynb > /tmp/na.txt
    diff /tmp/voor.txt /tmp/na.txt

Tekstuitvoer (tabellen, prints, foutmeldingen) wordt letterlijk afgedrukt; figuren alleen
als "image/png (<n> bytes)", zodat een onveranderde figuur ook onveranderd oogt.
"""
import json
import sys


def main(path):
    sys.stdout.reconfigure(encoding="utf-8")   # Windows-console en redirect: altijd UTF-8
    nb = json.load(open(path, encoding="utf-8"))
    k = 0
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        k += 1
        first = "".join(cell["source"]).strip().splitlines()[:1]
        print(f"=== cel {k}: {first[0] if first else ''}")
        for out in cell.get("outputs", []):
            kind = out.get("output_type")
            if kind == "stream":
                print("".join(out.get("text", "")).rstrip())
            elif kind in ("execute_result", "display_data"):
                data = out.get("data", {})
                if "text/plain" in data:
                    print("".join(data["text/plain"]).rstrip())
                for mime in data:
                    if mime.startswith("image/"):
                        print(f"[{mime} ({len(''.join(data[mime]))} bytes)]")
            elif kind == "error":
                print("ERROR:", out.get("ename"), out.get("evalue"))
        print()


if __name__ == "__main__":
    main(sys.argv[1])
