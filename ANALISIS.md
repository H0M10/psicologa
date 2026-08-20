# Análisis de la información entregada por Thania Huerta Pacheco

> Documento de trabajo · Agosto 2026
> Inventario literal de lo que mandó, instrucciones detectadas, inconsistencias
> encontradas, decisiones tomadas y lista de verificación para los bocetos.

---

## 1. Instrucciones explícitas

En el documento hay **tres frases en mayúsculas**. No son información: son
encargos. Se tratan como requisitos obligatorios, no como sugerencias.

| # | Instrucción textual | Dónde aparece | Estado |
|---|---|---|---|
| **A** | «INCLUIR EL MAPA Y LOS BOTONES CON LA OPCIÓN EN WAZE Y GOOGLE MAPS» | Bajo *Dirección* | Obligatorio |
| **B** | «INCLUIR UN BOTÓN QUE LOS LLEVE A MI WHATTSAP» | Bajo *Celular* | Obligatorio |
| **C** | «¿AGREGAR UN BOTÓN QUE LOS LLEVE A UN FORMULARIO?» | Tras la nota de costo | **Pregunta abierta** |

### Sobre la instrucción C — el formulario

Es la única redactada como pregunta, así que pide una respuesta, no una
ejecución ciega.

**Contexto técnico:** el sitio es estático y vive en GitHub Pages. No tiene
servidor. Un formulario HTML por sí solo no envía nada a ningún lado; hace
falta un servicio externo que reciba los datos.

**Opciones reales:**

| Opción | Cómo funciona | A favor | En contra |
|---|---|---|---|
| **WhatsApp con texto previo** | El botón abre el chat con las preguntas ya escritas | Cero fricción, sin costo, sin servidor, la conversación arranca sola | Las respuestas no quedan ordenadas en una tabla |
| **Google Forms** | Enlace a un formulario de Google | Gratis, respuestas en hoja de cálculo | Saca al visitante del sitio, se siente ajeno |
| **Formspree / Netlify Forms** | Formulario propio, envío a un servicio | Se ve integrado, llega por correo | Límite gratuito (~50/mes), otro servicio que mantener |

**Decisión tomada, y por qué.** Se implementó **WhatsApp con texto previo**,
porque ella ya recibe todo lo demás por ahí (instrucción B) y porque en un
asunto legal la persona suele querer hablar, no llenar campos. El botón dice
*«Solicitar cotización»* y abre el chat con esto ya escrito:

```
Hola Thania, quisiera solicitar una cotización.

• Tipo de servicio:
• Materia o juzgado:
• Breve descripción del asunto:
• ¿Hay una fecha límite?:
```

Así ella recibe la información mínima de entrada, que es lo que un formulario
le daría, sin depender de terceros.

> **Falta su visto bueno.** Si prefiere un formulario de verdad, se cambia a
> Google Forms en unos minutos.

---

## 2. Inventario literal de la información

### 2.1 Datos de contacto y ubicación

| Dato | Valor | Notas |
|---|---|---|
| Dirección | Calle Mauricio Garcés **#102**, Col. La Joya, Querétaro, Qro. | Sin código postal |
| Celular | 442 137 5118 | Sirve para llamada y WhatsApp |
| Cédula profesional | 14661976 | |
| Registro Consejo Certificador en Psicología Forense | 25-08-63 | Credencial específica del área forense |
| Correo | — | **No lo proporcionó** |

### 2.2 Horarios

| Día | Turno 1 | Turno 2 |
|---|---|---|
| Lunes a viernes | 9:00 – 14:00 | 16:00 – 21:00 |
| Sábado | 9:00 – 13:00 | — |
| Domingo | Cerrado | — |

> **Detalle de diseño:** el doble turno de lunes a viernes no cabe en una
> tabla de dos columnas sin quedar raro. Se resuelve con una segunda línea
> continuada, sin repetir el nombre del día.

### 2.3 Psicología forense — servicios

**Periciales psicológicas en materia familiar** (7 supuestos, textuales):

1. Guard**i**a y custodia ← *ver §3.2*
2. Establecimiento o modificación de regímenes de convivencia
3. Valoración de competencias y habilidades parentales
4. Conflictos derivados de una separación o divorcio
5. Interferencias parentales
6. Identificación de factores de riesgo y protección
7. Afectaciones psicológicas

**Metapericiales o análisis técnicos de dictámenes psicológicos.** Descripción
textual: revisión de peritajes de otros profesionales para valorar metodología,
cumplimiento de criterios científicos, técnicos y éticos, pertinencia de los
instrumentos y su relación con resultados y conclusiones.

