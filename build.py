# -*- coding: utf-8 -*-
"""Genera el portafolio estático (HTML) de Nyxum para el curso INCAE 5098."""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
SITE_TITLE = "Portafolio de dashboards · Nyxum"
AUTHOR = "Luis Alfredo Leiva Artavia"
COURSE = "Digital Business Intelligence: gobernanza práctica con herramientas y dashboards · INCAE Business School · 2026"

NAV = [("index.html","Inicio"),("empresa.html","Nyxum y sus datos"),("pivote-1.html","1 Alineamiento"),("pivote-2.html","2 Cultura"),
       ("pivote-3.html","3 Cliente"),("pivote-4.html","4 Agilidad"),("pivote-5.html","5 Datos"),("pivote-6.html","6 Ecosistemas"),("final.html","Síntesis final")]

def page(fname, hero, body, scripts=""):
    nav = "".join(f'<a href="{h}"{" class=\"active\"" if h==fname else ""}>{t}</a>' for h,t in NAV)
    meta = "".join(f"<span><b>{k}</b> {v}</span>" for k,v in hero.get("meta",[]))
    doc = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(hero['title'])} · {SITE_TITLE}</title>
<meta name="description" content="{html.escape(hero.get('lead',''))}">
<link rel="stylesheet" href="style.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
</head><body>
<div class="topbar"><div class="in"><a class="logo" href="index.html">NYXUM <span>· portafolio de dashboards</span></a><nav>{nav}</nav></div></div>
<header class="hero"><div class="in"><div class="kicker">{hero['kicker']}</div><h1>{hero['title']}</h1><p class="lead">{hero.get('lead','')}</p><div class="meta">{meta}</div></div></header>
<main>
{body}
</main>
<footer><div class="in"><span>{AUTHOR} · {COURSE}</span><span>Datos simulados con fines académicos · <a href="https://www.nyx-um.com/">nyx-um.com</a></span></div></footer>
<script src="data.js"></script><script src="charts.js"></script>
<script>{scripts}</script>
</body></html>"""
    with open(os.path.join(OUT,fname),"w",encoding="utf-8") as f: f.write(doc)

def tiles(items):
    return '<div class="tiles">'+"".join(f'<div class="tile"><div class="v">{v}</div><div class="l">{l}</div>{f"<div class=\"d {c}\">{d}</div>" if d else ""}</div>' for v,l,d,c in items)+'</div>'

def chart(id_, title, sub):
    return f'<div class="chart"><h4>{title}</h4><p class="sub">{sub}</p><div class="cv"><canvas id="{id_}" role="img" aria-label="{html.escape(title)}"></canvas></div></div>'

def table(headers, rows, cls="kpi"):
    th="".join(f"<th>{h}</th>" for h in headers)
    tr="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

def qa(items):
    return '<div class="qa">'+"".join(f'<div class="card"><b>{q}</b>{a}</div>' for q,a in items)+'</div>'

def refs(items):
    return '<h2>Referencias</h2><ul class="refs">'+"".join(f"<li>{r}</li>" for r in items)+'</ul>'

def prevnext(prev, nxt):
    p = f'<a href="{prev[0]}">← {prev[1]}</a>' if prev else "<span></span>"
    n = f'<a href="{nxt[0]}">{nxt[1]} →</a>' if nxt else "<span></span>"
    return f'<div class="prev-next">{p}{n}</div>'

REF_BARAHONA = "Barahona, J. C. (2024). <i>El gobierno corporativo frente a la irrupción de la IA generativa</i>. Revista INCAE Business School."
REF_NYXUM = "Nyxum (2026). Sitio web corporativo. <a href=\"https://www.nyx-um.com/\">https://www.nyx-um.com/</a> (consultado el 8 de octubre de 2026)."
NOTA_SIM = '<div class="card note"><b>Nota sobre los datos.</b> Las cifras de los tableros son un <b>set de datos simulado</b>, generado para este curso a partir de la estructura real de la operación de Nyxum (frentes de servicio, fases de proyecto, canales comerciales). No representan resultados financieros ni comerciales reales de la empresa. Sirven para probar que los indicadores se pueden calcular, visualizar y leer; cuando los sistemas acumulen historia suficiente, el mismo tablero se conecta a las fuentes reales.</div>'

# ------------------------------------------------------------------ INDEX
body = f"""
<section>
<div class="grid c3">
 <div class="card"><h3>Qué es este portafolio</h3><p>Una colección de <b>propuestas de indicadores y prototipos de dashboards</b> para Nyxum, construida semana a semana a lo largo del curso. Cada página toma uno de los seis pivotes de la evolución digital (Barahona, 2024), responde qué vamos a medir, por qué, por qué de esa manera y qué impacto tendría la medición, y lo aterriza en un tablero navegable.</p></div>
 <div class="card"><h3>Por qué existe</h3><p>Nyxum es una firma fundada en 2026 que promete a sus clientes <i>procesos medibles y datos confiables</i>. Es razonable exigirnos lo mismo. Como socio responsable de tecnología, necesito un instrumento para <b>guiar, apoyar y supervisar</b> la evolución digital de la firma con datos, no con intuición, antes de que la operación crezca y los hábitos se vuelvan difíciles de cambiar.</p></div>
 <div class="card"><h3>A quién va dirigido</h3><ul><li><b>Socios de Nyxum</b>: como base para el comité mensual de gestión.</li><li><b>Profesor y tutor del curso</b>: como evidencia del trabajo individual de cada semana.</li><li><b>Clientes y aliados</b> que quieran ver cómo medimos lo que ofrecemos.</li></ul></div>
</div>
</section>

<section>
<h2>La empresa en una frase</h2>
<p><b>Nyxum</b> (Costa Rica, 2026) es una consultoría boutique de IA, datos y arquitectura, socio de Salesforce, con cinco frentes de servicio: implementación, rescate y evolución de Salesforce; datos, analítica e integración; gobierno de datos y arquitectura; IA aplicada; y agentes de IA en cualquier plataforma. Trabaja con alcance y precio cerrados por fase, decisiones documentadas y un método de acompañamiento “antes, durante, después y siempre”. <a href="empresa.html">Ver el perfil completo, los dominios de datos y la arquitectura de información →</a></p>
</section>

<section>
<h2>Los seis pivotes y sus tableros</h2>
<p>El marco del curso propone que la junta directiva supervise seis pivotes interdependientes de la evolución digital, cada uno con sus dominios de datos, acciones de gobierno y KPI u OKR potenciales (Barahona, 2024). Para una firma de cinco personas no hay “junta directiva”, pero sí un comité de socios que debe cumplir ese rol. Cada tablero responde a una pregunta de ese comité.</p>
<div class="pivots">
 <a href="pivote-1.html"><div class="n">Pivote 1 · Semana 2</div><div class="t">Alineamiento dinámico</div><div class="s">¿Nuestra mezcla de servicios y nuestro embudo comercial siguen alineados con la estrategia? Caso de referencia: Huawei.</div></a>
 <a href="pivote-2.html"><div class="n">Pivote 2 · Semana 3</div><div class="t">Cultura y liderazgo digital</div><div class="s">¿Estamos construyendo una cultura de aprendizaje, experimentación y decisiones documentadas? Caso: FCC.</div></a>
 <a href="pivote-3.html"><div class="n">Pivote 3 · Semana 4</div><div class="t">Innovación centrada en el cliente</div><div class="s">¿Escuchamos al cliente y convertimos su retroalimentación en mejoras? Caso: RAPS.</div></a>
 <a href="pivote-4.html"><div class="n">Pivote 4 · Semana 5</div><div class="t">Agilidad operativa</div><div class="s">¿Entregamos por fases cortas, a tiempo y con criterios de aceptación cumplidos? Caso: DB Vertrieb.</div></a>
 <a href="pivote-5.html"><div class="n">Pivote 5 · Semana 6</div><div class="t">Acceso y uso de datos</div><div class="s">¿Nuestros propios datos son confiables y se usan para decidir? Caso: AXA Alemania.</div></a>
 <a href="pivote-6.html"><div class="n">Pivote 6 · Semana 7</div><div class="t">Ecosistemas colaborativos</div><div class="s">¿Cuánto valor nos aportan los socios y cuánto aportamos nosotros? Caso: Arçelik.</div></a>
</div>
</section>

<section>
<h2>Cómo está construido</h2>
<div class="grid c2">
 <div class="card"><h3>Método</h3><ol><li>Leer la nota técnica y el caso de la semana e identificar el dominio de datos del pivote.</li><li>Inventariar qué datos existen hoy en Nyxum, en qué sistema y con qué calidad.</li><li>Definir de 4 a 6 indicadores con fórmula, fuente, frecuencia, meta y responsable.</li><li>Prototipar el tablero con un set de datos simulado y leerlo como lo haría el comité de socios.</li><li>Registrar qué decisiones habilita y qué riesgos tiene medirlo así.</li></ol></div>
 <div class="card"><h3>Herramientas</h3><p>Sitio estático en HTML publicado en GitHub Pages; gráficos con Chart.js; cada gráfico tiene su tabla de datos para lectura sin color. Paleta de series validada para daltonismo. El código del portafolio es público en el repositorio.</p><p><b>Trabajo grupal.</b> La consigna semanal incluye una instancia grupal. El Equipo 6 no llegó a consolidar entregas conjuntas durante el curso; este portafolio contiene únicamente la parte individual y así se declara en cada entrega.</p></div>
