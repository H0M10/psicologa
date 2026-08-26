# Bitácora de los bocetos

> Cuaderno de trabajo. Qué significa «nivel de detalle», en qué estado está
> cada uno de los veinte y qué falta. Se actualiza conforme avanzo.

---

## 1. Qué es «el nivel de detalle»

La referencia es el sitio en marcha: **https://h0m10.github.io/psicologa/**
Un boceto está al nivel cuando tiene las trece piezas siguientes.

### Contenido (§6 de ANALISIS.md)

| # | Pieza | Nota |
|---|---|---|
| 1 | Las siete secciones | Portada, sobre mí, forense, psicoterapia, formación, consultorio, cierre |
| 2 | Los 7 supuestos periciales | En su propia maquetación, no en un bloque genérico |
| 3 | Metapericiales con su descripción | |
| 4 | Los 10 motivos de consulta | |
| 5 | Los 10 registros de formación | En dos vías |
| 6 | Credenciales | Cédula 14661976 y consejo forense 25-08-63 |
| 7 | Horarios con el doble turno | |

### Interacción y arquitectura móvil

| # | Pieza | Nota |
|---|---|---|
| 8 | **Barra inferior con scrollspy** | Navegación visible en la zona del pulgar; la pestaña se ilumina sola |
| 9 | **Formulario de cotización** | Formulario real con validación y vista previa; envía por WhatsApp |
| 10 | **Biografía plegable** | Solo en celular; sin JavaScript se ve completa |
| 11 | **Mapa con escudo táctil** | Para que arrastrar el dedo no secuestre el scroll |
| 12 | Botones de Google Maps y Waze | Instrucción explícita de Thania |
| 13 | Llamada directa y WhatsApp | Instrucción explícita de Thania |

---

## 2. Estado actual

### Fase 1 — completada

Se construyeron dos módulos compartidos que levantan los veinte de golpe:

- **`_detalle.css` + `_detalle.js`** — barra de pestañas con scrollspy, formulario
  de cotización y biografía plegable. Se arman leyendo las secciones que cada
  boceto realmente tiene, y se tiñen con las variables que ya define
  (`--mv-bg`, `--mv-fg`, `--mv-acc`, `--mv-line`).
- **`_completo.css` + `_completo.js`** — bloque provisional con el contenido que
  a los bocetos 01–10 les faltaba. **Es un parche**, no la solución: se ve como
  un añadido. La fase 2 lo sustituye por contenido nativo.

La galería pasa a destacar arriba el sitio en marcha, a todo el ancho, como
referencia de nivel.

### Fase 2 — en curso

Reescribir los bocetos **01 a 10** para que lleven el contenido en su propia
maquetación y puedan soltar `_completo.js`.

| # | Boceto | Contenido nativo | Barra + spy | Formulario | Bio plegable |
|---|---|---|---|---|---|
| 01 | Mid-century | ✅ **nativo** | ✅ | ✅ | ✅ |
| 02 | Editorial | ⏳ pendiente | ✅ | ✅ | ✅ |
| 03 | Botánico | ⏳ pendiente | ✅ | ✅ | ✅ |
| 04 | Modular | ⏳ pendiente | ✅ | ✅ | ✅ |
| 05 | Suizo | ⏳ pendiente | ✅ | ✅ | ✅ |
| 06 | Nocturno | ⏳ pendiente | ✅ | ✅ | ✅ |
| 07 | Risografía | ⏳ pendiente | ✅ | ✅ | ✅ |
| 08 | Art Déco | ⏳ pendiente | ✅ | ✅ | ✅ |
| 09 | Cobalto | ⏳ pendiente | ✅ | ✅ | ✅ |
| 10 | Acuarela | ⏳ pendiente | ✅ | ✅ | ✅ |
| 11 | Dos expedientes | ✅ | ✅ | ✅ | ✅ |
| 12 | Salvia | ✅ | ✅ | ✅ | ✅ |
| 13 | Taupe y jade | ✅ | ✅ | ✅ | ✅ |
| 14 | Coral solar | ✅ | ✅ | ✅ | ✅ |
| 15 | Vino y niebla | ✅ | ✅ | ✅ | ✅ |
| 16 | Azul polvo | ✅ | ✅ | ✅ | ✅ |
| 17 | Despacho | ✅ | ✅ | ✅ | ✅ |
| 18 | Clínica | ✅ | ✅ | ✅ | ✅ |
| 19 | Consultorio | ✅ | ✅ | ✅ | ✅ |
| 20 | Ficha profesional | ✅ | ✅ | ✅ | ✅ |

