#!/usr/bin/env python3
"""Accessibility checker for CHEM 427/527 course materials.

Checks the mechanical items of the course accessibility checklist on Markdown
files, on the markdown cells of Jupyter notebooks, and on PDF slide decks, then
prints the items that need a person's judgment as reminders. Exits 1 if any
check fails.

The checklist follows the UW Accessible Technology guidance for documents,
https://www.washington.edu/accesstech/documents/

Usage:
    python tools/a11y_check.py sessions/S01-onboarding
    python tools/a11y_check.py sessions/S02-python-with-chemical-data/slides/S02-opening-slides.pdf
    python tools/a11y_check.py setup.md ai-practices.md
    python tools/a11y_check.py .                      # whole repository
    python tools/a11y_check.py sessions/S01-onboarding --no-reminders
"""

import argparse
import json
import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".venv", ".ipynb_checkpoints", "node_modules", "__pycache__"}

ALT_MIN, ALT_MAX = 125, 250

# Link text that means nothing when a screen reader lists the links on a page.
VAGUE_LINK_TEXT = {
    "here", "click here", "this", "this link", "link", "this page", "page",
    "more", "read more", "learn more", "more info", "info", "go", "see here",
}

# Alt text should describe the image, not announce that it is one.
ALT_REDUNDANT_RE = re.compile(r"^\s*(an?\s+)?(image|picture|photo|graphic|figure|screenshot)\s+(of|showing)\b", re.I)

# Colormaps that are not perceptually uniform or not colorblind-safe.
BAD_CMAPS = {"jet", "rainbow", "hsv", "gist_rainbow", "nipy_spectral", "gist_ncar", "prism", "flag"}
CMAP_RE = re.compile(r"""(?:cmap\s*=\s*|get_cmap\(\s*|colormaps\[\s*)["']([A-Za-z_]+?)(?:_r)?["']""")

# A red and green pair in one plotting cell is the classic color-alone failure.
RED_RE = re.compile(r"""(?:color|c)\s*=\s*["'](?:r|red|tab:red|darkred)["']""")
GREEN_RE = re.compile(r"""(?:color|c)\s*=\s*["'](?:g|green|tab:green|lime|darkgreen)["']""")

PLOT_CALL_RE = re.compile(r"\bplt\.show\(|\bfig\.show\(|\bdisplay\(\s*fig")

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
ATX_RE = re.compile(r"^\s{0,3}(#{1,6})(?:\s+(.*?))?\s*#*\s*$")
SETEXT_RE = re.compile(r"^\s{0,3}(=+|-+)\s*$")
HTML_H_RE = re.compile(r"<h([1-6])\b", re.I)
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
HTML_ALT_RE = re.compile(r"""\balt\s*=\s*(["'])(.*?)\1""", re.I | re.S)
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]*)(?:\s+\"[^\"]*\")?\)")
HTML_LINK_RE = re.compile(r"<a\b[^>]*>(.*?)</a>", re.I | re.S)
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
BARE_URL_RE = re.compile(r"(?<![(<\"'=])\bhttps?://[^\s)>\]]+")
URLISH_RE = re.compile(r"^(https?://|www\.)\S+$", re.I)
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
HTML_TABLE_RE = re.compile(r"<table\b.*?</table>", re.I | re.S)
SPAN_RE = re.compile(r"\b(colspan|rowspan)\s*=", re.I)
DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.S)
INLINE_MATH_RE = re.compile(r"(?<![\\$\w])\$(?!\s)([^$\n]+?)(?<!\s)\$(?![\w$])")


# ── Report ────────────────────────────────────────────────────────────────────

class Report:
    def __init__(self, label):
        self.label = label
        self.failures = []
        self.warnings = []

    def fail(self, where, msg):
        self.failures.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")

    def print(self):
        print(f"\n{self.label}")
        for f in self.failures:
            print(f"  FAIL  {f}")
        for w in self.warnings:
            print(f"  WARN  {w}")
        if not self.failures and not self.warnings:
            print("  ok")


# ── Markdown text handling ────────────────────────────────────────────────────

def prose_lines(text):
    """Return [(line_number, line)] with fenced code blocks, inline code and
    HTML comments blanked out, so checks see only the prose."""
    text = HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    out = []
    fence = None
    for i, line in enumerate(text.splitlines(), start=1):
        m = FENCE_RE.match(line)
        if fence is None and m:
            fence = m.group(1)[0] * len(m.group(1))
            out.append((i, ""))
            continue
        if fence is not None:
            if line.strip().startswith(fence) and line.strip().strip(fence[0]) == "":
                fence = None
            out.append((i, ""))
            continue
        out.append((i, INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), line)))
    return out


