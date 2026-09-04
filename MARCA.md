# Indicio · manual de marca

> Thania ya tiene nombre, logotipo, paleta y tipografía. Este documento
> sustituye a `PERFIL.md` en todo lo visual: ya no hay que deducir su gusto,
> lo entregó resuelto.

---

## 1. El nombre

**INDICIO** · Psicología forense y psicoterapia
Firma personal: **Psic. Thania Huerta**

El nombre es una decisión inteligente y conviene entenderla, porque manda
sobre el resto del diseño. Un *indicio* es lo que se observa antes de poder
concluir: el rastro, la señal, lo que apunta a algo. Nombra a la vez las dos
mitades de su trabajo —lo que un peritaje busca y lo que una terapia
escucha— sin que ninguna de las dos se coma a la otra.

**Consecuencia:** la página no debe prometer certezas ni diagnósticos. Debe
sonar a observación cuidadosa. Los verbos son *acompañar*, *valorar*,
*escuchar*, *comprender*; nunca *resolver* ni *garantizar*.

---

## 2. La paleta

Seis colores. Las cuatro familias que había nombrado por WhatsApp —madera,
verdes, marrón y vino— están todas, más la mostaza, que no había mencionado.

| | Nombre de trabajo | Hex | Papel |
|---|---|---|---|
| ● | **Terracota** | `#A03812` | Acento de acción: botones y enlaces |
| ● | **Negro** | `#000000` | Texto y el logotipo en su versión principal |
| ● | **Mostaza** | `#AC8632` | Relleno de superficies grandes. **Casi nunca texto** |
| ● | **Olivo** | `#5C6046` | Color de sección y segundo acento |
| ● | **Arena** | `#C7B296` | Superficie cálida, y texto sobre los oscuros |
| ● | **Cacao** | `#513029` | Fondo oscuro y texto de peso |

Los valores no son estimaciones: salen de promediar el centro de cada círculo
en su archivo original, saltándose el antialias del borde.

### La regla que sale de medir el contraste

Se midió cada color como texto sobre cada fondo posible. El resultado no es
opinión, es la norma WCAG AA (4.5:1 para texto corrido):

| Color | Sobre claro | Sobre arena | Sobre olivo | Sobre cacao | Sobre negro |
|---|---|---|---|---|---|
| Terracota | ✅ 6.8 | ⚠️ 3.3 | ❌ 1.0 | ❌ 1.7 | ⚠️ 3.1 |
| Negro | ✅ 21.0 | ✅ 10.2 | ⚠️ 3.2 | ❌ 1.8 | — |
| **Mostaza** | ⚠️ **3.4** | ❌ 1.6 | ❌ 1.9 | ⚠️ **3.4** | ✅ 6.2 |
| Olivo | ✅ 6.5 | ⚠️ 3.2 | — | ❌ 1.8 | ⚠️ 3.2 |
| Arena | ❌ 2.1 | — | ⚠️ 3.2 | ✅ 5.7 | ✅ 10.2 |
| Cacao | ✅ 11.6 | ✅ 5.7 | ❌ 1.8 | — | ❌ 1.8 |
| Blanco | — | ❌ 2.1 | ✅ 6.5 | ✅ 11.6 | ✅ 21.0 |

**Lo que esto obliga:**

1. **La mostaza casi nunca puede llevar texto.** Solo llega a 4.5:1 sobre
   negro (6.2). Sobre claro da 3.4 y sobre cacao también 3.4. Es un color de
   superficie: un bloque, una banda, un relleno grande.
2. **La terracota y el olivo son colores de texto solo sobre claro.** Sobre
   arena se quedan en 3.3 y 3.2.
3. **Sobre arena va negro o cacao.** Nada más.
4. **Sobre olivo va blanco** (6.5), no arena (3.2).
5. **Sobre cacao va arena o blanco.**

Es una paleta de dos registros: uno claro y uno oscuro, cada uno con sus
colores. Mezclarlos es lo que la rompe.

---

## 3. La tipografía

| | Familia | Uso |
|---|---|---|
| 1 | **Trend Sans One** | Titulares y el logotipo |
| 2 | **Raleway** | Texto corrido |

**Raleway** está en Google Fonts: se usa tal cual, sin sustituto.

