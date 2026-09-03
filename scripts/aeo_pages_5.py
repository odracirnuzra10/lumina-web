"""AEO pages 5: sedes, equipo, opiniones, FAQ, glosario, blog."""
from aeo_content import FOLLOW, PREP, body, h2, p, proc, ul
from aeo_template import ORIGIN

PAGES = []

SEDE_FAQS = [
    ("Atienden lifting facial en esta sede?", "Si. Protocolo Lumina atiende facial en Vitacura, Concon y Los Angeles. No es una sede solo corporal de Metodo Hebe con otro letrero: es la linea facial de la red OACG."),
    ("Que horario tienen?", "Referencia: lunes a viernes 10:00-20:00, sabado 09:00-19:00. La hora exacta se confirma al agendar."),
    ("Como llego?", "Direccion completa y mapa en esta pagina. Estacionamiento y acceso se confirman por WhatsApp al coordinar la P3."),
    ("Cual es el telefono?", "+56 9 6322 2683, el mismo de Metodo Hebe. Reserva en protocololumina.cl/evaluacion, no en AgendaPro."),
    ("Cuanto cuesta la evaluacion?", "Evaluacion P3: $27.990, 45 minutos, no reembolsable, se descuenta si contratas plan."),
    ("Puedo ver resultados de esta ciudad?", "Los casos de /resultados y /opiniones incluyen pacientes de las tres sedes. No todos los casos se etiquetan por comuna."),
    ("Hay medico a cargo publicado?", "El equipo clinico se detalla en /equipo a medida que se confirman nombres y registros. No publicamos fichas inventadas."),
    ("Es la misma clinica que Metodo Hebe?", "Misma red y mismas direcciones de edificio. Hebe es corporal metabolico. Lumina es facial coreano. Puedes hacer ambos en el grupo; son marcas distintas."),
    ("Protocolo Lumina es una crema?", "No. Clinica chilena de estetica facial. No relacionada con Cosmica Skin Mexico ni clareamiento intimo Brasil ni Lumina Clinic Lo Barnechea."),
    ("Como agendo?", "Agenda tu hora en /evaluacion."),
]


