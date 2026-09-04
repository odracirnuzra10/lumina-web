#!/usr/bin/env python3
"""Shared HTML/JSON-LD template for Protocolo Lumina AEO pages."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from schema_dates import format_schema_date

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://www.protocololumina.cl"
ENTITY = (
    "Protocolo Lumina es una clínica chilena de rejuvenecimiento facial sin cirugía, "
    "con sedes en Vitacura, Concón y Los Ángeles, que combina tecnologías coreanas "
    "(EndoJiwoo, Endolaser, HIFU y radiofrecuencia) en protocolos de lifting facial."
)
DISAMBIG = (
    "Clínica de estética facial en Chile. No es una línea de cosméticos ni un protocolo "
    "de clareamiento; no relacionada con productos 'Protocolo Lumina' de Cosmica Skin "
    "(México), ni con protocolos de clareamiento íntimo de Brasil, ni con Lumina Clinic "
    "de Lo Barnechea."
)
DATE_PUB = format_schema_date("2026-04-14")
DATE_MOD = format_schema_date("2026-09-03")
REVIEWER = "Equipo clínico Protocolo Lumina"
PHONE = "+56963222683"
OG_IMG = f"{ORIGIN}/img/hero-endojiwoo.webp"
LOGO = f"{ORIGIN}/apple-touch-icon.png"
IG = "https://www.instagram.com/rejuvenecimiento.facial.lumina/"
GBP_VITACURA = "https://share.google/uKeMlkibRy1TPB7vK"
GBP_CONCON = "https://share.google/CeMMtlyCmwN5K3yxP"
GBP_LOS_ANGELES = "https://share.google/GKckpVUP3cGC9XGLq"
SAME_AS = [
    IG,
    GBP_VITACURA,
    GBP_CONCON,
    GBP_LOS_ANGELES,
    "https://oacg.cl/lumina/",
    "https://www.metodohebe.cl/",
]

HOURS = [
    {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "10:00",
        "closes": "20:00",
    },
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "19:00"},
]


def clinic(slug, name, url, street, locality, region, postal, lat, lng, maps, gbp):
    return {
        "@type": "MedicalClinic",
        "@id": f"{ORIGIN}/#{slug}",
        "name": name,
        "url": url,
        "parentOrganization": {"@id": f"{ORIGIN}/#organization"},
        "telephone": PHONE,
        "image": OG_IMG,
        "logo": LOGO,
        "priceRange": "$$$",
        "medicalSpecialty": "Dermatology",
        "sameAs": [gbp, IG],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": street,
            "addressLocality": locality,
            "addressRegion": region,
            "postalCode": postal,
            "addressCountry": "CL",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng},
        "hasMap": maps,
        "openingHoursSpecification": HOURS,
        "potentialAction": {
            "@type": "ReserveAction",
            "name": "Agenda tu hora",
            "target": f"{ORIGIN}/evaluacion",
        },
    }


def org_graph() -> list[dict]:
    return [
        {
            "@type": "Organization",
            "@id": f"{ORIGIN}/#organization",
            "name": "Protocolo Lumina",
            "alternateName": [
                "Lumina Clínica Facial",
                "Clínica Protocolo Lumina",
                "Protocolo Lumina Chile",
                "Lumina Rejuvenecimiento Facial",
            ],
            "description": ENTITY,
            "disambiguatingDescription": DISAMBIG,
            "url": ORIGIN,
            "logo": LOGO,
            "image": OG_IMG,
            "telephone": PHONE,
            "priceRange": "$$$",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Los Abedules 3085, Of. 105, Edificio Nueva Vitacura",
                "addressLocality": "Vitacura",
                "addressRegion": "Región Metropolitana",
                "postalCode": "7630573",
                "addressCountry": "CL",
            },
            "foundingDate": "2025",
            "parentOrganization": {"@type": "Organization", "name": "OACG Group", "url": "https://oacg.cl"},
            "sameAs": SAME_AS,
        },
        {
            "@type": "WebSite",
            "@id": f"{ORIGIN}/#website",
            "url": ORIGIN,
            "name": "Protocolo Lumina",
            "publisher": {"@id": f"{ORIGIN}/#organization"},
            "inLanguage": "es-CL",
            "potentialAction": {
                "@type": "ReserveAction",
                "name": "Agenda tu hora",
                "target": f"{ORIGIN}/evaluacion",
            },
        },
        clinic(
            "vitacura",
            "Protocolo Lumina Vitacura",
            f"{ORIGIN}/clinica-facial-vitacura",
            "Los Abedules 3085, Of. 105, Edificio Nueva Vitacura",
            "Vitacura",
            "Región Metropolitana",
            "7630573",
            -33.3936,
            -70.5831,
            GBP_VITACURA,
            GBP_VITACURA,
        ),
        clinic(
            "concon",
            "Protocolo Lumina Concón",
            f"{ORIGIN}/clinica-facial-concon",
            "Las Pelargonias 842, Oficina 1114, piso 11",
            "Concón",
            "Región de Valparaíso",
            "2510000",
            -32.9266,
            -71.5144,
            GBP_CONCON,
            GBP_CONCON,
        ),
        clinic(
            "losangeles",
            "Protocolo Lumina Los Ángeles",
            f"{ORIGIN}/clinica-facial-los-angeles",
            "Av. Gabriela Mistral 269",
            "Los Ángeles",
            "Región del Biobío",
            "4440000",
            -37.4693,
            -72.3527,
            GBP_LOS_ANGELES,
            GBP_LOS_ANGELES,
        ),
    ]


NAV = [
    ("/", "Inicio"),
    ("/tratamientos", "Tratamientos"),
    ("/planes", "Planes"),
    ("/resultados", "Resultados"),
    ("/preguntas-frecuentes", "Preguntas"),
]


def nav_html(active: str) -> str:
    links = "".join(
        f'<li><a href="{href}" class="{"active" if href == active else ""}">{label}</a></li>'
        for href, label in NAV
    )
    mob = "".join(f'<a href="{href}">{label}</a>' for href, label in NAV)
    return f"""<nav class="aeo-nav" id="mainNav">
  <div class="wrap">
    <a class="logo" href="/">lumina<span>CLÍNICA FACIAL COREANA</span></a>
    <ul class="nav-links">{links}</ul>
    <a class="nav-cta" href="/evaluacion">Agenda tu hora</a>
    <button class="hamburger" id="hamburger" aria-label="Abrir menú"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mob" id="mobileMenu">
  {mob}
  <a class="nav-cta" href="/evaluacion">Agenda tu hora</a>
