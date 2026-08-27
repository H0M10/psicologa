# Bitácora de los bocetos

> Estado actual. La investigación que gobierna los diseños está en
> [MIDCENTURY.md](MIDCENTURY.md); el perfil de Thania, en [PERFIL.md](PERFIL.md).

---

## 1. Qué hay ahora

Ocho bocetos, en una sola lista. Todos con la misma paleta documentada y la
misma información completa; lo que cambia es el diseño.

| Archivo | Nombre | Carácter | Tipografía |
|---|---|---|---|
| `propuesta-2.html` | Con textura | Arco, cono, azulejo y grano de papel | Bitter · Jost |
| `propuesta-4.html` | Mosaico | Los azulejos de su segunda imagen | Outfit · Karla |
| `mc-reticula.html` | Retícula | Estructura suiza con campos de color | Archivo |
| `propuesta-5.html` | Atómico | Madera oscura, paneles verde y vino | Josefin Sans · Lora |
| `mc-credenza.html` | Credenza | Materiales y horizontalidad | Jost · Archivo |
| `mc-silueta.html` | Silueta | Formas recortadas de Saul Bass | Jost · Archivo |
| `mc-ventanal.html` | Ventanal | Dentro y fuera se funden | Outfit · Hanken Grotesk |
| `propuesta.html` | Sin adornos | Sombras difusas, tinta gris cálida | Petrona · Hanken Grotesk |

Los cuatro `mc-` comparten `_mc.css` —tokens y piezas idénticas— y cada uno
tiene su hoja de personalidad, `_mcA` a `_mcD`.

**Retirados:** los veinte primeros, y después el boceto Cartel.

### Lo que pidió Thania sobre estos

- **Atómico le gusta**, pero era «muy verde». El fondo pasó de verde bosque a
  madera oscura `#2A2420`, y el verde quedó como un panel entre varios, junto
  al vino. Los acentos son aguacate y barro, ambos documentados.
- **Retícula le encanta**, pero le faltaba paleta. El color entró a la manera
  suiza: campos medidos en columnas en la portada, y cada sección con su
  fondo —lino, bronce, cilantro y vino.
- **Con textura y Mosaico** suben a la lista principal.


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