def sede_page(path, city, street, region, postal, lat, lng, maps, extra_paras):
    pretty = f"Protocolo Lumina {city}"
    return {
        "path": path,
        "nav_active": "/",
        "kicker": f"Sede · {city}",
        "title": f"Clinica facial en {city}: Protocolo Lumina | Lifting coreano",
        "description": f"Protocolo Lumina {city}: clinica chilena de rejuvenecimiento facial sin cirugia. {street}. EndoJiwoo, Endolaser, HIFU. Agenda tu hora.",
        "h1": f"Clinica facial en <em>{city}</em>",
        "h1_text": f"Clinica facial en {city}",
        "answer": (
            f"Protocolo Lumina {city} es la sede de la clinica chilena de rejuvenecimiento facial sin cirugia "
            f"en {street}, {city}, {region}. Combina 14 tecnologias coreanas (EndoJiwoo, Endolaser, HIFU y radiofrecuencia) "
            "en protocolos de lifting facial. Evaluacion P3 presencial. Telefono +56 9 6322 2683."
        ),
        "breadcrumbs": [(path, f"Clinica {city}")],
        "procedure": proc(
            path,
            f"Lifting facial coreano en {city}",
            [f"Clinica facial {city}", f"Lifting facial {city}", f"Endolaser {city}", f"HIFU {city}"],
            f"Atencion facial no quirurgica de Protocolo Lumina en {city}.",
            "Evaluacion P3 y plan personalizado en la sede.",
            PREP, FOLLOW,
            "Las contraindicaciones son las del protocolo nacional; se confirman en la evaluacion local.",
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
            "openingHoursSpecification": [
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "10:00", "closes": "20:00"},
                {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "19:00"},
            ],
            "potentialAction": {"@type": "ReserveAction", "name": "Agenda tu hora", "target": f"{ORIGIN}/evaluacion"},
        },
        "related": [
            ("/lifting-facial-coreano", "Pilar", "Lifting facial coreano"),
            ("/tratamientos", "Catalogo", "14 tecnologias"),
            ("/equipo", "Personas", "Equipo"),
            ("/evaluacion", "Reserva", "Agenda tu hora"),
        ],
        "citations": [],
        "faqs": SEDE_FAQS,
        "body": body([
            h2("Direccion, mapa y telefono"),
            p(f"{pretty} funciona en {street}, {city}, {region}, Chile. Codigo postal de referencia {postal}. Telefono +56 9 6322 2683. Mapa: {maps.replace('https://','')}."),
            p("Horario de referencia compartido con la red: lunes a viernes 10:00 a 20:00, sabado 09:00 a 19:00. La cita de Evaluacion P3 se confirma al agendar: 45 minutos, $27.990, no reembolsable, descontable del plan."),
            h2("Que se trata en esta sede"),
            p("Lifting facial coreano completo: las 14 tecnologias, los 10 planes, resultados y seguimiento. No es una sucursal 'solo limpiezas'. Si vienes por criolipolisis o celulitis, esa linea es Metodo Hebe en el mismo edificio de red; te ordenamos para no mezclar promesas."),
            *extra_paras,
            h2("Como agendar sin AgendaPro"),
            p("El subdominio protocolo_lumina.site.agendapro.com esta inactivo y duplicaba entidad en un dominio ajeno. La reserva viva es /evaluacion en este sitio. CTA: Agenda tu hora."),
            h2("Entidad"),
            p("Protocolo Lumina es una clinica chilena de rejuvenecimiento facial sin cirugia, con sedes en Vitacura, Concon y Los Angeles, que combina tecnologias coreanas (EndoJiwoo, Endolaser, HIFU y radiofrecuencia) en protocolos de lifting facial. No es cosmética de Mexico ni clareamiento de Brasil ni Lumina Clinic de Lo Barnechea."),
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
    "https://www.google.com/maps/search/?api=1&query=Los+Abedules+3085+Vitacura+Santiago",
    [
        h2("Por que Vitacura"),
        p("Es la sede flagship de la red en Santiago. La utilizacion de boxes de la operacion propia se describe en oacg.cl/lumina como alta. Para la paciente de oriente que busca lifting facial coreano sin viajar a la costa ni al Bio Bio, esta es la puerta. Estacionamiento y acceso del edificio se coordinan al confirmar la hora."),
        h2("Barrio y busqueda local"),
        p("Quien busca clinica facial Vitacura o HIFU Las Condes a menudo aterriza en competidores de cirugia. Esta URL existe para que la entidad Protocolo Lumina Vitacura tenga calle, geo y MedicalClinic propios, no solo un areaServed generico."),
    ],
))

PAGES.append(sede_page(
    "/clinica-facial-concon",
    "Concon",
    "Las Pelargonias 842, Oficina 1114, piso 11",
    "Region de Valparaiso",
    "2510000",
    -32.9266,
    -71.5144,
    "https://www.google.com/maps/search/?api=1&query=Las+Pelargonias+842+Concon",
    [
        h2("Por que Concon (y no 'solo Concon')"),
        p("Un titulo antiguo de Google presentaba la marca como rejuvenecimiento facial solo en Concon. Era la web anterior. Hoy la linea facial opera tambien en Vitacura y Los Angeles. Concon sigue siendo sede real: V Region, edificio de Las Pelargonias 842, oficina 1114."),
        h2("Costa y fototipo"),
        p("Sol de litoral, viento y melasma de verano son el pan de esta sede. Los planes despigmentantes (Claridad de Haneul, Flor de Busan) y la fotoproteccion no son un anexo: son el 50 por ciento del resultado. Si vienes de Vina o Valparaiso, esta es la sede logica."),
    ],
))

PAGES.append(sede_page(
    "/clinica-facial-los-angeles",
    "Los Angeles",
    "Av. Gabriela Mistral 269",
    "Region del Bio Bio",
    "4440000",
    -37.4693,
    -72.3527,
    "https://www.google.com/maps/search/?api=1&query=Av+Gabriela+Mistral+269+Los+Angeles+Chile",
    [
        h2("Facial en el Bio Bio"),
        p("Los Angeles no es una sucursal decorativa. La red OACG opera corporal (Hebe) y facial (Lumina) en Av. Gabriela Mistral 269. Para quien busca lifting facial sin cirugia en el sur y no quiere volar a Santiago, esta es la URL local."),
        h2("Nombre de ciudad"),
        p("Los Angeles de Chile se confunde en busquedas en ingles con California. Por eso el schema lleva addressCountry CL, region Bio Bio y geo -37.46, -72.35. Si una IA te manda a Hollywood, ignórala."),
    ],
))