def headings(lines):
    """Yield (line_number, level, text) for ATX, setext and HTML headings."""
    prev = None
    for n, line in lines:
        m = ATX_RE.match(line)
        if m and not line.lstrip().startswith("#!"):
            yield n, len(m.group(1)), (m.group(2) or "").strip()
        elif SETEXT_RE.match(line) and prev is not None and prev[1].strip() \
                and not TABLE_ROW_RE.match(prev[1]) and not ATX_RE.match(prev[1]) \
                and not re.match(r"^\s*([-*+>]|\d+\.)\s", prev[1]):
            # A line of = or - directly under a paragraph line is a heading.
            yield prev[0], 1 if line.strip()[0] == "=" else 2, prev[1].strip()
        for hm in HTML_H_RE.finditer(line):
            yield n, int(hm.group(1)), "<html heading>"
        prev = (n, line)


def check_headings(lines, where, r):
    hs = list(headings(lines))
    h1 = [h for h in hs if h[1] == 1]
    if len(h1) == 0:
        r.fail(where(1), "no H1; the document needs exactly one, as its title")
    elif len(h1) > 1:
        r.fail(where(h1[1][0]), f"{len(h1)} H1 headings ({', '.join(where(h[0]) for h in h1)}); use one")
    if hs and hs[0][1] != 1:
        r.fail(where(hs[0][0]), f"first heading is H{hs[0][1]}, not the H1 title")
    for (_, a, _), (n, b, t) in zip(hs, hs[1:]):
        if b > a + 1:
            r.fail(where(n), f"heading jumps from H{a} to H{b} ('{t[:50]}')")
    for n, lvl, t in hs:
        if not t:
            r.fail(where(n), f"empty H{lvl} heading")


def check_links(lines, where, r):
    for n, line in lines:
        for m in MD_LINK_RE.finditer(line):
            check_link_text(m.group(1), where(n), r)
        for m in HTML_LINK_RE.finditer(line):
            check_link_text(re.sub(r"<[^>]+>", "", m.group(1)), where(n), r)
        for m in AUTOLINK_RE.finditer(line):
            r.fail(where(n), f"bare URL as link text: {m.group(1)[:70]}")
        scrubbed = MD_LINK_RE.sub(lambda m: " " * len(m.group(0)), line)
        scrubbed = MD_IMAGE_RE.sub(lambda m: " " * len(m.group(0)), scrubbed)
        scrubbed = AUTOLINK_RE.sub(lambda m: " " * len(m.group(0)), scrubbed)
        scrubbed = re.sub(r"<[^>]+>", lambda m: " " * len(m.group(0)), scrubbed)
        for m in BARE_URL_RE.finditer(scrubbed):
            r.fail(where(n), f"bare URL in text; give it descriptive link text: {m.group(0)[:70]}")


def check_link_text(text, where, r):
    t = re.sub(r"[*_`]", "", text).strip()
    if not t:
        r.fail(where, "link with empty text")
    elif t.lower().rstrip(".:") in VAGUE_LINK_TEXT:
        r.fail(where, f"link text '{t}' does not say where it goes")
    elif URLISH_RE.match(t):
        r.fail(where, f"URL used as link text: {t[:70]}")


def check_images(lines, where, r):
    for n, line in lines:
        alts = [m.group(1) for m in MD_IMAGE_RE.finditer(line)]
        for tag in HTML_IMG_RE.findall(line):
            am = HTML_ALT_RE.search(tag)
            alts.append(None if am is None else am.group(2))
        for alt in alts:
            if alt is None:
                r.fail(where(n), "<img> without an alt attribute")
                continue
            a = alt.strip()
            if not a:
                r.fail(where(n), "image with empty alt text")
            elif not ALT_MIN <= len(a) <= ALT_MAX:
                r.fail(where(n), f"alt text is {len(a)} characters; the course range is {ALT_MIN} to {ALT_MAX}")
            if a and ALT_REDUNDANT_RE.match(a):
                r.fail(where(n), f"alt text opens with '{ALT_REDUNDANT_RE.match(a).group(0).strip()}'; describe the content instead")


