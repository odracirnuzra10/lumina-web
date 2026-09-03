#!/usr/bin/env python3
"""Chilean Spanish polish for AEO copy. Never mutates href/src/URL strings."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Exact first (over-corrections and voseo), then longest unaccented stems.
EXACT = [
    ("sesiónes", "sesiones"),
    ("Sesiónes", "Sesiones"),
    ("anestésia", "anestesia"),
    ("Anestésia", "Anestesia"),
    ("hemato más", "hematomas"),
    ("hematomás", "hematomas"),
    ("anonimás", "anónimas"),
    ("Firmás", "Firmas"),
    ("cremás", "cremas"),
    ("Cremás", "Cremas"),
]

WORDS = [
    ("Los Angeles", "Los Ángeles"),
    ("polinucleotidos", "polinucleótidos"),
    ("bioestimulacion", "bioestimulación"),
    ("bioestimuladores", "bioestimuladores"),
    ("fotoproteccion", "fotoprotección"),
    ("desambiguacion", "desambiguación"),
    ("contraindicacion", "contraindicación"),
    ("contraindicaciones", "contraindicaciones"),
    ("radiofrecuencia", "radiofrecuencia"),
    ("microfocalizado", "microfocalizado"),
    ("endoluminal", "endoluminal"),
    ("liposuccion", "liposucción"),
    ("ritidectomia", "ritidectomía"),
    ("tecnologias", "tecnologías"),
    ("tecnologia", "tecnología"),
    ("tecnologico", "tecnológico"),
    ("armonizacion", "armonización"),
    ("regeneracion", "regeneración"),
    ("inflamacion", "inflamación"),
    ("infeccion", "infección"),
    ("recuperacion", "recuperación"),
    ("cotizacion", "cotización"),
    ("confirmacion", "confirmación"),
    ("indicacion", "indicación"),
    ("descamacion", "descamación"),
    ("sensacion", "sensación"),
    ("conversacion", "conversación"),
    ("evaluacion", "evaluación"),
    ("Evaluacion", "Evaluación"),
    ("quirurgicos", "quirúrgicos"),
    ("quirurgicas", "quirúrgicas"),
    ("quirurgico", "quirúrgico"),
    ("quirurgica", "quirúrgica"),
    ("cirugias", "cirugías"),
    ("cirugia", "cirugía"),
    ("clinicas", "clínicas"),
    ("clinica", "clínica"),
    ("Clinica", "Clínica"),
    ("cosmeticos", "cosméticos"),
    ("cosmetico", "cosmético"),
    ("Cosmetico", "Cosmético"),
    ("esteticas", "estéticas"),
    ("estetica", "estética"),
    ("energetico", "energético"),
    ("energetica", "energética"),
    ("diagnostico", "diagnóstico"),
    ("diagnosticos", "diagnósticos"),
    ("polilactico", "poliláctico"),
    ("hidroxiapatita", "hidroxiapatita"),
    ("sinonimos", "sinónimos"),
    ("sinonimo", "sinónimo"),
    ("homonimos", "homónimos"),
    ("homonimo", "homónimo"),
    ("homonima", "homónima"),
    ("busquedas", "búsquedas"),
    ("busqueda", "búsqueda"),
    ("Busqueda", "Búsqueda"),
    ("grafias", "grafías"),
    ("grafia", "grafía"),
    ("farmacos", "fármacos"),
    ("farmaco", "fármaco"),
    ("colageno", "colágeno"),
    ("subcutaneo", "subcutáneo"),
    ("transcutaneo", "transcutáneo"),
    ("quirofano", "quirófano"),
    ("coagulopatia", "coagulopatía"),
    ("hinchazon", "hinchazón"),
    ("asimetria", "asimetría"),
    ("acido", "ácido"),
    ("Acido", "Ácido"),
    ("nodulo", "nódulo"),
    ("moreton", "moretón"),
    ("telefono", "teléfono"),
    ("Telefono", "Teléfono"),
    ("titulo", "título"),
    ("articulo", "artículo"),
    ("Articulo", "Artículo"),
    ("paginas", "páginas"),
    ("pagina", "página"),
    ("Catalogo", "Catálogo"),
    ("catalogo", "catálogo"),
    ("termino", "término"),
    ("legitimo", "legítimo"),
    ("semantico", "semántico"),
    ("semantica", "semántica"),
    ("Medico", "Médico"),
    ("medico", "médico"),
    ("medica", "médica"),
    ("Metodo", "Método"),
    ("Ana Maria", "Ana María"),
    ("Mexico", "México"),
    ("Concon", "Concón"),
    ("tambien", "también"),
    ("despues", "después"),
    ("sesion", "sesión"),
    ("dias", "días"),
    ("dia", "día"),
    ("asi", "así"),
    ("aqui", "aquí"),
    ("Aqui", "Aquí"),
    ("alli", "allí"),
    ("segun", "según"),
    ("area", "área"),
    ("ovalo", "óvalo"),
    ("Ovalo", "Óvalo"),
    ("laser", "láser"),
    ("Laser", "Láser"),
    ("lineas", "líneas"),
    ("linea", "línea"),
    ("paises", "países"),
    ("pais", "país"),
    ("maquina", "máquina"),
    ("tipica", "típica"),
    ("tipico", "típico"),
    ("decia", "decía"),
    ("usara", "usará"),
    ("Recien", "Recién"),
    ("recien", "recién"),
    ("deberia", "debería"),
    ("deberian", "deberían"),
    ("habia", "había"),
    ("habian", "habían"),
    ("varian", "varían"),
    ("tecnica", "técnica"),
    ("Tecnica", "Técnica"),
    ("lesion", "lesión"),
    ("tension", "tensión"),
    ("expresion", "expresión"),
    ("relacion", "relación"),
    ("Relacion", "Relación"),
    ("energia", "energía"),
    ("Energia", "Energía"),
    ("resenas", "reseñas"),
    ("resena", "reseña"),
    ("senal", "señal"),
    ("incomoda", "incómoda"),
    ("detras", "detrás"),
    ("Detras", "Detrás"),
    ("mantencion", "mantención"),
    ("angulos", "ángulos"),
    ("angulo", "ángulo"),
    ("comun", "común"),
    ("sabado", "sábado"),
    ("Sabado", "Sábado"),
    ("estas en", "estás en"),
    ("te esta ", "te está "),
    ("le esta ", "le está "),
    ("esta prometiendo", "está prometiendo"),
    ("esta vendiendo", "está vendiendo"),
    ("esta descrito", "está descrito"),
    ("esta inactivo", "está inactivo"),
    ("esta pagina", "esta página"),
    ("Esta pagina", "Esta página"),
    ("piel de mas", "piel de más"),
    ("de mas,", "de más,"),
    ("de mas.", "de más."),
    ("duele de mas", "duele de más"),
    ("Si. ", "Sí. "),
    ("Si.", "Sí."),
    ("Por que ", "Por qué "),
    ("por que ", "por qué "),
    ("Como ", "Cómo "),  # headings; "como" mid-sentence handled below
    ("Que es ", "Qué es "),
    ("Que es el ", "Qué es el "),
    ("Que es la ", "Qué es la "),
    ("Que dicen", "Qué dicen"),
    ("Que pasa", "Qué pasa"),
    ("Que horario", "Qué horario"),
    ("Que construye", "Qué construye"),
    ("Cual es", "Cuál es"),
    ("Cuales son", "Cuáles son"),
    ("Cual ", "Cuál "),
    ("Cuando se", "Cuándo se"),
    ("Donde se", "Dónde se"),
    ("Donde ", "Dónde "),
    ("Quien no", "Quién no"),
    ("Quien esta", "Quién está"),
    ("Quien ", "Quién "),
    ("Cuanto cuesta", "Cuánto cuesta"),
    ("Cuantos ", "Cuántos "),
    ("Cuantas ", "Cuántas "),
    ("hacerselo", "hacérselo"),
    ("no improvisar el", "no improvisa el"),
    ("clinicos", "clínicos"),
    ("clinico", "clínico"),
    ("organizacion", "organización"),
    ("publicaran", "publicarán"),
    ("listaran", "listarán"),
    ("esteticistas", "esteticistas"),
    ("revision", "revisión"),
    ("vacio", "vacío"),
    ("numero", "número"),
    ("En que se diferencia", "En qué se diferencia"),
    ("cuando se ve", "cuándo se ve"),
    ("y que no prometemos", "y qué no prometemos"),
    ("y como lo buscan", "y cómo lo buscan"),
    ("y que se siente", "y qué se siente"),
    ("Para quien si y", "Para quién sí y"),
    ("cual es para ti", "cuál es para ti"),
    ("quien las revisa", "quién las revisa"),
    ("Fotografia", "Fotografía"),
    ("fotografia", "fotografía"),
    ("Fotoproteccion", "Fotoprotección"),
    ("identico", "idéntico"),
    ("heuristica", "heurística"),
    ("tematica", "temática"),
    ("que si puedes", "que sí puedes"),
    ("que si pasan", "que sí pasan"),
]

# "Como " at start of H2 is good; mid-sentence "como funciona" in titles:
TITLE_FIXES = [
    (": que es", ": qué es"),
    (", como funciona", ", cómo funciona"),
    (" que es,", " qué es,"),
    (" como se ", " cómo se "),
    (" para quien ", " para quién "),
    (" sin cirugia", " sin cirugía"),
    (" sin milagros", " sin milagros"),
]

URL_STASH = [
    re.compile(r'href="[^"]*"'),
    re.compile(r"href='[^']*'"),
    re.compile(r'src="[^"]*"'),
    re.compile(r'content="https://[^"]*"'),
    re.compile(r'"https://[^"]*"'),
    re.compile(r"'https://[^']*'"),
    re.compile(r'"/[a-z0-9][a-z0-9_./-]*"'),
    re.compile(r"'/[a-z0-9][a-z0-9_./-]*'"),
    re.compile(r"/evaluacion\b"),
    re.compile(r"/clinica-facial-[a-z-]+"),
    re.compile(r"f\{ORIGIN\}/[a-z0-9_./-]+"),
]


def _stash_urls(text: str) -> tuple[str, list[str]]:
    held: list[str] = []

    def save(m: re.Match) -> str:
        held.append(m.group(0))
        return f"\x00U{len(held) - 1}\x00"

    for pat in URL_STASH:
        text = pat.sub(save, text)
    return text, held


def _unstash(text: str, held: list[str]) -> str:
    for i, chunk in enumerate(held):
        text = text.replace(f"\x00U{i}\x00", chunk)
    return text


def invert_question(s: str) -> str:
    if "?" not in s or "¿" in s:
        return s
    return re.sub(r"^(\s*)", r"\1¿", s, count=1)


def _word_swap(text: str, src: str, dst: str) -> str:
    if any(ch.isspace() for ch in src) or src.endswith(".") or src.endswith(","):
        return text.replace(src, dst)
    bound = r"(?<![A-Za-zÁÉÍÓÚÜáéíóúüÑñ])" + re.escape(src) + r"(?![A-Za-zÁÉÍÓÚÜáéíóúüÑñ])"
    return re.sub(bound, dst, text)


def polish_text(text: str) -> str:
    text, held = _stash_urls(text)
    for a, b in EXACT:
        text = text.replace(a, b)
    for a, b in WORDS:
        text = _word_swap(text, a, b)
    for a, b in TITLE_FIXES:
        text = text.replace(a, b)
    text = _unstash(text, held)
    return text


def invert_markup(html: str) -> str:
    def wrap(m: re.Match) -> str:
        return m.group(1) + invert_question(m.group(2)) + m.group(3)

    for tag in ("h1", "h2", "button"):
        html = re.sub(rf"(<{tag}\b[^>]*>)(.*?)(</{tag}>)", wrap, html, flags=re.S)

    def json_name(m: re.Match) -> str:
        inner = m.group(2)
        if inner.endswith("?") and not inner.startswith("¿"):
            inner = "¿" + inner
        return m.group(1) + inner + m.group(3)

    html = re.sub(r'("name": ")([^"]+\?)(")', json_name, html)
    return html


def polish_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = invert_markup(polish_text(original)) if path.suffix == ".html" else polish_text(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


AEO_DIRS = [
    "lifting-facial-coreano",
    "endojiwoo",
    "endolaser-facial",
    "hifu-facial",
    "radiofrecuencia-facial",
    "endolaser-vs-hifu",
    "lifting-coreano-vs-hilos-tensores",
    "endojiwoo-vs-bioestimuladores-inyectables",
    "lifting-sin-cirugia-vs-lifting-quirurgico",
    "ojeras-tratamiento-sin-cirugia",
    "manchas-faciales-despigmentacion",
    "flacidez-facial",
    "papada-sin-cirugia",
    "seguridad-contraindicaciones",
    "clinica-facial-vitacura",
    "clinica-facial-concon",
    "clinica-facial-los-angeles",
    "equipo",
    "opiniones",
    "preguntas-frecuentes",
    "glosario",
    "blog",
    "blog/lifting-facial-coreano-chile",
]


def main() -> None:
    n = 0
    for slug in AEO_DIRS:
        p = ROOT / slug / "index.html"
        if p.exists() and polish_file(p):
            n += 1
            print("html", p.relative_to(ROOT))
    extra = [ROOT / "404.html"]
    for p in extra:
        if p.exists() and polish_file(p):
            n += 1
            print("html", p.relative_to(ROOT))
    for p in (ROOT / "scripts").glob("aeo_*.py"):
        if p.name == "aeo_es.py":
            continue
        if polish_file(p):
            n += 1
            print("py", p.name)
    print("changed", n)


if __name__ == "__main__":
    main()
