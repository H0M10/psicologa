# Consultorio 1962 — sitio para psicóloga

Página puente de una sola pantalla: informa, genera confianza y manda al cliente
a **WhatsApp** o al **mapa del consultorio**. Sin login, sin registro, sin
formularios y sin base de datos.

HTML, CSS y JavaScript puros. Sin compilación, sin dependencias que instalar.
Se sube tal cual a GitHub Pages.

---

## Qué incluye

- **Portada** con titular, foto y botón de WhatsApp visible sin hacer scroll.
- **Motivos de consulta** en cuatro tarjetas.
- **Biografía** con formación y enfoque.
- **Cómo es la primera sesión**, en tres pasos, para bajar la ansiedad de agendar.
- **Preguntas frecuentes** desplegables (precio, frecuencia, confidencialidad…).
- **Mapa interactivo** con marcador propio y botones a Google Maps, Waze y Apple Maps.
- **Botón flotante de WhatsApp** que aparece al hacer scroll.
- Ficha de negocio local para Google (`schema.org/Psychologist`), `sitemap.xml` y `robots.txt`.
- Aviso responsable con la línea de crisis en el pie.

---

## El diseño

**Mid-century modern**, la estética de mobiliario y gráfica de los años 50–60:
formas geométricas planas, arcos tipo Palm Springs, estrellas atómicas, contornos
marcados y sombras sólidas desplazadas.

**Paleta "Teak & Teal"**, adaptada a un contexto de salud mental:

| Color | Hex | Uso |
|---|---|---|
| Teal profundo | `#2F6F73` | Color principal: transmite calma y confianza |
| Terracota | `#B9532F` | Botones y llamadas a la acción |
| Mostaza | `#D9A63C` | Acentos y detalles decorativos |
| Oliva | `#6E7F52` | WhatsApp y elementos secundarios |
| Crema papel | `#F4EADB` | Fondo, con una textura sutil de grano |
| Espresso | `#2E2622` | Texto y contornos |

Todas las combinaciones de texto cumplen contraste **WCAG AA**.

**Tipografía:** [Fraunces](https://fonts.google.com/specimen/Fraunces) para títulos
(serif variable con ejes `SOFT` y `WONK`, que le dan ese aire retro y cálido) y
[Jost](https://fonts.google.com/specimen/Jost) para el texto (geométrica, muy
cercana a la Futura de la época).

---

## Ver la página en tu computadora

Necesitas un servidor local, porque abrir el archivo con doble clic hace que
algunas cosas no carguen bien.

```bash
# con Node
npx serve .

# o con Python
python -m http.server 8000
```

Luego abre `http://localhost:8000`.

---

## Personalizarla

👉 **Sigue la lista de [DATOS.md](DATOS.md).** Ahí está todo lo que hay que cambiar,
paso a paso.

En resumen:

1. `assets/js/config.js` → teléfono, WhatsApp, dirección y coordenadas del mapa.
2. `index.html` → los textos (busca las marcas `⚠️ EDITAR`).
3. `assets/img/` → sustituir las ilustraciones de relleno por fotos reales.

---

## Publicar en GitHub Pages

### Primera vez

```bash
git init
git add .
git commit -m "Sitio de la psicóloga"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git push -u origin main
```

Después, en GitHub:

1. Entra al repositorio → **Settings** → **Pages**.
2. En *Source*, elige **Deploy from a branch**.
3. Branch: **`main`**, carpeta: **`/ (root)`** → **Save**.
4. Espera un par de minutos. La página queda en
   `https://TU-USUARIO.github.io/TU-REPO/`.

### Cada vez que cambies algo

```bash
git add .
git commit -m "Actualizo horarios"
git push
```

GitHub Pages se actualiza solo en menos de un minuto.

### Dominio propio (opcional)

Si compran un dominio como `psicologaanalopez.com`:

1. Crea un archivo llamado `CNAME` (sin extensión) en la raíz, con el dominio dentro.
2. En el panel del dominio, apunta los registros `A` a las IP de GitHub Pages.
3. En **Settings → Pages**, escribe el dominio y activa **Enforce HTTPS**.

---

## Estructura

```
.
├── index.html              ← toda la página (los textos van aquí)
├── 404.html
├── .nojekyll               ← evita que GitHub procese el sitio con Jekyll
├── robots.txt
├── sitemap.xml
├── DATOS.md                ← lista de lo que hay que rellenar
└── assets/
    ├── css/styles.css      ← todo el diseño
    ├── js/config.js        ← ⭐ datos de contacto y del mapa
    ├── js/main.js          ← lógica (no hace falta tocarlo)
    └── img/                ← imágenes de relleno, sustituir por fotos reales
```

---

## Notas técnicas

- **Mapa:** [Leaflet](https://leafletjs.com) 1.9.4 con teselas de OpenStreetMap.
  Gratis y **sin API key**, a diferencia de Google Maps Embed. Si el CDN llegara a
  fallar, aparece un aviso con un enlace directo a Google Maps.
- **Sin scroll-jack:** la rueda del ratón no hace zoom en el mapa salvo que hagas
  clic en él primero, para no atrapar el scroll de la página.
- **Accesibilidad:** navegación por teclado, `:focus-visible` visible, enlace para
  saltar al contenido, etiquetas ARIA y respeto a `prefers-reduced-motion`.
- **Rendimiento:** sin frameworks. El sitio pesa unos pocos KB más las fuentes.

---

## Aviso

El sitio incluye en el pie el número de la **Línea de la Vida (800 911 2000)**.
Conviene verificar que siga vigente antes de publicar, y confirmar con la
psicóloga cualquier afirmación sobre credenciales o resultados terapéuticos.
