#!/usr/bin/env python3

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = ROOT / "papers.bib"
COAUTHORS_PATH = ROOT / "coauthors.yml"
OUTPUT_PATH = ROOT / "_includes" / "research-content.html"

SELF_NAMES = {
    "sang yoon lee",
    "sang yoon tim lee",
    "tim lee",
}

SECTION_ORDER = [
    ("working", "working papers"),
    ("published", "published papers"),
    ("other", "other work"),
]

BUTTON_FIELDS = [
    ("html", "html"),
    ("pdf", "pdf"),
    ("appx", "appx"),
    ("slides", "slides"),
    ("data", "data"),
]


def parse_coauthors(path: Path) -> dict[str, str]:
    links: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        name, url = line.split(":", 1)
        links[name.strip()] = url.strip()
    return links


def iter_entries(text: str) -> list[str]:
    entries: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] != "@":
            i += 1
            continue
        if text.startswith("@Comment", i):
            i += 8
            continue
        start = i
        brace_start = text.find("{", i)
        if brace_start == -1:
            break
        depth = 0
        j = brace_start
        while j < n:
            char = text[j]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    entries.append(text[start : j + 1])
                    i = j + 1
                    break
            j += 1
        else:
            break
    return entries


def parse_bibtex(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    parsed: list[dict[str, str]] = []
    for entry_text in iter_entries(text):
        match = re.match(r"@(\w+)\s*{\s*([^,]+)\s*,", entry_text, re.DOTALL)
        if not match:
            continue
        entry_type, key = match.groups()
        body = entry_text[match.end() : -1].strip()
        fields = parse_fields(body)
        fields["ENTRYTYPE"] = entry_type
        fields["ID"] = key.strip()
        parsed.append(fields)
    return parsed


def parse_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    i = 0
    n = len(body)
    while i < n:
        while i < n and body[i] in " \t\r\n,":
            i += 1
        if i >= n:
            break
        key_start = i
        while i < n and body[i] not in "=":
            i += 1
        key = body[key_start:i].strip().lower()
        i += 1
        while i < n and body[i].isspace():
            i += 1
        value, i = read_value(body, i)
        fields[key] = normalize_value(value)
    return fields


def read_value(body: str, i: int) -> tuple[str, int]:
    if i >= len(body):
        return "", i
    if body[i] == "{":
        depth = 0
        start = i + 1
        while i < len(body):
            char = body[i]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return body[start:i], i + 1
            i += 1
        return body[start:], len(body)
    if body[i] == '"':
        start = i + 1
        i += 1
        while i < len(body):
            if body[i] == '"' and body[i - 1] != "\\":
                return body[start:i], i + 1
            i += 1
        return body[start:], len(body)
    start = i
    while i < len(body) and body[i] not in ",\n":
        i += 1
    return body[start:i].strip(), i


def normalize_value(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip())
    value = value.replace("\\&", "&")
    value = value.replace("``", '"').replace("''", '"')
    value = re.sub(r"[{}]", "", value)
    return value.strip()


def normalize_name(name: str) -> str:
    name = normalize_value(name)
    if "," in name:
        last, first = [part.strip() for part in name.split(",", 1)]
        name = f"{first} {last}".strip()
    name = re.sub(r"\s+", " ", name)
    return name


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def is_self(name: str) -> bool:
    compact = re.sub(r"[()]", " ", name.lower())
    compact = re.sub(r"\s+", " ", compact).strip()
    return compact in SELF_NAMES


def format_coauthors(author_field: str, links: dict[str, str]) -> str:
    authors = [normalize_name(part) for part in author_field.split(" and ")]
    coauthors = [name for name in authors if name and not is_self(name)]
    if not coauthors:
        return ""
    rendered: list[str] = []
    for name in coauthors:
        safe_name = html.escape(name)
        url = links.get(name)
        if url:
            rendered.append(
                f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener">{safe_name}</a>'
            )
        else:
            rendered.append(safe_name)
    return f'<div class="research-paper-coauthors">with {", ".join(rendered)}</div>'


def venue_text(entry: dict[str, str]) -> str:
    year = entry.get("year", "").strip()
    if entry.get("journal"):
        pieces = [entry["journal"].strip(), year]
        return ", ".join(piece for piece in pieces if piece)

    prefix = entry.get("abbr", "").strip()
    parts: list[str] = []
    if entry.get("acro"):
        parts.append(entry["acro"].strip())
    elif entry.get("institution"):
        parts.append(entry["institution"].strip())
    if entry.get("series"):
        parts.append(entry["series"].strip())
    if entry.get("number"):
        parts.append(entry["number"].strip())
    main = " ".join(parts).strip() or entry.get("series", "").strip()
    pieces = [piece for piece in (prefix, main, year) if piece]
    return ", ".join(pieces)


def button_links(entry: dict[str, str], abstract_id: str) -> str:
    buttons: list[str] = []
    if entry.get("abstract"):
        buttons.append(
            f'<button class="research-paper-btn js-abstract-toggle" type="button" '
            f'data-target="{abstract_id}" aria-expanded="false">abstract</button>'
        )
    for field, label in BUTTON_FIELDS:
        url = entry.get(field, "").strip()
        if not url:
            continue
        href = url if re.match(r"^https?://", url) else f"./pdfs/{url}"
        buttons.append(
            f'<a class="research-paper-btn" href="{html.escape(href, quote=True)}" '
            f'target="_blank" rel="noopener">{label}</a>'
        )
    return '<div class="research-paper-buttons">' + "".join(buttons) + "</div>"


def render_entry(entry: dict[str, str], links: dict[str, str]) -> str:
    abstract_id = f"abstract-{slugify(entry['ID'])}"
    title = html.escape(entry.get("title", "").strip())
    coauthors = format_coauthors(entry.get("author", ""), links)
    venue = html.escape(venue_text(entry))
    buttons = button_links(entry, abstract_id)
    abstract = entry.get("abstract", "").strip()
    abstract_html = ""
    if abstract:
        abstract_html = (
            f'<div id="{abstract_id}" class="research-paper-abstract" hidden>'
            f"{html.escape(abstract)}</div>"
        )
    parts = [
        '<article class="research-paper">',
        f'<div class="research-paper-title">{title}</div>',
    ]
    parts.append('<div class="research-paper-meta">')
    if coauthors:
        parts.append(coauthors)
    elif venue:
        parts.append(f'<div class="research-paper-venue">{venue}</div>')
    parts.append(buttons)
    parts.append("</div>")
    if coauthors and venue:
        parts.append(f'<div class="research-paper-venue">{venue}</div>')
    if abstract_html:
        parts.append(abstract_html)
    if entry.get("note"):
        parts.append(f'<div class="research-paper-note"><small><em>*{html.escape(entry["note"])}</em></small></div>')
    parts.append("</article>")
    return "\n".join(parts)


def sort_key(entry: dict[str, str]) -> tuple[int, int, str]:
    year = entry.get("year", "0").strip()
    try:
        numeric_year = int(year)
    except ValueError:
        numeric_year = 0
    return (int(entry.get("order", "999")), -numeric_year, entry.get("title", "").lower())


def render_page(entries: list[dict[str, str]], links: dict[str, str]) -> str:
    grouped: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        status = entry.get("status", "").strip().lower()
        if status:
            grouped.setdefault(status, []).append(entry)

    sections: list[str] = []
    for status, heading in SECTION_ORDER:
        items = sorted(grouped.get(status, []), key=sort_key)
        if not items:
            continue
        sections.append(f'<section class="research-section">')
        sections.append(f"<h2>{html.escape(heading)}</h2>")
        sections.extend(render_entry(item, links) for item in items)
        sections.append("</section>")

    sections.append(
        """<script>
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".js-abstract-toggle").forEach(function (button) {
    button.addEventListener("click", function () {
      const target = document.getElementById(button.dataset.target);
      if (!target) return;
      const isOpen = target.classList.toggle("is-open");
      target.hidden = !isOpen;
      button.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  });
});
</script>"""
    )
    return "\n".join(sections) + "\n"


def main() -> None:
    links = parse_coauthors(COAUTHORS_PATH)
    entries = parse_bibtex(BIB_PATH)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_page(entries, links), encoding="utf-8")


if __name__ == "__main__":
    main()
