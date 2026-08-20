#!/usr/bin/env python3
"""
Konverterar PDF-filer i references/ till läsbar text.

Användning:
    python scripts/pdf-to-text.py                          # alla PDF:er i references/
    python scripts/pdf-to-text.py references/nationella/migrations--och-asylpakten-ds-2025-30-volym-1.pdf

Output hamnar i references/_text/ med samma mappstruktur, t.ex.:
    references/_text/nationella/migrations--och-asylpakten-ds-2025-30-volym-1.txt

Kräver: pip install pymupdf
(PyMuPDF ger bättre resultat än pdfminer för svenska texter med tabeller)
"""

import sys
import os
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Saknar PyMuPDF. Installera med:")
    print("  pip install pymupdf")
    sys.exit(1)


REFERENCES_DIR = Path(__file__).resolve().parent.parent / "references"
TEXT_OUTPUT_DIR = REFERENCES_DIR / "_text"


def pdf_to_text(pdf_path: Path) -> str:
    """Extraherar text från en PDF med PyMuPDF."""
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text")
        pages.append(f"--- Sida {i} ---\n{text}")
    doc.close()
    return "\n\n".join(pages)


def convert_file(pdf_path: Path) -> Path:
    """Konverterar en PDF och sparar som .txt. Returnerar output-sökvägen."""
    rel = pdf_path.relative_to(REFERENCES_DIR)
    out_path = TEXT_OUTPUT_DIR / rel.with_suffix(".txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"  {rel} → _text/{rel.with_suffix('.txt')}")
    text = pdf_to_text(pdf_path)
    out_path.write_text(text, encoding="utf-8")
    return out_path


def find_all_pdfs() -> list[Path]:
    """Hittar alla PDF:er i references/ (exkl. _text/)."""
    return [
        p for p in REFERENCES_DIR.rglob("*.pdf")
        if "_text" not in p.parts
    ]


def main():
    if len(sys.argv) > 1:
        # Specifika filer
        targets = [Path(arg).resolve() for arg in sys.argv[1:]]
    else:
        # Alla PDF:er
        targets = find_all_pdfs()

    if not targets:
        print("Inga PDF:er hittades i references/")
        return

    print(f"Konverterar {len(targets)} PDF-fil(er)...\n")
    for pdf_path in sorted(targets):
        convert_file(pdf_path)

    print(f"\nKlart! Textfiler sparade i: {TEXT_OUTPUT_DIR}")
    print("Tips: Lägg till references/_text/ i .gitignore om du inte vill committa textfilerna.")


if __name__ == "__main__":
    main()