</div>"""


def footer_html() -> str:
    return f"""<footer class="aeo-foot">
  <div class="wrap">
    <div>
      <div class="foot-brand">lumina</div>
      <p class="foot-note">{html.escape(ENTITY)}</p>
    </div>
    <div>
      <h4>Tratamientos</h4>
      <a href="/lifting-facial-coreano">Lifting facial coreano</a>
      <a href="/endojiwoo">EndoJiwoo</a>
      <a href="/endolaser-facial">Endolaser facial</a>
      <a href="/hifu-facial">HIFU facial</a>
      <a href="/radiofrecuencia-facial">Radiofrecuencia</a>
      <a href="/tratamientos">Las 14 tecnologías</a>
    </div>
    <div>
      <h4>Guías</h4>
      <a href="/flacidez-facial">Flacidez facial</a>
      <a href="/ojeras-tratamiento-sin-cirugia">Ojeras</a>
      <a href="/manchas-faciales-despigmentacion">Manchas</a>
      <a href="/papada-sin-cirugia">Papada</a>
      <a href="/seguridad-contraindicaciones">Seguridad</a>
      <a href="/glosario">Glosario</a>
      <a href="/preguntas-frecuentes">Preguntas frecuentes</a>
    </div>
    <div>
      <h4>Clínica</h4>
      <a href="/clinica-facial-vitacura">Vitacura</a>
      <a href="/clinica-facial-concon">Concón</a>
      <a href="/clinica-facial-los-angeles">Los Ángeles</a>
      <a href="/equipo">Equipo</a>
      <a href="/opiniones">Opiniones</a>
      <a href="/resultados">Resultados</a>
      <a href="/evaluacion">Agenda tu hora</a>
      <a href="https://wa.me/56963222683" rel="noopener">WhatsApp +56 9 6322 2683</a>
      <a href="https://www.metodohebe.cl/">Método Hebe</a>
    </div>
  </div>
  <div class="foot-bottom">
    <span>© 2026 Protocolo Lumina · Clínica facial Chile · Parte de OACG Group</span>
    <span>Reserva en protocololumina.cl</span>
  </div>
