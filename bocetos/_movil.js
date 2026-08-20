/* ============================================================================
   Inyecta la barra inferior en los bocetos, para que en celular tengan la
   misma arquitectura que el sitio real: navegación en la zona del pulgar.
   El estilo lo pone _movil.css; el color, las variables de cada boceto.
   ========================================================================== */
(function () {
  if (document.querySelector('.mv')) return;

  var WA = 'https://wa.me/524428306799?text=' +
           encodeURIComponent('Hola Thania, vi tu página web y me gustaría agendar una cita.');
  var TEL = 'tel:+524428306799';

  var svg = {
    pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    tel: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M6.5 3h3l1.5 4.5-2 1.5a12 12 0 0 0 6 6l1.5-2 4.5 1.5v3a2 2 0 0 1-2.2 2A17.5 17.5 0 0 1 4.5 5.2 2 2 0 0 1 6.5 3Z"/></svg>',
    wa:  '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.2-1.4A10 10 0 1 0 12 2Zm5.5 14.2c-.2.6-1.2 1.1-1.7 1.2-.4 0-1 .1-1.6-.1-.4-.1-.8-.3-1.4-.5-2.5-1.1-4.1-3.6-4.2-3.7-.1-.2-1-1.3-1-2.5s.6-1.8.9-2.1c.2-.2.5-.3.6-.3h.5c.2 0 .4 0 .6.4l.7 1.8c.1.1.1.3 0 .4l-.2.4-.4.4c-.1.1-.2.3-.1.5.1.2.6 1 1.4 1.7.9.8 1.7 1.1 1.9 1.2s.4.1.5-.1l.8-1c.2-.2.3-.2.6-.1l1.7.8c.2.1.4.2.4.3 0 .1 0 .5-.2 1Z"/></svg>'
  };

  // Solo enlaza a "Consultorio" si el boceto tiene esa sección
  var hayMapa = !!document.getElementById('donde');

  var nav = document.createElement('nav');
  nav.className = 'mv';
  nav.setAttribute('aria-label', 'Acciones rápidas');
  nav.innerHTML =
    (hayMapa
      ? '<a class="mv__i" href="#donde">' + svg.pin + '<span>Consultorio</span></a>'
      : '<a class="mv__i" href="#">' + svg.pin + '<span>Inicio</span></a>') +
    '<a class="mv__wa" href="' + WA + '" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">' + svg.wa + '</a>' +
    '<a class="mv__i" href="' + TEL + '">' + svg.tel + '<span>Llamar</span></a>';

  document.body.appendChild(nav);
})();
