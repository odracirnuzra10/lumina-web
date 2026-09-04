"""AEO pages 5: sedes, equipo, opiniones, FAQ, glosario, blog."""
from aeo_content import FOLLOW, PREP, body, h2, p, proc, ul
from aeo_template import ORIGIN

PAGES = []

SEDE_FAQS = [
    ("Atienden lifting facial en esta sede?", "Sí. Protocolo Lumina atiende facial en Vitacura, Concón y Los Ángeles. No es una sede solo corporal de Método Hebe con otro letrero: es la línea facial de la red OACG."),
    ("Qué horario tienen?", "Referencia: lunes a viernes 10:00-20:00, sábado 09:00-19:00. La hora exacta se confirma al agendar."),
    ("Cómo llego?", "Direccion completa y mapa en esta página. Estacionamiento y acceso se confirman por WhatsApp al coordinar la P3."),
    ("Cuál es el teléfono?", "+56 9 6322 2683, el mismo de Método Hebe. Reserva en protocololumina.cl/evaluacion, no en AgendaPro."),
    ("Cuánto cuesta la evaluación?", "Evaluación P3: $27.990, 45 minutos, no reembolsable, se descuenta si contratas plan."),
    ("Puedo ver resultados de esta ciudad?", "Los casos de /resultados y /opiniones incluyen pacientes de las tres sedes. No todos los casos se etiquetan por comuna."),
    ("Hay médico a cargo publicado?", "El equipo clínico se detalla en /equipo a medida que se confirman nombres y registros. No publicamos fichas inventadas."),
    ("Es la misma clínica que Método Hebe?", "Misma red y mismas direcciones de edificio. Hebe es corporal metabolico. Lumina es facial coreano. Puedes hacer ambos en el grupo; son marcas distintas."),
    ("Protocolo Lumina es una crema?", "No. Clínica chilena de estética facial. No relacionada con Cosmica Skin México ni clareamiento intimo Brasil ni Lumina Clinic Lo Barnechea."),
    ("Cómo agendo?", "Agenda tu hora en /evaluacion."),
]


def sede_page(path, city, street, region, postal, lat, lng, maps, extra_paras):
    pretty = f"Protocolo Lumina {city}"
    return {
        "path": path,
        "nav_active": "/",
        "kicker": f"Sede · {city}",
        "title": f"Clínica facial en {city}: Protocolo Lumina | Lifting coreano",
        "description": f"Protocolo Lumina {city}: clínica chilena de rejuvenecimiento facial sin cirugía. {street}. EndoJiwoo, Endolaser, HIFU. Agenda tu hora.",
        "h1": f"Clínica facial en <em>{city}</em>",
        "h1_text": f"Clínica facial en {city}",
        "answer": (
            f"Protocolo Lumina {city} es la sede de la clínica chilena de rejuvenecimiento facial sin cirugía "
            f"en {street}, {city}, {region}. Combina 14 tecnologías coreanas (EndoJiwoo, Endolaser, HIFU y radiofrecuencia) "
            "en protocolos de lifting facial. Evaluación P3 presencial. Teléfono +56 9 6322 2683."
        ),
        "breadcrumbs": [(path, f"Clínica {city}")],
        "procedure": proc(
            path,
            f"Lifting facial coreano en {city}",
            [f"Clínica facial {city}", f"Lifting facial {city}", f"Endolaser {city}", f"HIFU {city}"],
            f"Atencion facial no quirúrgica de Protocolo Lumina en {city}.",
            "Evaluación P3 y plan personalizado en la sede.",
            PREP, FOLLOW,
            "Las contraindicaciones son las del protocolo nacional; se confirman en la evaluación local.",
        ),
        "extra_schema": {
            "@type": "MedicalClinic",
            "@id": f"{ORIGIN}/{path.strip('/')}#local",
            "name": pretty,
            "url": ORIGIN + path,
            "parentOrganization": {"@id": f"{ORIGIN}/#organization"},
            "telephone": "+56963222683",
            "image": f"{ORIGIN}/img/hero-endojiwoo.webp",
            "priceRange": "$$$",
            "medicalSpecialty": "Dermatology",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": street,
                "addressLocality": city,
                "addressRegion": region,
                "postalCode": postal,
                "addressCountry": "CL",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng},
            "hasMap": maps,
            "sameAs": [maps],
            "openingHoursSpecification": [
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "10:00", "closes": "20:00"},
                {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "19:00"},
            ],
            "potentialAction": {"@type": "ReserveAction", "name": "Agenda tu hora", "target": f"{ORIGIN}/evaluacion"},
        },
        "related": [
            ("/lifting-facial-coreano", "Pilar", "Lifting facial coreano"),
            ("/tratamientos", "Catálogo", "14 tecnologías"),
            ("/equipo", "Personas", "Equipo"),
            ("/evaluacion", "Reserva", "Agenda tu hora"),
        ],
        "citations": [],
        "faqs": SEDE_FAQS,
        "body": body([
            h2("Direccion, mapa y teléfono"),
            p(f"{pretty} funciona en {street}, {city}, {region}, Chile. Codigo postal de referencia {postal}. Teléfono +56 9 6322 2683. Mapa: {maps.replace('https://','')}."),
            p("Horario de referencia compartido con la red: lunes a viernes 10:00 a 20:00, sábado 09:00 a 19:00. La cita de Evaluación P3 se confirma al agendar: 45 minutos, $27.990, no reembolsable, descontable del plan."),
            h2("Que se trata en esta sede"),
            p("Lifting facial coreano completo: las 14 tecnologías, los 10 planes, resultados y seguimiento. No es una sucursal 'solo limpiezas'. Si vienes por criolipolisis o celulitis, esa línea es Método Hebe en el mismo edificio de red; te ordenamos para no mezclar promesas."),
            *extra_paras,
            h2("Cómo agendar sin AgendaPro"),
            p("El subdominio protocolo_lumina.site.agendapro.com está inactivo y duplicaba entidad en un dominio ajeno. La reserva viva es /evaluacion en este sitio. CTA: Agenda tu hora."),
            h2("Entidad"),
            p("Protocolo Lumina es una clínica chilena de rejuvenecimiento facial sin cirugía, con sedes en Vitacura, Concón y Los Ángeles, que combina tecnologías coreanas (EndoJiwoo, Endolaser, HIFU y radiofrecuencia) en protocolos de lifting facial. No es cosmética de México ni clareamiento de Brasil ni Lumina Clinic de Lo Barnechea."),
        ]),
    }