**Nota de costo (textual):** cada asunto es diferente y requiere un servicio
pensado según sus propias necesidades, el costo varía, y la cotización es
*sin costo y sin compromiso*.

### 2.4 Psicoterapia

**Enfoque:** cognitivo-conductual.
**Población:** exclusivamente adolescentes y juventudes.

**Motivos frecuentes de consulta** (10, textuales):

1. Ansiedad
2. Depresión
3. Regulación emocional
4. Autoestima, inseguridad, identidad y autoconocimiento
5. Habilidades sociales
6. Problemas de conducta en adolescentes
7. Cambios en la dinámica familiar derivado de procesos judiciales
8. Desarrollo de habilidades parentales y fortalecimiento del vínculo entre madres, padres e hijos
9. Educación sexual
10. Presión académica

### 2.5 Formación

**Vía forense (7 registros):**

| Estudio | Institución | Fechas |
|---|---|---|
| Maestría en Investigación y Evaluación Criminal y Forense | Instituto de Ciencia Aplicada | May 2024 – may 2026 |
| Curso de elaboración de peritajes judiciales | Poder Judicial del Estado de Querétaro | Mayo 2025 |
| Certificación en Análisis de Contexto en la Investigación Criminal | Consejo Certificador en Psicología Forense · Ciencia Aplicada | Mar – may 2025 |
| Curso-Taller de Peritajes psicológicos en guarda y custodia con Perspectiva de Infancia | FORENPSIC | Feb – may 2025 |
| Seminario especializado en disociación y trauma en víctimas de violencia | Instituto de Ciencia Aplicada | Sep – dic 2024 |
| Curso elaboración de peritaje psicológico | Centro de SubjetividadEs Identidad Clínica y Forense | Julio 2024 |
| Licenciatura en Psicología | Universidad Mondragón México | **Ago 2024 – may 2024** ⚠️ |

**Vía clínica (4 registros):**

| Estudio | Institución | Fechas |
|---|---|---|
| Maestría en Psicoterapia Cognitivo Conductual | Centro de Psicoterapia Cognitiva | May 2026 – en curso |
| Diplomado en Psicoterapia Infantojuvenil | CAPCIA | Ago 2026 – en curso |
| Licenciatura en Psicología | Universidad Mondragón México | Ago 2020 – may 2024 |
| Diplomado en Psicoterapia Cognitivo Conductual | UAQ · IMFAPSI | Ene 2025 – nov 2025 |

**Total: 10 estudios distintos** (la licenciatura aparece en ambas listas).

### 2.6 Sobre mí

Cuatro párrafos. Los puntos que sostienen todo el argumento:

- Formación y experiencia en **ambos ámbitos**, clínico y forense
- En forense: **principalmente materia familiar**
- En clínica: **exclusivamente** adolescentes y juventudes
- El porqué: *«la adolescencia es un momento decisivo en la construcción de las personas adultas del futuro»*
- La frase que resume su posición: *«aunque ambos ámbitos tienen objetivos y límites éticos diferentes, juntos enriquecen mi manera de comprender el comportamiento humano»*
- Su método: evidencia científica **y** cercanía; crea materiales y adapta actividades a cada adolescente

---

## 3. Inconsistencias encontradas

### 3.1 ⚠️ La licenciatura tiene dos fechas distintas

| Dónde | Fechas |
|---|---|
| Sección forense | «Agosto **2024** – mayo 2024» |
| Sección psicoterapia | «Agosto **2020** - mayo 2024» |

La primera va al revés: termina antes de empezar. La segunda cuadra con una
licenciatura de cuatro años.

**Decisión:** se usa **Ago 2020 – may 2024** en todos los bocetos.
**Pendiente de que ella confirme.**

### 3.2 «Guardia y custodia»

El término legal es **«guarda y custodia»**. «Guardia» parece un desliz de
tecleo.

**Decisión:** se escribe «guarda y custodia», que es como aparece en el
Código Civil. En un sitio dirigido a abogados, el término correcto importa.
**Pendiente de confirmar.**

### 3.3 Doble punto

*«…dentro de un contexto más amplio**..** Aunque ambos ámbitos…»*
Corregido a un solo punto. No requiere consulta.

### 3.4 La formación clínica no está en orden

El orden en que llegó mezcla fechas (2026, 2026, 2020, 2025).

**Decisión:** se ordena de lo más reciente a lo más antiguo, que es la
convención en un currículum profesional.

### 3.5 Falta el código postal

**Decisión:** se usa **76180**, que es el que OpenStreetMap asigna a Calle
Mauricio Garcés. **Pendiente de confirmar.**

---

## 4. Lo que NO dijo, y por eso no aparece