</div>
{NOTA_SIM}
</section>

<section>
<h2>Sobre el autor</h2>
<p><b>{AUTHOR}</b>. Heredia, Costa Rica. Más de 14 años en tecnología, la mayor parte en arquitectura y estrategia sobre Salesforce, CRM y nube; socio de Nyxum; MBA de INCAE Business School y participante del programa Chief Digital Officer de MIT Professional Education. <a href="https://www.linkedin.com/in/luis-alfredo-leiva-consultoria-ti/">LinkedIn</a>.</p>
</section>
{refs([REF_BARAHONA, REF_NYXUM])}
"""
page("index.html", {"kicker":"Portafolio de evidencias · Specialization in AI for Digital Business","title":"Gobernar la evolución digital de Nyxum con dashboards",
     "lead":"Propuestas de indicadores y prototipos de tableros para supervisar los seis pivotes de la evolución digital en una consultoría boutique de IA, datos y Salesforce.",
     "meta":[("Autor",AUTHOR),("Empresa","Nyxum · Costa Rica"),("Curso","Digital Business Intelligence · INCAE 2026")]}, body)

# ------------------------------------------------------------------ EMPRESA
body = f"""
<section>
<h2>Modelo de negocio</h2>
<div class="grid c2">
<div class="card"><h3>Qué vende Nyxum</h3><ul>
<li><b>Salesforce</b>: implementación desde cero (una nube principal, hasta 15 usuarios, 4 a 6 semanas), rescate y evolución de instancias existentes.</li>
<li><b>Datos, analítica e integración</b>: integración de Salesforce con ERP y sistemas legados, por fases con precio cerrado.</li>
<li><b>Gobierno de datos y arquitectura</b>: modelo de datos, catálogo, responsables por dominio, políticas de acceso, calidad y retención.</li>
<li><b>IA aplicada</b>: estrategia y hoja de ruta de IA (taller, casos priorizados, hoja de ruta de 90 días).</li>
<li><b>Agentes de IA</b>: pilotos acotados en Agentforce o en otras plataformas, con escala de autonomía de cuatro niveles y supervisión humana.</li>
<li><b>Socio tecnológico fraccional</b>: acompañamiento continuo con dedicación acordada.</li></ul></div>
<div class="card"><h3>Cómo compite</h3><ul>
<li>Arquitectos certificados en cuatro dominios (Application, System, Integration y Data Architect) y más de 15 certificaciones verificables.</li>
<li>Alcance y precio cerrados por fase; licencias, consumo e infraestructura de terceros se muestran aparte.</li>
<li>Decisiones documentadas y transferencia de conocimiento: “su equipo conserva el control”.</li>
<li>Método de acompañamiento: entender todos los frentes antes de proponer; acompañar durante; asegurar la transición; seguir encontrando mejoras.</li>
<li>Producto propio: ADN Futbol, gestión para academias deportivas.</li></ul></div>
</div>
</section>

<section>
<h2>Objetivos estratégicos que los tableros deben servir</h2>
<p>Los objetivos siguientes son una lectura de la propuesta de valor publicada por la firma y de las prioridades de sus socios para 2026 y 2027. Cada pivote del portafolio se conecta con al menos uno.</p>
{table(["Objetivo","Qué significa en la práctica","Pivotes que lo supervisan"],[
 ["O1. Crecer con una mezcla de servicios diversificada","Que la IA aplicada, los agentes y el gobierno de datos pesen cada vez más frente a la implementación clásica de Salesforce","1 Alineamiento · 6 Ecosistemas"],
 ["O2. Cumplir la promesa de “procesos medibles, datos confiables”","Entregar por fases con criterios de aceptación escritos y medir el éxito acordado antes de cada etapa","4 Agilidad · 5 Datos"],
 ["O3. Que el cliente conserve el control","Documentar decisiones, transferir conocimiento y medir adopción después de la entrega","3 Cliente · 2 Cultura"],
 ["O4. Ser una firma que aprende","Mantener certificaciones, experimentar con IA y agentes, y convertir el aprendizaje en oferta","2 Cultura · 6 Ecosistemas"],
 ["O5. Gobernar la IA con evidencia","Subir de nivel de autonomía de un agente solo cuando los datos lo respaldan","5 Datos · 3 Cliente"]])}
</section>

<section>
<h2>Arquitectura de sistemas de información y dominios de datos</h2>
<p>Inventario elaborado por el autor, socio de la firma, a partir de los sistemas y registros que Nyxum usa hoy. La columna de calidad es una valoración propia. Nyxum es pequeña y reciente: parte de los datos viven todavía en hojas de cálculo, y ese es precisamente uno de los hallazgos que motivan el portafolio.</p>
{table(["Dominio de datos","Productos de datos disponibles","Sistema o fuente","Ejemplo de registro","Calidad hoy (valoración del autor)","Pivote"],[
 ["Comercial","Leads y conversaciones iniciales, oportunidades por frente, propuestas, fases cerradas","CRM Salesforce propio y formulario del sitio web","Lead: fecha, canal (web, referido, LinkedIn, socio), asunto del formulario, rango de usuarios de Salesforce, frente, etapa, fecha de cierre","Media: canal de origen incompleto en parte de los registros","1"],
 ["Clientes","Satisfacción al cierre de fase, NPS, usuarios activos sobre licencias, reclamos","Encuesta al cierre de fase, reportes de adopción de la plataforma del cliente, correo","Encuesta: cliente, fase, fecha, puntuación 1 a 5, comentario, mejora sugerida","Baja: la encuesta se aplica, pero no se consolida","3"],
 ["Entrega de proyectos","Fases, criterios de aceptación, cambios de alcance, horas por fase, lead time","Tablero de proyectos y hojas de cálculo","Fase: proyecto, nombre, inicio, fin planificado, fin real, criterios cumplidos / total, horas","Media: la fecha real se registra con retraso","4"],
 ["Personas","Certificaciones, horas de formación, iniciativas internas, pulso de equipo","Trailhead (público), registro interno","Certificación: persona, nombre, fecha, vigencia","Alta para certificaciones; inexistente para pulso","2"],
 ["Datos y plataforma","Calidad del CRM, catálogo de datos, decisiones de arquitectura (ADR), incidentes de acceso","Salesforce, repositorio de documentación","ADR: fecha, decisión, contexto, alternativas, responsable","Media: catálogo parcial","5"],
 ["Ecosistema","Socios activos, proyectos con socios, leads referidos por socios, eventos de cocreación","CRM y registro de alianzas","Socio: tipo, desde, proyectos conjuntos, leads referidos","Baja: no existe registro formal","6"],
 ["Finanzas","Ingresos por frente y por fase, márgenes","Contabilidad","Factura: cliente, fase, frente, monto","Alta, pero no conectada a los demás dominios","1"]])}
<h3>¿Hay alineamiento entre productos de datos, dominios y objetivos?</h3>
<p>Parcial. Los dominios <b>comercial</b> y <b>finanzas</b> están bien soportados pero no conversan entre sí (el frente de servicio se registra distinto en el CRM y en contabilidad). Los dominios <b>clientes</b>, <b>personas</b> y <b>ecosistema</b> tienen datos dispersos o inexistentes, justo donde la firma promete más (adopción, aprendizaje, alianzas). La conclusión de la semana 2 es que el primer trabajo no es construir tableros vistosos sino <b>acordar definiciones</b> (qué es un lead, qué es una fase cerrada, qué frente se factura) y fijar un responsable por dominio, tal como Nyxum propone a sus propios clientes.</p>
</section>
{NOTA_SIM}
{refs([REF_NYXUM, REF_BARAHONA])}
{prevnext(("index.html","Inicio"),("pivote-1.html","Pivote 1 · Alineamiento dinámico"))}
"""
page("empresa.html", {"kicker":"Semana 2 · Contexto de la empresa","title":"Nyxum: la empresa, sus objetivos y sus dominios de datos",
     "lead":"Perfil de la firma, objetivos estratégicos que los tableros deben servir e inventario de los datos que existen hoy, con su calidad.",
     "meta":[("Sector","Consultoría de IA, datos y Salesforce"),("Tamaño","Firma boutique, fundada en 2026"),("País","Costa Rica")]}, body)

# ------------------------------------------------------------------ PIVOTES
def pivot_page(fname, hero, intro, qa_items, dominio_rows, alineamiento, kpi_rows, tiles_items, charts_html, lectura, riesgos, refs_items, prev, nxt, scripts):
    body = f"""
