/* ============================================================================
   FORMULARIO DE COTIZACIÓN
   ----------------------------------------------------------------------------
   Responde a la pregunta de Thania: «¿AGREGAR UN BOTÓN QUE LOS LLEVE A UN
   FORMULARIO?».

   Es un formulario de verdad —campos, etiquetas, validación— pero no necesita
   servidor: al enviarlo arma un mensaje ordenado y lo abre en su WhatsApp.
   Así ella recibe la información estructurada, que es lo que un formulario le
   daría, sin depender de ningún servicio de terceros ni de un backend.

   Si algún día quiere que las respuestas caigan en una hoja de cálculo, basta
   con cambiar el envío a Google Forms o Formspree; el formulario ya está hecho.
   ========================================================================== */
(function () {
  var form = document.getElementById('formCotiza');
  if (!form) return;

  var CFG = window.SITE_CONFIG || {};
  var numero = String((CFG.whatsapp || {}).numero || '').replace(/\D/g, '');
  var salida = document.getElementById('formSalida');

  // Etiqueta legible para cada campo, en el orden en que se envía
  var CAMPOS = [
    ['servicio',    'Tipo de servicio'],
    ['nombre',      'Nombre'],
    ['materia',     'Materia o juzgado'],
    ['descripcion', 'Descripción del asunto'],
    ['plazo',       'Fecha límite']
  ];

  function construirMensaje() {
    var d = new FormData(form);
    var lineas = ['Hola Thania, quisiera solicitar una cotización.', ''];
    CAMPOS.forEach(function (c) {
      var v = (d.get(c[0]) || '').toString().trim();
      if (v) lineas.push('• ' + c[1] + ': ' + v);
    });
    return lineas.join('\n');
  }

  // Vista previa en vivo: se ve exactamente qué se va a enviar
  function actualizarVista() {
    if (!salida) return;
    salida.textContent = construirMensaje();
  }
  form.addEventListener('input', actualizarVista);
  form.addEventListener('change', actualizarVista);
  actualizarVista();

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    // Validación del navegador, con el foco en el primer campo con error
    if (!form.checkValidity()) {
      var malo = form.querySelector(':invalid');
      if (malo) malo.focus();
      form.reportValidity();
      return;
    }

    var url = 'https://wa.me/' + numero + '?text=' + encodeURIComponent(construirMensaje());
    window.open(url, '_blank', 'noopener');

    var aviso = document.getElementById('formAviso');
    if (aviso) {
      aviso.textContent = 'Se abrió WhatsApp con tus respuestas. Si no se abrió, revisa que tu navegador no haya bloqueado la ventana.';
      aviso.hidden = false;
    }
  });
})();
