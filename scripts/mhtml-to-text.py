#!/usr/bin/env python3
"""
Konverterar EUR-Lex-sidor sparade som .mhtml i references/ till läsbar text.

Användning:
    python scripts/mhtml-to-text.py                                   # alla L_*.mhtml i references/
    python scripts/mhtml-to-text.py references/L_202401349SV.000101.fmx.xml.mhtml

Output hamnar i references/_text/ med samma namnkonvention som PDF-texterna:
    L_202401349SV.000101.fmx.xml.mhtml  ->  references/_text/OJ_L_202401349_SV_TXT.txt
Andra filnamn får samma namn som källan, med .txt.

Varje stycke hamnar på egen rad, så att t.ex. "Artikel 5" står ensamt på en rad
och kan sökas med grep/awk på samma sätt som de PDF-baserade texterna.
EUR-Lex innehållsförteckning (sidomenyn) tas bort.

Kräver endast Python standardbibliotek.
"""

import email
import email.policy
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REFERENCES_DIR = Path(__file__).resolve().parent.parent / "references"
TEXT_OUTPUT_DIR = REFERENCES_DIR / "_text"

BLOCK_TAGS = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6", "table", "td", "th"}
SKIP_TAGS = {"script", "style", "head", "nav"}
# Element utan sluttagg; får inte läggas på stacken
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class TextExtractor(HTMLParser):
    """Plockar ut synlig text och lägger radbrytningar vid blockelement."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0  # >0 när vi är inne i ett element som ska hoppas över
        self.stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in VOID_TAGS:
            if tag == "br":
                self.parts.append("\n")
            return
        skip = tag in SKIP_TAGS or attrs.get("id") == "TOC"
        self.stack.append((tag, skip))
        if skip:
            self.skip_depth += 1
        if tag in BLOCK_TAGS:
            self.parts.append("\n")
        if tag == "td":
            self.parts.append(" ")

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        # Poppa till närmaste matchande starttagg (tål ostängda element)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for _, skip in self.stack[i:]:
                    if skip:
                        self.skip_depth -= 1
                del self.stack[i:]
                break
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.skip_depth == 0:
            self.parts.append(data)


def extract_html(mhtml_path: Path) -> str:
    """Returnerar HTML-delen ur en mhtml-fil (avkodad från quoted-printable)."""
    msg = email.message_from_bytes(mhtml_path.read_bytes(), policy=email.policy.default)
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            # EUR-Lex anger inte charset i mhtml-delen; innehållet är UTF-8
            charset = part.get_content_charset() or "utf-8"
            return part.get_payload(decode=True).decode(charset, errors="replace")
    raise ValueError(f"Ingen text/html-del i {mhtml_path}")


def html_to_text(markup: str) -> str:
    parser = TextExtractor()
    parser.feed(markup)
    text = html.unescape("".join(parser.parts))
    text = text.replace("\u00a0", " ")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    out, blank = [], 0
    for line in lines:
        if not line:
            blank += 1
            if blank <= 1:
                out.append("")
            continue
        blank = 0
        out.append(line)
    return "\n".join(out).strip() + "\n"


def output_path(src: Path) -> Path:
    m = re.match(r"L_(\d{9})SV", src.name)
    name = f"OJ_L_{m.group(1)}_SV_TXT.txt" if m else src.with_suffix(".txt").name
    rel_dir = src.parent.relative_to(REFERENCES_DIR)
    return TEXT_OUTPUT_DIR / rel_dir / name


def convert_file(src: Path) -> Path:
    out = output_path(src)
    out.parent.mkdir(parents=True, exist_ok=True)
    text = html_to_text(extract_html(src))
    out.write_text(text, encoding="utf-8")
    print(f"  {src.relative_to(REFERENCES_DIR)} -> {out.relative_to(REFERENCES_DIR)} ({len(text.splitlines())} rader)")
    return out


def main():
    if len(sys.argv) > 1:
        targets = [Path(a).resolve() for a in sys.argv[1:]]
    else:
        targets = sorted(p for p in REFERENCES_DIR.glob("L_*.mhtml"))
    if not targets:
        print("Inga mhtml-filer hittades.")
        return
    print(f"Konverterar {len(targets)} mhtml-fil(er)...\n")
    for t in targets:
        convert_file(t)
    print(f"\nKlart! Textfiler sparade i: {TEXT_OUTPUT_DIR}")


if __name__ == "__main__":
    main()
