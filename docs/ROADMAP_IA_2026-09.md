# Roadmap IA — Protocolo Lumina (protocololumina.cl)

Horizonte: **15-sep → 15-dic 2026**. Repo: `lumina-web`. Sitio estático en la raíz (no hay `public/`).

Este documento es autosuficiente. Una tarea = una rama = un PR a `main`. No ejecutar otra tarea del roadmap en el mismo PR. No inventar datos clínicos, registros ni precios.

**Este PR cierra L0.4** (nota fechada en `docs/PROMPTS_PENDIENTES_PUENTE_CLINERA.md`). El resto de IDs L/T es trabajo futuro: no implementarlo desde aquí.

Prefijos: **L** Lumina · **T** transversal (misma red OACG) · **R** solo Ricardo.

Prioridad: **P0 esta semana** · **P1 septiembre** · **P2 oct–nov** · **P3 condicional** (espera R).

**R locked 2026-09-13 (Ricardo):** R1 = precios actuales (b). R2 = GTM-TZC56NQ5 + WA `56963222683` únicos. R3 = más de 5.000 pacientes · 5/5 Google (un par; sin `AggregateRating` ni Review oculto). R4 = solo Hebe (KPI AUGE; cero acción Lumina). R5 = baseline PageSpeed móvil (abajo); GSC sigue pendiente y **no bloquea**. R7 = sí merge [#41](https://github.com/odracirnuzra10/lumina-web/pull/41) (otro worker hace el merge). La IA **no reabre** estos IDs.

---

## 0. Prompt maestro para la IA ejecutora

Eres una IA que implementa **una sola** fila de la sección 3. No re-investigues el plan: este archivo y `CLAUDE.md` (cuando exista, L0.3) son la fuente.

### Cómo elegir la siguiente tarea

1. Lee `CLAUDE.md` (si existe) y esta sección 1.
2. En la sección 3, toma el ID de **menor prioridad numérica** (P0 → P3) cuyo `Depende de` esté cerrado (merge en `main` o R marcada hecha).
3. Si hay empate, elige el ID más bajo (L0.1 antes que L0.2).
4. Si `Depende de` cita un R **abierto** (R6, R9–R12) y Ricardo no respondió: **para y pregunta**. No asumas. R1–R5, R7 y **R8 `legalName`** ya están locked: no preguntar de nuevo.
5. No abras un segundo ID “porque es chico”.

### Una tarea = una rama + un PR

- Rama desde `main` actualizado: `cursor/<id-minusculas>-<slug-corto>`.
- Un PR a `main`, listo para review cuando el criterio de aceptación pase.
- Commit en **español, imperativo** (`Corrige…`, `Agrega…`, `Quita…`). No mezclar inglés.
- Un cambio medible por deploy.

### Qué leer primero (en este orden)

1. `CLAUDE.md` (L0.3; hasta que exista, esta sección 1).
2. Esta sección 1 (reglas duras).
3. Archivos de la fila (`Archivos`).
4. Si la tarea toca precios: `docs/H7-PRECIOS.md`.
5. Si toca citas de IA: `docs/SHARE-OF-MODEL-MES0.md`.
6. Fechas JSON-LD: `scripts/schema_dates.py` (`format_schema_date`, zona `America/Santiago`).
7. Páginas AEO (23): editar `scripts/aeo_pages_*.py` y regenerar. **Hasta L1.1, no correr** `scripts/build_aeo.py`.

### Cómo reportar

En el PR: ID, qué cambió, comando de `Verificación` pegado con salida, URLs `curl -sI` tocadas (código esperado). Si no puedes verificar algo (login GSC, Playwright local), dilo: no inventes el resultado.

### Cuándo parar y preguntar

Una cosa a la vez. Para y pregunta si:

- falta un R **abierto** (R6 Doctoralia, R9 `foundingDate`, R10 consentimiento Corea, R11 INAPI, R12 booking Clinera). No parar por R1–R5, R7 ni R8 (`legalName` locked).
- el generador AEO sigue roto y la tarea pide editar una de las 23 páginas;
- tendrías que inventar cm, reseñas, direcciones, fechas o registros;
- el cambio exige editar `vercel.json` y no es L1.7;
- dos `@id` iguales en la misma página no se pueden unir sin borrar un nodo que aún se usa.

---

## 1. Reglas del repo

### Prohibido (YMYL / schema)

- Nunca `AggregateRating` suelto ni `Review` oculto (sin texto visible emparejado). `/opiniones` puede tener `Review` visible. **R3 locked:** el único par de cifra Lumina es *más de 5.000 pacientes* y *5/5 estrellas en Google* (copy visible). No un segundo par. No pasar esas estrellas a schema.
- No inventar registros de Superintendencia, RUT, cm de pacientes, reseñas, direcciones ni fechas. `scripts/schema_dates.py` formatea; no inventa el día. No sustituir el par R3 por otra cifra.
- Español de Chile, **sin voseo** (`Firmas`, no `Firmás`). Tildes y `¿` en H1/H2/FAQ.
- JSON-LD parseable (`json.loads`). **Un nodo por `@id` por página.** Hoy `#organization` se repite en los 35 HTML (máx. 28 en `tratamientos/index.html`): L1.2 lo deduplica.
- CTA: límites **B.4** (Hebe, aplican igual): sticky ≤ 15 % del viewport; no antes de `scrollY > 400`; se oculta en el footer; cero pop-ups / exit-intent; máximo 5 puntos de conversión en el `<article>`; `padding-bottom` para no tapar texto.
- Un cambio medible por deploy.

### Generador AEO (23 páginas)

Se editan en `scripts/aeo_pages_1.py` … `scripts/aeo_pages_6.py` (+ `scripts/aeo_template.py`, `scripts/aeo_depth.py`, `scripts/aeo_content.py`) y se regeneran. **Nunca a mano** el HTML de esas 23.

Lista (`scripts/aeo_es.py`, `AEO_DIRS`):  
`lifting-facial-coreano`, `endojiwoo`, `endolaser-facial`, `hifu-facial`, `radiofrecuencia-facial`, `endolaser-vs-hifu`, `lifting-coreano-vs-hilos-tensores`, `endojiwoo-vs-bioestimuladores-inyectables`, `lifting-sin-cirugia-vs-lifting-quirurgico`, `ojeras-tratamiento-sin-cirugia`, `manchas-faciales-despigmentacion`, `flacidez-facial`, `papada-sin-cirugia`, `seguridad-contraindicaciones`, `clinica-facial-vitacura`, `clinica-facial-concon`, `clinica-facial-los-angeles`, `equipo`, `opiniones`, `preguntas-frecuentes`, `glosario`, `blog`, `blog/lifting-facial-coreano-chile`.

**Hasta L1.1 no correr** `scripts/build_aeo.py`. Riesgos actuales del generador:

- `STATIC` en `scripts/build_aeo.py` no incluye `/clinica/*` ni `/fundador` → un run **borra 4 `<loc>`** del sitemap (hoy 34).
- `DATE_MOD` está congelado en `scripts/aeo_template.py` (`2026-09-03`).
- `scripts/aeo_es.py` reescribe `scripts/aeo_*.py` (bucle de mutación).
- Over-corrections vivas: `honestás`, `mismás`, `direcciónes`, `evaluaciónes` (p. ej. `scripts/aeo_pages_3.py` línea 145 → `lifting-sin-cirugia-vs-lifting-quirurgico`).
- `sitemap-images.xml`: varias `<url>` con el mismo `<loc>` en vez de varios `image:image` anidados en una sola `<url>`.

Criterio de L1.1: `python3 scripts/build_aeo.py` reproduce `main` **sin diff salvo fechas**, antes de cualquier cambio de copy.

### Reglas B de Hebe que sí se transfieren

| Regla | En Lumina |
|---|---|
| URLs publicadas | No cambiar slugs indexados. `trailingSlash: false` en `vercel.json`. |
| Canonical | Self-canonical **sin** slash, alineado al 308 de Vercel. Excepción a corregir: `/fundador` (L1.2). |
| H1 / H2 | No reescribir H1/H2 de páginas que ya rankean salvo la tarea lo pida. Insertar, no reemplazar bloques YMYL. |
| Citas | No borrar bloques de referencias (HIFU / RF / láser). |
| Disclaimer | Pie AEO: resultados varían, P3 obligatoria. No diluir. |
| FAQ ↔ schema | Misma pregunta visible y en `FAQPage`. |
| `meta robots` | `index, follow, max-snippet:-1, max-image-preview:large` en páginas indexables. `/franquicia` y `/capacitacion` siguen `noindex` hasta R11 / decisión. |

### Convenciones de commit y verify (anticipan L0.3)

```bash
# Sitemap (main 2026-09-13 = 34)
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

# No deben quedar (tras L1.1; hoy SÍ hay hits en main)
# honestás mismás direcciónes evaluaciónes
```

---

## 2. Estado verificado (2026-09-13)

Resumen de lo **ya hecho** en `main` (no repetir). Pendiente = sección 3.

| Tema | Lumina 2026-09-13 | Shared / red |
|---|---|---|
| Redirects WooCommerce | **16** en `vercel.json` (`/producto`, `/tienda`, `/shop`, `/carrito`, `/checkout`, `/mi-cuenta`, …) | — |
| `sameAs` | **6** en `scripts/aeo_template.py` (`SAME_AS`): IG, 3 `share.google`, `oacg.cl/lumina`, `metodohebe.cl` | GBP share oficiales 2026-09-04 |
| Entidad | `disambiguatingDescription` + `parentOrganization` OACG | Frase de entidad en schema / llms |
| Video | `VideoObject` home (Vimeo `1186589095`); **sin** `duration` (L1.2) | — |
| Crawlers | `robots.txt`: SemrushBot / AhrefsBot Allow; 404 `noindex` | GTM-TZC56NQ5 · WA `56963222683` |
| AgendaPro | **0** `href` a agendapro.com (solo mención de texto en sedes) | Reserva = `/evaluacion` |
| Voseo | **0** `Firmás` en HTML (el par está en `scripts/aeo_es.py`) | — |
| Tecnologías | **14** en `main` hoy. **R7 locked:** mergear [#41](https://github.com/odracirnuzra10/lumina-web/pull/41) (14→18). Otro worker hace el merge; L0.2 desbloqueado | Adipolite no es Lumina |
| llms | `llms.txt` sin tabla de precios de planes (H7-b). P3 $27.990 sí aparece en copy de evaluación | `docs/H7-PRECIOS.md` |
| Sitemap | **34** `<loc>`: core + 23 AEO + 3 `/clinica/*` + `/fundador/` | `/clinica/*` y `/fundador` **no** están en `STATIC` del generador |
| Schema | 68 JSON-LD parsean. `#organization` **duplicado en 35/35 HTML** | — |
| Generador | **Roto** (ver §1). Over-corrections `honestás` (5), `mismás` (3), `direcciónes` (3), `evaluaciónes` (1) | — |
| H7 / R1 | **R1 locked = (b)** precios actuales. “desde” sigue en `::before` (L1.6 = texto real). No (c). Sin UI de cuotas mensuales nuevas | — |
| Cifra + estrellas / R3 | Par único locked: *más de 5.000 pacientes* · *5/5 estrellas en Google*. Cero `AggregateRating` / Review oculto | No mezclar con Hebe (30.000) |
| Tracking / R2 | GTM-TZC56NQ5 y WA `56963222683` **únicos** (no split por marca). Medir en Analytics por URL. `clinica:'lumina'` en 5 HTML + `js/aeo.js`; completar el resto es **opcional** (T6.1) | No nuevo contenedor ni número |
| PageSpeed móvil / R5 | Lab Lighthouse 12.8.2, 2026-09-13: **home 76** (LCP 3,1 s · CLS 0,014) · **`/planes` 88** (LCP 2,5 s · CLS 0,024). INP lab n/d (Lighthouse no emite INP; PSI field HTTP 429). GSC sigue pendiente: **no bloquea** | Baseline; no gate |
| PR abiertos | #29 `knowsAbout` (conflicto). #41 14→18 (R7 = mergear; otro worker) | L0.1 · L0.2 |
| Live `curl -sI` | 200: home, `/planes`, `/tratamientos`, `/evaluacion`, `/fundador`, `/franquicia`, `/capacitacion`, 3 `/clinica/*`, llms, sitemaps, robots, IndexNow, Clinera caso. 308: `/planes/` → `/planes`, `/fundador/` → `/fundador`, `/reserva` y `/agenda` → `/evaluacion` | Ver nota 2026-09-13 |

Hecho también (no reabrir): entity phrase, sedes con calle/geo/`hasMap`, `Speakable`, OG home → `/img/hero-endojiwoo.webp`, IndexNow `lumina-indexnow-2026-09-03.txt`, `lang`/`hreflang` `es-CL` en AEO, `/seguridad-contraindicaciones`, puente Clinera.

PageSpeed R5 (reproducir): `npx lighthouse@12.8.2 URL --only-categories=performance --form-factor=mobile --chrome-flags='--headless --no-sandbox'` contra `https://www.protocololumina.cl/` y `/planes`. INP es métrica de campo; el lab no la emite.

---

## 3. Bloques de trabajo

Formato fijo por tarea. Esfuerzo: **S** &lt; 2 h · **M** medio día · **L** un día.

### Bloque 0 — Arranque P0 (esta semana)

#### L0.1 · Prioridad P0 · Esfuerzo S · Depende de — · Archivos `index.html`

**Prompt para la IA.** PR [#29](https://github.com/odracirnuzra10/lumina-web/pull/29) (`claude/seo-ai-crawlers-audit-7lex09`) está **open** y `mergeable_state: dirty`. El diff **reemplaza** el JSON-LD compacto de `MedicalBusiness` de agosto por uno con `knowsAbout`. En `main` de hoy ese blob **ya no existe**: el home tiene `@graph` largo (Organization, sedes, FAQ, `VideoObject`, puente). **No mergear #29.** Reaplicar solo `knowsAbout` en el nodo `MedicalBusiness` / `#organization` del home (y, si el mismo objeto se duplica en el puente, en **un** nodo). Valores ya usados en el sitio, sin claims nuevos: rejuvenecimiento facial no invasivo, lifting facial coreano, HIFU, radiofrecuencia facial, EndoJiwoo. Cerrar #29 (comentario: reaplicado en PR nuevo; el original conflictúa).

**Criterio de aceptación.** `knowsAbout` presente y parseable en el home. #29 cerrado. Cero regresión del `@graph` actual (sedes, `sameAs` 6, `parentOrganization`, `VideoObject`).

**Verificación (comando).**

```bash
python3 - <<'PY'
from pathlib import Path
import json, re
html = Path('index.html').read_text(encoding='utf-8')
blocks = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, flags=re.I|re.S)
found = False
for b in blocks:
    data = json.loads(b)
    def walk(o):
        global found
        if isinstance(o, dict):
            if 'knowsAbout' in o: found = True
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(data)
assert found, 'knowsAbout missing'
print('knowsAbout ok', len(blocks), 'blocks')
PY
```

**Reversión.** Revertir el commit del home; reabrir #29 solo si hace falta el historial.

---

#### L0.2 · Prioridad P0 · Esfuerzo M · Depende de R7 (cerrado 2026-09-13) · Archivos `tratamientos/index.html` `index.html` `glosario/index.html` `llms.txt` `llms-full.txt`

**Prompt para la IA.** **R7 locked:** mergear [#41](https://github.com/odracirnuzra10/lumina-web/pull/41). **Otro worker posee el merge** — no mergear #41 desde un PR de L* de este roadmap. Este ID queda **desbloqueado**: el worker de #41 hace pre-review + merge. Tabla de consistencia **antes** de merge:

| Chequeo | `main` hoy | PR #41 | Acción |
|---|---|---|---|
| Cifra | 14 | 18 | Una sola cifra en home, `/tratamientos`, glosario, `llms.txt`, `llms-full.txt`, FAQ |
| Altas | — | Skin Wave Max, Carbox CK, Kimi Face, Hao Face | R7 = sí; verificar que el PR las liste y no meta Adipolite |
| Adipolite | No es ficha Lumina (es Hebe corporal) | No debe colarse en catálogo facial | Rechazar si aparece como 19.ª Lumina |
| Nombres | Cuky HIFU, Endo Jiwoo / EndoJiwoo, RejuveSkin, Sakura Ultra-Lift, Yori/Yoori Peel | Fotos `img/tech-*.webp` | Una grafía canónica + `alternateName` |
| FAQ glosario | “¿Por qué 14 y no 11?” | Debe pasar a 18 vs 14, no dejar “14” en el botón | |
| AEO 23 | Siguen diciendo 14 | #41 **no** toca `scripts/aeo_pages_*.py` | Tras merge, **no** regenerar hasta L1.1; sync schema/llms a mano en este PR de sync |

Tras el merge de #41 (otro worker): si ese merge no dejó cifra 18 en `llms.txt` / schema de home y `/tratamientos`, un PR de sync aparte. No correr `build_aeo.py`. Las 23 AEO siguen en 14 hasta L1.1.

**Criterio de aceptación.** Una cifra (18) en superficies listadas. Cero `Adipolite` en HTML/llms Lumina. Cero “14 tecnolog” residual en esos archivos. Schema parseable.

**Verificación (comando).**

```bash
test -e llms.txt && test -e llms-full.txt && test -e tratamientos/index.html
grep -nE 'Adipolite' llms.txt llms-full.txt tratamientos/index.html index.html glosario/index.html || true
grep -nE '14 tecnolog|18 tecnolog' llms.txt tratamientos/index.html index.html glosario/index.html
```

**Reversión.** Revertir merge #41; volver cifra 14 en llms/schema.

---

#### L0.3 · Prioridad P0 · Esfuerzo S · Depende de — · Archivos `CLAUDE.md` (crear)

**Prompt para la IA.** Crear `CLAUDE.md` en la raíz. Contenido mínimo:

1. **Stack:** HTML/CSS/JS estático en la raíz; Vercel (`cleanUrls`, `trailingSlash: false`); GTM-TZC56NQ5; WA `+56963222683`; 23 páginas AEO generadas; hand-pages: `index.html`, `planes.html`, `tratamientos/index.html`, `resultados.html`, `evaluacion/index.html`, `franquicia/index.html`, `fundador/index.html`, `capacitacion/index.html`, 3 `/clinica/*`, `404.html`.
2. **Verify:** comandos de la sección 1 (JSON-LD parse, `grep -c '<loc>' sitemap.xml` = 34 hoy, greps prohibidos).
3. **Commits:** español imperativo.
4. **Flujo generador:** editar `scripts/aeo_pages_*.py` → `python3 scripts/build_aeo.py`. **Riesgos:** overwrite de 23 HTML; `STATIC` omite 4 URLs; `DATE_MOD` congelado; `aeo_es.py` muta `scripts/*.py`. Hasta L1.1: no correr el builder.
5. Enlace a este roadmap y a `docs/H7-PRECIOS.md`.

**Criterio de aceptación.** `test -e CLAUDE.md`. Un onboarding puede verificar JSON-LD y sitemap sin este roadmap.

**Verificación (comando).**

```bash
test -e CLAUDE.md && grep -nE 'build_aeo|DATE_MOD|34|json.loads|imperativo' CLAUDE.md
```

**Reversión.** Borrar `CLAUDE.md`.

---

#### L0.4 · Prioridad P0 · Esfuerzo S · Depende de — · Archivos `docs/PROMPTS_PENDIENTES_PUENTE_CLINERA.md`

**Prompt para la IA.** **Ya hecho en el PR que publica este roadmap** (rama `claude/happy-rubin-lv29o9`). No reescribir el puente Clinera. Solo la nota fechada 2026-09-13 de URLs en 200/308. Si este ID aparece en la cola: cerrarlo como no-op.

**Criterio de aceptación.** Nota de 2–5 líneas con fecha 2026-09-13 y códigos live.

**Verificación (comando).**

```bash
grep -n '2026-09-13' docs/PROMPTS_PENDIENTES_PUENTE_CLINERA.md
```

**Reversión.** Quitar el párrafo fechado; no tocar el resto del archivo.

---

### Bloque 1 — P1 septiembre (generador, schema, a11y, CRO)

#### L1.1 · Prioridad P1 · Esfuerzo L · Depende de L0.3 · Archivos `scripts/build_aeo.py` `scripts/aeo_template.py` `scripts/aeo_es.py` `scripts/aeo_pages_3.py` `sitemap.xml` `sitemap-images.xml`

**Prompt para la IA.** **Arreglar el generador antes de cualquier edit de página AEO.**

1. `STATIC` en `scripts/build_aeo.py`: añadir las 3 `/clinica/*` y `/fundador` (path canónico **sin** slash, como el 308 live `/fundador/` → `/fundador`). Prioridad 0.6 / monthly, como el sitemap actual.
2. `DATE_MOD`: CLI o fecha de hoy vía `scripts/schema_dates.py` (`format_schema_date`). No hardcode `2026-09-03`.
3. `scripts/aeo_es.py` `main()`: **dejar de** iterar `scripts/aeo_*.py`. Solo HTML de `AEO_DIRS` (+ `404.html` si se mantiene).
4. `EXACT` (antes de `WORDS`): `honestás`→`honestas`, `mismás`→`mismas`, `direcciónes`→`direcciones`, `evaluaciónes`→`evaluaciones`. Cuidado: `("evaluacion","evaluación")` no debe producir `evaluaciónes`.
5. `scripts/aeo_pages_3.py:145` (`description` con `honestás`) y el HTML ya emitido de esa página: `honestas`.
6. `image_sitemap()`: un `<url>` por `loc`; varios `image:image` **anidados** dentro (home tiene 7 imágenes).

**Criterio de aceptación (duro).** En un worktree limpio de `main`, con L1.1 aplicado y **sin** cambios de copy: `python3 scripts/build_aeo.py` → `git diff` solo fechas (`lastmod` / `dateModified`) o vacío. Siguen 34 `<loc>`. Cero `honestás`/`mismás`/`direcciónes`/`evaluaciónes`. **No** commitear un rebuild que reescriba las 23 páginas “porque sí”.

**Verificación (comando).**

```bash
test -e scripts/build_aeo.py && test -e scripts/aeo_es.py && test -e scripts/aeo_pages_3.py
# Tras el fix, en worktree limpio (NO en el PR de este roadmap):
# python3 scripts/build_aeo.py
# git diff --stat
grep -c '<loc>' sitemap.xml   # 34
grep -nE 'honestás|mismás|direcciónes|evaluaciónes' scripts/aeo_pages_3.py lifting-sin-cirugia-vs-lifting-quirurgico/index.html equipo/index.html || true
```

**Reversión.** Revertir solo scripts; no dejar un sitemap de 30 URLs.

---

#### L1.2 · Prioridad P1 · Esfuerzo M · Depende de L1.1 · Archivos `fundador/index.html` `index.html` `scripts/aeo_template.py` (graph compartido)

**Prompt para la IA.**

1. **Slash `/fundador`:** live 308 `/fundador/` → `/fundador`. Canonical, `og:url` y JSON-LD hoy usan slash. Alinear a `https://www.protocololumina.cl/fundador` (sin slash). Sitemap: emitir sin slash.
2. Añadir `ProfilePage` que apunte al `Person` canónico `https://www.metodohebe.cl/fundador/#person` (no inventar un segundo Person Lumina).
3. `Person.image`: ya hay `https://www.metodohebe.cl/img/ricardo-oyarzun.jpg` en el puente; no inventar otra foto. Si 404 en Hebe, omitir `image` (no placeholder).
4. Home `VideoObject`: añadir `duration` ISO 8601 real del Vimeo `1186589095` (medir; no inventar). Si no hay duración verificable: **preguntar**, no adivinar.
5. Deduplicar `https://www.protocololumina.cl/#organization` en los **35** HTML: un objeto con ese `@id` por página; el resto solo `{"@id": "..."}`. Tras L1.1, el graph AEO sale de `scripts/aeo_template.py`.

**Criterio de aceptación.** `curl -sI` `/fundador` 200 y `/fundador/` 308. Canonical sin slash. Un `#organization` declarado por página. `VideoObject.duration` presente o issue abierto. JSON-LD 0 fallos.

**Verificación (comando).**

```bash
curl -sI https://www.protocololumina.cl/fundador | head -n 5
curl -sI https://www.protocololumina.cl/fundador/ | head -n 8
grep -n 'rel="canonical"' fundador/index.html
python3 - <<'PY'
from pathlib import Path
import re
nid = 'https://www.protocololumina.cl/#organization'
for p in sorted(Path('.').rglob('*.html')):
    if '.git' in p.parts: continue
    c = p.read_text(encoding='utf-8', errors='replace').count(f'"@id": "{nid}"') + p.read_text(encoding='utf-8', errors='replace').count(f'"@id":"{nid}"')
    # contar objetos con @type junto al @id es el criterio post-fix; pre-fix todos fallan
    print(f'{c:3d} {p}')
PY
```

**Reversión.** Restaurar canonical con slash solo si el 308 se revierte (no está en el plan).

---

#### L1.3 · Prioridad P1 · Esfuerzo S · Depende de — · Archivos `css/aeo.css` `index.html` `planes.html` `resultados.html` `tratamientos/index.html`

**Prompt para la IA.** Contraste (WCAG, texto sobre fondo claro):

- Enlaces / `--rose-ink`: hoy `#96585E` en `css/aeo.css`. Subir a **`#8E4F55`** (o más oscuro) en AEO y hand-pages que copian tokens.
- Sticky / CTA verde: `#4CAF7D` (home, planes, resultados, tratamientos, `css/aeo.css` `.nav-cta`) → **≥ `#2E7D52`**.
- Estrellas (`.review .stars`, `.testi-stars`): tinta `var(--ink)` / `#1E1818`, no `--rose-deep` `#C48B90`.

No tocar `vercel.json`. No cambiar copy.

**Criterio de aceptación.** Esas tres familias de color cumplen el piso. Sticky sigue B.4.

**Verificación (comando).**

```bash
grep -nE '#4CAF7D|#8E4F55|#2E7D52|#96585E' css/aeo.css index.html planes.html resultados.html tratamientos/index.html
```

**Reversión.** Revertir CSS/tokens.

---

#### L1.4 · Prioridad P1 · Esfuerzo M · Depende de — · Archivos `planes.html` `css/aeo.css` `js/aeo.js` (y hand-pages sin focus)

**Prompt para la IA.**

1. `:focus-visible` en enlaces/botones/inputs (ya existe en `franquicia/index.html`; copiar el patrón).
2. `@media (prefers-reduced-motion: reduce)`: cortar `animation`/`transition` largas (home fadeUp, sticky scale en tratamientos).
3. `href="javascript:void(0)"` en `planes.html` (modales “Ver opciones” / “Ver detalles”) → `<button type="button">`.

**Criterio de aceptación.** Cero `javascript:void(0)`. Tab + teclado abre/cierra modal. `prefers-reduced-motion: reduce` sin fade.

**Verificación (comando).**

```bash
grep -n 'javascript:void' planes.html || echo 'no void(0)'
grep -nE 'focus-visible|prefers-reduced-motion' css/aeo.css planes.html index.html franquicia/index.html
```

**Reversión.** Revertir markup de botones y CSS.

---

#### L1.5 · Prioridad P1 · Esfuerzo M · Depende de — · Archivos `tratamientos/index.html` `franquicia/index.html` `index.html` `resultados.html`

**Prompt para la IA.**

1. **OG:** `/tratamientos` no tiene `og:*`. Añadir `og:title`, `og:description`, `og:url` (sin slash), `og:image` = `https://www.protocololumina.cl/img/hero-endojiwoo.webp` (existe en AEO). `/franquicia` tiene OG sin `og:image` — añadirlo. No indexar franquicia (`noindex` se queda hasta R11).
2. Hangul decorativo (`.tech-kr`, `.hero-kr`, `.header-kr-watermark`, `.foot-kr`): `lang="ko"` **o** `aria-hidden="true"` (no las dos si el texto es el único nombre; si es ornamentación, `aria-hidden`).
3. Texto de UI **≥ 15px** donde hoy hay 9–11px en body/CTA (`.logo span` 9px, `.tech-kr` 9px, `.sticky-wa` 10px, `.hero-pretitle` 10px). Decoración pura puede quedar menor si `aria-hidden`.
4. Watermark coreano (`resultados.html` `.header-kr-watermark`): no tapar H1; contraste o `aria-hidden`.

**Criterio de aceptación.** `og:image` en ambas URLs. Hangul no se anuncia como español. CTAs ≥ 15px.

**Verificación (comando).**

```bash
grep -nE 'og:image|og:url|og:title' tratamientos/index.html franquicia/index.html
grep -nE 'lang="ko"|header-kr-watermark|tech-kr' index.html resultados.html tratamientos/index.html franquicia/index.html
curl -sI https://www.protocololumina.cl/tratamientos | head -n 5
curl -sI https://www.protocololumina.cl/franquicia | head -n 5
```

**Reversión.** Quitar metas OG nuevas; restaurar tamaños.

---

#### L1.6 · Prioridad P1 · Esfuerzo M · Depende de R1 (cerrado 2026-09-13 = b) · Archivos `planes.html` `docs/H7-PRECIOS.md` `tratamientos/index.html`

**Prompt para la IA.** **R1 locked = (b)** precios actuales. **No** ejecutar H7 (c) cero precio. **No** añadir UI de cuotas mensuales.

En `planes.html`: `.plan-price::before { content:'desde ' }` → texto real `desde` en el HTML (lectores de pantalla e IA). Precios visibles **bajo 900px** (el breakpoint no debe ocultar `.plan-price`). Guía de intensidad: segundo canal en `.intensity-legend` de `tratamientos/index.html` (hoy pills de color: añadir texto o `aria-label` “Suave / Regenerativo / Estructural”). Leer `docs/H7-PRECIOS.md` solo como contexto del escenario (b).

**Criterio de aceptación.** “desde” en el DOM; precio visible a 390px y 899px. Cero UI nueva de cuotas. Cifras de plan siguen.

**Verificación (comando).**

```bash
grep -nE "content:'desde|desde " planes.html
grep -n 'intensity-legend' tratamientos/index.html
# Playwright 390px: screenshot /planes — precio visible (post-deploy)
```

**Reversión.** Restaurar `::before`; no tocar cifras.

---

#### L1.7 · Prioridad P1 · Esfuerzo S · Depende de — · Archivos `vercel.json`

**Prompt para la IA.** **Este roadmap no edita `vercel.json`.** En un PR futuro, espejar headers de Hebe (`metodo-hebe-web` / `vercel.json`): `X-Frame-Options: DENY`, `X-XSS-Protection: 1; mode=block` (además de `nosniff` + `Referrer-Policy` que Lumina ya tiene). Opcional alineado: `Cache-Control` de `/img/`, `Content-Type` de `sitemap.xml`, `s-maxage` de llms. No tocar `redirects` (16 WooCommerce).

**Criterio de aceptación.** `curl -sI` home muestra `X-Frame-Options: DENY`. Los 16 redirects siguen.

**Verificación (comando).**

```bash
python3 -c "import json; print(len(json.load(open('vercel.json'))['redirects']))"  # 16
curl -sI https://www.protocololumina.cl/ | grep -iE 'x-frame-options|x-content-type'
```

**Reversión.** Revertir solo el bloque `headers`.

---

### Bloque 2 — Evaluación

#### L2.1 · Prioridad P1 · Esfuerzo M · Depende de L1.4 · Archivos `evaluacion/index.html`

**Prompt para la IA.** Misma a11y que Hebe H2.2 (el wizard es gemelo: `inputNombre`, `inputCelular`, `inputCorreo`). Hoy las `<label>` **no** tienen `for`; los inputs no tienen `aria-invalid` / `aria-describedby` / `required`. Asociar `label for` ↔ `id`. Errores en texto (no solo color) + `aria-live`. Prefijo `+56` ya `aria-hidden`. `btnSubmit`: `type="button"` explícito. **R1 locked:** no añadir UI de cuotas mensuales ni cambiar cifras de P3.

**Criterio de aceptación.** Un lector de pantalla nombra los tres campos. Error de teléfono vacío es anunciado. Cero UI de cuotas nuevas.

**Verificación (comando).**

```bash
grep -nE 'for="inputNombre"|for="inputCelular"|for="inputCorreo"|aria-invalid|aria-describedby' evaluacion/index.html
curl -sI https://www.protocololumina.cl/evaluacion | head -n 5
```

**Reversión.** Revertir atributos; no tocar el flujo Mercado Pago.

---

### Bloque 5 — AEO / Share of Model (P2 oct–nov · cierre dic)

#### L5.1 · Prioridad P2 · Esfuerzo L · Depende de L1.1 · Archivos `scripts/aeo_pages_*.py` + URLs SoM débiles · `docs/SHARE-OF-MODEL-MES0.md`

**Prompt para la IA.** Mes 0 (`docs/SHARE-OF-MODEL-MES0.md`) marca citas débiles o nulas. Añadir / reforzar bloque **answer-first** (40–60 palabras, H1 pregunta o `.answer-first#respuesta`) en las URLs que deben ganar en mes 3, **sin** inventar resultados:

| # SoM | URL |
|---|---|
| 1 | `/endojiwoo` |
| 2, 7, 8 | `/endolaser-facial` + `resultados.html` (answer-first; no cm) |
| 3 | `/lifting-facial-coreano` |
| 5 | `/lifting-sin-cirugia-vs-lifting-quirurgico` |
| 10 | `/tratamientos` (hand-page) |
| 11 | `/hifu-facial` |
| 12 | `/ojeras-tratamiento-sin-cirugia` |
| 13 | `/flacidez-facial` |
| 15 | `/radiofrecuencia-facial` |

Editar `scripts/aeo_pages_*.py` y regenerar. `resultados.html` y `/tratamientos` a mano. Una URL (o un cluster mínimo) por PR si el diff es grande.

**Criterio de aceptación.** Cada URL tocada tiene párrafo inicial citeable. FAQ visible = schema. Cero cifras nuevas de planes.

**Verificación (comando).**

```bash
grep -nE 'answer-first|id="respuesta"' endojiwoo/index.html endolaser-facial/index.html lifting-facial-coreano/index.html
curl -sI https://www.protocololumina.cl/endojiwoo | head -n 5
```

**Reversión.** Revertir pages_*.py y rebuild.

---

#### L5.2 · Prioridad P2 · Esfuerzo S · Depende de L0.2 · Archivos `llms.txt` `llms-full.txt` `robots.txt`

**Prompt para la IA.** Tras merge de L0.2 (cifra 18 + lista). Releer `llms.txt` / `llms-full.txt`: una cifra, sin tabla de precios (salvo R1=a), desambiguación México/Brasil/Lo Barnechea, enlaces a pilares. `robots.txt` ya declara ambos.

**Criterio de aceptación.** Primera línea / bloque tecnologías = 18. Cero `1.177.990` u Offer de plan.

**Verificación (comando).**

```bash
grep -nE '18 tecnolog|14 tecnolog|1\.177' llms.txt llms-full.txt
curl -sI https://www.protocololumina.cl/llms.txt | head -n 8
```

**Reversión.** Restaurar llms de `main` pre-L0.2.

---

#### L5.3 · Prioridad P2 · Esfuerzo M · Depende de L5.1 · Archivos `docs/SHARE-OF-MODEL-MES0.md` + páginas citeables

**Prompt para la IA.** **1–15 dic 2026:** refresh trimestral (fechas `dateModified` vía `format_schema_date`, bloque “actualización” solo con dato operativo real — no inventar). Repetir las **15 preguntas** de `docs/SHARE-OF-MODEL-MES0.md` en Perplexity, ChatGPT (búsqueda) y AI Overviews Chile. Anexar tabla mes 3 (citas con URL `protocololumina.cl`). Meta: 10 % de citas con URL propia. No implementar esto antes de diciembre.

**Criterio de aceptación.** Doc mes 3 + `dateModified` coherente. Mismas 15 preguntas.

**Verificación (comando).**

```bash
test -e docs/SHARE-OF-MODEL-MES0.md
grep -nE 'mes 3|diciembre|2026-12' docs/SHARE-OF-MODEL-MES0.md
```

**Reversión.** Quitar anexo mes 3; no revertir contenido AEO de L5.1.

---

#### L5.4 · Prioridad P2 · Esfuerzo S · Depende de — · Archivos `capacitacion/index.html`

**Prompt para la IA.** `capacitacion/index.html`: `lang="es"` (no `es-CL`), **sin** canonical, `noindex`. Añadir `<link rel="canonical" href="https://www.protocololumina.cl/capacitacion">` y `html lang="es-CL"`. **Seguir `noindex`** (manual interno). No meterla al sitemap. No inventar copy clínico.

**Criterio de aceptación.** Canonical + `es-CL`. `robots` sigue `noindex, nofollow`.

**Verificación (comando).**

```bash
grep -nE 'lang=|canonical|robots' capacitacion/index.html | head
curl -sI https://www.protocololumina.cl/capacitacion | head -n 8
```

**Reversión.** Quitar canonical; restaurar `lang="es"`.

---

### Bloque 6 — Transversal (T)

Misma red (**R2 locked**): GTM **GTM-TZC56NQ5**, WhatsApp **+56 9 6322 2683** (`56963222683`). Medir en Analytics **por URL de página**. No crear un GTM ni un WA “de Lumina” distinto.

#### T6.1 · Prioridad P2 · Esfuerzo S · Depende de — · Archivos `js/aeo.js` (solo si se elige el opcional)

**Prompt para la IA.** **R2 locked:** no provisionar contenedor GTM nuevo ni otro número WA. Completar `clinica:'lumina'` en las páginas que aún no lo tienen es **opcional, no requerido**. Hoy está en 5 HTML + `js/aeo.js`. Si se hace, no cambiar `GTM-TZC56NQ5`. Si no se hace, este ID se cierra como no-op. La medición oficial es por page URL en Analytics.

**Criterio de aceptación.** Sigue un solo GTM y un solo WA. Cero contenedor/número nuevo. El opcional `clinica:'lumina'` no es gate.

**Verificación (comando).**

```bash
grep -rlE "clinica: 'lumina'|clinica:'lumina'" --include='*.html' --include='*.js' . | grep -v '/.git/' | wc -l
grep -rE "GTM-TZC56NQ5" --include='*.html' . | grep -v '/.git/' | wc -l
```

**Reversión.** Revertir pushes de dataLayer.

---

#### T6.2 · Prioridad P2 · Esfuerzo S · Depende de — · Archivos `js/aeo.js` `evaluacion/index.html`

**Prompt para la IA.** Unificar evento de contacto: `contacto_web` + `cta_destination` `whatsapp` | `evaluacion_form` (ya en `js/aeo.js`). El wizard de `/evaluacion` ya manda `clinica:'lumina'` en varios `dataLayer.push`: no duplicar `Lead` de Meta en cada clic de CTA (el Lead legítimo es el submit). Documentar en el PR qué eventos disparan `fbq`.

**Criterio de aceptación.** Un `Lead` por envío de formulario, no por sticky. WA usa `56963222683`.

**Verificación (comando).**

```bash
grep -nE 'fbq\(|Lead|contacto_web|56963222683' js/aeo.js evaluacion/index.html | head -n 40
```

**Reversión.** Revertir JS de tracking.

---

#### T6.3 · Prioridad P2 · Esfuerzo S · Depende de — · Archivos todos los `wa.me` / tel

**Prompt para la IA.** **R2 locked:** un solo número `56963222683` / `+56963222683`. No añadir un segundo WA “Lumina”. Footer AEO ya lo usa (`scripts/aeo_template.py` `PHONE`). No copiar un número de otro repo.

**Criterio de aceptación.** Grep de `wa.me/` y `tel:` solo ese número (salvo `+56` visual).

**Verificación (comando).**

```bash
grep -rhoE 'wa.me/[0-9]+|\+569[0-9]+' --include='*.html' --include='*.py' --include='*.js' . | grep -v '/.git/' | sort | uniq -c
```

**Reversión.** No aplica si no hubo cambio.

---

## 4. Solo Ricardo

R1–R5, R7 y **R8** (`legalName`) están **locked**. No reabrir. Si un L/T depende de un R **abierto** (R6, R9–R12), parar.

### Locked

| ID | Estado | Decisión | Acción Lumina |
|---|---|---|---|
| **R1** | Locked | Precios actuales = H7 **(b)**. No (c) cero precio | L1.6: “desde” texto real, precio visible &lt;900px, segundo canal de intensidad. **Sin** UI nueva de cuotas mensuales |
| **R2** | Locked | Un GTM `GTM-TZC56NQ5` y un WA `56963222683`. Medir en Analytics **por URL**. No split por marca | T6.1: **no** provisionar contenedor/número. Completar `clinica:'lumina'` es opcional |
| **R3** | Locked | Un solo par de copy: *más de 5.000 pacientes* · *5/5 estrellas en Google* | Nunca `AggregateRating` ni Review oculto. No usar la cifra Hebe (30.000) |
| **R4** | Locked · **solo Hebe** | KPI AUGE (sesiones que arrancan `/evaluacion` con origen AUGE; +20 % relativo; tope WA). Decidido en el repo Hebe | **Cero acción** en Lumina. No inventar un KPI AUGE facial |
| **R5** | Locked baseline | PageSpeed **móvil** es el baseline. GSC sigue pendiente | Scores en §2. GSC **no bloquea** L1–L5 ni T6 |
| **R7** | Locked | Mergear [#41](https://github.com/odracirnuzra10/lumina-web/pull/41) (14→18). Adipolite no es Lumina | L0.2 **desbloqueado**. **Otro worker** hace el merge |
| **R8** | Locked | `legalName` **Protocolo Lumina Limitada** · RUT **78.066.765-6** (`taxID`). No `vatID` (no había slot). No URL Clinera `app.clinera.io/hebe` | Organization `#organization` + pie / llms |

### Abiertos (la IA no asume)

| ID | Decisión / cuenta | Bloquea |
|---|---|---|
| **R6** | Fichas Doctoralia (clínica + personas reales) | Off-site |
| **R9** | `foundingDate` 2025 en `scripts/aeo_template.py` | Fechas schema |
| **R10** | Consentimiento testimonio Corea (reel) para web | Review extra en `/opiniones` |
| **R11** | INAPI marcas → quitar `noindex` de `/franquicia` | Indexación franquicia |
| **R12** | URL pública de booking Clinera (`URL_RESERVA_LUMINA`) | Sustituir `/evaluacion` en `/clinica/*` |

Siguen abiertas **sin reciclar IDs locked:** nombres/fotos/Superintendencia en `/equipo`; handle IG (`rejuvenecimiento.facial.lumina`); Wikidata. GSC/Bing es la cola de R5, no un gate.

No crear `?cid=` de Google. Shares oficiales ya están (Vitacura `uKeMlkibRy1TPB7vK` · Concón `CeMMtlyCmwN5K3yxP` · Los Ángeles `GKckpVUP3cGC9XGLq`).

---

## 5. Checklist post-deploy (cada merge)

Tras el deploy de Vercel, en las URLs **tocadas**:

```bash
# 1) Headers
curl -sI https://www.protocololumina.cl/<path> | head -n 12

# 2) IndexNow (si la URL está en sitemap y el cambio es indexable)
curl -sS https://api.indexnow.org/indexnow -H 'Content-Type: application/json' \
  -d '{"host":"www.protocololumina.cl","key":"lumina-indexnow-2026-09-03","keyLocation":"https://www.protocololumina.cl/lumina-indexnow-2026-09-03.txt","urlList":["https://www.protocololumina.cl/<path>"]}'

# 3) Sitemap
grep -c '<loc>' sitemap.xml   # 34 en main 2026-09-13; no bajar

# 4) JSON-LD (comando de la sección 1) — 0 FAIL

# 5) Playwright 390px en la URL tocada (nav, sticky B.4, precio L1.6, form L2.1)
```

También: Rich Results Test en home / `/evaluacion` / `/fundador` si se tocó schema. No pinguear IndexNow por `/capacitacion` ni `/franquicia` mientras sean `noindex`.

---

## 6. Calendario y ventana de evaluación

T0 = **13-sep-2026** (estado verificado). Mes 3 SoM = **1–15 dic 2026**.

| Ventana | Fecha | Lumina | Transversal |
|---|---|---|---|
| Semana P0 | 13–20 sep | L0.1 `knowsAbout` · L0.2 **desbloqueado** (R7; merge #41 = otro worker) · L0.3 `CLAUDE.md` · **L0.4 este PR** | — |
| T+7 | 20 sep | L1.1 generador (gate AEO). No editar las 23 páginas antes | — |
| T+14 | 27 sep | L1.2 fundador/schema · L1.3 contraste · L1.4 focus/motion | — |
| P1 cierre sep | 28–30 sep | L1.5 OG/lang · L1.6 (b) “desde” + precio &lt;900px · L1.7 headers · L2.1 form (sin cuotas) | — |
| T+30 | 13 oct | Primer corte: 34 loc, JSON-LD 0 fail, greps `honestás` = 0 | T6.1 opcional; no nuevo GTM/WA |
| Oct | oct | L5.1 answer-first SoM (por URL) · L5.2 llms post-L0.2 · L5.4 `/capacitacion` | T6.2 eventos · T6.3 WA único |
| T+60 | 12 nov | SoM cualitativo intermedio (mismas 15 preguntas, no es mes 3) | Revisar GTM-TZC56NQ5 |
| T+90 / mes 3 | **1–15 dic** | **L5.3** refresh + Share of Model mes 3 · meta 10 % citas con URL | Misma medición en Hebe (repo hermano) |
| Cierre horizonte | 15 dic | Stop de features; solo hotfix YMYL / generador | — |

P3 (condicional, R abiertos): Person/Superintendencia, index `/franquicia` (R11), booking Clinera (R12). R8 `legalName` ya locked. **No** `AggregateRating` (R3).

---

## Apéndice — URLs live 2026-09-13 (`curl -sI`)

| Código | URL |
|---|---|
| 200 | `https://www.protocololumina.cl/` |
| 200 | `https://www.protocololumina.cl/planes` |
| 308 → `/planes` | `https://www.protocololumina.cl/planes/` |
| 200 | `https://www.protocololumina.cl/tratamientos` |
| 200 | `https://www.protocololumina.cl/evaluacion` |
| 200 | `https://www.protocololumina.cl/fundador` |
| 308 → `/fundador` | `https://www.protocololumina.cl/fundador/` |
| 200 | `https://www.protocololumina.cl/franquicia` |
| 200 | `https://www.protocololumina.cl/capacitacion` |
| 200 | `https://www.protocololumina.cl/clinica/como-confirmamos-tu-hora-por-whatsapp` |
| 200 | `https://www.protocololumina.cl/clinica/que-pasa-con-tu-ficha-entre-sesiones` |
| 200 | `https://www.protocololumina.cl/clinica/por-que-respondemos-en-minutos` |
| 200 | `https://www.protocololumina.cl/llms.txt` |
| 200 | `https://www.protocololumina.cl/llms-full.txt` |
| 200 | `https://www.protocololumina.cl/sitemap.xml` |
| 200 | `https://www.protocololumina.cl/sitemap-images.xml` |
| 200 | `https://www.protocololumina.cl/robots.txt` |
| 200 | `https://www.protocololumina.cl/lumina-indexnow-2026-09-03.txt` |
| 308 → `/evaluacion` | `https://www.protocololumina.cl/reserva` · `/agenda` |
| 200 | `https://www.clinera.io/casos/protocolo-lumina` |
