"""Page bodies as plain sections (no raw HTML tags in source strings)."""
from __future__ import annotations

ORIGIN = "https://www.protocololumina.cl"
COMMON_CONTRA = (
    "Embarazo, lactancia, infeccion activa en la zona, heridas abiertas, "
    "enfermedades del tejido conectivo no controladas, marcapasos cuando hay radiofrecuencia, "
    "expectativa de resultado quirurgico inmediato. Se confirma en Evaluacion P3."
)
PREP = (
    "Evaluacion facial P3 presencial (45 minutos). Fotografia clinica. "
    "Retirar maquillaje. Informar farmacos, herpes, rellenos o toxina previos."
)
FOLLOW = (
    "Fotoproteccion diaria, higiene suave, control clinico segun el plan. "
    "No se indica un protocolo identico a todas las pieles."
)


def h2(title: str) -> str:
    return f"<h2>{title}</h2>"


def p(text: str) -> str:
    return f"<p>{text}</p>"


def ul(items: list[str]) -> str:
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"<ul>{lis}</ul>"


def ol(items: list[str]) -> str:
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"<ol>{lis}</ol>"


def body(parts: list[str]) -> str:
    return "\n".join(parts)


def proc(path, pretty, alts, desc, how, prep, follow, contra):
    return {
        "@type": "MedicalProcedure",
        "@id": f"{ORIGIN}{path}#procedure",
        "url": ORIGIN + path,
        "name": pretty,
        "alternateName": alts,
        "description": desc,
        "bodyLocation": "Face",
        "procedureType": "https://schema.org/NoninvasiveProcedure",
        "howPerformed": how,
        "preparation": prep,
        "followup": follow,
        "contraindication": contra,
        "provider": {"@id": f"{ORIGIN}/#organization"},
    }


def faqs_tech(nombre: str) -> list[tuple[str, str]]:
    return [
        (
            f"Que es {nombre}?",
            f"{nombre} es una tecnologia de estetica facial no quirurgica que se usa dentro de Protocolo Lumina, "
            "una clinica chilena de rejuvenecimiento facial sin cirugia, con sedes en Vitacura, Concon y Los Angeles.",
        ),
        (
            f"Duele {nombre}?",
            "La molestia es variable. La mayoria describe calor, presion o pinchazos tolerables. "
            "EndoJiwoo usa anestesia local. Lo concreto se conversa en la Evaluacion P3.",
        ),
        (
            f"Cuantas sesiones de {nombre} necesito?",
            "Depende de flacidez, edad, fototipo y si se combina con otras de las 14 tecnologias. "
            "No vendemos sesiones sueltas: se indica un plan.",
        ),
        (
            f"Cuando se ven resultados de {nombre}?",
            "Hay cambios inmediatos de turgencia en varias tecnologias; el colageno nuevo se organiza en semanas a meses. "
            "HIFU y bioestimuladores se juzgan a 8-12 semanas.",
        ),
        (
            f"Cuanto cuesta {nombre} en Chile?",
            "Protocolo Lumina no cotiza tratamientos por adelantado. El valor se arma despues de la Evaluacion P3 "
            "($27.990, 45 minutos, descontable del plan). Agenda tu hora.",
        ),
        (f"Quien no puede hacerse {nombre}?", COMMON_CONTRA),
        (
            f"{nombre} reemplaza un lifting quirurgico?",
            "No. Es una alternativa no quirurgica para flacidez leve a moderada. "
            "La flacidez severa con exceso de piel sigue siendo territorio del cirujano.",
        ),
        (
            f"Donde se hace {nombre} en Chile?",
            "En las tres sedes de Protocolo Lumina: Vitacura, Concon y Los Angeles. "
            "Misma red que Metodo Hebe, telefono +56 9 6322 2683.",
        ),
        (
            "Hay downtime?",
            "HIFU y radiofrecuencia: vuelves a tu dia. EndoJiwoo: 3 a 7 dias de inflamacion segun zona. "
            "Peelings: descamacion 3 a 7 dias.",
        ),
        (
            "Se combina con otras tecnologias?",
            "Si. El protocolo combina 14 tecnologias coreanas porque el envejecimiento ataca en paralelo "
            "(flacidez, mancha, textura, volumen).",
        ),
    ]


def get_pages() -> list[dict]:
    from aeo_pages_all import PAGES

    return PAGES
