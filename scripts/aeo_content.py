"""Page bodies as plain sections (no raw HTML tags in source strings)."""
from __future__ import annotations

ORIGIN = "https://www.protocololumina.cl"
COMMON_CONTRA = (
    "Embarazo, lactancia, infección activa en la zona, heridas abiertas, "
    "enfermedades del tejido conectivo no controladas, marcapasos cuando hay radiofrecuencia, "
    "expectativa de resultado quirúrgico inmediato. Se confirma en Evaluación P3."
)
PREP = (
    "Evaluación facial P3 presencial (45 minutos). Fotografía clínica. "
    "Retirar maquillaje. Informar fármacos, herpes, rellenos o toxina previos."
)
FOLLOW = (
    "Fotoprotección diaria, higiene suave, control clínico según el plan. "
    "No se indica un protocolo idéntico a todas las pieles."
)


def h2(title: str) -> str:
    from aeo_es import invert_question, polish_text

    title = invert_question(polish_text(title))
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
            f"Qué es {nombre}?",
            f"{nombre} es una tecnología de estética facial no quirúrgica que se usa dentro de Protocolo Lumina, "
            "una clínica chilena de rejuvenecimiento facial sin cirugía, con sedes en Vitacura, Concón y Los Ángeles.",
        ),
        (
            f"Duele {nombre}?",
            "La molestia es variable. La mayoria describe calor, presion o pinchazos tolerables. "
            "EndoJiwoo usa anestesia local. Lo concreto se conversa en la Evaluación P3.",
        ),
        (
            f"Cuántas sesiones de {nombre} necesito?",
            "Depende de flacidez, edad, fototipo y si se combina con otras de las 14 tecnologías. "
            "No vendemos sesiones sueltas: se indica un plan.",
        ),
        (
            f"Cuándo se ven resultados de {nombre}?",
            "Hay cambios inmediatos de turgencia en varias tecnologías; el colágeno nuevo se organiza en semanas a meses. "
            "HIFU y bioestimuladores se juzgan a 8-12 semanas.",
        ),
        (
            f"Cuánto cuesta {nombre} en Chile?",
            "Protocolo Lumina no cotiza tratamientos por adelantado. El valor se arma después de la Evaluación P3 "
            "($27.990, 45 minutos, descontable del plan). Agenda tu hora.",
        ),
        (f"Quién no puede hacerse {nombre}?", COMMON_CONTRA),
        (
            f"{nombre} reemplaza un lifting quirúrgico?",
            "No. Es una alternativa no quirúrgica para flacidez leve a moderada. "
            "La flacidez severa con exceso de piel sigue siendo territorio del cirujano.",
        ),
        (
            f"Dónde se hace {nombre} en Chile?",
            "En las tres sedes de Protocolo Lumina: Vitacura, Concón y Los Ángeles. "
            "Misma red que Método Hebe, teléfono +56 9 6322 2683.",
        ),
        (
            "Hay downtime?",
            "HIFU y radiofrecuencia: vuelves a tu día. EndoJiwoo: 3 a 7 días de inflamación según zona. "
            "Peelings: descamación 3 a 7 días.",
        ),
        (
            "Se combina con otras tecnologías?",
            "Sí. El protocolo combina 14 tecnologías coreanas porque el envejecimiento ataca en paralelo "
            "(flacidez, mancha, textura, volumen).",
        ),
    ]


def get_pages() -> list[dict]:
    from aeo_pages_all import PAGES

    return PAGES