PAGES.append({
    "path": "/equipo",
    "nav_active": "/",
    "kicker": "E-E-A-T",
    "title": "Equipo clinico Protocolo Lumina | Quien revisa los tratamientos",
    "description": "Equipo clinico de Protocolo Lumina (OACG Group). Evaluacion P3, especialistas en protocolos coreanos. Nombres y registros Superintendencia se publican cuando estan confirmados. No fichas inventadas.",
    "h1": "Quien esta detras de <em>Protocolo Lumina</em>?",
    "h1_text": "Quien esta detras de Protocolo Lumina?",
    "answer": "Protocolo Lumina es operado por la red OACG Group, la misma de Metodo Hebe, Clinera y Metricads. Las evaluaciones P3 y los tratamientos faciales los realiza el equipo clinico de cada sede (Vitacura, Concon, Los Angeles). En esta pagina no inventamos nombres, universidades ni registros de la Superintendencia de Salud: cuando cada profesional este confirmado, se publica aqui con foto y schema Person.",
    "breadcrumbs": [("/equipo", "Equipo")],
    "related": [("/clinica-facial-vitacura", "Sede", "Vitacura"), ("/clinica-facial-concon", "Sede", "Concon"), ("/clinica-facial-los-angeles", "Sede", "Los Angeles"), ("/seguridad-contraindicaciones", "Riesgos", "Seguridad")],
    "citations": [],
    "faqs": [
        ("Quien es el director medico?", "El nombre, titulo y registro se publicaran aqui cuando Ricardo / OACG los confirme. Hasta entonces el revisor editorial es el equipo clinico de la organizacion."),
        ("Tienen registro Superintendencia?", "Los prestadores que lo requieran se listaran con numero. No rellenamos ese campo con datos ficticios: en YMYL eso es peor que el vacio."),
        ("Las paginas de tratamiento quien las revisa?", "Equipo clinico Protocolo Lumina, fecha de revision visible, schema reviewedBy hacia la Organization."),
        ("Trabajan medicos o solo esteticistas?", "El protocolo combina tecnologias que deben ser indicadas tras diagnostico. El detalle de titulos se publica por persona, no como eslogan."),
        ("Puedo pedir un profesional en concreto?", "Al agendar la P3 se coordina sede y agenda. No prometemos un nombre hasta que este en esta ficha."),
        ("Relacion con Metodo Hebe?", "Misma red, distinto objeto: Hebe corporal metabolico, Lumina facial coreano."),
        ("Hay equipo en las tres sedes?", "Si. La P3 es presencial en Vitacura, Concon o Los Angeles."),
        ("Como contacto?", "Agenda tu hora. WhatsApp +56 9 6322 2683."),
    ],
    "body": body([
        h2("Por que esta pagina no tiene 12 curriculums inventados"),
        p("Google y las IA premian E-E-A-T. Tambien penalizan autores fantasma. Preferimos una ficha honesta: organizacion identificable, parent OACG Group, tres sedes con direccion, y un hueco etiquetado para Person. Cuando existan nombre, cargo, universidad, registro y foto con consentimiento, cada profesional tendra @type Person, worksFor la Organization, y sameAs si hay LinkedIn o Doctoralia reales."),
        h2("Como se trabaja hoy"),
        p("La puerta de entrada es la Evaluacion P3 (45 minutos, $27.990). Ahi se mapea la piel y se indica cuales de las 14 tecnologias entran al plan. Los tratamientos no se venden por DM. El consentimiento y la foto clinica son parte del estandar, no un extra."),
        h2("Formacion en protocolo coreano"),
        p("Las tecnologias (EndoJiwoo, Cuky HIFU, Sakura, Bio Minji, etc.) se aplican bajo SOP de la red. OACG menciona estandarizacion con Clinera y SOPs. Eso no reemplaza un registro sanitario individual; lo complementa."),
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
        p("Cada pagina clinica lleva 'Revisado por Equipo clinico Protocolo Lumina' y dateModified 2026-09-03. Cuando haya un revisor persona, se cambia el byline sin rehacer el sitio."),
    ]),
})