<section><p>{intro}</p></section>
<section><h2>Qué vamos a medir y por qué</h2>{qa(qa_items)}</section>
<section><h2>Dominio y productos de datos</h2>{table(["Producto de datos","Fuente","Ejemplo de registro","Frecuencia"],dominio_rows)}
<p style="margin-top:10px"><b>Datos reales o simulados.</b> El prototipo usa el set de datos simulado del curso, porque la fuente real tiene menos de un año de historia y, en este dominio, su calidad es {hero['calidad']}. La estructura de los registros sí corresponde a la de los sistemas de Nyxum.</p></section>
<section><h2>Alineamiento con la estrategia y el modelo de negocio</h2><p>{alineamiento}</p></section>
<section><h2>Indicadores propuestos</h2>{table(["Indicador","Definición y fórmula","Fuente","Frecuencia","Meta","Responsable"],kpi_rows)}</section>
<section><h2>Prototipo de dashboard</h2>{tiles(tiles_items)}<div class="grid c2">{charts_html}</div></section>
<section><h2>Cómo se lee el tablero y qué decisiones habilita</h2>{lectura}</section>
<section><h2>Riesgos y ética de la medición</h2>{riesgos}</section>
{NOTA_SIM}
{refs(refs_items)}
{prevnext(prev,nxt)}
"""
    page(fname, hero, body, scripts)

# ---- Pivote 1
pivot_page("pivote-1.html",
 {"kicker":"Pivote 1 · Semana 2 · Autoestudio 2","title":"Alineamiento dinámico: ¿seguimos apuntando a donde dijimos?",
  "lead":"Un tablero para que el comité de socios verifique, cada mes, que la mezcla de servicios, el embudo comercial y la velocidad de respuesta siguen alineados con la estrategia de Nyxum.",
  "meta":[("Dominio de datos","Comercial y estrategia"),("Fuente","CRM Salesforce, contabilidad"),("Frecuencia","Mensual, revisión trimestral de OKR")],"calidad":"media (canal de origen incompleto en parte de los leads)"},
 "El alineamiento dinámico es la recalibración continua de estrategias y recursos para mantener el ajuste con un entorno que cambia (Murillo-Esquivel y Barahona, 2024). Para una firma nueva el riesgo no es tener una estrategia equivocada sino <b>deslizarse sin notarlo</b>: aceptar los proyectos que llegan en lugar de los que se quieren, y descubrirlo cuando ya se perdió la diferenciación. Huawei pasó de distribuidor de conmutadores a líder global combinando claridad estratégica con descentralización y foco en el cliente (Guerrero, Lattemann y Michalke, 2021); la lección aplicable a Nyxum es que la estrategia se sostiene con mecanismos de seguimiento, no con declaraciones.",
 [("¿Qué vamos a medir?","La mezcla de ingresos por frente de servicio, el origen y la conversión del embudo comercial, el tiempo de primera respuesta y el ciclo comercial, además de tres OKR trimestrales."),
  ("¿Por qué eso?","Porque son las señales tempranas de desalineamiento: si el 90 % de los ingresos vuelve a ser implementación clásica, o si los socios no generan conversaciones, la estrategia de diversificación y ecosistema queda en el papel."),
  ("¿Por qué medirlo así?","Mezclamos un indicador de resultado (ingresos por frente), indicadores de actividad (leads y conversión) y un OKR con meta explícita, siguiendo la tabla de mecanismos del pivote 1 (Barahona, 2024): objetivos estratégicos, métricas de rendimiento e inteligencia de mercado."),
  ("¿Qué impacto tendría?","Obliga a registrar el canal y el frente en cada lead (cambio de hábito), convierte la reunión mensual de socios en una revisión de datos y permite reasignar tiempo de los socios hacia los frentes que la estrategia prioriza.")],
 [["Leads y conversaciones iniciales","CRM Salesforce (formulario web, registro manual)","Lead: fecha, canal, asunto, frente, etapa, fecha de cierre","Diaria"],
  ["Oportunidades y fases cerradas","CRM Salesforce","Oportunidad: cliente, frente, monto estimado, fecha de cierre","Semanal"],
  ["Ingresos por frente","Contabilidad","Factura: cliente, fase, frente, monto, mes","Mensual"],
  ["OKR trimestrales","Registro de socios","Objetivo, resultado clave, línea base, meta, actual","Trimestral"]],
 "La propuesta de valor de Nyxum se apoya en diversificar más allá de Salesforce (IA aplicada, agentes, gobierno de datos) y en un ecosistema de socios que origine conversaciones. Este tablero sirve al objetivo <b>O1 (mezcla de servicios diversificada)</b> y, de forma indirecta, al <b>O5 (gobernar la IA con evidencia)</b>, porque muestra si los pilotos de agentes están entrando al embudo. El modelo de negocio de alcance cerrado por fase hace que el ciclo comercial sea una variable crítica: cada semana de propuesta sin cierre es capacidad senior sin facturar.",
 [["Ingresos por frente (%)","Ingresos facturados de cada frente / ingresos totales del mes","Contabilidad","Mensual","≥ 40 % fuera de implementación Salesforce","Socio comercial"],
  ["Conversaciones iniciales por canal","Número de leads que llegan a conversación inicial, por canal (web, referidos, LinkedIn, socios)","CRM","Mensual","Socios ≥ 20 % del total","Socio comercial"],
  ["Conversión del embudo","Fases cerradas / contactos del periodo; también por etapa","CRM","Mensual","≥ 10 % contacto → fase cerrada","Socio comercial"],
  ["Tiempo de primera respuesta","Mediana de horas hábiles entre el contacto y la primera respuesta de un socio","CRM","Semanal","≤ 8 horas hábiles (promesa pública: un día hábil)","Socio de turno"],
  ["Ciclo comercial","Mediana de días entre contacto y fase cerrada","CRM","Mensual","≤ 30 días","Socio comercial"],
  ["Avance de OKR","% de resultados clave en verde al cierre del trimestre","Registro de socios","Trimestral","≥ 2 de 3","Comité de socios"]],
 [("54 %","Ingresos fuera de implementación Salesforce (acumulado)","Meta 40 % · en verde","up"),("14 %","Conversaciones originadas por socios (sep.)","Meta 20 % · en camino","" ),("11 h","Tiempo de primera respuesta (mediana, sep.)","Desde 30 h en enero","up"),("37 días","Ciclo comercial (mediana, sep.)","Meta 30 días","")],
 chart("c1","Conversaciones iniciales por canal","Número de leads que llegan a conversación inicial, por mes (apiladas)")+chart("c2","Embudo comercial acumulado 2026","De contacto a fase cerrada")+chart("c3","Mezcla de ingresos por frente","Participación acumulada enero a setiembre, %")+chart("c4","Tiempo de primera respuesta","Mediana mensual de horas hábiles entre el contacto y la primera respuesta")+chart("c5","Ciclo comercial","Mediana mensual de días entre contacto y fase cerrada"),
 "<ul><li><b>Verde</b> en mezcla de ingresos: la diversificación avanza, pero hay que mirar el embudo: casi la mitad de las conversaciones siguen llegando por el sitio web y preguntan por Salesforce. Si el frente de agentes no entra al embudo en el cuarto trimestre, la mezcla de 2027 volverá a concentrarse.</li><li><b>Amarillo</b> en socios: crecen desde cero, pero el OKR exige duplicar el ritmo. Decisión: dedicar una hora semanal de un socio a los tres aliados activos y medir en noviembre.</li><li><b>Ciclo comercial</b>: bajó de 52 a 37 días. La causa visible es la primera respuesta más rápida; la siguiente palanca es la propuesta estándar por fase, que hoy se redacta desde cero.</li></ul>",
 "<ul><li><b>Medir el embudo puede empujar a cerrar rápido lo que llega</b>, justo lo contrario del alineamiento. Por eso el indicador de mezcla de ingresos manda sobre el de conversión.</li><li><b>Datos de prospectos</b>: el CRM contiene datos personales; el tablero usa conteos agregados y nunca nombres, y el registro cumple la Ley 8968 de Costa Rica.</li><li><b>Atribución de canal</b>: un lead referido por un socio que llega por el formulario web se contaría como “web”. Regla: el canal se confirma en la conversación inicial, no se infiere del formulario.</li></ul>",
 ["Murillo-Esquivel, D. y Barahona, J. C. (2024). <i>Alineamiento dinámico: asegurando el ajuste estratégico en la era digital</i>. Revista INCAE Business School.", REF_BARAHONA,
  "Guerrero, R., Lattemann, C. y Michalke, S. (2021). Huawei. En N. Urbach et al. (Eds.), <i>Digitalization Cases Vol. 2</i> (pp. 141-164). Springer.",
  "Kiron, D., Schrage, M., Candelon, F., Khodabandeh, S. y Chu, M. (2023). <i>Strategic alignment with AI and smart KPIs</i>. MIT Sloan Management Review.", REF_NYXUM],
 ("empresa.html","Nyxum y sus datos"),("pivote-2.html","Pivote 2 · Cultura y liderazgo digital"),
 """const M=NYX.meses, C=NYX.comercial;
