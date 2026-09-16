"""Konvertera en Blink-sparad .mhtml (EUR-Lex) till ren text.

Användning:
    python build/mhtml_to_text.py <in.mhtml> <ut.txt>

Extraherar text/html-delen, avkodar quoted-printable, tar bort
script/style och HTML-taggar, normaliserar whitespace och skriver UTF-8.
"""
import sys
import email
import re
import html as htmllib


def main(src: str, dst: str) -> None:
    with open(src, "rb") as fh:
        msg = email.message_from_binary_file(fh)

    html_payload = None
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            html_payload = part.get_payload(decode=True)
            break

    if html_payload is None:
        raise SystemExit("Ingen text/html-del hittades i MHTML-filen.")

    text = html_payload.decode("utf-8", errors="replace")

    # Ta bort script/style-block
    text = re.sub(r"(?is)<script.*?</script>", " ", text)
    text = re.sub(r"(?is)<style.*?</style>", " ", text)

    # Blockelement -> radbrytning
    text = re.sub(r"(?i)<(br|/p|/div|/tr|/li|/h[1-6])\s*>", "\n", text)

    # Ta bort resterande taggar
    text = re.sub(r"(?s)<[^>]+>", " ", text)

    # Avkoda HTML-entiteter
    text = htmllib.unescape(text)

    # Normalisera whitespace
    text = re.sub(r"[ \t\u00a0]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    lines = [ln.strip() for ln in text.splitlines()]
    text = "\n".join(ln for ln in lines if ln)

    with open(dst, "w", encoding="utf-8") as out:
        out.write(text)

    print(f"Skrev {len(text)} tecken till {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Användning: python build/mhtml_to_text.py <in.mhtml> <ut.txt>")
    main(sys.argv[1], sys.argv[2])
