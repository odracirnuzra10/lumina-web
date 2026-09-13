#!/usr/bin/env python3
"""Build all AEO HTML pages and sitemap."""
from __future__ import annotations

import argparse
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import aeo_template
from aeo_template import ORIGIN, write_page
from schema_dates import date_only, format_schema_date, today_santiago


def all_pages():
    from aeo_pages_1 import PAGES as p1
    from aeo_pages_2 import PAGES as p2
    from aeo_pages_3 import PAGES as p3
    from aeo_pages_4 import PAGES as p4
    from aeo_pages_5 import PAGES as p5
    from aeo_pages_6 import PAGES as p6
    return p1 + p2 + p3 + p4 + p5 + p6


STATIC = [
    ("/", "1.0", "weekly"),
    ("/planes", "0.9", "weekly"),
    ("/tratamientos", "0.88", "weekly"),
    ("/resultados", "0.85", "weekly"),
    ("/evaluacion", "0.8", "weekly"),
    ("/llms.txt", "0.5", "weekly"),
    ("/llms-full.txt", "0.5", "weekly"),
]

# Path canónico sin slash (308 live /fundador/ → /fundador). Prioridad 0.6 / monthly.
PUENTE = [
    ("/clinica/como-confirmamos-tu-hora-por-whatsapp", "0.6", "monthly"),
    ("/clinica/que-pasa-con-tu-ficha-entre-sesiones", "0.6", "monthly"),
    ("/clinica/por-que-respondemos-en-minutos", "0.6", "monthly"),
    ("/fundador", "0.6", "monthly"),
]


def set_date_mod(day: str) -> None:
    aeo_template.DATE_MOD = format_schema_date(day)


def lastmod() -> str:
    return date_only(aeo_template.DATE_MOD)


def sitemap(pages):
    urls = []
    for loc, pri, freq in STATIC:
        urls.append((ORIGIN + loc, pri, freq))
    for p in pages:
        urls.append((ORIGIN + p["path"], "0.8", "monthly"))
    for loc, pri, freq in PUENTE:
        urls.append((ORIGIN + loc, pri, freq))
    seen = set()
    items = []
    day = lastmod()
    for loc, pri, freq in urls:
        if loc in seen:
            continue
        seen.add(loc)
        items.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{day}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(items)
        + "\n</urlset>\n"
    )
    Path(__file__).resolve().parents[1].joinpath("sitemap.xml").write_text(xml, encoding="utf-8")
    print("sitemap urls", len(items))


def image_sitemap():
    images = [
        ("/", "/img/hero-endojiwoo.webp", "Lurayen Benavides — caso real EndoJiwoo, Protocolo Lumina"),
        ("/resultados", "/img/ana-antes.webp", "Ana Maria Rosales, 57 anos, antes del protocolo de lifting facial"),
        ("/resultados", "/img/ana-despues.webp", "Ana Maria Rosales, 57 anos, despues del protocolo de lifting facial"),
        ("/", "/img/11.webp", "Antes y despues luminosidad, plan Eternal Gangnam"),
        ("/", "/img/13.webp", "Antes y despues firmeza ovalo facial, Eternal Gangnam"),
        ("/", "/img/15.webp", "Antes y despues textura e hidratacion, Armonia de Busan"),
        ("/", "/img/19.webp", "Lifting facial masculino tercio medio e inferior, Eternal Gangnam"),
        ("/", "/img/20.webp", "Lifting facial mujer 35 anos, Eternal Gangnam"),
        ("/", "/img/21.webp", "Lifting tercio medio e inferior mujer 50+, Armonia de Busan"),
    ]
    by_loc: OrderedDict[str, list[tuple[str, str]]] = OrderedDict()
    for page, img, cap in images:
        by_loc.setdefault(ORIGIN + page, []).append((ORIGIN + img, cap))
    blocks = []
    for loc, imgs in by_loc.items():
        inner = "\n".join(
            "    <image:image>\n"
            f"      <image:loc>{img}</image:loc>\n"
            f"      <image:caption>{cap}</image:caption>\n"
            f"      <image:title>{cap}</image:title>\n"
            "    </image:image>"
            for img, cap in imgs
        )
        blocks.append(f"  <url>\n    <loc>{loc}</loc>\n{inner}\n  </url>")
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
        + "\n".join(blocks)
        + "\n</urlset>\n"
    )
    Path(__file__).resolve().parents[1].joinpath("sitemap-images.xml").write_text(xml, encoding="utf-8")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Regenera sitemap AEO. HTML solo con --rebuild-html.")
    parser.add_argument(
        "--date",
        default=None,
        help="YYYY-MM-DD para DATE_MOD (America/Santiago). Default: hoy.",
    )
    parser.add_argument(
        "--rebuild-html",
        action="store_true",
        help="Sobrescribe las 23 páginas AEO. Por defecto se conservan.",
    )
    args = parser.parse_args(argv)
    day = args.date or today_santiago().isoformat()
    set_date_mod(day)
    aeo_template.REBUILD_HTML = bool(args.rebuild_html)

    pages = all_pages()
    from aeo_depth import DEPTH

    for p in pages:
        extra = DEPTH.get(p["path"])
        if extra:
            p = dict(p)
            p["body"] = p.get("body", "") + "\n" + "\n".join(extra)
        write_page(p)
    sitemap(pages)
    image_sitemap()
    print("pages", len(pages), "date", day, "rebuild_html", args.rebuild_html)


if __name__ == "__main__":
    main()
