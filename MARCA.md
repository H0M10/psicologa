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

| | Nombre de trabajo | Hex leído | Papel |
|---|---|---|---|
| ● | **Terracota** | `#B84A22` | Acento de acción: botones y enlaces |
| ● | **Negro** | `#000000` | Texto y el logotipo en su versión principal |
| ● | **Mostaza** | `#C9A22B` | Relleno de superficies grandes. **Nunca texto sobre claro** |
| ● | **Olivo** | `#5F6B4F` | Color de sección y segundo acento |
| ● | **Arena** | `#D5C0A6` | Superficie cálida, y texto sobre los oscuros |
| ● | **Cacao** | `#4A2E24` | Fondo oscuro y texto de peso |

> **Pendiente:** los hexadecimales están leídos de la imagen, no de un archivo.
> Si su diseñadora tiene el `.ase` o el manual, conviene pedirlos y sustituir.

### La regla que sale de medir el contraste

Se midió cada color como texto sobre cada fondo posible. El resultado no es
opinión, es la norma WCAG AA (4.5:1 para texto corrido):

| Color | Sobre claro | Sobre olivo | Sobre cacao / negro |
|---|---|---|---|
| Terracota | ✅ 5.2 | ❌ 1.1 | ❌ 2.4 |
| Negro | ✅ 21.0 | ⚠️ 3.7 | ❌ |
| **Mostaza** | ❌ **2.4** | ❌ 2.3 | ✅ 5.1 |
| Olivo | ✅ 5.7 | ❌ | ❌ 2.2 |
| Arena | ❌ 1.8 | ⚠️ 3.2 | ✅ 7.0 |
| Cacao | ✅ 12.3 | ❌ 2.2 | ❌ |

**Lo que esto obliga:**

1. **La mostaza no puede llevar texto sobre fondo claro.** Da 2.4:1. Es un
   color de superficie: un bloque, una banda, un relleno grande. En cuanto
   se pone como letra sobre hueso, desaparece.
2. **La terracota y el olivo son colores de texto solo sobre claro.**
3. **La arena y la mostaza son colores de texto solo sobre cacao o negro.**
4. **Sobre olivo va blanco** (5.67), no arena (3.22).

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

**Pendiente:** hace falta el logotipo en **SVG**. En la página va dibujado en
vectores, no como imagen: tiene que verse nítido en cualquier pantalla y poder
cambiar de color según el fondo. Mientras llega, va una reconstrucción, y se
nota que lo es.

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

1. **El logotipo en SVG**, y las tres versiones de color.
2. **Los hexadecimales exactos** de la paleta.
3. **Trend Sans One** para web: archivos y licencia.
4. **La foto real del consultorio.**
5. **El número de la calle:** su documento dice #102; la última indicación, 808.
6. **La coordenada exacta**, que ahora cae en la calle y no en el número.
