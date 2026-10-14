# /home2 — pendientes de revisión

Página de revisión del home premium (`home2/index.html`). No indexable, fuera del sitemap. El home actual (`/`) no se toca hasta "aprobado home2".

## Pendientes

1. **Retrato del Dr. Eugenio Castro.** Falta la foto B/N. Hoy hay un marco vacío (`.portrait`); ver `TODO` en el HTML. Usar webp con `width`/`height` y `loading="lazy"`.
2. **Cita del Dr. Castro.** Texto provisorio. `TODO: validar cita con Dr. Castro`.
3. **Nombrar al Dr. Castro.** `CLAUDE.md` (R6) permite nombrar solo a Ricardo Oyarzún. La página sigue la instrucción de nombrarlo; confirmar antes de aprobar.
4. **Etiquetas diferidas.** GTM, Meta Pixel y Clarity cargan en la primera interacción o 4 s después de `load`, para cumplir Lighthouse. Un rebote sin interacción en menos de 4 s no se mide. Si se prefiere medición inmediata, cargar el snippet GTM estándar en `<head>` (baja la nota móvil).
5. **`click_location`.** Los eventos de CTA usan `home`, igual que el home actual. En el preview se mezclan con los del home real.
6. **Footer.** Es el del home actual, con su link a `metodohebe.cl`. Quitarlo si "sin contenido de Método Hebe" incluye ese link.
7. **Fuentes del logo.** El logo conserva Playfair Display y Sora (subconjunto mínimo desde Google Fonts).

## Paso 2 (solo con "aprobado home2")

Reemplazar `/` por el contenido de `/home2`, quitar `noindex`, restaurar canonical propio, conservar el JSON-LD del home actual y dejar `/home2` con 301 a `/`.
