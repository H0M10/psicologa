# Plan de estructura

> Qué dijo Thania, qué encontré al medirlo, qué dice la investigación y qué
> cambio en consecuencia.

> «Siento que de repente la info se ve como si todo fuera un mismo apartado y
> se pierde un poco. Igual y si pudiera tener otra estructura para que sea más
> sencilla de leer estaría increíble.»

---

## 1. El diagnóstico, medido

Antes de proponer nada conté lo que hay en la página.

| Sección | Palabras | Bloques | Forma |
|---|---|---|---|
| Sobre mí | 223 | 3 | apertura + prosa |
| Área forense | 106 | 10 | **apertura + lista** |
| Psicoterapia | 61 | 10 | **apertura + lista** |
| Formación | 114 | 10 | **apertura + lista** |
| Consultorio | 129 | 1 | apertura + mapa |

Y las anclas visuales de todo el documento: **cero fotografías, cero iconos**.
Un mapa. Todo lo demás son 633 palabras de texto sobre color plano.

**Tenía razón, y es literal.** Tres secciones seguidas —forense, psicoterapia
y formación— tienen exactamente la misma forma: una apertura y una lista de
unos diez elementos. Cambia el texto, no la estructura. Al leer son
indistinguibles, y por eso se funden en «un mismo apartado».

El color no era el problema de fondo. Yo había estado arreglando el contraste
entre fondos, que también fallaba, pero eso era el síntoma menor.

---

## 2. Lo que dice la investigación

**El 79 % de la gente escanea; solo el 16 % lee línea por línea.** Resaltar y
escribir conciso mejoró la usabilidad medida entre un 47 y un 58 % (Nielsen
Norman Group).

**Patrón de pastel de capas.** Al escanear, la vista salta de encabezado en
encabezado buscando dónde está lo suyo, y se salta el texto intermedio. Si
todos los encabezados van seguidos de lo mismo, el patrón deja de servir.

**La variación es lo que reinicia la atención.** Una sección densa de texto
debe ir seguida de una visual; una explicación larga, de un resumen corto; una
compleja, de una llamada simple. *«Esa variación le da a la atención del
visitante la oportunidad de reiniciarse.»*

**Y una que me corrigió el plan.** Mi primer impulso fue partir la página por
público —abogados por un lado, pacientes por otro—. NN/G desaconseja la
navegación por público con cinco razones: la gente no se identifica con una
sola categoría, las etiquetas son ambiguas, añade un paso mental, genera
ansiedad por lo que se está perdiendo, y obliga a duplicar contenido.

**Recomiendan organizar por tarea, no por quién eres.** Y admiten la excepción
cuando el contenido es de verdad distinto, las categorías son excluyentes y la
etiqueta dice explícitamente «para».

En su caso encaja la excepción, pero con la corrección: no «soy abogado / soy
paciente», sino **qué necesitas**. Y como entrada, no como bifurcación que
esconda nada.

---

## 3. Los seis cambios

### 1 · Un índice de entrada, por tarea

Justo bajo la portada, dos accesos:

- **Necesito un peritaje psicológico** → área forense
- **Busco terapia para un adolescente** → psicoterapia

Son enlaces a secciones de la misma página, no puertas que oculten la otra
mitad. Quien no se reconozca en ninguno sigue bajando y lo encuentra todo.

### 2 · Que las tres listas dejen de ser la misma lista

Este es el cambio que ella pidió. Cada una toma una forma distinta:

| Sección | Forma nueva | Por qué |
|---|---|---|
| Área forense | Fichas numeradas en retícula | Son supuestos legales: piden peso y orden |
| Psicoterapia | Lista corrida, de aire | Son temas para hablar: piden ligereza |
| Formación | Línea de tiempo vertical | Es un recorrido: pide secuencia |

### 3 · Alternar densidad

Detrás de cada bloque denso va uno ligero. Después de la biografía, una cita
sola. Después de los siete supuestos, una llamada corta. El mapa a sangre hace
de respiro visual antes del cierre.

### 4 · Anclas visuales

Sus propios elementos de marca hacen de marcador: el sello, el patrón de
volutas, las tres insignias de color. De cero anclas a varias, sin inventar
adorno: todo sale de su hoja de marca.

### 5 · Lo que hace, antes de quién es

La biografía son 223 palabras de prosa seguida, el bloque más denso de la
página, y hoy es lo primero tras la portada. Es el peor sitio: quien llega
buscando un peritaje tiene que atravesarla.

El orden pasa a ser **qué hace → quién es → dónde**. La biografía no se
recorta ni se esconde; baja dos secciones.

> **Es una decisión de criterio, no una regla.** Si prefiere abrir
> presentándose, se vuelve a subir en un minuto.

### 6 · El corte entre secciones, rehecho

Aquí me equivoqué dos veces y ella lo dijo las dos.

**Primero** dejé la portada y la primera sección en el mismo blanco: 1.00:1.
**Después** metí un claro intermedio y me quedé tranquilo en 1.38:1, con un
umbral de 1.20 que **me inventé**. Ella volvió a decir que no lo percibía, y
tenía razón otra vez.