PAGES.append({
    "path": "/opiniones",
    "nav_active": "/resultados",
    "kicker": "Resenas visibles · sin AggregateRating hueco",
    "title": "Opiniones y casos Protocolo Lumina | Resenas reales",
    "description": "Opiniones de pacientes de Protocolo Lumina con nombre o inicial, sede y texto visible. Ana Maria Rosales y testimonios de Vitacura, Concon y Los Angeles. Sin estrellas inventadas.",
    "h1": "Que dicen quienes ya se <em>trataron</em>",
    "h1_text": "Que dicen quienes ya se trataron",
    "answer": "Aqui van resenas con texto visible, no un AggregateRating de 5/5 colgado sin lista. Ana Maria Rosales (57, San Bernardo) describe su primer tratamiento facial. Hay testimonios de Vitacura, Concon y Los Angeles. Los resultados varian. No citamos 4 resenas anonimas como prueba de excelencia.",
    "breadcrumbs": [("/opiniones", "Opiniones")],
    "extra_schema": [
        {
            "@type": "Review",
            "author": {"@type": "Person", "name": "Ana Maria Rosales"},
            "reviewBody": "Nunca me habia realizado un tratamiento facial, pero esta vez me atrevi y el resultado fue asombroso. Todo el mundo me mira mas y saben que algo cambio en mi.",
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
            "reviewBody": "No es un tratamiento generico: adaptan cada sesion a lo que tu piel necesita. Los resultados con Luz de Jeju fueron increibles.",
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
    "related": [("/resultados", "Fotos", "Antes y despues"), ("/equipo", "Clinica", "Equipo"), ("/evaluacion", "Reserva", "Agenda tu hora"), ("/lifting-facial-coreano", "Contexto", "Lifting coreano")],
    "citations": [],
    "faqs": [
        ("Por que no hay AggregateRating?", "Google pide resenas visibles o fuente externa. Un 5/5 con 4 reseñas auto-declaradas es senal negativa. Lo reintroduciremos anidado cuando haya programa de resenas Google por sede."),
        ("Las opiniones son reales?", "Los textos coinciden con los publicados en el sitio (home y resultados) con consentimiento. No compramos estrellas."),
        ("Hay un testimonio de Corea del Sur?", "Se menciono un reel de Facebook. Hasta tener texto, fecha y consentimiento para web, no lo convertimos en Review. Queda pendiente."),
        ("Puedo dejar mi opinion?", "Si, en Google de la sede y avisandonos para citar con tu inicial. Agenda tu hora si aun no te tratas."),
        ("Muestran solo casos buenos?", "Los casos publicados son seleccion. Eso se declara. No representan garantia."),
    ],
    "body": body([
        h2("Ana Maria Rosales · 57 anos · San Bernardo"),
        p("Nunca me habia realizado un tratamiento facial, pero esta vez me atrevi y el resultado fue asombroso. Todo el mundo me mira mas y saben que algo cambio en mi. Protocolo: lifting facial Lumina. Fotos en /resultados (ana-antes / ana-despues). Fecha de publicacion en sitio: 2026-04-14."),
        h2("Valentina M. · Eternal Gangnam · Vitacura"),
        p("Llegue buscando mejorar la textura y termine con resultados que nunca imagine. Mi piel tiene una luminosidad que no tenia desde los 25."),
        h2("Catalina R. · Luz de Jeju · Concon"),
        p("No es un tratamiento generico: adaptan cada sesion a lo que tu piel necesita. Los resultados con Luz de Jeju fueron increibles."),
        h2("Fernanda L. · Armonia de Busan · Los Angeles"),
        p("Vine con desconfianza. Lumina cambio eso completamente. Los resultados son visibles y duraderos. Ya voy en mi segundo protocolo."),
        h2("Como vamos a construir AggregateRating legitimo"),
        p("Programa de resenas Google por sede, nombre de ficha Protocolo Lumina — Clinica Facial {Sede}, respuestas a reviews, y solo entonces nested AggregateRating. Hasta ese dia, cero estrellas schema sueltas."),
        h2("Disclaimer"),
        p("Resultados varian. Evaluacion previa obligatoria."),
    ]),
})