Esto importa tanto como lo que sí dijo. En versiones anteriores yo había
inventado varias cosas; todas se eliminaron.

| Inventado antes | Por qué se quitó |
|---|---|
| «Consulta en línea» | Nunca la mencionó. Solo hay consultorio físico. |
| «Ocho años de práctica» | No dio antigüedad. Su formación arranca en 2024. |
| «Enfoque humanista» | Dijo **cognitivo-conductual**, y nada más. |
| Precios («$000 MXN») | Dice expresamente que el costo **varía**. |
| Duración de sesión | No la mencionó. |
| Política de cancelación | No la mencionó. |
| Preguntas frecuentes | No aportó ninguna. |

> **Regla adoptada:** si no está en su documento, no está en el sitio.
> Un dato inventado en un sitio profesional con cédula visible es un riesgo,
> no un adorno.

---

## 5. Qué se deduce para el diseño

### 5.1 No hay que dividir el sitio en dos

Su documento **fluye como uno solo**: información general → forense →
psicoterapia → sobre mí. Nunca pidió bifurcar. La conclusión correcta no es
partir la página, sino que **una sola página sostenga dos registros de tono**
sin romperse.

*(El boceto 11 conserva la bifurcación como propuesta alternativa, por si le
resulta útil; los demás siguen su orden.)*

### 5.2 «Sobre mí» va arriba, no al final

Ella lo colocó al final del documento, pero en una consulta psicológica la
persona **es** el servicio. Las guías de sitios de terapeutas coinciden: la
biografía y la foto real son el factor número uno de confianza.

### 5.3 La formación no es relleno: es el argumento

En el área forense, un abogado contrata por credenciales. Los 10 estudios y
los dos registros (cédula y consejo certificador) **son el producto**, y por
eso tienen sección propia y aparecen también en la cabecera.

### 5.4 Dos públicos, un solo sitio

- **Forense:** abogados, juzgados, particulares en proceso familiar.
  Evalúan competencia técnica. Registro: preciso, ordenado, verificable.
- **Clínico:** madres y padres de adolescentes, y los propios adolescentes.
  Evalúan si se van a sentir cómodos. Registro: cercano, claro, sin jerga.

---

## 6. Lista de verificación de los bocetos

Todo boceto debe reflejar lo siguiente. La columna **Origen** indica si viene
de una instrucción explícita suya o de su información.

| # | Elemento | Origen |
|---|---|---|
| 1 | Nombre completo: Thania Huerta Pacheco | Información |
| 2 | Cédula profesional 14661976 | Información |
| 3 | Registro consejo forense 25-08-63 | Información |
| 4 | Dirección Mauricio Garcés 102, Col. La Joya | Información |
| 5 | **Mapa del consultorio** | **Instrucción A** |
| 6 | **Botón de Google Maps** | **Instrucción A** |
| 7 | **Botón de Waze** | **Instrucción A** |
| 8 | **Botón de WhatsApp** | **Instrucción B** |
| 9 | Celular visible y con enlace de llamada | Información |
| 10 | Horarios completos, con el doble turno | Información |
| 11 | Los 7 supuestos de periciales en materia familiar | Información |
| 12 | Metapericiales, con su descripción | Información |
| 13 | Nota de costo variable + cotización sin costo | Información |
| 14 | **Botón de cotización** (respuesta a la instrucción C) | **Instrucción C** |
| 15 | Los 10 motivos de consulta | Información |
| 16 | Enfoque cognitivo-conductual | Información |
| 17 | Población: exclusivamente adolescentes y juventudes | Información |
| 18 | Formación forense (7 registros) | Información |
| 19 | Formación clínica (4 registros) | Información |
| 20 | Texto de «Sobre mí» | Información |

---

## 7. Pendientes de resolver con ella

| # | Asunto | Propuesta actual |
|---|---|---|
| 1 | **Coordenada exacta del consultorio** | El pin cae en la calle, no en el 102. Se necesita clic derecho en Google Maps sobre la puerta. |
| 2 | Fecha de la licenciatura | Se usa Ago 2020 – may 2024 |
| 3 | «Guardia» o «guarda» y custodia | Se usa «guarda» |
| 4 | Código postal | Se usa 76180 |
| 5 | ¿Formulario real o WhatsApp con texto previo? | WhatsApp con texto previo |
| 6 | Correo electrónico | No aparece |
| 7 | **Fotografías** | Hay ilustraciones de relleno |

---

## 8. Notas sobre el número de WhatsApp

Los bocetos usan **442 830 6799** (número de pruebas) en lugar del de Thania.
Antes de entregar hay que cambiarlo a **442 137 5118** en `assets/js/config.js`
y en los bocetos.
