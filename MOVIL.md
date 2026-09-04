# Diseño para teléfono

> Qué medí, qué dice la investigación y qué cambié. El móvil no es el
> escritorio estrechado: es otro problema.

---

## 1. Lo que medí antes de tocar nada

Con el navegador, a 390 × 844, que es un iPhone corriente.

| | Antes |
|---|---|
| Alto total | **11.7 pantallas** |
| Objetivos táctiles por debajo de 44 px | **11 de 34** |
| Desbordes horizontales | Los enlaces de la barra superior |
| Sección más larga | Formación, 2.1 pantallas |
| Secciones alcanzables desde la barra inferior | **4 de 6** |

Y en la captura, tres cosas que los números no dicen:

- **Dos barras de navegación a la vez**, arriba y abajo.
- La de arriba, **cortada a media palabra**: «Psicoter…».
- El logotipo centrado ocupando media pantalla, con el titular a la
  izquierda: dos alineaciones distintas seguidas.

---

## 2. Lo que dice la investigación

**Sobre la barra que se desliza.** Nielsen Norman Group: *«cuando la barra de
pestañas se convierte en carrusel por desbordamiento, las pestañas ocultas
pierden descubribilidad y sube el coste de interacción»*. Y más directo:
*«fuera de la vista, fuera de la mente»* — nadie adivina qué hay detrás.

Esa barra la había puesto yo, y era el antipatrón exacto.

**Sobre tener las dos.** El artículo de patrones de navegación móvil de NN/G
no recomienda combinar navegación arriba y abajo. Y del menú superior dice
que *«consume espacio valioso sobre el pliegue»*, que en teléfono es
justamente lo que falta.

**Sobre cuántas pestañas.** Las barras funcionan con **pocas opciones**; por
encima de cinco cuesta mantener el objetivo táctil.

**Sobre leer.** El cuerpo de texto necesita **16 px como mínimo**, y para
párrafos largos en teléfono lo cómodo son **16–18 px**, con interlínea de
1.4–1.6. La medida de línea ideal es de 50 a 75 caracteres; los lectores menos
entrenados van mejor sobre 45.

---

## 3. Lo que cambié

### La navegación

**En teléfono se queda solo la barra inferior.** Los enlaces de arriba
desaparecen y la barra superior conserva únicamente la marca. Tres razones,
las tres de la investigación: el carrusel escondía opciones, no conviene
duplicar navegación, y arriba se comía el espacio del pliegue.

La de abajo además cae en **la zona del pulgar**, que es donde se alcanza sin
recolocar el teléfono.

**Pasa de cuatro secciones a cinco**, y suelta «Inicio» —en una página de una
sola tirada es redundante—. Con eso, las seis secciones son alcanzables; antes
Formación y Consultorio no lo eran desde ningún sitio.

**Las etiquetas suben de 9.6 px a 12 px**, que es el mínimo para texto de
interfaz. Para que quepan, «Formación» pasa a «Estudios» y «Consultorio» a
«Dónde».

### La lectura

- La marca de la barra pasa a **INDICIO · Psic. Thania Huerta**: más corta,
  más suya, y deja de cortarse a media palabra.
- El logotipo de portada **deja de ser un cartel y pasa a ser una firma**,
  alineada con el titular. Se llevaba media pantalla él solo.
- El texto largo sube a **17 px**, dentro del rango cómodo para párrafos.
- Los apartados de la biografía se separan con un **filete**: en una sola
  columna el hueco solo no basta para que se lea como cambio de tema.
- El **número de sección pasa a la misma línea** que el nombre. En vertical un
  numeral de 40 px cuesta una línea entera y no aporta nada.
- En los supuestos, **el numeral va al lado del texto** y no encima: siete
  fichas a dos líneas eran siete líneas de scroll regaladas.
- En formación, **institución y fechas comparten línea**. Diez registros,
  diez líneas menos.
- La **retícula de líneas verticales se retira**: a 390 px no organiza nada y
  se lee como rayas sueltas encima del texto.

---

## 4. El resultado, medido

| | Antes | Ahora |
|---|---|---|
| Alto total | 11.7 pantallas | **10.3** |
| Portada | 1.3 pantallas | **1.0** |
| Formación | 2.1 pantallas | **1.8** |
| Táctiles por debajo de 44 px | 11 | **2** |
| Secciones alcanzables | 4 de 6 | **6 de 6** |
| Desbordes horizontales | Sí | **No** |
| Fallos de contraste a 390 y 320 px | — | **0** |

Los dos objetivos táctiles que quedan cortos son los enlaces de crédito del
mapa, que son de Leaflet y nadie pulsa.

## Fuentes

- Nielsen Norman Group · [Basic Patterns for Mobile Navigation](https://www.nngroup.com/articles/mobile-navigation-patterns/)
- Nielsen Norman Group · [Beware Horizontal Scrolling](https://www.nngroup.com/articles/horizontal-scrolling/)
- Nielsen Norman Group · [Mobile Subnavigation](https://www.nngroup.com/articles/mobile-subnavigation/)
- [Optimal Line Length for Readability](https://www.uxpin.com/studio/blog/optimal-line-length-for-readability/) · UXPin
- [What Font Size Should Body Text Be? 16px Minimum](https://www.greadme.com/blog/seo/best-font-sizes-for-readability-complete-guide)