**Faltan diez**, del 01 al 10.

---

## 3. Criterios que se mantienen en todos

Vienen de la investigación acumulada. Nada de esto se negocia por estética.

- **Nada inventado.** Si no está en el documento de Thania, no está en el sitio.
- **Medida de línea entre 50 y 75 caracteres.** Pasando de 80 la gente deja de leer.
- **Objetivos táctiles de 44–48 px** como mínimo, con 8 px de separación.
- **Encabezados descriptivos**, porque la vista se fija en ellos y se salta el
  texto intermedio.
- **`prefers-reduced-motion` respetado**, `:focus-visible` visible, nunca
  `transition: all`.
- **Sin morado saturado, sin rojo dominante, sin amarillo brillante en cantidad,
  sin negro pesado.**
- **En celular**: las rotaciones y los solapes se anulan, y los botones van a
  todo el ancho.

---

## 4. Pendientes que no dependen de mí

1. **Coordenada exacta del consultorio.** El pin cae en la calle, no en el número.
2. **El número de la calle.** El documento dice #102; la última indicación dice 808.
   Ahora mismo está el 808.
3. **Fecha de la licenciatura.** El documento la trae invertida.
4. **Código postal.** Se usa 76180.
5. **Fotografías.** Siguen las ilustraciones de relleno.
6. ~~El número de WhatsApp de pruebas.~~ Resuelto: ya está el de Thania, 442 137 5118.

---

## 5. Corrección sobre el morado

Una observación de campo obligó a matizar lo que había escrito en ANALISIS.md.
Se visitaron varias páginas reales de psicólogos y **varias usan morado**, con
letras en negro y cafés tenues. Tenían razón: mi conclusión anterior era
demasiado tajante.

### Lo que dice la investigación

- Los tonos **lavanda y violeta puntúan más alto en «confianza emocional
  percibida»** que cualquier otra familia, según investigación de psicología
  del diseño.
- El **malva** —morado con subtono gris o rosa— equilibra tranquilidad y
  profundidad. Estudios de yoga, apps de salud mental y marcas de cuidado lo
  usan justamente por eso.
- **Morado con teal** favorece la conciencia y la calma; se recomienda
  específicamente para terapeutas de trauma.

### Dónde estaba el error

La distinción no es *morado sí o morado no*, sino **cuál**:

| Registro | Ejemplo | Veredicto |
|---|---|---|
| Morado saturado sobre blanco | `#8B5CF6` (violeta de Tailwind) | Es el tell de diseño generado por IA |
| Malva apagado con neutros | `#9B8AA6`, `#B5A0AE` | Legítimo y bien respaldado |
| Amatista sobria | `#9966CC` bien dosificado | Espiritualidad y sofisticación |

Y el **café tenue** que observaron encaja: el malva comparte subtono cálido
con los cafés apagados, así que la combinación tiene fundamento, no es casual.

### Qué hacer con esto

Ninguno de los veinte usa hoy la familia malva. Es un hueco real de la
propuesta y conviene cubrirlo con un boceto propio: **malva apagado + café
tenue + negro para el texto**, exactamente lo que vieron funcionando.
Queda propuesto, pendiente de luz verde.
