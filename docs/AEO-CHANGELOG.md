# Changelog AEO Protocolo Lumina — 2026-09-03

Hallazgo → acción → URL/archivo → cómo verificar.

## H1 — Contenido citeable (crítico)

| Acción | Dónde | Verificar |
|---|---|---|
| Pilar answer-first | `/lifting-facial-coreano` | H1 pregunta, 40–60 palabras al inicio, FAQ, Revisado por |
| Fichas tecnología | `/endojiwoo` `/endolaser-facial` `/hifu-facial` `/radiofrecuencia-facial` | `MedicalProcedure` + `alternateName` + FAQ |
| Comparativas | `/endolaser-vs-hifu` `/lifting-coreano-vs-hilos-tensores` `/endojiwoo-vs-bioestimuladores-inyectables` `/lifting-sin-cirugia-vs-lifting-quirurgico` | H2 pregunta |
| Problemas | `/ojeras-tratamiento-sin-cirugia` `/manchas-faciales-despigmentacion` `/flacidez-facial` `/papada-sin-cirugia` | FAQ 8+ |
| Hub FAQ / glosario / blog | `/preguntas-frecuentes` `/glosario` `/blog` `/blog/lifting-facial-coreano-chile` | DefinedTermSet en glosario |
| Sitemap ≥ 25 URLs | `sitemap.xml` (30 loc) | `grep -c '<loc>' sitemap.xml` |

## H2 — Desambiguación de entidad (crítico)

| Acción | Dónde | Verificar |
|---|---|---|
| Frase de entidad idéntica | schema `Organization.description`, meta home, `llms.txt`, `llms-full.txt`, footer AEO, `/preguntas-frecuentes` | buscar la frase completa |
| `disambiguatingDescription` + `alternateName` | `#organization` en todas las páginas AEO y home/planes/tratamientos/resultados/evaluacion | Rich Results / vista JSON-LD |
| México / Brasil / Lo Barnechea | mismos textos | no confundir con Cosmica Skin ni Lumina Clinic |
| `parentOrganization` OACG | schema | url https://oacg.cl |
| `sameAs` ≥ 6 | Instagram, oacg.cl/lumina, metodohebe.cl, 3 Google Maps | contar URLs en JSON-LD |
| Instagram handle | **pendiente Ricardo** (off-site): pasar a `protocololumina` o nombre visible “Protocolo Lumina · Clínica facial Chile” | no se puede cambiar desde el repo |

## H3 — Schema que puede penalizar (alto)

| Acción | Dónde | Verificar |
|---|---|---|
| Eliminado `AggregateRating` standalone | `resultados.html` | no debe quedar `@type":"AggregateRating"` |
| `Organization` + `WebSite` + 3 `MedicalClinic` (calle, geo, horarios, `priceRange`, `medicalSpecialty`) | graph en páginas | streetAddress Los Abedules / Pelargonias / Mistral |
| `MedicalWebPage` + `BreadcrumbList` + `FAQPage` | todas las URLs nuevas + core | FAQ visible |
| Canonical 100% | tratamientos, evaluacion, nuevas | `<link rel="canonical"` |
| `/evaluacion` H1 + meta description | `evaluacion/index.html` | H1 “Evaluación facial P3 — Protocolo Lumina” |
| `Speakable` | cssSelector `.answer-first` / `h1` | JSON-LD |
| OG image rota (`og-lumina.jpg` no existía) | apunta a `/img/hero-endojiwoo.webp` | |
| VideoObject Vimeo | home | `player.vimeo.com/video/1186589095` |

## H4 — E-E-A-T (alto YMYL)

| Acción | Dónde | Verificar |
|---|---|---|
| `/equipo` honesto (sin Person inventado) | `/equipo` | plantilla lista; no hay RUT/registro falso |
| “Revisado por Equipo clínico Protocolo Lumina” + fechas | meta-eeat / FAQ | datePublished / dateModified 2026-09-03 |
| Citas HIFU / RF / láser | pilares y fichas | bloque Referencias |
| Disclaimer médico | pie de páginas AEO | resultados varían, P3 obligatoria |
| Person + Superintendencia | **pendiente Ricardo** | |

## H5 — Inconsistencias y residuos (medio)

| Acción | Dónde | Verificar |
|---|---|---|
| 11 → **14** | `llms.txt`, textos, /tratamientos | grep “11 tecnolog” debe ser 0 en llms |
| 301 WooCommerce | `vercel.json` `/producto/:path*` `/tienda/:path*` `/planes/` `/shop` `/carrito` | curl -I |
| Recrawl Search Console | **pendiente humano** | GSC URL inspection |
| Sedes facial confirmadas | las 3 se mantienen | evaluacion ya listaba las 3 direcciones |
| AgendaPro no enlazado | reserva `/evaluacion`; aliases `/reserva` `/agenda` | grep agendapro.com en href = 0 |
| Título Concón-only | no se emite; sedes en schema | |
| Ticker `/evaluacion` con precios viejos ($897.990 / $3.997.990) | reemplazado por “desde” | |

## H6 — Semrush/Ahrefs (medición)

| Acción | Dónde | Verificar |
|---|---|---|
| `SemrushBot` y `AhrefsBot` Allow | `robots.txt` | ya no Disallow |
| IndexNow key | `/lumina-indexnow-2026-09-03.txt` | 200 |
| GSC + Bing verify | **pendiente credenciales** | |
| Share of Model mes 0 | `docs/SHARE-OF-MODEL-MES0.md` | 15 preguntas, cita ~0% |

## H7 — Precios (decisión)

Ver `docs/H7-PRECIOS.md`. Implementado **(b)** en IA; visibles en `/planes` con rótulo “desde”. CTA unificado **Agenda tu hora**.

## S5 llms

- `llms.txt` reescrito (frase, desambiguación, 14, FAQ, sin tabla de planes).
- `llms-full.txt` publicado (~24 KB).
- Ambos en robots + sitemap.

## S6 off-site (código vs humano)

| Hecho en repo | Pendiente humano |
|---|---|
| Cross-link Hebe (PR hermano) | GBP por sede, Doctoralia, Wikidata, TikTok/YouTube, cambio handle IG, desindexar AgendaPro, menciones en medios |

## S7 + sección 5 evaluada

- CWV: imágenes ya WebP + lazy; OG corregido.
- `lang`/`hreflang` `es-CL` unificado (franquicia ya era es-CL).
- Cookies: GTM/pixel no bloquean HTML a bots (sin cookie wall).
- Sitemap de imágenes: `sitemap-images.xml` con `image:caption`.
- Idioma único declarado en llms.
- 404 `noindex` + enlaces.
- Enlazado interno: nav/footer AEO + related.
- Speakable en JSON-LD.
- VideoObject en home (Vimeo). Testimonio Corea: pendiente consentimiento.
- Programa reseñas Google: documentado, sin AggregateRating prematuro.
- `/seguridad-contraindicaciones` publicada.
- Franquicia: FAQPage B2B, Offer LeaseOut, sigue `noindex` por INAPI.

## No hecho (fuera de código o sin dato)

- Cambiar handle de Instagram.
- Verificar GSC/Bing (hace falta login).
- Wikidata / GBP / Doctoralia.
- Nombres reales de profesionales.
- legalName (razón social chilena no confirmada; se omite a propósito).
- Confirmar foundingDate 2025 si Ricardo tiene otra fecha.