PAGES.append(sede_page(
    "/clinica-facial-vitacura",
    "Vitacura",
    "Los Abedules 3085, Of. 105, Edificio Nueva Vitacura",
    "Region Metropolitana",
    "7630573",
    -33.3936,
    -70.5831,
    "https://share.google/uKeMlkibRy1TPB7vK",
    [
        h2("Por qué Vitacura"),
        p("Es la sede flagship de la red en Santiago. La utilizacion de boxes de la operacion propia se describe en oacg.cl/lumina como alta. Para la paciente de oriente que busca lifting facial coreano sin viajar a la costa ni al Bio Bio, esta es la puerta. Estacionamiento y acceso del edificio se coordinan al confirmar la hora."),
        h2("Barrio y búsqueda local"),
        p("Quién busca clínica facial Vitacura o HIFU Las Condes a menudo aterriza en competidores de cirugía. Esta URL existe para que la entidad Protocolo Lumina Vitacura tenga calle, geo y MedicalClinic propios, no solo un areaServed generico."),
    ],
))

PAGES.append(sede_page(
    "/clinica-facial-concon",
    "Concón",
    "Las Pelargonias 842, Oficina 1114, piso 11",
    "Region de Valparaiso",
    "2510000",
    -32.9266,
    -71.5144,
    "https://share.google/CeMMtlyCmwN5K3yxP",
    [
        h2("Por qué Concón (y no 'solo Concón')"),
        p("Un título antiguo de Google presentaba la marca como rejuvenecimiento facial solo en Concón. Era la web anterior. Hoy la línea facial opera también en Vitacura y Los Ángeles. Concón sigue siendo sede real: V Region, edificio de Las Pelargonias 842, oficina 1114."),
        h2("Costa y fototipo"),
        p("Sol de litoral, viento y melasma de verano son el pan de esta sede. Los planes despigmentantes (Claridad de Haneul, Flor de Busan) y la fotoprotección no son un anexo: son el 50 por ciento del resultado. Si vienes de Vina o Valparaiso, esta es la sede logica."),
    ],
))

PAGES.append(sede_page(
    "/clinica-facial-los-angeles",
    "Los Ángeles",
    "Av. Gabriela Mistral 269",
    "Region del Bio Bio",
    "4440000",
    -37.4693,
    -72.3527,
    "https://share.google/GKckpVUP3cGC9XGLq",
    [
        h2("Facial en el Bio Bio"),
        p("Los Ángeles no es una sucursal decorativa. La red OACG opera corporal (Hebe) y facial (Lumina) en Av. Gabriela Mistral 269. Para quien busca lifting facial sin cirugía en el sur y no quiere volar a Santiago, esta es la URL local."),
        h2("Nombre de ciudad"),
        p("Los Ángeles de Chile se confunde en búsquedas en ingles con California. Por eso el schema lleva addressCountry CL, region Bio Bio y geo -37.46, -72.35. Si una IA te manda a Hollywood, ignórala."),
    ],
))

