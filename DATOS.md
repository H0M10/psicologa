# ✅ Lista de lo que falta

Los datos de contacto, formación y servicios de Thania **ya están cargados**.
Esto es lo que queda pendiente antes de publicar.

---

## 1. 📍 Afinar la coordenada del mapa — lo más importante

El pin cae sobre **Calle Mauricio Garcés**, pero **no sobre el número 102**.
El callejero abierto de OpenStreetMap no tiene números en esa calle, así que
solo conoce la calle entera (unos 157 metros).

**Cómo arreglarlo:**

1. Abre [Google Maps](https://maps.google.com) y busca la dirección.
2. **Clic derecho** justo sobre la puerta del consultorio.
3. Arriba del menú aparecen dos números, por ejemplo `20.572439, -100.418402`.
4. Cópialos en `assets/js/config.js` → `consultorio.lat` y `consultorio.lng`.

> Para un consultorio, que el pin caiga en la puerta correcta importa mucho.

---

## 2. 📷 Las fotos

Hay dos ilustraciones de relleno. Las guías de sitios de terapeutas coinciden:
la foto real es el factor número uno de confianza, y las fotos de banco restan.

| Archivo | Qué debe ser | Proporción |
|---|---|---|
| `assets/img/retrato.svg` | Retrato profesional de Thania | vertical 4:5 |
| `assets/img/consultorio.svg` | Foto del consultorio, o una más informal | vertical 3:4 |
| `assets/img/portada.svg` | Para cuando compartan el link | 1200 × 630 px |

**Cómo sustituirlas:** guarda tus fotos como `.jpg` en `assets/img/` y cambia
la ruta en `index.html`. Comprímelas antes en [squoosh.app](https://squoosh.app);
que ninguna pase de 300 KB.

> ⚠️ La de portada **tiene que ser `.jpg` o `.png`**. WhatsApp y Facebook no
> leen SVG, así que hasta cambiarla el link se comparte sin miniatura.

---

## 3. 🔍 Dudas sobre los datos que mandaron

- [ ] **Código postal.** No venía en la información. Puse **76180**, que es el
      que OpenStreetMap asigna a Calle Mauricio Garcés. ¿Es correcto?
- [ ] **Fecha de la licenciatura.** En la sección de psicología forense decía
      *"Agosto 2024 – mayo 2024"*, que va al revés. En la de psicoterapia decía
      *"Agosto 2020 – mayo 2024"*. Usé esta segunda, que es la que cuadra.
- [ ] **Correo electrónico.** No venía ninguno, así que el pie solo muestra
      WhatsApp y teléfono. Si quiere añadirlo, va en `config.js` → `email`.

---

## 4. 📝 Sobre el formulario de cotización

Preguntaban si añadir un botón a un formulario. **Sí, y ya está puesto**, pero
resuelto sin formulario: el botón **"Solicitar cotización"** abre WhatsApp con
las preguntas ya escritas.

```
• Tipo de servicio: (pericial en materia familiar / metapericial / no estoy seguro)
• Materia o juzgado:
• Breve descripción del asunto:
• ¿Hay una fecha límite?:
```

**Por qué así y no un formulario de verdad:** el sitio es estático en GitHub
Pages, no tiene servidor, así que un formulario necesitaría contratar un
servicio aparte. Además, por WhatsApp la conversación empieza de inmediato y
ella ya recibe ahí todo lo demás.

**Si prefiere un formulario real** hay dos caminos, ambos gratis:

| Opción | Ventaja | Desventaja |
|---|---|---|
| **Google Forms** | Respuestas ordenadas en una hoja de cálculo | Saca al visitante del sitio |
| **Formspree** | Se ve integrado, llega por correo | Límite de 50 envíos al mes gratis |

Para cambiarlo, edita el texto en `config.js` → `whatsapp.mensajeCotizacion`.

---

## 5. 🚀 El día del lanzamiento

- [ ] Borrar `<meta name="robots" content="noindex, nofollow">` de `index.html`
- [ ] Sustituir `robots.txt` por la versión que viene comentada dentro
- [ ] Cambiar `og:image` a un `.jpg` o `.png` real

---

## 6. ✔️ Probar antes de dar el link

- [ ] Tocar el botón de WhatsApp **desde un celular** y ver que abre el chat de Thania
- [ ] Tocar **"Solicitar cotización"** y comprobar que el mensaje llega con las preguntas
- [ ] Tocar Google Maps, Waze y Apple Maps y ver que la ruta cae en la puerta
- [ ] Abrirlo en un celular chico y revisar que nada se salga de la pantalla
- [ ] Confirmar que el número de la Línea de la Vida del pie siga vigente
