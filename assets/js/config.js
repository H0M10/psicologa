/* ============================================================================
   CONFIGURACIÓN DEL SITIO
   ----------------------------------------------------------------------------
   ESTE ES EL ÚNICO ARCHIVO QUE NECESITAS EDITAR PARA LOS DATOS DE CONTACTO.
   Cambia los valores de la derecha y todo el sitio se actualiza solo:
   los botones de WhatsApp, el mapa, las rutas, el teléfono y el pie.

   Los TEXTOS (biografía, servicios, formación) se editan en index.html
   ========================================================================== */

window.SITE_CONFIG = {

  /* --- Identidad ------------------------------------------------------- */
  nombre: 'Thania Huerta',
  nombreCorto: 'Thania Huerta',
  profesion: 'Psicóloga clínica y forense',
  cedula: '14661976',
  registroForense: '25-08-63',

  /* --- WhatsApp -------------------------------------------------------- */
  whatsapp: {
    // 52 + 10 dígitos, solo números
    numero: '524421375118',

    // Mensaje general (botones de "Escribir por WhatsApp")
    mensaje: 'Hola Thania, vi tu página web y me gustaría agendar una cita.',

    // Mensaje para psicoterapia
    mensajeTerapia: 'Hola Thania, vi tu página web y me interesa una consulta de psicoterapia para adolescentes.',

    // Mensaje para cotización de servicios forenses, ya estructurado
    // para que ella reciba la información mínima de entrada
    mensajeCotizacion:
      'Hola Thania, quisiera solicitar una cotización de servicios forenses.\n\n' +
      '• Tipo de servicio: (pericial en materia familiar / metapericial / no estoy seguro)\n' +
      '• Materia o juzgado: \n' +
      '• Breve descripción del asunto: \n' +
      '• ¿Hay una fecha límite?: '
  },

  /* --- Contacto -------------------------------------------------------- */
  telefono: '+52 442 137 5118',
  telefonoVisible: '442 137 5118',
  email: '',

  /* --- Consultorio ----------------------------------------------------- */
  consultorio: {
    nombre: 'Consultorio',
    calle: 'Calle Mauricio Garcés 808',
    colonia: 'Col. La Joya',
    ciudad: 'Santiago de Querétaro, Qro.',
    cp: '76180',
    pais: 'México',

    // Referencia para llegar (deja '' y no se muestra nada).
    referencia: '',

    // ⚠️ COORDENADAS — VERIFICAR ANTES DE PUBLICAR
    // Apuntan a la calle Mauricio Garcés (CP 76180), pero NO al número 102
    // exacto: el callejero abierto no llega a ese detalle.
    // Para afinar: abre Google Maps, busca la dirección, clic derecho justo
    // sobre la puerta y copia los dos números del menú.
    lat: 20.572439,
    lng: -100.4184025,
    zoom: 17
  },

  /* --- Horarios -------------------------------------------------------- */
  horarios: [
    { dias: 'Lunes a viernes', horas: '9:00 – 14:00' },
    { dias: '',                horas: '16:00 – 21:00' },
    { dias: 'Sábado',          horas: '9:00 – 13:00' },
    { dias: 'Domingo',         horas: 'Cerrado' }
  ],

  /* --- Redes (deja '' vacío para ocultar el enlace) --------------------- */
  redes: { instagram: '', facebook: '', linkedin: '' }
};