PAGES.append({
    "path": "/equipo",
    "nav_active": "/",
    "kicker": "E-E-A-T",
    "title": "Equipo clínico Protocolo Lumina | Quién revisa los tratamientos",
    "description": "Equipo clínico de Protocolo Lumina (OACG Group). Evaluación P3, especialistas en protocolos coreanos. Nombres y registros Superintendencia se publican cuando estan confirmados. No fichas inventadas.",
    "h1": "Quién está detrás de <em>Protocolo Lumina</em>?",
    "h1_text": "Quién está detrás de Protocolo Lumina?",
    "answer": "Protocolo Lumina es operado por la red OACG Group, la misma de Método Hebe, Clinera y Metricads. Las evaluaciones P3 y los tratamientos faciales los realiza el equipo clínico de cada sede (Vitacura, Concón, Los Ángeles). En esta página no inventamos nombres, universidades ni registros de la Superintendencia de Salud: cuando cada profesional este confirmado, se publica aquí con foto y schema Person.",
    "breadcrumbs": [("/equipo", "Equipo")],
    "related": [("/clinica-facial-vitacura", "Sede", "Vitacura"), ("/clinica-facial-concon", "Sede", "Concón"), ("/clinica-facial-los-angeles", "Sede", "Los Ángeles"), ("/seguridad-contraindicaciones", "Riesgos", "Seguridad")],
    "citations": [],
    "faqs": [
        ("Quién es el director médico?", "El nombre, título y registro se publicarán aquí cuando Ricardo / OACG los confirme. Hasta entonces el revisor editorial es el equipo clínico de la organización."),
        ("Tienen registro Superintendencia?", "Los prestadores que lo requieran se listarán con número. No rellenamos ese campo con datos ficticios: en YMYL eso es peor que el vacío."),
        ("Las páginas de tratamiento quién las revisa?", "Equipo clínico Protocolo Lumina, fecha de revisión visible, schema reviewedBy hacia la Organization."),
        ("Trabajan medicos o solo esteticistas?", "El protocolo combina tecnologías que deben ser indicadas tras diagnóstico. El detalle de titulos se publica por persona, no como eslogan."),
        ("Puedo pedir un profesional en concreto?", "Al agendar la P3 se coordina sede y agenda. No prometemos un nombre hasta que este en esta ficha."),
        ("Relación con Método Hebe?", "Misma red, distinto objeto: Hebe corporal metabolico, Lumina facial coreano."),
        ("Hay equipo en las tres sedes?", "Sí. La P3 es presencial en Vitacura, Concón o Los Ángeles."),
        ("Cómo contacto?", "Agenda tu hora. WhatsApp +56 9 6322 2683."),
    ],
    "body": body([
        h2("Por qué esta página no tiene 12 curriculums inventados"),
        p("Google y las IA premian E-E-A-T. Tambien penalizan autores fantasma. Preferimos una ficha honesta: organización identificable, parent OACG Group, tres sedes con direccion, y un hueco etiquetado para Person. Cuando existan nombre, cargo, universidad, registro y foto con consentimiento, cada profesional tendra @type Person, worksFor la Organization, y sameAs si hay LinkedIn o Doctoralia reales."),
        h2("Cómo se trabaja hoy"),
        p("La puerta de entrada es la Evaluación P3 (45 minutos, $27.990). Ahi se mapea la piel y se indica cuales de las 14 tecnologías entran al plan. Los tratamientos no se venden por DM. El consentimiento y la foto clínica son parte del estandar, no un extra."),
        h2("Formacion en protocolo coreano"),
        p("Las tecnologías (EndoJiwoo, Cuky HIFU, Sakura, Bio Minji, etc.) se aplican bajo SOP de la red. OACG menciona estandarizacion con Clinera y SOPs. Eso no reemplaza un registro sanitario individual; lo complementa."),
        h2("Plantilla lista para el primer Person"),
        ul([
            "Nombre y apellido.",
            "Titulo y especialidad.",
            "Universidad.",
            "Registro Superintendencia de Salud.",
            "Sede(s) donde atiende.",
            "Foto con alt.",
            "sameAs (Doctoralia, LinkedIn) solo si la URL es suya.",
        ]),
        h2("Revision de contenidos"),
        p("Cada página clínica lleva 'Revisado por Equipo clínico Protocolo Lumina' y dateModified 2026-09-03. Cuando haya un revisor persona, se cambia el byline sin rehacer el sitio."),
    ]),
})

