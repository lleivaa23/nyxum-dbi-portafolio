// Set de datos SIMULADO para fines académicos (curso INCAE, 2026).
// Las cifras NO representan resultados reales de Nyxum; se generaron para prototipar los dashboards.
window.NYX = {
  meses: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep"],
  // Pivote 1 · Alineamiento dinámico (dominio: comercial + estrategia)
  comercial: {
    leadsPorCanal: { // conversaciones iniciales por canal y mes
      "Sitio web":   [3,4,5,6,7,8,9,10,11],
      "Referidos":   [2,3,3,4,5,5,6,7,7],
      "LinkedIn":    [1,2,2,3,3,4,4,5,6],
      "Socios":      [0,0,1,1,2,2,3,3,4]
    },
    embudo: { etapas:["Contacto","Conversación inicial","Propuesta","Fase cerrada"], valores:[128,74,31,12] },
    ingresosPorFrente: { frentes:["Salesforce","Datos e integración","Gobernanza","IA aplicada","Agentes"], pct:[46,22,9,13,10] },
    horasPrimeraRespuesta: [30,26,24,20,18,16,14,12,11], // horas hábiles (mediana)
    okr: [
      {obj:"Diversificar ingresos: 40 % fuera de implementación Salesforce al cierre de 2026", kr:"% de ingresos de frentes no Salesforce", base:"38 %", meta:"40 %", actual:"54 %"},
      {obj:"Reducir el ciclo comercial a 30 días", kr:"Días entre contacto y fase cerrada (mediana)", base:"52", meta:"30", actual:"37"},
      {obj:"Que los socios aporten 20 % de las conversaciones", kr:"% de conversaciones iniciales originadas por socios", base:"0 %", meta:"20 %", actual:"14 %"}
    ],
    cicloDias: [52,50,47,45,43,41,40,38,37]
  },
  // Pivote 2 · Cultura y liderazgo digital (dominio: personas)
  personas: {
    certificaciones: [15,15,16,16,17,17,18,19,19],
    horasFormacion: [6,8,10,9,12,11,14,12,15], // horas por persona y mes
    iniciativasInternas: { propuestas:[1,2,2,3,2,3,4,3,4], implementadas:[0,1,1,2,1,2,3,2,3] },
    decisionesDocumentadas: [40,48,55,60,68,74,80,85,90], // % de decisiones de arquitectura con registro (ADR)
    pulso: { dimensiones:["Claridad de la estrategia","Autonomía para experimentar","Aprendizaje continuo","Colaboración entre frentes","Uso de datos para decidir"], ene:[3.4,3.6,3.5,3.8,3.2], sep:[4.3,4.1,4.2,4.4,4.0] }
  },
  // Pivote 3 · Innovación centrada en el cliente (dominio: clientes)
  clientes: {
    satisfaccionFase: [4.2,4.3,4.1,4.4,4.5,4.4,4.6,4.5,4.6], // 1-5 al cierre de cada fase
    nps: [null,null,35,40,42,48,50,55,58],
    adopcion: { clientes:["Cliente A","Cliente B","Cliente C","Cliente D","Cliente E"], activos:[92,78,85,64,88] }, // % usuarios activos / licencias
    mejorasPorFeedback: { recibidas:[2,3,4,4,5,6,6,7,8], implementadas:[1,2,3,3,4,4,5,5,6] },
    reclamos: { dias:[9,8,7,7,6,5,5,4,4] }
  },
  // Pivote 4 · Agilidad operativa (dominio: entrega de proyectos)
  entrega: {
    fases: { planificadas:[2,3,3,4,4,5,5,6,6], cerradasATiempo:[1,2,3,3,4,4,4,5,6] },
    criteriosAceptacion: [70,75,80,82,85,88,90,92,94], // % de criterios cumplidos en la primera revisión
    cambiosAlcance: { solicitados:[1,2,2,3,3,2,3,2,2], aprobadosAntes:[1,1,2,3,3,2,3,2,2] },
    leadTime: [21,20,18,17,16,15,14,13,12], // días desde solicitud aprobada hasta entrega en sandbox
    horasPorFase: { fases:["Descubrimiento","Diseño","Construcción","Pruebas","Transición"], horas:[24,32,96,40,28] }
  },
  // Pivote 5 · Acceso y uso de datos (dominio: datos y plataforma)
  datos: {
    calidadCRM: { completitud:[62,66,70,74,78,82,85,88,91], duplicados:[9,8,7,6,5,5,4,3,3] },
    catalogo: { dominios:["Comercial","Clientes","Entrega","Personas","Finanzas","Ecosistema"], documentado:[90,80,85,70,60,50] },
    incidentesAcceso: [2,1,1,0,1,0,0,0,0],
    decisionesConDatos: [35,40,45,52,58,63,70,74,78], // % de decisiones del comité con un tablero de respaldo
    tableros: { activos:[1,1,2,2,3,3,4,5,6], usoSemanal:[2,2,3,4,5,6,7,8,9] }
  },
  // Pivote 6 · Ecosistemas colaborativos (dominio: socios)
  ecosistema: {
    socios: { tipos:["Salesforce (partner)","Startups y herramientas","Proveedores especializados","Academia y comunidad"], activos:[1,3,2,2] },
    proyectosConSocios: [0,0,1,1,1,2,2,3,3],
    leadsSocios: [0,0,1,1,2,2,3,3,4],
    cocreacion: { eventos:[0,0,1,0,1,1,1,2,1], ideas:[0,0,3,0,4,3,5,6,4] },
    exitoColaboracion: { proyectos:["P1","P2","P3","P4","P5"], cumplimiento:[100,80,100,90,100] }
  }
};
