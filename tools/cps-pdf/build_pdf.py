#!/usr/bin/env python3
"""
Build a print-quality PDF from an Actalis CP/CPS Markdown file.

Pipeline:  Markdown (+ YAML front matter)  --pandoc-->  HTML  --WeasyPrint-->  PDF

Usage:
    python build_pdf.py CPS/TLS_CP_CPS_v6.1.md -o out/TLS_CP_CPS_v6.1_EN.pdf
    python build_pdf.py CPS/it/TLS_CP_CPS_v6.1_IT.md --lang it -o out/TLS_CP_CPS_v6.1_IT.pdf

Requirements: pandoc (>= 2.19) on PATH, `pip install weasyprint pyyaml`.
"""
import argparse
import html
import pathlib
import re
import subprocess
import sys

import yaml
from weasyprint import HTML, CSS

HERE = pathlib.Path(__file__).resolve().parent

# Labels printed by the template (cover page, header/footer, TOC).
LABELS = {
    "en": {
        "version": "Version",
        "date": "Date",
        "approved_by": "Approved by",
        "doc_code": "Document code",
        "distribution": "Distribution",
        "toc": "Table of contents",
        "page": "Page",
        "of": "of",
        "authoritative": "",
    },
    "it": {
        "version": "Versione",
        "date": "Data",
        "approved_by": "Approvato da",
        "doc_code": "Codice documento",
        "distribution": "Distribuzione",
        "toc": "Indice",
        "page": "Pagina",
        "of": "di",
        # Shown on the cover of the Italian edition (EN prevails, see §1.2).
        "authoritative": "In caso di discordanza tra la versione italiana e quella "
                         "inglese, prevale la versione inglese.",
    },
}

# Front-matter keys as they appear in the repository's Markdown files.
META_KEYS = {
    "title": ["Title", "Titolo"],
    "version": ["Version", "Versione"],
    "date": ["Date", "Data"],
    "approved_by": ["Approved by", "Approvato da"],
    "doc_code": ["Document Code", "Codice documento"],
    "distribution": ["Distribution", "Distribuzione"],
    "lang": ["Language", "Lingua", "lang"],
    "cover_title": ["Cover Title"],
    "subtitle": ["Subtitle", "Sottotitolo"],
}


def split_front_matter(text: str):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    raw = yaml.safe_load(m.group(1)) or {}
    meta = {}
    for key, aliases in META_KEYS.items():
        for a in aliases:
            if a in raw:
                meta[key] = str(raw[a])
                break
    return meta, text[m.end():]


KV_LINE = re.compile(r"^\s*([^:\n]{2,40}?):\s+(\S.*)$")


def _kv_table(block: str):
    """A fenced block made only of 'Label: value' lines -> boxed two-column table."""
    lines = [l for l in block.splitlines() if l.strip()]
    if len(lines) < 2 or not all(KV_LINE.match(l) for l in lines):
        return None
    rows = []
    for l in lines:
        k, v = KV_LINE.match(l).groups()
        v = html.escape(v.strip())
        v = re.sub(r"(https?://\S+)", r'<a href="\1">\1</a>', v)
        v = re.sub(r"\b([\w.+-]+@[\w-]+\.[\w.]+)\b", r'<a href="mailto:\1">\1</a>', v)
        rows.append(f'<tr><td class="k">{html.escape(k.strip())}:</td><td class="v">{v}</td></tr>')
    return '\n<table class="kv">\n' + "\n".join(rows) + "\n</table>\n"


def preprocess(md: str) -> str:
    # Stray invisible marks copied from Word (LRM, RLM) break line wrapping.
    md = md.replace("‎", "").replace("‏", "")

    def fence(m):
        return _kv_table(m.group(1)) or m.group(0)
    md = re.sub(r"^```[^\n]*\n(.*?)\n```[ \t]*$", fence, md, flags=re.S | re.M)
    return md


def md_to_html(md: str) -> str:
    """Convert Markdown to an HTML fragment (body + TOC) with pandoc."""
    tpl = HERE / "pandoc_fragment.html"
    cmd = [
        "pandoc",
        "-f", "gfm+footnotes+raw_html",
        "-t", "html5",
        "--toc", "--toc-depth=3",
        "--template", str(tpl),
        "--wrap=none",
    ]
    res = subprocess.run(cmd, input=md.encode("utf-8"), capture_output=True, check=True)
    out = res.stdout.decode("utf-8")
    toc, body = out.split("<!--BODY-->", 1)
    return toc, body


NUM = r"(\d+(?:\.\d+)*\.?|[A-Z]\.\d+(?:\.\d+)*)"


def postprocess_toc(toc: str) -> str:
    # Put the section number in its own column, like Word's TOC styles.
    return re.sub(r'(<a href="#[^"]+"[^>]*>)' + NUM + r"\s+",
                  r'\1<span class="tn">\2</span>', toc)