**Trend Sans One** es de Latinotype, comercial, y **no está en Google Fonts**.
Para la web hacen falta dos cosas: la licencia *webfont* y el archivo. Mientras
tanto se usa un sustituto geométrico del mismo registro —trazo uniforme, «O»
casi circular, buena en versalitas espaciadas— y se marca como provisional.

**Pendiente:** preguntarle si su diseñadora entregó los archivos `.woff2` de
Trend Sans One y si la licencia cubre uso web.

---

## 4. El logotipo

### Qué es

Una espiral doble abierta, trazada a mano con grosor variable. Se lee de tres
maneras a la vez, y las tres funcionan:

- Una **voluta** o rastro que se enrolla: el indicio.
- Un **remolino de huella dactilar**: lo forense, sin caer en literalidades.
- Una **oreja** estilizada: escuchar, que es la otra mitad del trabajo.

Alrededor, en trayectoria curva, **PSIC. THANIA HUERTA**. Debajo, **INDICIO**
en versalitas muy espaciadas y de trazo fino, con la bajada opcional
**PSICOLOGÍA FORENSE Y PSICOTERAPIA**.

### Las versiones que entregó

| Versión | Cuándo usarla |
|---|---|
| Vertical con bajada | Portada, pie, cualquier sitio con aire |
| Vertical sin bajada | Cuando la bajada no se leería |
| **Sello circular** | Favicon, avatar, sello de documento |
| **Círculo de color** (olivo, terracota, cacao) con la marca en crema | Icono de aplicación, viñeta, redes |
| **Patrón de volutas** sueltas | Textura de fondo, muy tenue |

El patrón de volutas es el hallazgo aprovechable: da textura de marca sin
tener que inventar adornos, que es justo lo que sobraba en los bocetos.

### Cómo están puestos en la página

Sus archivos van como **máscara**, no como imagen. La razón es práctica: así
el mismo archivo se tiñe del color que toque en cada fondo —cacao sobre
blanco, arena sobre cacao, blanco sobre olivo— en vez de necesitar una versión
clara y otra oscura de cada pieza. Como una máscara no da texto alternativo,
cada una lleva `role="img"` y su etiqueta.

| Archivo | De dónde sale |
|---|---|
| `indicio-logo.png` | Su logotipo vertical completo |
| `indicio-sello.png` | El sello circular de su hoja |
| `indicio-patron.png` | El patrón de volutas |
| `indicio-insignia-olivo/terracota/cacao.png` | Las tres versiones en círculo |

**Compartió el Canva editable**, que es de donde debe salir el SVG:
`canva.link/s1tbcmyedzqx3ma`

Lo que hay ahora son PNG recortados de su hoja, y a tamaño grande se les nota
el borde. Desde el Canva se exporta el logotipo en SVG —nítido en cualquier
pantalla y más ligero— y de paso se confirman los hexadecimales contra los
que muestreé.

---

## 5. Lo que dijo del diseño, y qué hacer

> «Siento que de repente la info se ve como si todo fuera un mismo apartado y
> se pierde un poco. Si pudiera tener otra estructura para que sea más
> sencilla de leer estaría increíble.»

Tiene razón, y el diagnóstico es preciso. Los dos bocetos que eligió separan
las secciones con **filetes finos y nada más**: mismo fondo, mismo tamaño de
letra, misma densidad de arriba abajo. El ojo no encuentra dónde termina una
cosa y empieza la siguiente, así que lo lee todo como un bloque.

### Los cinco cambios que lo arreglan

| # | Cambio | Por qué |
|---|---|---|
| 1 | **Cada sección con su propio fondo** | El cambio de color es la señal de corte más barata y más fuerte que existe |
| 2 | **Apertura de sección con peso**: número, nombre y una frase | Da un punto de entrada claro y descansa la vista |
| 3 | **Un tratamiento distinto por tipo de contenido** | Los supuestos, los motivos y la formación no deben verse iguales |
| 4 | **Más aire entre secciones que dentro** | La proximidad es lo que agrupa; si el hueco es igual, no agrupa nada |
| 5 | **Cortar los bloques largos** | La biografía en cuatro párrafos con un intertítulo, no en un muro |

---

## 6. Lo que sigue pendiente

1. **El logotipo en SVG**, exportado desde su Canva.
2. **Trend Sans One** para web: archivos `.woff2` y licencia de uso web.
4. **La foto real del consultorio.**
5. **El número de la calle:** su documento dice #102; la última indicación, 808.
6. **La coordenada exacta**, que ahora cae en la calle y no en el número.
