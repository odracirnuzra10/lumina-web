# Prompts pendientes — puente Lumina → Clinera

Lo cerrado en este repo (schema compartido, `/clinica/*`, `/fundador/`, `llms.txt`, FAQ, footer, metas faciales) no se repite.
Solo lo que depende de otro repo o de trabajo off-site.

---

## 1) Repo Clinera (`clinera.io`)

```
Contexto: Protocolo Lumina (https://www.protocololumina.cl) ya enlaza entidad hacia
Clinera con los mismos @id que Método Hebe:
  - https://oacg.cl/#organization
  - https://clinera.io/#organization
  - https://www.metodohebe.cl/fundador/#person

En el sitio Clinera:

1) Crear https://clinera.io/casos/protocolo-lumina
   - Operación facial en Vitacura, Concón y Los Ángeles.
   - AURA: confirmación WhatsApp, recordatorios, reagendamiento.
   - Enlaces dofollow a https://www.protocololumina.cl y a
     https://www.protocololumina.cl/clinica/como-confirmamos-tu-hora-por-whatsapp
   - Schema con about Clinera y mentions Protocolo Lumina.

2) Asegurar que Organization Clinera use los @id de arriba (idénticos a Hebe/Lumina).

3) Si hay URL de reserva pública en dominio Clinera para Lumina, devolverla
   (hoy los CTA del sitio van a https://www.protocololumina.cl/evaluacion).

Sin nofollow a las clínicas. Sin comparativas vs competidores.
```

Cuando exista la URL del caso, actualizar en este repo
`/clinica/por-que-respondemos-en-minutos` (hoy → clinera.io + TODO).

---

## 2) Post-deploy

```
Tras merge + deploy de protocololumina.cl, Rich Results Test en:
  - https://www.protocololumina.cl/
  - https://www.protocololumina.cl/fundador/
  - https://www.protocololumina.cl/clinica/como-confirmamos-tu-hora-por-whatsapp
  - https://www.protocololumina.cl/evaluacion
Pedir indexación de /clinica/* y /fundador/.
```
