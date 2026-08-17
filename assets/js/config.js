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
    nombre: 'Consultorio Roble',
    calle: 'Av. Ejemplo 123, interior 4',
    colonia: 'Col. Centro',
    ciudad: 'Santiago de Querétaro, Qro.',
    cp: '76000',
    pais: 'México',
    referencia: 'Edificio de fachada blanca, junto a la farmacia. Estacionamiento en el sótano.',

    // COORDENADAS DEL CONSULTORIO  ← lo más importante del mapa
    // Cómo obtenerlas: abre Google Maps, clic derecho sobre el punto exacto
    // y copia los dos números que aparecen arriba del menú.
    lat: 20.588793,
    lng: -100.389888,
    zoom: 16
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