mkBar('c1',M,Object.entries(C.leadsPorCanal).map(([k,v])=>({name:k,data:v})),{stacked:true});
mkBar('c2',C.embudo.etapas,[{name:'Registros',data:C.embudo.valores}],{horizontal:true});
mkDonut('c3',C.ingresosPorFrente.frentes,C.ingresosPorFrente.pct,{unit:' %',name:'% ingresos'});
mkLine('c4',M,[{name:'Horas hábiles',data:C.horasPrimeraRespuesta}],{unit:' h'});
mkLine('c5',M,[{name:'Días',data:C.cicloDias}]);""")

# ---- Pivote 2
pivot_page("pivote-2.html",
 {"kicker":"Pivote 2 · Semana 3 · Autoestudio 3","title":"Cultura y liderazgo digital: ¿somos la firma que aprende que decimos ser?",
  "lead":"Un tablero para observar si Nyxum sostiene el aprendizaje continuo, la experimentación y la disciplina de documentar decisiones, que son su argumento comercial.",
  "meta":[("Dominio de datos","Personas"),("Fuente","Trailhead, registro interno, pulso trimestral"),("Frecuencia","Mensual; pulso trimestral")],"calidad":"alta para certificaciones e inexistente para el pulso de equipo"},
 "Una cultura digital efectiva se construye con una mentalidad de transformación, una cultura innovadora, agilidad organizacional y aprendizaje continuo (Murillo-Esquivel y Barahona, 2024), y la cultura digital es un antecedente de la madurez digital (Weritz, Braojos y Matute, 2020). La FCC modernizó 207 sistemas heredados y bajó el gasto en mantenimiento de más del 85 % a menos del 50 % con presupuesto plano, y lo hizo empoderando “agentes de cambio” dentro de cada oficina y alineando expectativas antes de migrar (Desouza, Denford y Krishnamurthy, 2019). En una firma de cinco personas la cultura no se delega: se mide en lo que hacen los socios cada semana.",
 [("¿Qué vamos a medir?","Certificaciones vigentes, horas de formación por persona, iniciativas internas propuestas e implementadas, porcentaje de decisiones de arquitectura documentadas y un pulso trimestral de cinco preguntas."),
  ("¿Por qué eso?","Porque son los comportamientos observables de la cultura que Nyxum vende: evidencia verificable (certificaciones), decisiones documentadas y aprendizaje continuo. Si el equipo deja de aprender, la oferta de IA y agentes se vuelve un folleto."),
  ("¿Por qué medirlo así?","Combinamos datos de hecho (certificaciones, ADR) con percepción (pulso), como sugiere la tabla del pivote 2: engagement, eficacia del liderazgo, resultados de formación y proyectos de innovación impulsados por los empleados (Barahona, 2024). Lo que se mide por percepción se declara como tal."),
  ("¿Qué impacto tendría?","Da a los socios una conversación mensual sobre personas y no solo sobre ventas; hace visible el tiempo invertido en aprender, que hoy compite con la facturación, y lo convierte en una decisión explícita.")],
 [["Certificaciones","Trailhead (verificación pública) y registro interno","Persona, certificación, fecha, vigencia","Mensual"],
  ["Horas de formación","Registro interno de tiempo","Persona, tema, horas, mes","Mensual"],
  ["Iniciativas internas","Tablero de ideas de la firma","Idea, proponente, fecha, estado (propuesta, en prueba, implementada, descartada)","Mensual"],
  ["Decisiones de arquitectura (ADR)","Repositorio de documentación","Fecha, decisión, contexto, alternativas, responsable","Por proyecto"],
  ["Pulso de equipo","Encuesta anónima de 5 preguntas, escala 1 a 5","Trimestre, dimensión, promedio","Trimestral"]],
 "El objetivo <b>O4 (ser una firma que aprende)</b> y el <b>O3 (que el cliente conserve el control)</b> dependen de este pivote: solo un equipo que documenta sus propias decisiones puede exigirlo en los proyectos. En el modelo de negocio, el tiempo de los socios es el inventario; medir las horas de formación es decidir cuánto de ese inventario se reinvierte.",
 [["Certificaciones vigentes","Conteo de certificaciones activas del equipo (las vencidas se descuentan)","Trailhead","Mensual","≥ 18 y ninguna vencida","Socio de tecnología"],
  ["Horas de formación por persona","Horas registradas / personas","Registro interno","Mensual","≥ 12 horas por persona y mes","Cada socio"],
  ["Iniciativas implementadas","Iniciativas internas implementadas / propuestas (acumulado trimestral)","Tablero de ideas","Trimestral","≥ 60 %","Comité de socios"],
  ["Decisiones documentadas","Decisiones de arquitectura con ADR / decisiones tomadas en proyectos","Repositorio","Por proyecto","≥ 90 %","Arquitecto responsable"],
  ["Pulso de equipo","Promedio de cinco dimensiones (claridad de estrategia, autonomía, aprendizaje, colaboración, uso de datos)","Encuesta anónima","Trimestral","≥ 4,0 en todas","Socio administrador"]],
 [("19","Certificaciones vigentes","Desde 15 en enero","up"),("15 h","Formación por persona (sep.)","Meta 12 h · en verde","up"),("90 %","Decisiones con ADR (sep.)","Desde 40 % en enero","up"),("4,2","Pulso promedio (sep.)","Desde 3,5 en enero","up")],
 chart("c1","Certificaciones vigentes y decisiones documentadas","Conteo mensual de certificaciones y % de decisiones de arquitectura con registro")+chart("c2","Horas de formación por persona","Horas registradas por persona y mes")+chart("c3","Iniciativas internas","Propuestas e implementadas por mes")+chart("c4","Pulso de equipo: enero frente a setiembre","Promedio por dimensión, escala 1 a 5"),
 "<ul><li>La dimensión más baja del pulso en setiembre es <b>uso de datos para decidir</b> (4,0). Es coherente con el inventario de la semana 2: la firma tiene datos pero no tableros. Este portafolio es, en parte, la respuesta.</li><li>Las horas de formación oscilan con la carga de proyectos (bajan en abril y junio). Decisión: bloquear medio día quincenal de aprendizaje y revisar en el pulso de diciembre si la autonomía para experimentar sube.</li><li>El salto de decisiones documentadas (40 % a 90 %) fue el efecto de una regla simple: ninguna fase se cierra sin su ADR. Es la práctica que la FCC llamaría “victoria rápida”.</li></ul>",
 "<ul><li><b>Medir personas en un equipo de cinco</b> puede exponer a individuos. El pulso es anónimo y se reporta solo el promedio; las horas de formación se usan para planificar, no para evaluar.</li><li><b>Las certificaciones no equivalen a competencia</b>; son evidencia verificable, no la única. El indicador se complementa con iniciativas implementadas.</li><li><b>Sesgo de registro</b>: lo que no se anota no existe. Se acepta ese sesgo a cambio de simplicidad, y se revisa el proceso cada trimestre.</li></ul>",
 ["Murillo-Esquivel, D. y Barahona, J. C. (2024). <i>Construyendo una organización preparada para el futuro: estrategias de cultura y liderazgo digital</i>. Revista INCAE Business School.", REF_BARAHONA,
  "Desouza, K. C., Denford, J. S. y Krishnamurthy, R. (2019). How the US Federal Communications Commission managed the process of IT modernization. En N. Urbach y M. Röglinger (Eds.), <i>Digitalization Cases</i> (pp. 411-428). Springer.",
  "Weritz, P., Braojos, J. y Matute, J. (2020). Exploring the antecedents of digital transformation: Dynamic capabilities and digital culture aspects to achieve digital maturity. <i>AMCIS 2020 Proceedings</i>.",
  "Gray, P., Cross, R. y Arena, M. (2022). Use networks to drive culture change. <i>MIT Sloan Management Review, 63</i>(2), 51-58.", REF_NYXUM],
 ("pivote-1.html","Pivote 1 · Alineamiento dinámico"),("pivote-3.html","Pivote 3 · Innovación centrada en el cliente"),
 """const M=NYX.meses, P=NYX.personas;