El número real es **3:1**, que es lo que pide WCAG 1.4.11 para que un límite
entre dos zonas se perciba sin borde. Y medido, su paleta no tiene **dos
claros que lleguen a 3:1 entre sí**: el máximo es blanco contra arena, 2.05.

O sea: **separar dos secciones claras solo con el fondo es imposible con su
paleta.** Hay que alternar con los oscuros.

Así que las secuencias dejan de elegirse a ojo. Se buscan por ordenador,
maximizando el salto más corto, con estas restricciones:

- La portada no abre en blanco. Lo pidió ella.
- Ningún fondo se usa más de dos veces.
- El negro solo en el pie.
- Retícula mantiene mayoría de claros; Ventanal alterna bloques.

| | Antes | Ahora |
|---|---|---|
| Retícula · salto mínimo | 1.38 | **2.05** |
| Ventanal · salto mínimo | 1.38 | **6.53** |

Ventanal abre en **olivo** y Retícula en **arena clara**. Ninguna abre en
blanco.

### 7 · Y la causa de fondo: el color dejó de depender de la sección

Las reglas de color estaban atadas a *qué sección* era —el acento de
«forense», el filete de «formación»—. Por eso cada reordenación rompía algo
y había que ir persiguiendo fallos uno a uno.

Ahora **cada fondo declara todo lo que va encima**: texto, acento, filete,
color de ficha y color sobre la ficha. Los componentes no nombran colores,
usan esos tokens. Cualquier sección puede llevar cualquier fondo y nada se
pierde.

Los mínimos, medidos sobre los archivos generados: **texto 5.67, acento
4.96**, con AA en 4.5.

---

## 4. Orden resultante

| | Antes | Ahora |
|---|---|---|
| 1 | Portada | Portada |
| 2 | Sobre mí · 223 palabras de prosa | **Índice · dos accesos por tarea** |
| 3 | Área forense · lista | Área forense · fichas numeradas |
| 4 | Psicoterapia · lista | Psicoterapia · lista corrida |
| 5 | Formación · lista | **Sobre mí** · prosa y cita |
| 6 | Consultorio | Formación · línea de tiempo |
| 7 | Cierre | Consultorio · mapa a sangre |
| 8 | | Cierre |

---

## 5. Lo que sigue faltando

**La fotografía real del consultorio.** Es el ancla visual que ninguna
solución de maquetación sustituye, y además es el argumento: el sitio es la
puerta a un espacio que ya existe y que ella está decorando en mid-century.
Sin esa foto, la página lo cuenta en vez de enseñarlo.

## Fuentes

- Nielsen Norman Group · [Audience-Based Navigation: 5 Reasons to Avoid It](https://www.nngroup.com/articles/audience-based-navigation/)
- [How Chunking Boosts User Experience](https://websites.it.utah.edu/announcements/posts/2025/july/chunking.php) · University of Utah
- [UI Design Best Practices for Better Scannability](https://www.toptal.com/designers/web/ui-design-best-practices) · Toptal
- [Rhythm and Flow in Editorial Design](https://fiveable.me/advanced-editorial-design/unit-2/rhythm-flow-editorial-design/study-guide/RyqTytOWkCcd0y6x)
- [How to Design Pages That Keep Visitors Scrolling](https://www.flowvibe.studio/blog/how-to-design-webflow-pages-that-keep-visitors-scrolling)

---

## 6. La restricción que impone su paleta

Al colocar los fondos aparece algo que no es opinión, es aritmética.

**Sus dos claros no se distinguen entre sí** (crema contra arena: 1.60) y
**sus tres oscuros tampoco** (olivo/cacao 1.78, olivo/terracota 1.05,
cacao/terracota 1.70). Ninguno de esos pares llega al 3:1 que hace falta para
que un corte de sección se perciba.

**Consecuencia:** claro y oscuro tienen que alternar obligatoriamente. No hay
otra secuencia posible. Y el negro solo puede ir al final, porque es el único
oscuro que salta de verdad contra los otros oscuros.

De ahí sale algo que no habría adivinado: **las dos páginas tienen que abrir
en un fondo claro.** Como la biografía va en la posición 4 y necesita fondo
neutro, y la alternancia fija las paridades, la posición 0 queda neutra
también. No es una preferencia estética: es lo único que cumple.

### Y una regla que faltaba: dónde puede ir la prosa

El contraste mide si se distingue una letra, no si cansa leer un párrafo. Un
fondo saturado a 5:1 cumple la norma y aun así fatiga en 223 palabras
seguidas.

Ventanal tenía la biografía sobre terracota y el consultorio sobre olivo.
Los dos bloques de prosa de la página, sobre los dos colores más saturados.
Por eso costaba leerlo, aunque los números pasaran.

**La regla:** la prosa seguida solo va sobre crema o arena. Los saturados
llevan trozos cortos —el índice, las listas, la línea de tiempo, el mapa y la
llamada final—, que se escanean en vez de leerse.

| | Retícula | Ventanal |
|---|---|---|
| Abre en | arena | crema |
| Salto mínimo | 3.07 | 3.07 |
| Prosa sobre saturado | 0 | 0 |
| Fondos saturados | 4 de 9 | 4 de 9 |
