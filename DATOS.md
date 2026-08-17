# ✅ Lista de datos por rellenar

Todo lo que trae el sitio ahora es **contenido de ejemplo**. Ve tachando esta lista.

---

## 1. `assets/js/config.js` — lo más importante

Es el único archivo que controla contacto y mapa. Cámbialo y todo el sitio se actualiza solo.

| Campo | Qué poner | Ejemplo |
|---|---|---|
| `nombre` | Nombre completo con título | `Mtra. Ana López` |
| `profesion` | Cómo se presenta | `Psicóloga clínica` |
| `cedula` | Cédula profesional SEP | `12345678` |
| `whatsapp.numero` | **52 + 10 dígitos, solo números** | `524421234567` |
| `whatsapp.mensaje` | Texto que se autoescribe al abrir el chat | — |
| `telefono` | Teléfono para llamar | `+52 442 123 4567` |
| `email` | Correo de contacto | — |
| `consultorio.lat` / `.lng` | **Coordenadas exactas** (ver abajo) | `20.588793` |
| `consultorio.*` | Calle, colonia, ciudad, CP, referencia | — |
| `horarios` | Días y horas de atención | — |

### 📍 Cómo sacar las coordenadas exactas

1. Abre [Google Maps](https://maps.google.com).
2. Busca la dirección del consultorio.
3. **Clic derecho** justo sobre la puerta del consultorio.
4. Arriba del menú aparecen dos números, por ejemplo `20.588793, -100.389888`.
5. Cópialos: el **primero es `lat`**, el **segundo es `lng`**.

> Ponlos sin comillas, tal cual. El `lng` en México siempre lleva signo negativo.

---

## 2. `index.html` — los textos

Abre el archivo y busca `⚠️ EDITAR`. Cada aparición marca algo por cambiar:

- [ ] **`<title>` y `<meta description>`** — es lo que sale en Google. Incluye ciudad y especialidad.
- [ ] **Nombre en el encabezado** (aparece 2 veces: arriba y en el pie).
- [ ] **Titular principal (`<h1>`)** — debe decir **a quién ayuda**, no "bienvenido a mi sitio".
- [ ] **Las 4 tarjetas de servicios** — cámbialas por sus especialidades reales.
- [ ] **Biografía "Sobre mí"** — 3 o 4 frases contando *por qué* es psicóloga.
- [ ] **Lista de credenciales** — cédula, maestría, enfoque, idiomas.
- [ ] **Preguntas frecuentes** — sobre todo el **precio** y la política de cancelación.
- [ ] **Datos del bloque `application/ld+json`** (arriba del todo) — es la ficha que lee Google.

---

## 3. Fotografías — el punto más importante de todos

Ahora hay dos ilustraciones de relleno. **Hay que sustituirlas por fotos reales.**

Todas las guías de diseño para consultas de psicología coinciden en lo mismo: la foto
real de la profesional es el factor número uno de confianza, y las fotos de banco
(sillones vacíos, manos entrelazadas, gente sonriendo genéricamente) **restan**
credibilidad en lugar de sumarla.

| Archivo | Qué debe ser | Proporción |
|---|---|---|
| `assets/img/retrato.svg` | Retrato profesional, mirando a cámara | vertical 4:5 |
| `assets/img/consultorio.svg` | Foto del consultorio o una más informal de ella | vertical 3:4 |
| `assets/img/portada.jpg` | Imagen para cuando compartan el link en WhatsApp/redes | 1200 × 630 px |

> ⚠️ La portada **tiene que ser `.jpg` o `.png`**. WhatsApp y Facebook no leen SVG,
> así que hasta que la cambies el link se compartirá sin vista previa.

**Cómo sustituirlas:** guarda tus fotos como `.jpg` en `assets/img/` y cambia la ruta
en `index.html`. Por ejemplo, cambia esto:

```html
<img src="assets/img/retrato.svg" alt="Retrato de la Mtra. Valeria Fuentes...">
```

por esto:

```html
<img src="assets/img/retrato.jpg" alt="Retrato de la Mtra. Ana López, psicóloga clínica">
```

> Comprime las fotos antes de subirlas (en [squoosh.app](https://squoosh.app), gratis).
> Que ninguna pase de 300 KB o la página tardará en abrir en celular.

---

## 4. El día del lanzamiento — quitar el modo borrador

El sitio vive en **https://h0m10.github.io/psicologa/** y ahora mismo está en
modo borrador: **Google no lo indexa**, a propósito, porque anuncia una cédula
inventada. Cuando el contenido ya sea real:

- [ ] Borra la etiqueta `<meta name="robots" content="noindex, nofollow">` de `index.html`
- [ ] Sustituye `robots.txt` por la versión que viene comentada dentro del archivo
- [ ] Cambia `og:image` a un `.jpg` o `.png` real

---

## 5. Prueba antes de dar el link

- [ ] Toca el botón de WhatsApp **desde un celular** y confirma que abre el chat correcto.
- [ ] Toca "Google Maps", "Waze" y "Apple Maps" y confirma que la ruta cae en la puerta correcta.
- [ ] Ábrelo en un celular chico y revisa que nada se salga de la pantalla.
- [ ] Revisa que el número de la Línea de la Vida en el pie siga vigente.