def postprocess_body(body: str) -> str:
    body = re.sub(r"(<h[1-6][^>]*>)" + NUM + r"\s+", r'\1<span class="hn">\2</span>', body)
    # Short table cells (dates, versions, author initials) are centred, long ones left-aligned.
    def cell(m):
        inner = re.sub(r"<[^>]+>", "", m.group(2))
        if "class=" in m.group(1):
            return m.group(0)
        cls = ' class="c"' if len(inner.strip()) <= 40 and "<br" not in m.group(2) else ""
        return f"<td{cls}{m.group(1)}>{m.group(2)}</td>"
    body = re.sub(r"<td([^>]*)>(.*?)</td>", cell, body, flags=re.S)
    # Keep the PKI diagram (and any centred <p> image block) together and centred.
    body = re.sub(r'<p align="center">', '<p class="figure">', body)
    # Let the browser engine size table columns from their content.
    body = re.sub(r"<colgroup>.*?</colgroup>", "", body, flags=re.S)
    # Long unbreakable tokens (SHA-256 fingerprints, OIDs, URLs) may break anywhere
    # inside table cells without shrinking every other column.
    body = re.sub(r"(<td[^>]*>)(.*?)(</td>)",
                  lambda m: m.group(1) + re.sub(r"(?<![\w/=\"-])([0-9A-Fa-f]{24,})(?![\w\"])",
                                                r'<span class="long">\1</span>', m.group(2)) + m.group(3),
                  body, flags=re.S)
    # Pandoc keeps the gfm footnote section at the end; mark it for styling.
    body = body.replace('<section id="footnotes"', '<section id="footnotes" class="footnotes"')
    return body


def load_settings():
    f = HERE / "documents.yml"
    return yaml.safe_load(f.read_text(encoding="utf-8")) if f.exists() else {}


def cover_titles(meta, lang, settings):
    doc = (settings.get(meta.get("doc_code", "")) or {}).get(lang) or {}
    title = meta.get("cover_title") or doc.get("title")
    subtitle = meta.get("subtitle") or doc.get("subtitle")
    if not title:
        # "Actalis TLS Certificate Policy and ..." -> "Certificate Policy and ...", "TLS certificates"
        full = meta.get("title", "")
        m = re.match(r"^(?:Actalis\s+)?(.*?)\s*(Certificate Policy.*)$", full)
        title, subtitle = (m.group(2), subtitle or (m.group(1) + " certificates" if m.group(1) else "")) \
            if m else (full, subtitle or "")
    return title, subtitle or ""


def build(md_path: pathlib.Path, out_path: pathlib.Path, lang: str | None, logo: pathlib.Path | None):
    text = md_path.read_text(encoding="utf-8")
    meta, md = split_front_matter(text)
    lang = (lang or meta.get("lang") or "en").lower()
    L = LABELS[lang]
    settings = load_settings()
    md = preprocess(md)
    toc, body = md_to_html(md)
    toc = postprocess_toc(toc)
    body = postprocess_body(body)
    for url, local in (settings.get("images") or {}).items():
        path = (HERE / local).resolve()
        if path.exists():
            body = body.replace(f'src="{url}"', f'src="{path.as_uri()}"')
    cover_title, cover_subtitle = cover_titles(meta, lang, settings)

    template = (HERE / "template.html").read_text(encoding="utf-8")
    logo_html = ""
    if logo and logo.exists():
        logo_html = f'<img class="logo" src="{logo.resolve().as_uri()}" alt="Actalis">'
    else:
        logo_html = '<span class="logo-text">ACTALIS</span>'

    def e(s):
        return html.escape(s or "")

    page = template
    repl = {
        "{{lang}}": lang,
        "{{cover_title}}": e(cover_title),
        "{{cover_subtitle}}": e(cover_subtitle),
        "{{title}}": e(meta.get("title", md_path.stem)),
        "{{version}}": e(meta.get("version", "")),
        "{{date}}": e(meta.get("date", "")),
        "{{approved_by}}": e(meta.get("approved_by", "")),
        "{{doc_code}}": e(meta.get("doc_code", "")),
        "{{distribution}}": e(meta.get("distribution", "")),
        "{{L.version}}": L["version"],
        "{{L.date}}": L["date"],
        "{{L.approved_by}}": L["approved_by"],
        "{{L.doc_code}}": L["doc_code"],
        "{{L.distribution}}": L["distribution"],
        "{{L.toc}}": L["toc"],
        "{{L.page}}": L["page"],
        "{{L.of}}": L["of"],
        "{{L.authoritative}}": e(L["authoritative"]),
        "{{logo}}": logo_html,
        "{{toc}}": toc,
        "{{body}}": body,
    }
    for k, v in repl.items():
        page = page.replace(k, v)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    # base_url = folder of the .md so relative image paths (e.g. images/pki.png) resolve.
    HTML(string=page, base_url=str(md_path.parent.resolve()) + "/").write_pdf(
        out_path,
        stylesheets=[CSS(filename=str(HERE / "style.css"))],
        pdf_variant=None,
    )
    print(f"OK  {md_path} -> {out_path} ({lang})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown", type=pathlib.Path)
    ap.add_argument("-o", "--output", type=pathlib.Path, required=True)
    ap.add_argument("--lang", choices=sorted(LABELS), default=None,
                    help="Language of labels (default: from front matter, else 'en')")
    ap.add_argument("--logo", type=pathlib.Path, default=HERE / "assets" / "logo.png")
    a = ap.parse_args()
    build(a.markdown, a.output, a.lang, a.logo)


if __name__ == "__main__":
    sys.exit(main())
