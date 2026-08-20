/* ============================================================================
   Inyecta en los bocetos 01–10 toda la información de Thania que les faltaba.
   Contenido literal del documento que entregó. No inventa nada.

   Se omite solo si el boceto ya la trae (11–16 la tienen en su maquetación).
   ========================================================================== */
(function () {
  if (document.querySelector('.info-completa')) return;
  // Si el boceto ya lista los 10 motivos, no hace falta el bloque
  if (/Presión académica/.test(document.body.textContent)) return;

  var TEL = '+524428306799';
  var WA  = 'https://wa.me/524428306799?text=';
  var LAT = '20.572439', LNG = '-100.4184025';

  var msgGeneral = encodeURIComponent(
    'Hola Thania, vi tu página web y me gustaría agendar una cita.');
  var msgCotiza = encodeURIComponent(
    'Hola Thania, quisiera solicitar una cotización.\n\n' +
    '• Tipo de servicio: \n• Materia o juzgado: \n' +
    '• Breve descripción del asunto: \n• ¿Hay una fecha límite?: ');

  var supuestos = [
    'Guarda y custodia',
    'Establecimiento o modificación de regímenes de convivencia',
    'Valoración de competencias y habilidades parentales',
    'Conflictos derivados de una separación o divorcio',
    'Interferencias parentales',
    'Identificación de factores de riesgo y protección',
    'Afectaciones psicológicas'
  ];

  var motivos = [
    'Ansiedad', 'Depresión', 'Regulación emocional',
    'Autoestima, inseguridad, identidad y autoconocimiento',
    'Habilidades sociales', 'Problemas de conducta en adolescentes',
    'Cambios en la dinámica familiar derivados de procesos judiciales',
    'Desarrollo de habilidades parentales y fortalecimiento del vínculo entre madres, padres e hijos',
    'Educación sexual', 'Presión académica'
  ];

  var forense = [
    ['May 2024 – may 2026', 'Maestría en Investigación y Evaluación Criminal y Forense', 'Instituto de Ciencia Aplicada'],
    ['Mayo 2025', 'Curso de elaboración de peritajes judiciales', 'Poder Judicial del Estado de Querétaro'],
    ['Mar – may 2025', 'Certificación en Análisis de Contexto en la Investigación Criminal', 'Consejo Certificador en Psicología Forense · Ciencia Aplicada'],
    ['Feb – may 2025', 'Curso-taller de peritajes psicológicos en guarda y custodia con perspectiva de infancia', 'FORENPSIC'],
    ['Sep – dic 2024', 'Seminario especializado en disociación y trauma en víctimas de violencia', 'Instituto de Ciencia Aplicada'],
    ['Julio 2024', 'Curso de elaboración de peritaje psicológico', 'Centro de SubjetividadEs Identidad Clínica y Forense']
  ];

  var clinica = [
    ['Ago 2026 – en curso', 'Diplomado en Psicoterapia Infantojuvenil', 'CAPCIA'],
    ['May 2026 – en curso', 'Maestría en Psicoterapia Cognitivo Conductual', 'Centro de Psicoterapia Cognitiva'],
    ['Ene – nov 2025', 'Diplomado en Psicoterapia Cognitivo Conductual', 'Universidad Autónoma de Querétaro · IMFAPSI'],
    ['Ago 2020 – may 2024', 'Licenciatura en Psicología', 'Universidad Mondragón México']
  ];

  var horarios = [
    ['Lunes a viernes', '9:00 – 14:00'],
    ['', '16:00 – 21:00'],
    ['Sábado', '9:00 – 13:00'],
    ['Domingo', 'Cerrado']
  ];

  function li(a) { return '<li>' + a + '</li>'; }
  function estudio(e) {
    return '<li><span class="f">' + e[0] + '</span><b>' + e[1] + '</b>' +
           '<span class="e">' + e[2] + '</span></li>';
  }
  function hora(h) {
    return '<li><span>' + h[0] + '</span><span>' + h[1] + '</span></li>';
  }

  var iconoWA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.2-1.4A10 10 0 1 0 12 2Zm5.5 14.2c-.2.6-1.2 1.1-1.7 1.2-.4 0-1 .1-1.6-.1-.4-.1-.8-.3-1.4-.5-2.5-1.1-4.1-3.6-4.2-3.7-.1-.2-1-1.3-1-2.5s.6-1.8.9-2.1c.2-.2.5-.3.6-.3h.5c.2 0 .4 0 .6.4l.7 1.8c.1.1.1.3 0 .4l-.2.4-.4.4c-.1.1-.2.3-.1.5.1.2.6 1 1.4 1.7.9.8 1.7 1.1 1.9 1.2s.4.1.5-.1l.8-1c.2-.2.3-.2.6-.1l1.7.8c.2.1.4.2.4.3 0 .1 0 .5-.2 1Z"/></svg>';

  var s = document.createElement('section');
  s.className = 'info-completa';
  s.id = 'informacion';
  s.innerHTML =
    '<div class="info-completa__w">' +

    // --- Sobre mí ---
    '<div class="ic-sec">' +
      '<p class="ic-k">Sobre mí</p>' +
      '<h2>Hola, soy Thania Huerta Pacheco</h2>' +
      '<p>Soy psicóloga con formación y experiencia profesional en los ámbitos clínico y forense. Dentro del área forense trabajo principalmente en materia familiar, lo que me ha permitido comprender las distintas situaciones y necesidades que pueden presentarse en las familias. En el área clínica, mi práctica está dedicada exclusivamente al acompañamiento de adolescentes y juventudes.</p>' +
      '<p>Elegí trabajar con esta población porque considero que la adolescencia es un momento decisivo en la construcción de las personas adultas del futuro. Acompañarlos oportunamente puede generar cambios importantes en el presente, mientras desarrollan su identidad y su propia manera de relacionarse con el mundo.</p>' +
      '<blockquote class="ic-cita">Aunque ambos ámbitos tienen objetivos y límites éticos diferentes, juntos enriquecen mi manera de comprender el comportamiento humano.</blockquote>' +
      '<p>Disfruto estudiar y mantenerme en constante actualización. Procuro que mi trabajo se sustente en evidencia científica, pero también creo que la terapia puede ser cercana y creativa: disfruto crear materiales y adaptar actividades y herramientas a la personalidad, los intereses y las necesidades de cada adolescente.</p>' +
    '</div>' +

    // --- Psicología forense ---
    '<div class="ic-sec" id="forense-detalle">' +
      '<p class="ic-k">Psicología forense</p>' +
      '<h2>Servicios periciales en materia familiar</h2>' +
      '<h3 class="ic-h3">Periciales psicológicas en materia familiar</h3>' +
      '<ul class="ic-lista">' + supuestos.map(li).join('') + '</ul>' +
      '<h3 class="ic-h3">Metapericiales o análisis técnicos de dictámenes psicológicos</h3>' +
      '<p>Revisión de peritajes realizados por otros profesionales para valorar la metodología empleada, el cumplimiento de criterios científicos, técnicos y éticos, la pertinencia de los instrumentos y su relación con los resultados y conclusiones.</p>' +
      '<div class="ic-costo">' +
        '<p>Cada asunto es diferente y requiere un servicio pensado de acuerdo con sus propias necesidades. Por eso el costo puede variar según sus características y su alcance. Puedes solicitar una cotización personalizada, <strong>sin costo y sin compromiso</strong>.</p>' +
        '<a class="ic-b" href="' + WA + msgCotiza + '" target="_blank" rel="noopener">Solicitar cotización</a>' +
        '<small>Se abre WhatsApp con las preguntas ya escritas.</small>' +
      '</div>' +
    '</div>' +

    // --- Psicoterapia ---
    '<div class="ic-sec" id="terapia-detalle">' +
      '<p class="ic-k">Psicoterapia</p>' +
      '<h2>Adolescentes y juventudes</h2>' +
      '<p>Mi práctica clínica está dedicada <strong>exclusivamente</strong> a esta etapa. Enfoque <strong>cognitivo-conductual</strong>.</p>' +
      '<h3 class="ic-h3">Motivos frecuentes de consulta</h3>' +
      '<ul class="ic-lista">' + motivos.map(li).join('') + '</ul>' +
    '</div>' +

    // --- Formación ---
    '<div class="ic-sec" id="formacion-detalle">' +
      '<p class="ic-k">Formación</p>' +
      '<h2>Dónde me formé</h2>' +
      '<div class="ic-form">' +
        '<div><h3>Vía forense</h3><ol>' + forense.map(estudio).join('') + '</ol></div>' +
        '<div><h3>Vía clínica</h3><ol>' + clinica.map(estudio).join('') + '</ol></div>' +
      '</div>' +
    '</div>' +

    // --- Información general ---
    '<div class="ic-sec" id="general">' +
      '<p class="ic-k">Información general</p>' +
      '<h2>Consultorio y contacto</h2>' +
      '<div class="ic-datos">' +
        '<div>' +
          '<h3>Dirección</h3>' +
          '<address>Calle Mauricio Garcés 102<br>Col. La Joya<br>Santiago de Querétaro, Qro.</address>' +
          '<div class="ic-a">' +
            '<a class="ic-b" href="https://www.google.com/maps/dir/?api=1&destination=' + LAT + ',' + LNG + '" target="_blank" rel="noopener">Google Maps</a>' +
            '<a class="ic-b ic-b--o" href="https://waze.com/ul?ll=' + LAT + ',' + LNG + '&navigate=yes" target="_blank" rel="noopener">Waze</a>' +
          '</div>' +
        '</div>' +
        '<div>' +
          '<h3>Horarios</h3>' +
          '<ul>' + horarios.map(hora).join('') + '</ul>' +
          '<h3 style="margin-top:1.1rem">Contacto</h3>' +
          '<ul><li><span>Celular</span><span>442 830 6799</span></li>' +
          '<li><span>Cédula profesional</span><span>14661976</span></li>' +
          '<li><span>Consejo forense</span><span>25-08-63</span></li></ul>' +
          '<div class="ic-a">' +
            '<a class="ic-b" href="' + WA + msgGeneral + '" target="_blank" rel="noopener">' + iconoWA + 'WhatsApp</a>' +
            '<a class="ic-b ic-b--o" href="tel:' + TEL + '">Llamar</a>' +
          '</div>' +
        '</div>' +
      '</div>' +
    '</div>' +

    '</div>';

  // Va antes del pie o del enlace de vuelta, lo que aparezca primero
  var ancla = document.querySelector('footer, .pie, .volver');
  if (ancla) ancla.parentNode.insertBefore(s, ancla);
  else document.body.appendChild(s);
})();