mkLine('c1',M,[{name:'Certificaciones vigentes',data:P.certificaciones},{name:'% decisiones con ADR',data:P.decisionesDocumentadas}]);
mkBar('c2',M,[{name:'Horas por persona',data:P.horasFormacion}],{unit:' h'});
mkBar('c3',M,[{name:'Propuestas',data:P.iniciativasInternas.propuestas},{name:'Implementadas',data:P.iniciativasInternas.implementadas}]);
mkBar('c4',P.pulso.dimensiones,[{name:'Enero',data:P.pulso.ene},{name:'Setiembre',data:P.pulso.sep}],{horizontal:true});""")

# ---- Pivote 3
pivot_page("pivote-3.html",
 {"kicker":"Pivote 3 · Semana 4 · Autoestudio 4","title":"Innovación centrada en el cliente: ¿escuchamos y convertimos lo que oímos en mejoras?",
  "lead":"Un tablero para seguir la satisfacción al cierre de cada fase, la adopción real de lo entregado y el ciclo que va de la retroalimentación a la mejora implementada.",
  "meta":[("Dominio de datos","Clientes"),("Fuente","Encuesta de cierre de fase, reportes de adopción, registro de mejoras"),("Frecuencia","Por fase y mensual")],"calidad":"baja (la encuesta se aplica pero no se consolida)"},
 "La innovación centrada en el cliente consiste en integrar su retroalimentación en todo el ciclo y medir servicio, compromiso, satisfacción y adopción (Barahona, 2024). RAPS, un fabricante alemán de especias, desarrolló con Fraunhofer FIT la plataforma myRAzept incluyendo a los carniceros desde la identificación del problema hasta la prueba de prototipos, y aprendió que la preparación digital del usuario y la transferencia de la propuesta de valor física al mundo digital son decisivas (Glismann et al., 2020). Para Nyxum la pregunta es incómoda y necesaria: después de la entrega, ¿la gente del cliente usa lo que construimos?",
 [("¿Qué vamos a medir?","Satisfacción al cierre de cada fase, NPS acumulado, adopción (usuarios activos sobre licencias) en las plataformas entregadas, mejoras recibidas e implementadas a partir de retroalimentación, y tiempo de resolución de reclamos."),
  ("¿Por qué eso?","Porque la promesa de “su equipo conserva el control” se verifica en la adopción, no en el acta de entrega. Y porque una firma pequeña vive de referidos: el NPS es el indicador adelantado del embudo del pivote 1."),
  ("¿Por qué medirlo así?","La tabla del pivote 3 propone perspectiva del cliente, loops de retroalimentación, métricas de satisfacción, índices de adopción y reclamos (Barahona, 2024). Elegimos una medición ligera por fase, porque una encuesta anual no sirve en proyectos de 4 a 6 semanas."),
  ("¿Qué impacto tendría?","Convierte la encuesta de cierre en un dato que se consolida; obliga a acordar con el cliente cómo se medirá la adopción antes de empezar, que es una práctica publicada de la firma; y crea un registro de mejoras que alimenta la oferta.")],
 [["Encuesta de cierre de fase","Formulario corto al cliente","Cliente, fase, fecha, puntuación 1 a 5, comentario, mejora sugerida","Por fase"],
  ["NPS","Pregunta de recomendación a los contactos activos","Cliente, fecha, puntuación 0 a 10","Trimestral"],
  ["Adopción","Reportes de uso de la plataforma del cliente (con su autorización)","Cliente, mes, usuarios activos, licencias","Mensual"],
  ["Mejoras por retroalimentación","Registro de mejoras","Origen, fecha, descripción, estado, fase de implementación","Mensual"],
  ["Reclamos","Correo y CRM","Cliente, fecha de reclamo, fecha de resolución, causa","Por evento"]],
 "Sirve a los objetivos <b>O3 (el cliente conserva el control)</b> y <b>O5 (gobernar la IA con evidencia)</b>: un agente de IA solo sube de nivel de autonomía si la adopción y la satisfacción lo respaldan. En el modelo de negocio, cada fase cerrada con criterios de éxito acordados es la unidad natural de medición; el tablero la aprovecha en lugar de inventar un ciclo distinto.",
 [["Satisfacción al cierre de fase","Promedio de la puntuación 1 a 5 de las fases cerradas en el mes","Encuesta de cierre","Mensual","≥ 4,5","Socio responsable del proyecto"],
  ["NPS","% promotores (9-10) menos % detractores (0-6)","Pregunta de recomendación","Trimestral","≥ 50","Socio comercial"],
  ["Adopción de lo entregado","Usuarios activos en el mes / licencias asignadas, por cliente","Reporte de uso","Mensual","≥ 80 % a los 3 meses","Socio responsable"],
  ["Mejoras implementadas por retroalimentación","Mejoras implementadas / mejoras recibidas (acumulado)","Registro de mejoras","Mensual","≥ 70 %","Comité de socios"],
  ["Tiempo de resolución de reclamos","Mediana de días entre reclamo y resolución","CRM","Mensual","≤ 5 días","Socio de turno"]],
 [("4,6","Satisfacción al cierre de fase (sep.)","Meta 4,5 · en verde","up"),("58","NPS (sep.)","Desde 35 en marzo","up"),("81 %","Adopción promedio en 5 clientes","Un cliente por debajo de 70 %",""),("4 días","Resolución de reclamos (mediana)","Meta 5 días · en verde","up")],
 chart("c1","Satisfacción al cierre de fase","Promedio mensual, escala 1 a 5")+chart("c2","NPS trimestral acumulado","Desde que hay suficientes respuestas (marzo)")+chart("c3","Adopción por cliente","Usuarios activos sobre licencias asignadas, %")+chart("c4","Del comentario a la mejora","Mejoras recibidas e implementadas por mes"),
 "<ul><li><b>Cliente D</b> está en 64 % de adopción: es la señal para activar la fase de transición “después” del método de Nyxum (capacitación y ajustes) antes de que se convierta en licencias ociosas, el problema que la firma promete evitar.</li><li>Las mejoras implementadas van por detrás de las recibidas (6 de 8 en setiembre). Decisión: cada mejora no implementada se cierra con una respuesta escrita al cliente, aunque sea un “no por ahora”.</li><li>El NPS crece con pocos encuestados; el tablero muestra el número de respuestas junto al valor para no sobreinterpretarlo.</li></ul>",
 "<ul><li><b>Datos de uso del cliente</b>: se recogen solo con autorización escrita y agregados por mes; nunca se reportan usuarios individuales del cliente.</li><li><b>Satisfacción sesgada</b>: quien responde la encuesta suele ser el patrocinador, no el usuario final. Se añade al menos un usuario por fase.</li><li><b>Efecto perverso</b>: perseguir el NPS puede llevar a evitar conversaciones difíciles. La regla de la firma de no ocultar riesgos ni costos manda sobre el indicador.</li></ul>",
 [REF_BARAHONA, "Glismann, K., Jöhnk, J., Kratsch, W., Nüske, N. y Schmied, F. (2020). How RAPS spiced up the German butcher’s trade. En N. Urbach et al. (Eds.), <i>Digitalization Cases Vol. 2</i> (pp. 184-190). Springer.", REF_NYXUM],
 ("pivote-2.html","Pivote 2 · Cultura y liderazgo digital"),("pivote-4.html","Pivote 4 · Agilidad operativa"),
 """const M=NYX.meses, K=NYX.clientes;
