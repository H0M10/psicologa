# Bitácora de los bocetos

> Estado actual. La investigación que gobierna los diseños está en
> [MIDCENTURY.md](MIDCENTURY.md); el perfil de Thania, en [PERFIL.md](PERFIL.md).

---

## 1. Qué hay ahora

Ocho bocetos, en dos grupos.

### Los cuatro mid-century

Dibujados **después** de investigar el estilo. Cada uno pone por delante un
principio distinto, para que ella elija por carácter y no solo por color.

| Archivo | Nombre | Principio | Tipografía |
|---|---|---|---|
| `mc-credenza.html` | Credenza | Materiales y horizontalidad | Jost · Archivo |
| `mc-reticula.html` | Retícula | Estructura suiza y asimetría | Archivo |
| `mc-silueta.html` | Silueta | Formas recortadas de Saul Bass | Jost · Archivo |
| `mc-ventanal.html` | Ventanal | Dentro y fuera se funden | Outfit · Hanken Grotesk |

Comparten `_mc.css` —tokens y piezas idénticas— y cada uno tiene su propia
hoja de personalidad, `_mcA` a `_mcD`.

### Las cuatro anteriores

Se conservan por si alguna sirve.

| Archivo | Nombre | De dónde salió |
|---|---|---|
| `propuesta.html` | Sin adornos | De leer el código de la página que ella compartió |
| `propuesta-2.html` | Con textura | La primera versión, la más decorada |
| `propuesta-4.html` | Mosaico | De los azulejos de su segunda imagen |
| `propuesta-5.html` | Atómico | Su paleta invertida, sobre fondo oscuro |

**Retirados:** los veinte primeros, y después el boceto Cartel.

---

## 2. Cómo se generan

`_build.py` y `_build_mc.py` guardan el contenido de Thania **una sola vez** y
lo reparten. Por eso los ocho llevan lo mismo sin depender de que yo lo copie
bien ocho veces.

Cada boceto lleva, verificado por conteo:

- Las 6 secciones: portada, sobre mí, forense, psicoterapia, formación, consultorio
- Los **7 supuestos periciales** y las metapericiales
- Los **9 motivos de consulta**
- Los **9 registros de formación**, en dos vías
- Cédula 14661976 y consejo forense 25-08-63
- Horario de doble turno y sábados
- Mapa con Google Maps, Waze y Apple Maps
- Formulario de cotización y barra inferior con scrollspy

Para regenerarlos:

```
python bocetos/_build.py       # propuesta-4 y propuesta-5
python bocetos/_build_mc.py    # los cuatro mid-century
```

---

## 3. Criterios que no se negocian

- **Nada inventado.** Si no está en el documento de Thania, no está en el sitio.
- **Contraste verificado** con WCAG 2. La tabla está en MIDCENTURY.md.
- **Medida de línea de 50 a 75 caracteres.**
- **Objetivos táctiles de 44 a 48 px.**
- **`prefers-reduced-motion` respetado**, `:focus-visible` visible, nunca `transition: all`.
- **Bandera a la izquierda.** El estilo nunca justifica.
- **Función antes que adorno.** Si un elemento no hace nada, se quita.

---

## 4. Pendientes que no dependen de mí

1. **La foto real del consultorio.** Es lo que más falta: el sitio es la puerta
   a un espacio que ya existe.
2. **Coordenada exacta.** El pin cae en la calle, no en el número.
3. **El número de la calle.** Su documento dice #102; la última indicación, 808.
   Ahora está el 808.
4. **Fecha de la licenciatura.** Su documento la trae invertida.
5. **Código postal.** Se usa 76180.
6. ~~El número de WhatsApp de pruebas.~~ Resuelto: ya está el suyo, 442 137 5118.
