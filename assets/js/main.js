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
  ['btnTel', 'pieTel', 'barraTel'].forEach(function (id) {
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
  /* 5. Menú móvil                                                      */
  /* ------------------------------------------------------------------ */
  var btnMenu = document.getElementById('btnMenu');
  var nav = document.getElementById('nav');

  if (btnMenu && nav) {
    var alternar = function (abrir) {
      var estado = abrir !== undefined ? abrir : !nav.classList.contains('is-open');
      nav.classList.toggle('is-open', estado);
      btnMenu.setAttribute('aria-expanded', String(estado));
      btnMenu.setAttribute('aria-label', estado ? 'Cerrar menú' : 'Abrir menú');
      document.body.style.overflow = estado ? 'hidden' : '';
    };

    btnMenu.addEventListener('click', function () { alternar(); });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) alternar(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) alternar(false);
    });
  }

  /* ------------------------------------------------------------------ */
  /* 6. Encabezado al hacer scroll + botón flotante                     */
  /* ------------------------------------------------------------------ */
  var header = document.getElementById('header');
  var flotante = document.getElementById('waFlotante');
  var barra = document.querySelector('.barra-movil');
  var ticking = false;

  function alScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle('is-stuck', y > 24);
    // Aparecen cuando el botón de la portada ya se fue de pantalla
    if (flotante) flotante.classList.toggle('is-on', y > 520);
    if (barra) barra.classList.toggle('is-on', y > 420);
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