mkLine('c1',M,[{name:'Satisfacción (1-5)',data:K.satisfaccionFase}],{zero:false,max:5});
mkLine('c2',M,[{name:'NPS',data:K.nps}],{max:70});
mkBar('c3',K.adopcion.clientes,[{name:'% usuarios activos',data:K.adopcion.activos}],{horizontal:true,unit:' %'});
mkBar('c4',M,[{name:'Recibidas',data:K.mejorasPorFeedback.recibidas},{name:'Implementadas',data:K.mejorasPorFeedback.implementadas}]);""")

# ---- Pivote 4
pivot_page("pivote-4.html",
 {"kicker":"Pivote 4 · Semana 5 · Autoestudio 5","title":"Agilidad operativa: ¿entregamos por fases cortas, a tiempo y con criterios cumplidos?",
  "lead":"Un tablero para vigilar la promesa operativa de Nyxum: fases cortas con criterios de aceptación escritos, cambios de alcance aprobados antes de ejecutarse y un lead time que baje.",
  "meta":[("Dominio de datos","Entrega de proyectos"),("Fuente","Tablero de proyectos, registro de cambios"),("Frecuencia","Semanal y por fase")],"calidad":"media (la fecha real de cierre se registra con retraso)"},
 "La agilidad operativa permite responder rápido a los cambios e iterar sobre la estrategia digital; sus dominios de datos son la eficiencia de los procesos, la adopción de prácticas ágiles, el compromiso del equipo, los tiempos de finalización y la velocidad de decisión (Barahona, 2024). DB Vertrieb creó una segunda unidad de TI pequeña y flexible para sus canales digitales (TI bimodal) y quince años después la reintegró, aprendiendo que la configuración debe reevaluarse continuamente y que las diferencias culturales entre modos cuestan (Fortmann, Haffke y Benlian, 2019). Nyxum no tiene dos modos: tiene un método de fases cortas que necesita demostrar con datos.",
 [("¿Qué vamos a medir?","Fases cerradas a tiempo sobre planificadas, porcentaje de criterios de aceptación cumplidos en la primera revisión, cambios de alcance aprobados antes de ejecutarse, lead time de solicitud a entrega en sandbox y distribución de horas por fase."),
  ("¿Por qué eso?","Porque el modelo de precio cerrado por fase solo es sostenible si las fases se cierran a tiempo y sin retrabajo. Un cambio de alcance ejecutado sin aprobación es, a la vez, un riesgo financiero y un incumplimiento del compromiso publicado de la firma."),
  ("¿Por qué medirlo así?","Medimos resultados (a tiempo, criterios cumplidos) y disciplina (cambios aprobados antes), no actividad. Evitamos métricas de “velocidad” de los equipos de software que no aplican a una consultoría de cinco personas."),
  ("¿Qué impacto tendría?","Obliga a cerrar cada fase con una revisión formal de criterios, hace visible el retrabajo y permite estimar mejor la siguiente propuesta con datos de horas por fase.")],
 [["Fases de proyecto","Tablero de proyectos","Proyecto, fase, inicio, fin planificado, fin real, estado","Semanal"],
  ["Criterios de aceptación","Acta de cierre de fase","Fase, criterio, cumplido en primera revisión (sí/no), fecha","Por fase"],
  ["Cambios de alcance","Registro de cambios","Proyecto, fecha de solicitud, fecha de aprobación, impacto en horas y precio","Por evento"],
  ["Lead time","Tablero de proyectos","Solicitud aprobada, entrega en sandbox, días","Por entrega"],
  ["Horas por fase","Registro de tiempo","Proyecto, fase, persona, horas","Semanal"]],
 "Es el tablero del objetivo <b>O2 (procesos medibles, datos confiables)</b>: la firma dice que acuerda cómo se medirá el éxito antes de cada etapa y que ningún cambio de alcance avanza sin aprobación. Estos indicadores son la auditoría interna de esas dos frases. También alimenta el pivote 1: el lead time y las horas por fase explican el ciclo comercial y la rentabilidad de cada frente.",
 [["Fases cerradas a tiempo","Fases cerradas en la fecha planificada / fases planificadas en el mes","Tablero de proyectos","Mensual","≥ 90 %","Socio responsable"],
  ["Criterios cumplidos en primera revisión","Criterios cumplidos / criterios definidos, por fase","Acta de cierre","Por fase","≥ 90 %","Arquitecto responsable"],
  ["Cambios aprobados antes de ejecutar","Cambios con aprobación previa / cambios solicitados","Registro de cambios","Mensual","100 %","Socio comercial"],
  ["Lead time a sandbox","Mediana de días entre solicitud aprobada y entrega en sandbox","Tablero de proyectos","Mensual","≤ 12 días","Arquitecto responsable"],
  ["Horas por fase frente a estimado","Horas reales / horas estimadas, por fase","Registro de tiempo","Por fase","Entre 0,9 y 1,1","Socio responsable"]],
 [("100 %","Fases cerradas a tiempo (sep.)","6 de 6","up"),("94 %","Criterios cumplidos en primera revisión (sep.)","Desde 70 % en enero","up"),("100 %","Cambios aprobados antes de ejecutar (sep.)","Meta 100 %","up"),("12 días","Lead time a sandbox (sep.)","Desde 21 en enero","up")],
 chart("c1","Fases planificadas y cerradas a tiempo","Conteo mensual")+chart("c2","Criterios de aceptación cumplidos en la primera revisión","% mensual")+chart("c3","Lead time de solicitud a sandbox","Mediana de días por mes")+chart("c4","Distribución de horas por fase","Promedio de los proyectos cerrados en 2026"),
 "<ul><li>El retrabajo bajó (criterios cumplidos de 70 % a 94 %) después de escribir los criterios <i>antes</i> de construir, no después. Es la práctica que más vale la pena estandarizar en la propuesta.</li><li>En marzo y mayo hubo cambios de alcance ejecutados antes de aprobarse. Se corrigió con una regla operativa: el cambio se cotiza el mismo día y no se toca el sandbox hasta el visto bueno.</li><li>La construcción concentra el 44 % de las horas; la transición solo el 13 %. Dado lo que muestra el pivote 3 sobre adopción, conviene revisar si la transición está subestimada en las propuestas.</li></ul>",
 "<ul><li><b>Medir “a tiempo” puede empujar a cerrar fases con criterios flojos</b>; por eso ambos indicadores se leen juntos y los criterios los firma el cliente.</li><li><b>Horas por persona</b>: el registro de tiempo se usa para estimar y facturar, no para vigilar a las personas; se reporta por fase, no por individuo.</li><li><b>Fechas reales registradas tarde</b>: hasta que el tablero sea fuente única, el dato se valida en la reunión semanal.</li></ul>",
 [REF_BARAHONA, "Fortmann, L., Haffke, I. y Benlian, A. (2019). Navigating through digital transformation using bimodal IT: How changing IT at DB Vertrieb. En N. Urbach y M. Röglinger (Eds.), <i>Digitalization Cases</i> (pp. 400-407). Springer.", REF_NYXUM],
 ("pivote-3.html","Pivote 3 · Innovación centrada en el cliente"),("pivote-5.html","Pivote 5 · Acceso y uso de datos"),
 """const M=NYX.meses, E=NYX.entrega;
mkBar('c1',M,[{name:'Planificadas',data:E.fases.planificadas},{name:'Cerradas a tiempo',data:E.fases.cerradasATiempo}]);
mkLine('c2',M,[{name:'% criterios cumplidos',data:E.criteriosAceptacion}],{max:100,unit:' %'});
mkLine('c3',M,[{name:'Días',data:E.leadTime}]);
mkBar('c4',E.horasPorFase.fases,[{name:'Horas',data:E.horasPorFase.horas}],{horizontal:true,unit:' h'});""")

# ---- Pivote 5
pivot_page("pivote-5.html",
 {"kicker":"Pivote 5 · Semana 6 · Autoestudio 6","title":"Acceso y uso de datos: ¿nuestros propios datos son confiables y se usan para decidir?",
  "lead":"Un tablero sobre la calidad del CRM, la cobertura del catálogo de datos, los incidentes de acceso y, sobre todo, cuántas decisiones del comité de socios se toman con un tablero delante.",
  "meta":[("Dominio de datos","Datos y plataforma"),("Fuente","Salesforce, catálogo de datos, actas del comité"),("Frecuencia","Mensual")],"calidad":"media (catálogo parcial; las actas no registraban si hubo datos de respaldo)"},
 "El acceso y uso de datos exige estrategias sólidas de gestión de datos y capacidad de integrar nuevas tecnologías; sus dominios son la adopción de tecnología, la utilización del análisis, la calidad de los datos y el cumplimiento (Barahona, 2024). AXA Alemania creó un Laboratorio de Innovación de Datos que une análisis de datos, oficina de gestión de datos e ingeniería de datos bajo un mismo techo, y aprendió que la transformación hacia una aseguradora guiada por datos es de abajo hacia arriba y necesita el apoyo de la alta dirección (Scheffler y Wirths, 2019). Nyxum vende gobierno de datos; este tablero mide si lo practica en casa.",
 [("¿Qué vamos a medir?","Completitud y duplicados en el CRM, porcentaje del catálogo de datos documentado por dominio, incidentes de acceso, número de tableros activos y su uso semanal, y el porcentaje de decisiones del comité de socios respaldadas por un tablero."),
  ("¿Por qué eso?","Porque la calidad del dato es la condición de todos los demás pivotes: un embudo con canal vacío o un cliente duplicado invalidan el tablero comercial. Y porque “usar datos para decidir” fue la dimensión más baja del pulso del pivote 2."),
  ("¿Por qué medirlo así?","Seguimos la tabla del pivote 5: métricas de calidad de datos, utilización del análisis, cumplimiento y protección (Barahona, 2024). El indicador de decisiones con datos es deliberadamente simple: se marca en el acta si la decisión tuvo un tablero de respaldo."),
  ("¿Qué impacto tendría?","Nombra un responsable por dominio de datos (el modelo de oficina de gestión de datos de AXA, a escala de cinco personas), hace de la calidad del CRM una tarea semanal y cambia la dinámica del comité: primero el tablero, después la opinión.")],
 [["Calidad del CRM","Salesforce (reportes de completitud y duplicados)","Mes, % de leads con canal y frente, % de cuentas duplicadas","Semanal"],
  ["Catálogo de datos","Repositorio de documentación","Dominio, producto de datos, responsable, definición, fuente, calidad, fecha de revisión","Mensual"],
  ["Incidentes de acceso","Registro de seguridad","Fecha, tipo (acceso indebido, permiso excesivo, dato expuesto), gravedad, cierre","Por evento"],
  ["Tableros","Inventario de tableros","Tablero, dominio, dueño, usos por semana","Mensual"],
  ["Decisiones con datos","Actas del comité de socios","Fecha, decisión, tablero de respaldo (sí/no)","Mensual"]],
 "Sirve a <b>O2 (datos confiables)</b> y <b>O5 (gobernar la IA con evidencia)</b>. La firma publica que un agente recibe “solo los datos y el contexto necesarios” y que no delega una decisión que la organización no puede explicar; eso presupone un catálogo con responsables y datos limpios. Este tablero es el prerrequisito de cualquier piloto de agente sobre los propios datos de Nyxum.",
 [["Completitud del CRM","% de leads del mes con canal, frente y etapa registrados","Salesforce","Semanal","≥ 95 %","Socio comercial"],
  ["Duplicados","% de cuentas o contactos duplicados detectados","Salesforce","Mensual","≤ 2 %","Responsable del dominio comercial"],
  ["Cobertura del catálogo","Productos de datos documentados / productos identificados, por dominio","Catálogo","Mensual","≥ 80 % en todos los dominios","Socio de tecnología"],
  ["Incidentes de acceso","Número de incidentes en el mes y días hasta su cierre","Registro de seguridad","Mensual","0 abiertos al cierre","Socio de tecnología"],
  ["Decisiones con datos","Decisiones del comité con tablero de respaldo / decisiones registradas","Actas","Mensual","≥ 80 %","Comité de socios"],
  ["Uso de tableros","Usos por semana del conjunto de tableros activos","Inventario","Mensual","Creciente; cada tablero ≥ 1 uso semanal","Dueño de cada tablero"]],
 [("91 %","Completitud del CRM (sep.)","Desde 62 % en enero","up"),("3 %","Duplicados (sep.)","Meta 2 %",""),("78 %","Decisiones con tablero de respaldo (sep.)","Meta 80 % · casi","up"),("0","Incidentes de acceso (jun. a sep.)","Dos en el primer trimestre","up")],
 chart("c1","Calidad del CRM","Completitud de leads y % de duplicados, por mes")+chart("c2","Cobertura del catálogo por dominio","% de productos de datos documentados (setiembre)")+chart("c3","Decisiones del comité con un tablero de respaldo","% mensual")+chart("c4","Tableros activos y uso semanal","Conteo de tableros y usos por semana"),
 "<ul><li>La completitud del CRM subió cuando el canal y el frente pasaron a ser campos obligatorios en la conversación inicial (regla del pivote 1). Los duplicados siguen en 3 %: decisión de activar reglas de duplicados en Salesforce, lo mismo que la firma configura a sus clientes.</li><li>Los dominios <b>ecosistema</b> (50 %) y <b>finanzas</b> (60 %) son los menos documentados; coincide con las brechas del inventario de la semana 2. Se asignan responsables en octubre.</li><li>El uso semanal de tableros crece más rápido que el número de tableros: señal de que se consultan, no solo de que existen.</li></ul>",
 "<ul><li><b>Protección de datos</b>: el CRM contiene datos de prospectos y clientes; aplica la Ley 8968 (Costa Rica) y, para clientes europeos, el RGPD. Los tableros muestran agregados; el acceso a registros individuales se limita por rol.</li><li><b>Calidad como vanidad</b>: completar campos por obligación puede producir datos inventados. Se audita una muestra mensual contra la conversación real.</li><li><b>Decisiones con datos</b> no significa decisiones correctas; el indicador mide el hábito, no el resultado. El resultado se lee en los demás pivotes.</li></ul>",
 [REF_BARAHONA, "Scheffler, A. y Wirths, C. P. (2019). Data innovation @ AXA Germany: Journey towards a data-driven insurer. En N. Urbach y M. Röglinger (Eds.), <i>Digitalization Cases</i> (pp. 366-374). Springer.", "Ley 8968, Ley de Protección de la Persona frente al Tratamiento de sus Datos Personales (Costa Rica, 2011).", REF_NYXUM],
 ("pivote-4.html","Pivote 4 · Agilidad operativa"),("pivote-6.html","Pivote 6 · Ecosistemas colaborativos"),
 """const M=NYX.meses, D=NYX.datos;
