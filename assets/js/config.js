/* ============================================================================
   CONFIGURACIÓN DEL SITIO
   ----------------------------------------------------------------------------
   ESTE ES EL ÚNICO ARCHIVO QUE NECESITAS EDITAR PARA LOS DATOS DE CONTACTO.
   Cambia los valores de la derecha y todo el sitio se actualiza solo:
   el botón de WhatsApp, el mapa, las rutas, el teléfono y el pie de página.

   Los TEXTOS (biografía, servicios, preguntas frecuentes) se editan
   directamente en index.html — busca los comentarios que dicen  ⚠️ EDITAR
   ========================================================================== */

window.SITE_CONFIG = {

  /* --- Identidad ------------------------------------------------------- */
  nombre: 'Mtra. Valeria Fuentes',      // Nombre completo, con título
  nombreCorto: 'Valeria Fuentes',       // Como aparece en el logo, sin título
  profesion: 'Psicóloga clínica',
  cedula: '00000000', // Cédula profesional (SEP)

  /* --- WhatsApp -------------------------------------------------------- */
  whatsapp: {
    // Número en formato internacional, SOLO DÍGITOS.
    // México: 52 + 10 dígitos.  Ej: 524421234567
    numero: '524420000000',

    // Mensaje que se escribe solo cuando abren el chat.
    mensaje: 'Hola, vi tu página web y me gustaría agendar una primera sesión.'
  },

  /* --- Contacto -------------------------------------------------------- */
  telefono: '+52 442 000 0000',
  email: 'contacto@ejemplo.com',

  /* --- Consultorio ----------------------------------------------------- */
  consultorio: {
    nombre: 'Consultorio',
    calle: 'Mauricio Garcés 808',
    colonia: 'La Joya',
    ciudad: 'Santiago de Querétaro, Qro.',
    cp: '76180',
    pais: 'México',

    // Referencia para llegar (deja '' y no se muestra nada).
    // Ej: 'Edificio de fachada gris, timbre 4. Hay estacionamiento en la calle.'
    referencia: '',

    // ⚠️ COORDENADAS — VERIFICAR ANTES DE PUBLICAR
    // Estas apuntan a la calle Mauricio Garcés (CP 76180), pero NO al
    // número 808 exacto: el callejero abierto no llega a ese detalle.
    // Para afinar: abre Google Maps, busca la dirección, haz clic derecho
    // justo sobre la puerta y copia los dos números del menú.
    lat: 20.572439,
    lng: -100.4184025,
    zoom: 17
  },

  /* --- Horarios (se imprimen tal cual en la sección de ubicación) ------- */
  horarios: [
    { dias: 'Lunes a viernes', horas: '9:00 – 20:00' },
    { dias: 'Sábado',          horas: '9:00 – 14:00' },
    { dias: 'Domingo',         horas: 'Cerrado' }
  ],

  /* --- Redes (deja '' vacío para ocultar el enlace) --------------------- */
  redes: {
    instagram: '',
    facebook: '',
    linkedin: ''
  }
};
