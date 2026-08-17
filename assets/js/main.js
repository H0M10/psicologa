/* ============================================================================
   main.js — Lógica del sitio
   ----------------------------------------------------------------------------
   No necesitas tocar este archivo. Todos los datos salen de config.js
   ========================================================================== */
(function () {
  'use strict';

  var CFG = window.SITE_CONFIG || {};
  var C = CFG.consultorio || {};
  var LAT = C.lat, LNG = C.lng;

  /* ------------------------------------------------------------------ */
  /* 1. Enlaces de WhatsApp                                             */
  /* ------------------------------------------------------------------ */
  function enlaceWhatsApp() {
    var wa = CFG.whatsapp || {};
    var num = String(wa.numero || '').replace(/\D/g, '');
    var url = 'https://wa.me/' + num;
    if (wa.mensaje) url += '?text=' + encodeURIComponent(wa.mensaje);
    return url;
  }

  var urlWA = enlaceWhatsApp();
  Array.prototype.forEach.call(document.querySelectorAll('[data-wa]'), function (a) {
    a.href = urlWA;
    a.target = '_blank';
  });

  /* ------------------------------------------------------------------ */
  /* 2. Datos de config.js → DOM                                        */
  /* ------------------------------------------------------------------ */
  var mapaCfg = {
    nombre: CFG.nombre,
    nombreCorto: CFG.nombreCorto || CFG.nombre,
    profesion: CFG.profesion,
    cedula: CFG.cedula,
    calle: C.calle,
    colonia: C.colonia,
    ciudad: C.ciudad,
    cp: C.cp,
    referencia: C.referencia
  };

  Array.prototype.forEach.call(document.querySelectorAll('[data-cfg]'), function (el) {
    var v = mapaCfg[el.getAttribute('data-cfg')];
    if (v) el.textContent = v;
  });

  // Teléfono y correo
  var tel = String(CFG.telefono || '').replace(/[^\d+]/g, '');
  // Vista previa del mensaje: enseñar exactamente qué se va a enviar
  // quita incertidumbre, que es la fricción principal al agendar
  var preview = document.getElementById('waPreview');
  if (preview && CFG.whatsapp && CFG.whatsapp.mensaje) {
    preview.textContent = CFG.whatsapp.mensaje;
  }

  ['btnTel', 'pieTel', 'llamarMovil', 'agendarTel'].forEach(function (id) {
    var el = document.getElementById(id);
    if (el && tel) el.href = 'tel:' + tel;
  });
  var mail = document.getElementById('pieMail');
  if (mail && CFG.email) mail.href = 'mailto:' + CFG.email;

  // Año actual en el pie
  var anio = document.getElementById('anio');
  if (anio) anio.textContent = new Date().getFullYear();

  // Horarios
  var ulHorarios = document.getElementById('horarios');
  if (ulHorarios && Array.isArray(CFG.horarios)) {
    ulHorarios.innerHTML = CFG.horarios.map(function (h) {
      return '<li><span>' + h.dias + '</span><span>' + h.horas + '</span></li>';
    }).join('');
  }

  /* ------------------------------------------------------------------ */
  /* 3. Enlaces de navegación (Google Maps / Waze / Apple Maps)          */
  /* ------------------------------------------------------------------ */
  var direccionTxt = [C.calle, C.colonia, C.ciudad, C.cp].filter(Boolean).join(', ');
  var coords = LAT + ',' + LNG;

  var rutas = {
    google: 'https://www.google.com/maps/dir/?api=1&destination=' + encodeURIComponent(coords),
    waze:   'https://waze.com/ul?ll=' + encodeURIComponent(coords) + '&navigate=yes',
    apple:  'https://maps.apple.com/?daddr=' + encodeURIComponent(coords) + '&q=' + encodeURIComponent(C.nombre || 'Consultorio')
  };

  [['rutaGoogle', 'google'], ['rutaGoogle2', 'google'], ['pieMapa', 'google'],
   ['rutaWaze', 'waze'], ['rutaApple', 'apple']].forEach(function (par) {
    var el = document.getElementById(par[0]);
    if (el) el.href = rutas[par[1]];
  });

  /* ------------------------------------------------------------------ */
  /* 4. Mapa interactivo (Leaflet + OpenStreetMap)                      */
  /* ------------------------------------------------------------------ */
  var cajaMapa = document.getElementById('mapa');
  var fallback = document.getElementById('mapaFallback');
  var escudo   = document.getElementById('mapaToque');

  // ¿Pantalla táctil? Entonces el mapa arranca bloqueado, porque si no
  // arrastrar el dedo mueve el mapa en vez de desplazar la página.
  var esTactil = window.matchMedia('(pointer: coarse)').matches;

  if (cajaMapa) {
    if (typeof L === 'undefined' || typeof LAT !== 'number' || typeof LNG !== 'number') {
      if (fallback) fallback.classList.add('is-on');
    } else {
      try {
        var mapa = L.map('mapa', {
          center: [LAT, LNG],
          zoom: C.zoom || 16,
          scrollWheelZoom: false,   // evita capturar el scroll de la página
          dragging: !esTactil,      // en celular se activa al tocar el escudo
          attributionControl: true
        });

        if (esTactil && escudo) {
          escudo.hidden = false;
          escudo.addEventListener('click', function () {
            mapa.dragging.enable();
            escudo.classList.add('se-va');
            setTimeout(function () { escudo.hidden = true; }, 400);
          });
        }

        // Ctrl/⌘ + rueda sí hace zoom (comportamiento esperado en escritorio)
        mapa.on('focus', function () { mapa.scrollWheelZoom.enable(); });
        mapa.on('blur',  function () { mapa.scrollWheelZoom.disable(); });

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
          attribution: '&copy; colaboradores de <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(mapa);

        // Marcador con estilo mid-century
        var pin = L.divIcon({
          className: '',
          html: '<div class="pin"><div class="pin__cuerpo"></div><div class="pin__pulso"></div></div>',
          iconSize: [40, 52],
          iconAnchor: [20, 46],
          popupAnchor: [0, -44]
        });

        L.marker([LAT, LNG], { icon: pin, title: C.nombre || 'Consultorio', riseOnHover: true })
          .addTo(mapa)
          .bindPopup(
            '<b>' + (C.nombre || 'Consultorio') + '</b>' +
            direccionTxt +
            '<br><a href="' + rutas.google + '" target="_blank" rel="noopener">Cómo llegar &rarr;</a>'
          )
          .openPopup();

        // Recentrar bien cuando la sección entra en pantalla
        setTimeout(function () { mapa.invalidateSize(); }, 400);
        window.addEventListener('resize', function () { mapa.invalidateSize(); });

      } catch (e) {
        if (fallback) fallback.classList.add('is-on');
      }
    }
  }

  /* ------------------------------------------------------------------ */
  /* 5. Barra de pestañas: marcar la sección en la que estás            */
  /* ------------------------------------------------------------------ */
  var pestanas = document.querySelectorAll('.tabbar__item[data-spy]');

  if (pestanas.length && 'IntersectionObserver' in window) {
    var porId = {};
    var secciones = [];

    Array.prototype.forEach.call(pestanas, function (p) {
      var id = p.getAttribute('data-spy');
      var sec = document.getElementById(id);
      if (sec) { porId[id] = p; secciones.push(sec); }
    });

    var visibles = {};

    var espia = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) {
        visibles[en.target.id] = en.isIntersecting ? en.intersectionRatio : 0;
      });

      // Gana la sección que más superficie ocupa en pantalla
      var mejorId = null, mejor = 0;
      Object.keys(visibles).forEach(function (id) {
        if (visibles[id] > mejor) { mejor = visibles[id]; mejorId = id; }
      });

      Array.prototype.forEach.call(pestanas, function (p) {
        p.classList.toggle('is-activo', p.getAttribute('data-spy') === mejorId);
        if (p.getAttribute('data-spy') === mejorId) {
          p.setAttribute('aria-current', 'true');
        } else {
          p.removeAttribute('aria-current');
        }
      });
    }, {
      threshold: [0, .15, .35, .6, .9],
      rootMargin: '-72px 0px -45% 0px'   // descuenta encabezado y barra inferior
    });

    secciones.forEach(function (s) { espia.observe(s); });
  }

  /* Al llegar a "Agendar", el botón central se resalta: la acción que toca */
  var secAgendar = document.getElementById('agendar');
  var waTab = document.querySelector('.tabbar__wa');

  if (secAgendar && waTab && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (ent) {
      waTab.classList.toggle('is-llamando', ent[0].isIntersecting);
    }, { threshold: .25 }).observe(secAgendar);
  }

  /* ------------------------------------------------------------------ */
  /* 5b. Biografía plegable (solo donde la barra inferior está activa)  */
  /* ------------------------------------------------------------------ */
  var bioMas = document.getElementById('bioMas');
  var bioBtn = document.getElementById('bioBtn');

  if (bioMas && bioBtn) {
    var esMovil = window.matchMedia('(max-width: 760px)');

    var prepararBio = function () {
      if (esMovil.matches) {
        // La clase la pone el JS: sin JS el texto se ve completo
        bioMas.classList.add('js-plegable');
        bioBtn.hidden = false;
      } else {
        bioMas.classList.remove('js-plegable', 'esta-abierto');
        bioBtn.hidden = true;
        bioBtn.setAttribute('aria-expanded', 'false');
        bioBtn.querySelector('.mas__btn-txt').textContent = 'Leer más';
      }
    };

    prepararBio();
    if (esMovil.addEventListener) esMovil.addEventListener('change', prepararBio);

    bioBtn.addEventListener('click', function () {
      var abierto = bioMas.classList.toggle('esta-abierto');
      bioBtn.setAttribute('aria-expanded', String(abierto));
      bioBtn.querySelector('.mas__btn-txt').textContent = abierto ? 'Leer menos' : 'Leer más';
    });
  }

  /* ------------------------------------------------------------------ */
  /* 6. Encabezado al hacer scroll + botón flotante                     */
  /* ------------------------------------------------------------------ */
  var header = document.getElementById('header');
  var flotante = document.getElementById('waFlotante');
  var ticking = false;

  function alScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle('is-stuck', y > 24);
    // Solo el flotante de escritorio: la barra de pestañas está siempre visible
    if (flotante) flotante.classList.toggle('is-on', y > 520);
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(alScroll); ticking = true; }
  }, { passive: true });
  alScroll();

  /* ------------------------------------------------------------------ */
  /* 7. Revelado progresivo                                             */
  /* ------------------------------------------------------------------ */
  var elementos = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window) ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    Array.prototype.forEach.call(elementos, function (el) { el.classList.add('is-visible'); });
  } else {
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('is-visible');
          obs.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    Array.prototype.forEach.call(elementos, function (el) { obs.observe(el); });
  }

  /* ------------------------------------------------------------------ */
  /* 8. Una sola pregunta abierta a la vez                              */
  /* ------------------------------------------------------------------ */
  var faqs = document.querySelectorAll('.faq__item');
  Array.prototype.forEach.call(faqs, function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      Array.prototype.forEach.call(faqs, function (otro) {
        if (otro !== d) otro.open = false;
      });
    });
  });

})();
