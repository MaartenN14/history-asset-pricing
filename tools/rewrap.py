"""Breek te lange prozaregels (> 92 tekens) in een jupytext-.md op spaties af tot ~90.

Raakt niets aan in code-fences, directives, $$-blokken, frontmatter, tabellen, kopjes,
label- of optieregels; breekt niet binnen $…$, `…` of [..](..). Kortere regels blijven
zoals ze zijn, dus de diff blijft klein.   gebruik: uv run python tools/rewrap.py FILE...
"""
import re, sys
WIDTH = 90
SKIP = re.compile(r"^(\||#|:|<|!\[|\(.*\)=\s*$|---\s*$|\s*$)")
LIST = re.compile(r"^(\s*(?:[-*+]|\d{1,2}\.)\s+)")

def open_span(s):
    return (s.count("$") % 2 or s.count("`") % 2 or s.count("[") > s.count("]")
            or s.rfind("](") > s.rfind(")"))

def wrap(line):
    m = LIST.match(line); prefix = m.group(1) if m else ""
    indent = " " * len(prefix) if m else re.match(r"^\s*", line).group(0)
    words = line[len(prefix):].split(" ") if m else line.strip().split(" ")
    out, cur = [], prefix if m else indent
    for w in words:
        cand = cur + w if (cur == "" or cur.endswith(" ")) else cur + " " + w
        if len(cand) > WIDTH and cur.strip() and not open_span(cur):
            out.append(cur.rstrip()); cur = indent + w
        else:
            cur = cand
    out.append(cur.rstrip())
    return out

def rewrap(text):
    lines, out, fence, math, fm = text.split("\n"), [], None, False, 0
    for i, ln in enumerate(lines):
        st = ln.strip()
        if i == 0 and st == "---": fm = 1; out.append(ln); continue
        if fm == 1:
            out.append(ln)
            if st == "---": fm = 2
            continue
        if fence is None and re.match(r"^\s*(`{3,}|:{3,})", st):
            fence = re.match(r"^\s*(`{3,}|:{3,})", st).group(1)[0] * 3; out.append(ln); continue
        if fence is not None:
            out.append(ln)
            if st.startswith(fence): fence = None
            continue
        if st.startswith("$$"):
            out.append(ln); math = not math if st == "$$" or st.count("$$") == 1 else math; continue
        if math or len(ln) <= WIDTH + 2 or SKIP.match(ln) or "$$" in ln:
            out.append(ln); continue
        out.extend(wrap(ln))
    # ponytail: een onafgesloten fence verschuift alle paren erna en breekt dan codecellen af
    assert fence is None and not math, "onafgesloten fence of $$-blok: bestand niet herschreven"
    return "\n".join(out)

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        t = "Dit is een lange zin met $x_{t} + y$ erin die zeker langer is dan negentig tekens en daarom moet breken, maar niet in de wiskunde.\n"
        r = rewrap(t)
        assert all(len(l) <= WIDTH + 12 for l in r.split("\n")) and "$x_{t} + y$" in r and r.replace("\n", " ") == t.replace("\n", " ")
        li = rewrap("- " + "woord " * 30 + "\n")
        assert li.startswith("- woord") and "-  " not in li and li.split("\n")[1].startswith("  woord")
        assert rewrap("```{code-cell}\n" + "x" * 200 + "\n```\n") == "```{code-cell}\n" + "x" * 200 + "\n```\n"
        print("selftest OK"); sys.exit()
    for f in sys.argv[1:]:
        s = open(f, encoding="utf-8").read(); r = rewrap(s)
        if r != s:
            open(f, "w", encoding="utf-8", newline="\n").write(r)
        print(f, "regels:", s.count("\n"), "->", r.count("\n"))