</footer>
<a class="sticky-wa" href="/evaluacion">Agenda tu hora</a>
<script src="/js/aeo.js" defer></script>"""


def faq_html(faqs: list[tuple[str, str]]) -> str:
    items = []
    for q, a in faqs:
        items.append(
            f'<div class="faq-item"><button type="button" aria-expanded="false">{html.escape(q)}</button>'
            f'<div class="faq-a">{a}</div></div>'
        )
    return '<section class="faq" id="faq"><h2>Preguntas frecuentes</h2>' + "".join(items) + "</section>"


def _strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s)


def faq_schema(faqs: list[tuple[str, str]], page_id: str) -> dict:
    return {
        "@type": "FAQPage",
        "@id": page_id + "#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": _strip_tags(a)},
            }
            for q, a in faqs
        ],
    }


def related_html(links: list[tuple[str, str, str]]) -> str:
    cards = "".join(f'<a href="{href}"><span>{kicker}</span>{title}</a>' for href, kicker, title in links)
    return f'<div class="related">{cards}</div>'


def render_page(p: dict) -> str:
    url = ORIGIN + p["path"]
    webpage_id = url.rstrip("/") + "#webpage"
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": ORIGIN + "/"}]
    for i, (href, name) in enumerate(p.get("breadcrumbs", []), start=2):
        crumbs.append({"@type": "ListItem", "position": i, "name": name, "item": ORIGIN + href})
    graph = org_graph()
    about = {"@id": f"{ORIGIN}/#organization"}
    if p.get("procedure"):
        about = p["procedure"]
        graph.append(p["procedure"])
    webpage = {
        "@type": ["MedicalWebPage", "WebPage"],
        "@id": webpage_id,
        "url": url,
        "name": p["title"],
        "headline": p["h1_text"],
        "description": p["description"],
        "inLanguage": "es-CL",
        "isPartOf": {"@id": f"{ORIGIN}/#website"},
        "about": about,
        "datePublished": format_schema_date(p.get("date_published", "2026-04-14")),
        "dateModified": DATE_MOD,
        "lastReviewed": DATE_MOD,
        "reviewedBy": {"@type": "Organization", "@id": f"{ORIGIN}/#organization", "name": REVIEWER},
        "author": {"@id": f"{ORIGIN}/#organization"},
        "publisher": {"@id": f"{ORIGIN}/#organization"},
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".answer-first", "h1"]},
        "primaryImageOfPage": {"@type": "ImageObject", "url": p.get("image", OG_IMG)},
    }
    graph.extend(
        [
            webpage,
            {"@type": "BreadcrumbList", "@id": url.rstrip("/") + "#breadcrumb", "itemListElement": crumbs},
            faq_schema(p["faqs"], url.rstrip("/")),
        ]
    )
    extra = p.get("extra_schema")
    if extra:
        graph.extend(extra if isinstance(extra, list) else [extra])
    schema = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    bc = p.get("breadcrumbs") or [("/", p["h1_text"])]
    crumbs_html = " / ".join(
        [f'<a href="/">Inicio</a>']
        + [f'<a href="{h}">{n}</a>' for h, n in bc[:-1]]
        + [html.escape(bc[-1][1])]
    )
    citations = ""
    if p.get("citations"):
        lis = "".join(f"<li>{c}</li>" for c in p["citations"])
        citations = f'<div class="cite"><strong>Referencias</strong><ul>{lis}</ul></div>'
    title = html.escape(p["title"])
    desc = html.escape(p["description"])
    og_title = html.escape(p.get("og_title") or p["title"])
    return f"""<!DOCTYPE html>
<html lang="es-CL">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Protocolo Lumina">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es-CL" href="{url}">
<link rel="alternate" hreflang="es" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Protocolo Lumina">
<meta property="og:image" content="{p.get("image", OG_IMG)}">
<meta property="og:locale" content="es_CL">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta property="article:published_time" content="{p.get("date_published", DATE_PUB)}">
<meta property="article:modified_time" content="{DATE_MOD}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<link rel="llms" type="text/plain" href="/llms.txt">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Sora:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/aeo.css">
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-TZC56NQ5');</script>
<script type="application/ld+json">{schema}</script>
</head>
<body data-page="{p["path"]}">
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TZC56NQ5" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
{nav_html(p.get("nav_active", "/"))}
<main class="narrow article">
  <p class="crumbs">{crumbs_html}</p>
  <header class="hero-aeo">
    <p class="kicker">{html.escape(p.get("kicker", "Protocolo Lumina · Chile"))}</p>
    <h1>{p["h1"]}</h1>
    <p class="answer-first" id="respuesta">{p["answer"]}</p>
    <p class="meta-eeat">
      <span>Revisado por {REVIEWER}</span>
      <span>Publicado {p.get("date_published", DATE_PUB)}</span>
      <span>Actualizado {DATE_MOD}</span>
      <span>Lectura clínica · es-CL</span>
    </p>
  </header>
  {p["body"]}
  {related_html(p.get("related", []))}
  {faq_html(p["faqs"])}
  {citations}
  <p class="disclaimer">Los resultados varían según edad, fototipo, hábito de sol, consistencia del plan y condición de base. La Evaluación P3 presencial es obligatoria antes de indicar cualquier tecnología. Esto no reemplaza una consulta médica. Si tienes una enfermedad activa de la piel, estás embarazada o en lactancia, dímelo en la evaluación.</p>
</main>
<section class="cta-band">
  <div class="narrow">
    <h2>¿Es este el protocolo para ti?</h2>
    <p>La Evaluación P3 dura 45 minutos y vale $27.990 (se descuenta si contratas un plan). No cotizamos tratamientos por adelantado: el plan se arma después de ver tu piel.</p>
    <a class="btn-ink" href="/evaluacion">Agenda tu hora</a>
  </div>
</section>
{footer_html()}
</body>
</html>
"""


def write_page(p: dict) -> None:
    path = p["path"].strip("/")
    dest_dir = ROOT / path
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "index.html").write_text(render_page(p), encoding="utf-8")
    print("wrote", dest_dir / "index.html")