mkLine('c1',M,[{name:'% completitud de leads',data:D.calidadCRM.completitud},{name:'% duplicados',data:D.calidadCRM.duplicados}],{max:100,unit:' %'});
mkBar('c2',D.catalogo.dominios,[{name:'% documentado',data:D.catalogo.documentado}],{horizontal:true,unit:' %'});
mkLine('c3',M,[{name:'% decisiones con tablero',data:D.decisionesConDatos}],{max:100,unit:' %'});
mkBar('c4',M,[{name:'Tableros activos',data:D.tableros.activos},{name:'Usos por semana',data:D.tableros.usoSemanal}]);""")

# ---- Pivote 6
pivot_page("pivote-6.html",
 {"kicker":"Pivote 6 · Semana 7 · Entregable final","title":"Ecosistemas colaborativos: ¿cuánto valor nos aportan los socios y cuánto aportamos nosotros?",
  "lead":"Un tablero para gobernar las alianzas de una firma que se define como socio: cuántos socios activos, cuántos proyectos y conversaciones nacen de ellos y qué tan bien cumplen los proyectos conjuntos.",
  "meta":[("Dominio de datos","Ecosistema"),("Fuente","CRM, registro de alianzas"),("Frecuencia","Mensual; revisión semestral de alianzas")],"calidad":"baja (no existe un registro formal de socios)"},
 "Al operar digitalmente dentro de un ecosistema, involucrar a socios, proveedores y clientes deja de ser deseable y se convierte en una capacidad vital; sus dominios son el engagement de los stakeholders, la actividad de la red, los resultados de las asociaciones y el éxito de los proyectos colaborativos (Barahona, 2024). Arçelik se asoció con la startup Simularge para construir un gemelo digital del termoformado de refrigeradores, con ahorros iniciales de más de dos millones de dólares al año, apoyándose en su laboratorio Atölye 4.0 y en la incubadora ITU Çekirdek (Yıldırım et al., 2019). Nyxum nace dentro del ecosistema de Salesforce y declara que también trabaja fuera de él; el tablero mide si esa red existe de verdad.",
 [("¿Qué vamos a medir?","Socios activos por tipo, proyectos con socios, conversaciones iniciales referidas por socios, eventos e ideas de cocreación y el cumplimiento de los proyectos conjuntos."),
  ("¿Por qué eso?","Porque una firma de cinco personas no escala sola: la oferta de agentes en otras plataformas y la capacidad de rescate dependen de aliados (startups de herramientas, proveedores especializados, comunidad). Y porque la estrategia del pivote 1 asigna a los socios el 20 % del embudo."),
  ("¿Por qué medirlo así?","Seguimos la tabla del pivote 6: número de proyectos con socios, tasa de éxito de la colaboración, soluciones cocreadas y eventos con startups (Barahona, 2024), adaptados a la escala de la firma. Un socio “activo” es uno con al menos una interacción registrada en el trimestre."),
  ("¿Qué impacto tendría?","Crea el registro de alianzas que hoy no existe, asigna un socio responsable de cada relación y permite decidir con datos qué alianzas profundizar y cuáles dejar ir.")],
 [["Socios","Registro de alianzas","Socio, tipo, responsable en Nyxum, desde, última interacción","Mensual"],
  ["Proyectos con socios","Tablero de proyectos","Proyecto, socio, rol del socio, fase, criterios cumplidos","Por fase"],
  ["Conversaciones referidas por socios","CRM (canal = socio)","Lead, socio que refiere, fecha, etapa","Mensual"],
  ["Cocreación","Registro de eventos","Evento, fecha, socios participantes, ideas registradas, ideas que pasaron a prueba","Por evento"]],
 "Sirve a <b>O1 (mezcla diversificada)</b> y <b>O4 (firma que aprende)</b>. En el modelo de negocio, los socios son a la vez canal (leads), capacidad (especialistas por proyecto) y aprendizaje (nuevas plataformas de agentes). Medirlos cierra el ciclo del portafolio: el ecosistema alimenta el embudo del pivote 1, y la disciplina de entrega del pivote 4 es lo que hace que un socio quiera repetir.",
 [["Socios activos","Socios con al menos una interacción registrada en el trimestre, por tipo","Registro de alianzas","Trimestral","≥ 8, con al menos 2 fuera del ecosistema Salesforce","Socio comercial"],
  ["Proyectos con socios","Proyectos activos en los que participa un socio","Tablero de proyectos","Mensual","≥ 30 % de los proyectos","Comité de socios"],
  ["Conversaciones referidas por socios","Leads con canal = socio que llegan a conversación inicial","CRM","Mensual","≥ 20 % del total (OKR del pivote 1)","Socio comercial"],
  ["Cumplimiento de proyectos conjuntos","Criterios de aceptación cumplidos en proyectos con socios","Acta de cierre","Por fase","≥ 90 %","Socio responsable"],
  ["Cocreación","Eventos con socios en el trimestre e ideas que pasaron a prueba","Registro de eventos","Trimestral","≥ 2 eventos y ≥ 3 ideas en prueba","Socio de tecnología"]],
 [("8","Socios activos (3er trimestre)","4 tipos","up"),("3","Proyectos con socios (sep.)","De 7 activos",""),("4","Conversaciones referidas por socios (sep.)","14 % del total",""),("94 %","Cumplimiento en proyectos conjuntos","5 proyectos · meta 90 %","up")],
 chart("c1","Socios activos por tipo","Tercer trimestre de 2026")+chart("c2","Proyectos y conversaciones que nacen de socios","Conteo mensual")+chart("c3","Cocreación con socios","Eventos e ideas registradas por mes")+chart("c4","Cumplimiento de proyectos con socios","% de criterios de aceptación cumplidos, por proyecto"),
 "<ul><li>Las conversaciones referidas por socios crecen pero no alcanzan el 20 % del embudo. Decisión: formalizar con los dos socios de mejor cumplimiento (P1 y P3) un acuerdo de referidos recíproco y medirlo en el primer trimestre de 2027.</li><li>Los eventos de cocreación producen ideas (4 a 6 por evento) pero el registro de cuáles pasaron a prueba está incompleto; se corrige en el catálogo del pivote 5.</li><li>El proyecto P2 (80 %) es el único por debajo de la meta: la revisión semestral de alianzas decidirá si el problema es del socio o de la definición de criterios.</li></ul>",
 "<ul><li><b>Confidencialidad</b>: los socios tienen acceso a información de clientes en proyectos conjuntos; cada alianza tiene acuerdo de confidencialidad antes de contar como “activa”.</li><li><b>Dependencia</b>: medir el peso de los socios en el embudo también protege contra depender de uno solo (incluida Salesforce); el tablero muestra la concentración por socio.</li><li><b>Reciprocidad</b>: un ecosistema no es solo lo que recibimos. Se registra también qué referimos y aportamos a cada socio, aunque no se convierta en ingreso.</li></ul>",
 [REF_BARAHONA, "Yıldırım, N., Tunçalp, D., İstanbullu, G. G., Konuşkan, Y., İnan, M., Yasin, O., Apaçoğlu-Turan, B., Turan, E., Özer, Ö. F. y Kerimoğlu, V. (2019). Digitalization of manufacturing processes with startup collaboration. En N. Urbach et al. (Eds.), <i>Digitalization Cases Vol. 2</i>. Springer.", REF_NYXUM],
 ("pivote-5.html","Pivote 5 · Acceso y uso de datos"),("final.html","Síntesis final"),
 """const M=NYX.meses, S=NYX.ecosistema;
