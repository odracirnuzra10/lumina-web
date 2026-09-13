# Protocolo Lumina — onboarding IA

Repo `lumina-web`. Sitio estático de [protocololumina.cl](https://www.protocololumina.cl). Una tarea = una rama = un PR a `main`. Plan: [`docs/ROADMAP_IA_2026-09.md`](docs/ROADMAP_IA_2026-09.md). Precios: [`docs/H7-PRECIOS.md`](docs/H7-PRECIOS.md).

## Stack

- HTML / CSS / JS estático **en la raíz** (no hay `public/`).
- Vercel: `cleanUrls`, `trailingSlash: false` (`vercel.json`).
- GTM `GTM-TZC56NQ5`. WhatsApp `+56963222683` (`56963222683`). Únicos en la red OACG.
- **23 páginas AEO** generadas desde `scripts/aeo_pages_1.py` … `scripts/aeo_pages_6.py` (+ `aeo_template.py`, `aeo_depth.py`, `aeo_content.py`, `aeo_es.py`).
- **Hand-pages** (no las toca el generador): `index.html`, `planes.html`, `tratamientos/index.html`, `resultados.html`, `evaluacion/index.html`, `franquicia/index.html`, `fundador/index.html`, `capacitacion/index.html`, las 3 `/clinica/*`, `404.html`.
- Fechas JSON-LD: `scripts/schema_dates.py` (`format_schema_date`, zona `America/Santiago`). No inventar el día.

## Commits

Español, **imperativo** (`Corrige…`, `Agrega…`, `Quita…`). No mezclar inglés.

## Verify

```bash
# Sitemap (main 2026-09-13 = 34). No bajar.
grep -c '<loc>' sitemap.xml

# JSON-LD parseable (main 2026-09-13 = 68 bloques, 0 fallos)
python3 - <<'PY'
from pathlib import Path
import json, re
ok = fail = 0
for p in sorted(Path('.').rglob('*.html')):
    if '.git' in p.parts:
        continue
    text = p.read_text(encoding='utf-8', errors='replace')
    for i, b in enumerate(re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        text, flags=re.I | re.S), 1):
        try:
            json.loads(b); ok += 1
        except Exception as e:
            fail += 1
            print(f'FAIL {p} block{i}: {e}')
print(f'blocks_ok={ok} blocks_fail={fail}')
PY
```

Prohibido en copy (tras L1.1; hoy puede haber hits en `main`):

```bash
grep -nE 'honestás|mismás|direcciónes|evaluaciónes' --include='*.html' --include='*.py' . || true
```

Nunca `AggregateRating` suelto ni `Review` oculto. Español de Chile, sin voseo (`Firmas`, no `Firmás`). Un nodo por `@id` por página.

## Flujo del generador AEO

1. Editar `scripts/aeo_pages_*.py` (nunca el HTML de las 23 a mano).
2. Regenerar sitemap: `python3 scripts/build_aeo.py` (`--date YYYY-MM-DD` o hoy Santiago).
3. Polish HTML: `python3 scripts/aeo_es.py` (solo `AEO_DIRS` + `404.html`; **no** toca `scripts/*.py`).
4. Sobrescribir las 23 HTML desde plantilla: `python3 scripts/build_aeo.py --rebuild-html`. **No** lo uses si las fuentes aún no reproducen el HTML publicado (puente Clinera, leftovers).

`STATIC` + `PUENTE` = 34 `<loc>` (core + 23 AEO + 3 `/clinica/*` + `/fundador` sin slash). `DATE_MOD` sale de `--date` o hoy (`schema_dates.format_schema_date`). `sitemap-images.xml` anida varios `image:image` en un `<url>` por `loc`.

## YMYL / schema (resumen)

- Cifra locked (R3): *más de 5.000 pacientes* · *5/5 estrellas en Google*. Un par. No pasar estrellas a schema.
- Persona nombrada en página (R6): solo **Ricardo Alfredo Oyarzún Acuña**. El resto: “profesionales altamente capacitados”. Sin registros Superintendencia inventados. `/equipo` es plantilla honesta; no añadir clínicos ficticios.
- R8 Concepción es **solo Hebe**. Cero trabajo Lumina de Concepción.
- Canonical self **sin** slash, alineado al 308 de Vercel. Excepción actual: `/fundador` (L1.2).
