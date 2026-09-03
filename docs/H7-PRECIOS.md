# H7 — Precios públicos legibles por IA

**Estado:** escenario **(b) preparado e implementado en superficies de IA**. Precios visibles en `/planes` **no se eliminaron** (pendiente confirmación de Ricardo).

## Escenarios

| | llms.txt / llms-full.txt | Schema | `/planes` visible | CTA |
|---|---|---|---|---|
| (a) mantener exactos | tabla CLP | `Offer.price` | cifras | — |
| **(b) este PR** | sin tabla exacta; P3 $27.990 y “cotiza en evaluación” | `Service` + `ReserveAction` “Agenda tu hora”; sin `Offer.price` | cifras + rótulo CSS **desde** | Agenda tu hora |
| (c) cero precio | igual que b + quitar P3 | igual que b | borrar cifras | Agenda tu hora |

## Cómo pasar a (c) si Ricardo confirma

1. Quitar `.plan-price` / tabla / modal JS en `planes.html`.
2. Quitar `$27.990` de CTAs (ya no está) y de copy de P3 si también se oculta la evaluación.
3. Regenerar `llms.txt` sin el valor de P3.

## Cómo volver a (a)

Restaurar el `ItemList` con `Product`/`Offer.price` (el JSON anterior está en git history de `planes.html`) y la tabla de `llms.txt`.

## Toggle

No hay feature flag de runtime (sitio estático). El comentario `H7` vive en este archivo y en el schema de `/planes` (`ReserveAction`).