def split_cells(row):
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|") and not row.endswith("\\|"):
        row = row[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", row)]


def check_tables(lines, raw_text, where, r):
    i = 0
    while i < len(lines):
        n, line = lines[i]
        if not TABLE_ROW_RE.match(line):
            i += 1
            continue
        block = []
        while i < len(lines) and TABLE_ROW_RE.match(lines[i][1]):
            block.append(lines[i])
            i += 1
        if len(block) < 2 or not TABLE_SEP_RE.match(block[1][1]):
            r.fail(where(n), "table without a header row; the second line must be the |---| separator")
            continue
        header = split_cells(block[0][1])
        if any(not c for c in header):
            r.fail(where(n), "table header has an empty cell; every column needs a header")
        width = len(header)
        for bn, bline in block[2:]:
            if len(split_cells(bline)) != width:
                r.fail(where(bn), f"table row has {len(split_cells(bline))} cells, header has {width}; "
                                  "merged or missing cells")
    for m in HTML_TABLE_RE.finditer(raw_text):
        start = raw_text[: m.start()].count("\n") + 1
        if SPAN_RE.search(m.group(0)):
            r.fail(where(start), "HTML table with colspan or rowspan; split it into simple tables")
        if "<th" not in m.group(0).lower():
            r.fail(where(start), "HTML table without <th> header cells")


def find_math(lines):
    text = "\n".join(l for _, l in lines)
    hits = []
    for m in DISPLAY_MATH_RE.finditer(text):
        hits.append((text[: m.start()].count("\n") + 1, "$$" + m.group(1).strip()[:40] + "$$"))
    stripped = DISPLAY_MATH_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    for m in INLINE_MATH_RE.finditer(stripped):
        hits.append((stripped[: m.start()].count("\n") + 1, "$" + m.group(1)[:40] + "$"))
    return sorted(hits)


def check_markdown_text(text, where, r, math_hits):
    lines = prose_lines(text)
    check_headings(lines, where, r)
    check_links(lines, where, r)
    check_images(lines, where, r)
    blank = "\n".join(l for _, l in lines)
    check_tables(lines, blank, where, r)
    for n, snippet in find_math(lines):
        math_hits.append(where(n) + " " + snippet)


# ── PDF ───────────────────────────────────────────────────────────────────────

def struct_figures(reader):
    """[(page, alt)] for each /Figure in the PDF's structure tree; alt is None if missing."""
    from pypdf.generic import ArrayObject, DictionaryObject

    pages = {pg.indirect_reference.idnum: i for i, pg in enumerate(reader.pages, start=1)}
    figures = []

    def walk(node, page):
        node = node.get_object()
        if isinstance(node, ArrayObject):
            for kid in node:
                walk(kid, page)
            return
        if not isinstance(node, DictionaryObject):
            return
        if "/Pg" in node:
            page = pages.get(node.raw_get("/Pg").idnum, page)
        if node.get("/S") == "/Figure":
            alt = node.get("/Alt")
            figures.append((page, str(alt).strip() if alt is not None else None))
        kids = node.get("/K")
        if kids is not None and not isinstance(kids, int):
            walk(kids, page)

    walk(reader.trailer["/Root"]["/StructTreeRoot"], None)
    return figures


def check_pdf(path, r, figure_hits):
    """A slide deck's PDF: tagged, titled, in a language, with text on every page."""
    try:
        from pypdf import PdfReader
    except ImportError:
        r.fail("file", "pypdf is not installed; run uv sync and check the PDF again")
        return
    reader = PdfReader(path)
    root = reader.trailer["/Root"]
    mark = root.get("/MarkInfo")
    if "/StructTreeRoot" not in root or not (mark and mark.get_object().get("/Marked")):
        r.fail("file", "PDF is not tagged; export it with tags (Chrome: --export-tagged-pdf)")
    title = (reader.metadata or {}).get("/Title")
    if not title or not str(title).strip():
        r.fail("file", "PDF has no title in its document properties")
    prefs = root.get("/ViewerPreferences")
    if not (prefs and prefs.get_object().get("/DisplayDocTitle")):
        r.warn("file", "PDF does not ask viewers to show its title in place of the file name")
    if not str(root.get("/Lang") or "").strip():
        r.fail("file", "PDF has no document language (/Lang)")
    for n, page in enumerate(reader.pages, start=1):
        if not (page.extract_text() or "").strip():
            r.fail(f"page {n}", "no extractable text; a page that is only an image cannot be read aloud")
    if "/StructTreeRoot" in root:
        for page, alt in struct_figures(reader):
            if not alt:
                r.fail(f"page {page}", "figure without alt text")
            else:
                figure_hits.append(f"page {page}: {alt[:90]}")


# ── Files ─────────────────────────────────────────────────────────────────────

def check_md_file(path, r, math_hits):
    text = path.read_text(encoding="utf-8")
    check_markdown_text(text, lambda n: f"line {n}", r, math_hits)


def check_notebook(path, r, math_hits):
    nb = json.loads(path.read_text(encoding="utf-8"))
    cells = nb.get("cells", [])

    # Headings, links, images, tables and math: all markdown cells read as one
    # document, since a screen reader user navigates the rendered notebook
    # as one page. Locations are reported as cell and line.
    joined, index = [], []
    for ci, c in enumerate(cells, start=1):
        if c["cell_type"] != "markdown":
            continue
        src = "".join(c.get("source", []))
        for li, _ in enumerate(src.splitlines() or [""], start=1):
            index.append((ci, li))
        joined.append(src if src.endswith("\n") or not src else src + "\n")
    text = "".join(joined)

    def where(n):
        if 1 <= n <= len(index):
            ci, li = index[n - 1]
            return f"cell {ci} line {li}"
        return "notebook"

    check_markdown_text(text, where, r, math_hits)

    # Every plot is followed by a markdown cell that describes it in words.
    for ci, c in enumerate(cells, start=1):
        if c["cell_type"] != "code":
            continue
        src = "".join(c.get("source", []))
        code = "\n".join(l for l in src.splitlines() if not l.lstrip().startswith("#"))
        has_image = any("image/png" in o.get("data", {}) or "image/svg+xml" in o.get("data", {})
                        for o in c.get("outputs", []))
        if PLOT_CALL_RE.search(code) or has_image:
            nxt = cells[ci] if ci < len(cells) else None
            nxt_src = "".join(nxt.get("source", [])).strip() if nxt else ""
            if nxt is None or nxt["cell_type"] != "markdown" or not nxt_src:
                r.fail(f"cell {ci}", "plot is not followed by a markdown cell describing it")
            elif ATX_RE.match(nxt_src.splitlines()[0]):
                r.fail(f"cell {ci + 1}", "the cell after the plot opens with a heading, "
                                         "not a sentence describing the plot")
        for m in CMAP_RE.finditer(code):
            if m.group(1).lower() in BAD_CMAPS:
                r.fail(f"cell {ci}", f"colormap '{m.group(1)}' is not colorblind-safe; "
                                     "use viridis, cividis, or another perceptually uniform map")
        if RED_RE.search(code) and GREEN_RE.search(code):
            r.warn(f"cell {ci}", "red and green in one plot; make sure marker, line style or a "
                                 "label also tells the series apart")


def collect(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.suffix in {".md", ".ipynb", ".pdf"} and f.is_file() \
                        and not SKIP_DIRS.intersection(f.relative_to(p).parts):
                    files.append(f)
        elif p.is_file():
            files.append(p)
        else:
            print(f"a11y_check: no such file or folder: {p}", file=sys.stderr)
            sys.exit(2)
    return files


REMINDERS = """
Judgment items the script cannot check. Look at each before publishing:
  - Alt text says what the image shows (axes, trend, the feature that matters),
    and a chart has its detailed description in the text nearby.
  - The sentence after each notebook plot matches what the plot actually shows.
  - Nothing is conveyed by color alone, in prose ("the red peak") or in figures:
    series differ by marker, line style, or a direct label as well as color.
  - Figures use a colorblind-safe palette (Okabe-Ito, viridis, cividis; the
    Matplotlib default cycle only with a marker or line style per series, since
    its third and fourth colors are green and red) and text and lines in
    figures have enough contrast.
  - Each equation is also said in words in the sentence around it.
  - Link text makes sense read alone, out of its sentence.
  - Lists are Markdown lists, not lines that only look like one.
  - Instructions do not rely on position alone ("the button on the right").
  - In a slide deck PDF, each chart has a text description on its own slide
    that a student who missed the opening can read: the trend and the numbers
    the slide's point rests on, not only axis labels.
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+", help="Markdown files, notebooks, PDFs, or folders to search")
    ap.add_argument("--no-reminders", action="store_true", help="skip the judgment-item reminders")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    files = collect(args.paths)
    if not files:
        print("a11y_check: no .md, .ipynb or .pdf files found", file=sys.stderr)
        sys.exit(2)

    n_fail = 0
    math_hits, figure_hits = [], []
    for f in files:
        r = Report(f.as_posix())
        hits = []
        if f.suffix == ".pdf":
            check_pdf(f, r, hits)
            figure_hits += [f"{f.as_posix()}, {h}" for h in hits]
        else:
            if f.suffix == ".ipynb":
                check_notebook(f, r, hits)
            else:
                check_md_file(f, r, hits)
            math_hits += [f"{f.as_posix()}, {h}" for h in hits]
        r.print()
        n_fail += len(r.failures)

    if math_hits:
        print("\nMath to check for a text alternative in the surrounding sentence:")
        for h in math_hits:
            print(f"  {h}")

    if figure_hits:
        print("\nPDF figures, with the alt text a screen reader announces; check it against the chart:")
        for h in figure_hits:
            print(f"  {h}")

    if not args.no_reminders:
        print(REMINDERS, end="")

    print(f"\n{len(files)} file(s) checked, {n_fail} failure(s).")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