mkBar('c1',S.socios.tipos,[{name:'Socios activos',data:S.socios.activos}],{horizontal:true});
mkLine('c2',M,[{name:'Proyectos con socios',data:S.proyectosConSocios},{name:'Conversaciones referidas',data:S.leadsSocios}]);
mkBar('c3',M,[{name:'Eventos',data:S.cocreacion.eventos},{name:'Ideas registradas',data:S.cocreacion.ideas}]);
mkBar('c4',S.exitoColaboracion.proyectos,[{name:'% criterios cumplidos',data:S.exitoColaboracion.cumplimiento}],{unit:' %',max:100});""")

# ------------------------------------------------------------------ FINAL
body = f"""
<section>
<h2>El tablero como iniciador de conversaciones</h2>
<div class="card soft"><p><b>Mensaje para los socios de Nyxum.</b> Vendemos procesos medibles y datos confiables. Este portafolio es el primer tablero que nos aplicamos a nosotros mismos: seis preguntas, una por pivote, que el comité de socios puede responder cada mes con datos en lugar de con memoria. No es un reporte para mirar; es la agenda de la reunión. Cada indicador tiene un dueño, una fuente y una meta, y cada página termina con las decisiones que habilita. Si un indicador no provoca una decisión en tres meses, se elimina.</p></div>
</section>

<section>
<h2>Cómo se conectan los seis tableros</h2>
<p>Los pivotes son interdependientes: cada uno cataliza la efectividad de los otros (Barahona, 2024). En Nyxum la cadena se lee así:</p>
{table(["Si este tablero muestra…","…se nota en este otro","Ejemplo en el prototipo"],[
 ["5 Datos: CRM incompleto o duplicado","1 Alineamiento: embudo y mezcla de ingresos no confiables","La completitud pasó de 62 % a 91 % y el canal “socios” apareció en el embudo"],
 ["2 Cultura: pocas horas de formación, decisiones sin ADR","4 Agilidad: más retrabajo y criterios incumplidos","Las decisiones documentadas subieron a 90 % y los criterios cumplidos a 94 %"],
 ["4 Agilidad: transición con pocas horas","3 Cliente: adopción baja después de la entrega","Cliente D en 64 % de adopción; la transición pesa solo 13 % de las horas"],
 ["3 Cliente: NPS alto","1 Alineamiento: referidos crecen; 6 Ecosistemas: socios quieren repetir","Referidos pasaron de 2 a 7 conversaciones mensuales"],
 ["6 Ecosistemas: socios activos y proyectos conjuntos","1 Alineamiento: 14 % del embudo originado por socios","OKR de 20 % en camino"]])}
</section>

<section>
<h2>Dominios y productos de datos: estado al cierre del curso</h2>
{table(["Dominio","Responsable propuesto","Productos de datos en el portafolio","Calidad en setiembre","Siguiente paso"],[
 ["Comercial","Socio comercial","Leads por canal, embudo, ciclo, primera respuesta","Media → alta","Reglas de duplicados en el CRM"],
 ["Personas","Socio administrador","Certificaciones, formación, iniciativas, ADR, pulso","Alta (pulso nuevo)","Pulso de diciembre"],
 ["Clientes","Socio responsable de cada proyecto","Satisfacción por fase, NPS, adopción, mejoras, reclamos","Baja → media","Consolidar la encuesta en el CRM"],
 ["Entrega","Arquitecto responsable","Fases, criterios, cambios de alcance, lead time, horas","Media","Fecha real como campo obligatorio"],
 ["Datos y plataforma","Socio de tecnología","Calidad del CRM, catálogo, incidentes, decisiones con datos","Media → alta","Catálogo de finanzas y ecosistema"],
 ["Ecosistema","Socio comercial","Socios, proyectos conjuntos, referidos, cocreación","Baja → media","Registro de alianzas y acuerdos de referidos"]])}
</section>

<section>
<h2>Hoja de ruta: del prototipo al tablero real</h2>
<div class="grid c3">
<div class="card"><h3>0 a 30 días</h3><ul><li>Campos obligatorios en el CRM: canal, frente, etapa.</li><li>Acta de cierre de fase con criterios y encuesta de satisfacción.</li><li>Registro de alianzas y de ADR en el repositorio.</li></ul></div>
<div class="card"><h3>30 a 90 días</h3><ul><li>Conectar los tableros 1, 4 y 5 a Salesforce y al tablero de proyectos (datos reales).</li><li>Primer pulso de equipo (diciembre).</li><li>Revisión de OKR del cuarto trimestre con el tablero 1.</li></ul></div>
<div class="card"><h3>90 a 180 días</h3><ul><li>Tableros 3 y 6 con datos reales de adopción y socios.</li><li>Evaluar un asistente de IA que resuma los tableros para el comité (nivel 1 de autonomía: asiste).</li><li>Eliminar los indicadores que no hayan provocado decisiones.</li></ul></div>
</div>
</section>

<section>
<h2>Lo que aprendí construyendo el portafolio</h2>
<ul>
<li><b>Primero las definiciones, después los gráficos.</b> La mayor parte del esfuerzo fue acordar qué es un lead, una fase cerrada o un socio activo. Es el mismo trabajo que Nyxum hace para sus clientes y que no había hecho para sí misma.</li>
<li><b>Pocos indicadores con dueño</b> valen más que muchos sin él. Cada tablero quedó con cinco o seis, y cada uno con una decisión asociada.</li>
<li><b>Los casos del curso escalan hacia abajo.</b> La oficina de gestión de datos de AXA, los agentes de cambio de la FCC o la inclusión del cliente en RAPS funcionan en una firma de cinco personas si se traducen a reglas simples: un campo obligatorio, un acta, una encuesta.</li>
<li><b>Simular datos fue útil y riesgoso.</b> Permitió probar que los tableros se pueden leer, pero obliga a declarar en cada página que las cifras no son reales y a fijar la fecha en que dejarán de serlo.</li>
</ul>
</section>
{NOTA_SIM}
{refs([REF_BARAHONA, "Murillo-Esquivel, D. y Barahona, J. C. (2024). Notas técnicas de las semanas 2 a 7. Revista INCAE Business School.", "Urbach, N. y Röglinger, M. (Eds.) (2019). <i>Digitalization Cases</i>. Springer; Urbach, N. et al. (Eds.) (2021). <i>Digitalization Cases Vol. 2</i>. Springer.", REF_NYXUM])}
{prevnext(("pivote-6.html","Pivote 6 · Ecosistemas colaborativos"),("index.html","Inicio"))}
"""
page("final.html", {"kicker":"Semana 7 · Entregable final","title":"Síntesis: un sistema de seis tableros para gobernar la evolución digital de Nyxum",
     "lead":"Cómo se conectan los pivotes, el estado de los dominios de datos al cierre del curso y la hoja de ruta para pasar del prototipo simulado al tablero con datos reales.",
     "meta":[("Autor",AUTHOR),("Empresa","Nyxum"),("Cierre","Octubre de 2026")]}, body)
print("ok", sorted(f for f in os.listdir(OUT) if f.endswith('.html')))