PAGES.append({
    "path": "/opiniones",
    "nav_active": "/resultados",
    "kicker": "Resenas visibles · sin AggregateRating hueco",
    "title": "Opiniones y casos Protocolo Lumina | Resenas reales",
    "description": "Opiniones de pacientes de Protocolo Lumina con nombre o inicial, sede y texto visible. Ana María Rosales y testimonios de Vitacura, Concón y Los Ángeles. Sin estrellas inventadas.",
    "h1": "Qué dicen quienes ya se <em>trataron</em>",
    "h1_text": "Qué dicen quienes ya se trataron",
    "answer": "Aquí van reseñas con texto visible, no un AggregateRating de 5/5 colgado sin lista. Ana María Rosales (57, San Bernardo) describe su primer tratamiento facial. Hay testimonios de Vitacura, Concón y Los Ángeles. Los resultados varían. No citamos 4 reseñas anonimas como prueba de excelencia.",
    "breadcrumbs": [("/opiniones", "Opiniones")],
    "extra_schema": [
        {
            "@type": "Review",
            "author": {"@type": "Person", "name": "Ana María Rosales"},
            "reviewBody": "Nunca me había realizado un tratamiento facial, pero esta vez me atrevi y el resultado fue asombroso. Todo el mundo me mira mas y saben que algo cambio en mi.",
            "datePublished": "2026-04-14",
            "itemReviewed": {"@id": f"{ORIGIN}/#organization"},
        },
        {
            "@type": "Review",
            "author": {"@type": "Person", "name": "Valentina M."},
            "reviewBody": "Llegue buscando mejorar la textura y termine con resultados que nunca imagine. Mi piel tiene una luminosidad que no tenia desde los 25.",
            "datePublished": "2026-04-14",
            "itemReviewed": {"@id": f"{ORIGIN}/#organization"},
        },
        {
            "@type": "Review",
            "author": {"@type": "Person", "name": "Catalina R."},
            "reviewBody": "No es un tratamiento generico: adaptan cada sesión a lo que tu piel necesita. Los resultados con Luz de Jeju fueron increibles.",
            "datePublished": "2026-04-14",
            "itemReviewed": {"@id": f"{ORIGIN}/#organization"},
        },
        {
            "@type": "Review",
            "author": {"@type": "Person", "name": "Fernanda L."},
            "reviewBody": "Vine con desconfianza. Lumina cambio eso completamente. Los resultados son visibles y duraderos. Ya voy en mi segundo protocolo.",
            "datePublished": "2026-04-14",
            "itemReviewed": {"@id": f"{ORIGIN}/#organization"},
        },
    ],
    "related": [("/resultados", "Fotos", "Antes y después"), ("/equipo", "Clínica", "Equipo"), ("/evaluacion", "Reserva", "Agenda tu hora"), ("/lifting-facial-coreano", "Contexto", "Lifting coreano")],
    "citations": [],
    "faqs": [
        ("Por qué no hay AggregateRating?", "Google pide reseñas visibles o fuente externa. Un 5/5 con 4 reseñas auto-declaradas es señal negativa. Lo reintroduciremos anidado cuando haya programa de reseñas Google por sede."),
        ("Las opiniones son reales?", "Los textos coinciden con los publicados en el sitio (home y resultados) con consentimiento. No compramos estrellas."),
        ("Hay un testimonio de Corea del Sur?", "Se menciono un reel de Facebook. Hasta tener texto, fecha y consentimiento para web, no lo convertimos en Review. Queda pendiente."),
        ("Puedo dejar mi opinion?", "Si, en Google de la sede y avisandonos para citar con tu inicial. Agenda tu hora si aun no te tratas."),
        ("Muestran solo casos buenos?", "Los casos publicados son seleccion. Eso se declara. No representan garantia."),
    ],
    "body": body([
        h2("Ana María Rosales · 57 anos · San Bernardo"),
        p("Nunca me había realizado un tratamiento facial, pero esta vez me atrevi y el resultado fue asombroso. Todo el mundo me mira mas y saben que algo cambio en mi. Protocolo: lifting facial Lumina. Fotos en /resultados (ana-antes / ana-después). Fecha de publicacion en sitio: 2026-04-14."),
        h2("Valentina M. · Eternal Gangnam · Vitacura"),
        p("Llegue buscando mejorar la textura y termine con resultados que nunca imagine. Mi piel tiene una luminosidad que no tenia desde los 25."),
        h2("Catalina R. · Luz de Jeju · Concón"),
        p("No es un tratamiento generico: adaptan cada sesión a lo que tu piel necesita. Los resultados con Luz de Jeju fueron increibles."),
        h2("Fernanda L. · Armonia de Busan · Los Ángeles"),
        p("Vine con desconfianza. Lumina cambio eso completamente. Los resultados son visibles y duraderos. Ya voy en mi segundo protocolo."),
        h2("Cómo vamos a construir AggregateRating legítimo"),
        p("Programa de reseñas Google por sede, nombre de ficha Protocolo Lumina — Clínica Facial {Sede}, respuestas a reviews, y solo entonces nested AggregateRating. Hasta ese día, cero estrellas schema sueltas."),
        h2("Disclaimer"),
        p("Resultados varían. Evaluación previa obligatoria."),
    ]),
})
