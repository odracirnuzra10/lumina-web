# Eventos dataLayer — Protocolo Lumina

Contenedor único **GTM-TZC56NQ5** (R2). WhatsApp único **56963222683**. La medición oficial es **por URL de página** en Analytics; `clinica: "lumina"` es dimensión de marca en el mismo contenedor, no un GTM aparte. No hay dashboard en este repo.

`fbq` **Lead** se dispara **una vez**, en el submit de `/evaluacion`. Los CTA (sticky, footer, nav) no son Lead.

## Dimensión de página

Toda página con GTM emite al cargar (o ya lo lleva en eventos de esa vista):

```json
{ "clinica": "lumina" }
```

404 y `/capacitacion` no cargan GTM (error / noindex).

## Eventos

### `contacto_web`

Clic a WhatsApp o a `/evaluacion`. Fuente canónica: `js/aeo.js` (páginas AEO) y el snippet de home / planes / resultados. `/evaluacion` también lo emite en clics `wa.me`.

```json
{
  "event": "contacto_web",
  "cta_destination": "whatsapp",
  "cta_label": "WhatsApp +56 9 6322 2683",
  "cta_type": "whatsapp",
  "click_location": "/hifu-facial",
  "clinica": "lumina"
}
```

`cta_destination`: `whatsapp` | `evaluacion_form`.

### `contacto_whatsapp_2026` y `whatsapp_click`

Alias históricos en home / planes / resultados / wizard. Seguir escuchándolos en GTM si ya existen tags. El evento nuevo a mapear es `contacto_web`.

### `view_content`

Scroll ≥ 50 % en home, `/planes`, `/resultados`.

```json
{
  "event": "view_content",
  "content_name": "home",
  "scroll_depth": "50",
  "clinica": "lumina"
}
```

### Wizard `/evaluacion`

| event | Cuándo |
|---|---|
| `eval_select_sede` | Elige sede |
| `eval_select_schedule` | Día + slot listos |
| `eval_submit_form` | Submit válido (`event_id` = Pixel + CAPI) |
| `eval_confirm_whatsapp` | Clic WA post-submit |
| `eval_pago_evaluacion` | Clic pagar P3 ($27.990 CLP) |

```json
{
  "event": "eval_submit_form",
  "sede": "vitacura",
  "day": "LUN 14",
  "slot": "10:00",
  "event_id": "lead_…",
  "clinica": "lumina"
}
```

## Qué dispara `fbq`

| Pixel | Dónde | No es |
|---|---|---|
| `PageView` | home, planes, resultados, evaluación, franquicia | — |
| `ViewContent` | scroll 50 % (home/planes/resultados); elegir sede en P3 | Lead |
| `InitiateCheckout` | avanza horario en P3 | Lead |
| `Contact` | clic `wa.me` (home, planes, resultados, `js/aeo.js`) | Lead |
| `Lead` | **solo** submit del formulario P3 | sticky / nav / footer |
| `ClickPagar` (custom) | clic pagar; **no** es `Purchase` | compra |

`Purchase` lo confirma el webhook de pago (fuera de este spec). No duplicar Lead en el sticky.

## Constante

```json
{
  "gtm": "GTM-TZC56NQ5",
  "whatsapp": "56963222683",
  "clinica": "lumina",
  "measure_by": "page_url"
}
```
