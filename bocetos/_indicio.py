# -*- coding: utf-8 -*-
u"""
Genera los dos bocetos que Thania eligio, ya con la marca Indicio.

Su contenido vive aqui una sola vez, asi que los dos lo llevan completo por
construccion. Lo que cambia entre ellos es la estructura visual, no la
informacion.
"""
import io, os, hashlib
D = 'c:/Users/hanni/Desktop/THPSICOLOGOA/bocetos/'

WA  = 'https://wa.me/524421375118?text=Hola%20Thania%2C%20vi%20la%20p%C3%A1gina%20de%20Indicio%20y%20me%20gustar%C3%ADa%20preguntarte%20algo.'
TEL = 'tel:+524421375118'
LAT, LNG = '20.572439', '-100.4184025'

BIO_LEAD = u'Soy psic\u00f3loga con formaci\u00f3n y experiencia profesional en los \u00e1mbitos cl\u00ednico y forense. Dentro del \u00e1rea forense trabajo principalmente en materia familiar, lo que me ha permitido comprender las distintas situaciones y necesidades que pueden presentarse en las familias. En el \u00e1rea cl\u00ednica, mi pr\u00e1ctica est\u00e1 dedicada exclusivamente al acompa\u00f1amiento de adolescentes y juventudes.'

BIO = [
 (u'Por qu\u00e9 la adolescencia',
  u'Eleg\u00ed trabajar con esta poblaci\u00f3n porque considero que la adolescencia es un momento decisivo en la construcci\u00f3n de las personas adultas del futuro. Acompa\u00f1arlos oportunamente puede generar cambios importantes en el presente, mientras desarrollan su identidad y su propia manera de relacionarse con el mundo.'),
 (u'C\u00f3mo se cruzan las dos \u00e1reas',
  u'Mi experiencia cl\u00ednica me permite crear espacios de crecimiento, cuestionamiento y desarrollo personal. Por su parte, mi formaci\u00f3n forense me ha ense\u00f1ado a comprender a cada persona dentro de un contexto m\u00e1s amplio. Aunque ambos \u00e1mbitos tienen objetivos y l\u00edmites \u00e9ticos diferentes, juntos enriquecen mi manera de comprender el comportamiento humano.'),
 (u'C\u00f3mo trabajo',
  u'Disfruto estudiar y mantenerme en constante actualizaci\u00f3n. Procuro que mi trabajo se sustente en evidencia cient\u00edfica, pero tambi\u00e9n creo que la terapia puede ser cercana y creativa: disfruto crear materiales y adaptar actividades y herramientas a la personalidad, los intereses y las necesidades de cada adolescente.'),
]
CITA = u'Creo que la terapia puede ser cercana y creativa.'

SUPUESTOS = [u'Guarda y custodia',
 u'Establecimiento o modificaci\u00f3n de reg\u00edmenes de convivencia',
 u'Valoraci\u00f3n de competencias y habilidades parentales',
 u'Conflictos derivados de una separaci\u00f3n o divorcio',
 u'Interferencias parentales',
 u'Identificaci\u00f3n de factores de riesgo y protecci\u00f3n',
 u'Afectaciones psicol\u00f3gicas']

MOTIVOS = [u'Depresi\u00f3n', u'Regulaci\u00f3n emocional',
 u'Autoestima, inseguridad, identidad y autoconocimiento',
 u'Habilidades sociales', u'Problemas de conducta en adolescentes',
 u'Cambios en la din\u00e1mica familiar derivados de procesos judiciales',
 u'Desarrollo de habilidades parentales y fortalecimiento del v\u00ednculo',
 u'Educaci\u00f3n sexual', u'Presi\u00f3n acad\u00e9mica']

# Formacion. Tomada de la tabla de su documento -no de la version anterior
# del sitio, que traia cinco instituciones cambiadas y dos estudios de menos-.
# Cada registro es (estudio, institucion, fechas), ordenado del mas reciente.
# Formacion. Tomada de la tabla de su documento -no de la version anterior
# del sitio, que traia cinco instituciones cambiadas y dos estudios de menos-.
# Cada registro es (estudio, institucion, fechas).
#
# El orden es por rango academico, no por fecha: primero la licenciatura, que
# es el titulo que habilita, luego la maestria, despues certificaciones y
# diplomados, y al final cursos y seminarios. Quien lee credenciales busca
# primero el grado, no el ano.
CLINICA = [
 (u'Licenciatura en Psicología', u'Universidad Mondragón México', u'Ago 2020 – may 2024'),
 (u'Maestría en Psicoterapia Cognitivo Conductual', u'Centro de Psicoterapia Cognitiva', u'May 2026 – en curso'),
 (u'Diplomado en Psicoterapia Cognitivo Conductual', u'UAQ · IMFAPSI', u'Ene – nov 2025'),
 (u'Diplomado en Psicoterapia Infantojuvenil', u'CAPCIA', u'Ago 2026 – en curso')]

FORENSE = [
 (u'Maestría en Investigación y Evaluación Criminal y Forense', u'Instituto de Ciencia Aplicada', u'May 2024 – may 2026'),
 (u'Certificación en Análisis de Contexto en la Investigación Criminal', u'Consejo Certificador en Psicología Forense', u'Mar – may 2025'),
 (u'Curso de elaboración de peritajes judiciales', u'Poder Judicial del Estado de Querétaro', u'Mayo 2025'),
 (u'Curso-taller de peritajes psicológicos en guarda y custodia', u'FORENPSIC · con perspectiva de infancia', u'Feb – may 2025'),
 (u'Seminario en disociación y trauma en víctimas de violencia', u'Instituto de Ciencia Aplicada', u'Sep – dic 2024'),
 (u'Curso de elaboración de peritaje psicológico', u'Centro de SubjetividadEs, Identidad Clínica y Forense', u'Julio 2024')]

# Sus archivos, no una reconstruccion. Van como mascara para poder tenirlos:
# el mismo logo sirve sobre claro y sobre oscuro sin tener dos versiones.
def logo(clase='lg', etiqueta=u'Indicio · Psic. Thania Huerta'):
    return u'<span class="%s" role="img" aria-label="%s"></span>' % (clase, etiqueta)

def sello(clase='sl'):
    return u'<span class="%s" role="img" aria-label="Indicio"></span>' % clase

def firma(*archivos):
    u"""Firma corta del contenido de los archivos. Se cuelga de cada enlace
    para que el navegador no pueda servir una version vieja en cache: si el
    archivo cambia, cambia la direccion."""
    h = hashlib.md5()
    for f in archivos:
        try: h.update(io.open(D + f, 'rb').read())
        except IOError: pass
    return h.hexdigest()[:8]

def cabeza(titulo, css, tema, fondo_form):
    v = firma('_base.css', '_detalle.css', '_nav.css', '_indicio.css', css, '_movil.css')
    return u'''<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="%s">
<title>%s</title>
<link rel="icon" href="../assets/img/indicio-sello.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="_base.css?v=%s">
<link rel="stylesheet" href="_detalle.css?v=%s">
<link rel="stylesheet" href="_nav.css?v=%s">
<link rel="stylesheet" href="_indicio.css?v=%s">
<link rel="stylesheet" href="%s?v=%s">
<link rel="stylesheet" href="_movil.css?v=%s">
</head>
<body data-fondo-form="%s">''' % (tema, titulo, v, v, v, v, css, v, v, fondo_form)

def pie():
    v = firma('_mapa.js', '_nav.js', '_detalle.js', '_rv.js')
    return u'''
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="_mapa.js?v=%s"></script>
<script src="_nav.js?v=%s"></script>
<script src="_detalle.js?v=%s"></script>
<script src="_rv.js?v=%s"></script>
</body>
</html>''' % (v, v, v, v)

def cab(num, clave, titulo, entrada=u''):
    u"""Apertura de seccion. Es la pieza que arregla lo que ella noto: da un
    punto de entrada con peso, en vez de que todo empiece igual."""
    e = u'\n    <p class="cab__d">%s</p>' % entrada if entrada else u''
    return u'''<div class="cab">
    <p class="cab__n" aria-hidden="true">%s</p>
    <p class="cab__k">%s</p>
    <h2>%s</h2>%s
  </div>''' % (num, clave, titulo, e)

def bloque_supuestos():
    li = u''.join([u'\n    <li><span class="sup__n">%02d</span><span class="sup__t">%s</span></li>'
                   % (i + 1, s) for i, s in enumerate(SUPUESTOS)])
    return u'<ol class="sup">%s\n  </ol>' % li

def bloque_motivos():
    u"""Lista corrida, no fichas. Son temas para hablar, no supuestos legales:
    piden ligereza, y de paso rompen la igualdad con la seccion de al lado."""
    return u'<ul class="mot">%s\n  </ul>' % u''.join(
        [u'\n    <li><span>%s</span></li>' % m for m in MOTIVOS])

def bloque_formacion():
    u"""Cada registro en tres partes: estudio, institucion y fechas. Las
    fechas salen de la tabla de su documento; la de la licenciatura venia
    invertida -agosto 2024 a mayo 2024- y se corrige a agosto 2020."""
    def via(nombre, lista, clase):
        li = u''.join([u'\n      <li><strong>%s</strong>'
                       u'<em>%s</em><time>%s</time></li>' % (a, b, f)
                       for a, b, f in lista])
        return (u'<div class="via via--%s">\n      <h3>%s</h3>\n'
                u'      <ol class="linea">%s\n      </ol>\n    </div>') % (clase, nombre, li)
    return u'<div class="vias">\n    %s\n    %s\n  </div>' % (
        via(u'V\u00eda cl\u00ednica', CLINICA, 'c'),
        via(u'V\u00eda forense', FORENSE, 'f'))

def bloque_indice():
    u"""Entrada por tarea, no por publico. NN/G desaconseja la navegacion por
    publico: la gente no se identifica con una sola categoria y anade un paso
    mental. Aqui la pregunta es que necesitas, y no esconde la otra mitad:
    son enlaces a secciones de la misma pagina."""
    return (u'<div class="idx">\n'
      u'    <a class="idx__c idx__c--f" href="#forense">\n'
      u'      <span class="idx__k">Para abogados, juzgados y particulares</span>\n'
      u'      <span class="idx__t">Necesito un peritaje psicol\u00f3gico</span>\n'
      u'      <span class="idx__d">Siete supuestos en materia familiar, y metapericiales.</span>\n'
      u'      <span class="idx__b">Ver el \u00e1rea forense</span>\n'
      u'    </a>\n'
      u'    <a class="idx__c idx__c--t" href="#terapia">\n'
      u'      <span class="idx__k">Para adolescentes, juventudes y sus familias</span>\n'
      u'      <span class="idx__t">Busco terapia para un adolescente</span>\n'
      u'      <span class="idx__d">Nueve motivos de consulta, y lo que no est\u00e9 en la lista tambi\u00e9n.</span>\n'
      u'      <span class="idx__b">Ver psicoterapia</span>\n'
      u'    </a>\n  </div>')

def bloque_bio():
    p = u''.join([u'''
    <div class="bio__b">
      <h3>%s</h3>
      <p>%s</p>
    </div>''' % (t, c) for t, c in BIO])
    return u'''<p class="bio__lead">%s</p>
  <div class="bio">%s
  </div>
  <blockquote class="cita"><p>%s</p></blockquote>''' % (BIO_LEAD, p, CITA)

def bloque_mapa():
    return u'''<div class="mapa-caja">
    <div id="mapa" data-lat="%s" data-lng="%s" data-zoom="17"
         role="application" aria-label="Mapa del consultorio"></div>
    <button class="mapa-toque" id="mapaToque" type="button" hidden><span>Toca para mover el mapa</span></button>
    <p class="mapa-aviso" id="mapaAviso" hidden>No se pudo cargar el mapa.</p>
  </div>
  <div class="rutas">
    <a class="b b--p" href="https://www.google.com/maps/dir/?api=1&amp;destination=%s,%s" target="_blank" rel="noopener">Google Maps</a>
    <a class="b b--s" href="https://waze.com/ul?ll=%s,%s&amp;navigate=yes" target="_blank" rel="noopener">Waze</a>
    <a class="b b--s" href="https://maps.apple.com/?daddr=%s,%s" target="_blank" rel="noopener">Apple Maps</a>
  </div>
  <dl class="datos">
    <div><dt>Direcci\u00f3n</dt><dd>Mauricio Garc\u00e9s 808, La Joya<span>76180 Santiago de Quer\u00e9taro, Qro.</span></dd></div>
    <div><dt>Horario</dt><dd>Lunes a viernes, 9:00 a 14:00 y 16:00 a 21:00<span>S\u00e1bados de 9:00 a 13:00</span></dd></div>
    <div><dt>Tel\u00e9fono</dt><dd><a href="%s">442 137 5118</a><span>Tambi\u00e9n por WhatsApp</span></dd></div>
    <div><dt>C\u00e9dula</dt><dd>14661976<span>Consejo de Psicolog\u00eda Forense 25-08-63</span></dd></div>
  </dl>''' % (LAT, LNG, LAT, LNG, LAT, LNG, LAT, LNG, TEL)

def bloque_cierre(fondo):
    return u'''<section class="cierre %s">
  <div class="w">
    %s
    <h2>Escr\u00edbeme, sin compromiso</h2>
    <p>Cu\u00e9ntame qu\u00e9 necesitas y te digo si puedo ayudarte. Si es un asunto legal,
       p\u00eddeme una cotizaci\u00f3n; si es para consulta, agendamos.</p>
    <div class="rutas rutas--2">
      <a class="b b--p" href="%s" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      <a class="b b--s" href="%s">Llamar ahora</a>
    </div>
  </div>
</section>

<footer class="fin"><div class="w fin__g">
  <div class="fin__m">%s<b>INDICIO<span>Psicolog\u00eda forense y psicoterapia</span></b></div>
  <div class="fin__d">
    <p>Psic. Thania Huerta \u00b7 C\u00e9dula profesional 14661976</p>
    <p>Consejo de Psicolog\u00eda Forense 25-08-63 \u00b7 Santiago de Quer\u00e9taro, Qro.</p>
  </div>
</div></footer>''' % (fondo, sello('sl sl--c'), WA, TEL, sello('sl sl--f'))

def cuerpo(clases):
    u"""Orden nuevo: que hace antes de quien es. La biografia son 223 palabras
    de prosa seguida, el bloque mas denso de la pagina, y estaba de primera:
    quien llega buscando un peritaje tenia que atravesarla. Baja dos sitios.

    Y cada lista toma una forma distinta -fichas, lista corrida, linea de
    tiempo- porque forense, psicoterapia y formacion tenian exactamente la
    misma, y por eso se leian como un solo apartado."""
    return u"""
<main>

<section class="s %s" id="empezar"><div class="w">
  <h2 class="idx__h">\u00bfQu\u00e9 necesitas?</h2>
  %s
</div></section>

<section class="s %s" id="forense"><div class="w">
  %s
  %s
  <div class="par">
    <article class="par__c">
      <h3>Metapericiales y an\u00e1lisis t\u00e9cnicos</h3>
      <p>Revisi\u00f3n t\u00e9cnica de un dictamen ya emitido, para valorar su m\u00e9todo y sus conclusiones.</p>
    </article>
    <article class="par__c par__c--acc">
      <h3>C\u00f3mo empieza</h3>
      <p>Cu\u00e9ntame el asunto y la fecha l\u00edmite, y te devuelvo el alcance y el costo.</p>
      <p class="par__l"><a href="#cotizacion">Pedir una cotizaci\u00f3n</a></p>
    </article>
  </div>
</div></section>

<section class="s %s" id="terapia"><div class="w">
  %s
  %s
</div></section>

<section class="s %s" id="sobre-mi"><div class="w">
  %s
  %s
</div></section>

<section class="s %s" id="formacion"><div class="w">
  %s
  %s
</div></section>

<section class="s %s" id="donde"><div class="w">
  %s
  %s
</div></section>

%s
</main>""" % (
   clases[0], bloque_indice(),
   clases[1], cab(u'01', u'\u00c1rea forense',
                  u'Cuando un proceso familiar necesita una valoraci\u00f3n psicol\u00f3gica',
                  u'Trabajo con abogados, juzgados y particulares. Estos son los siete '
                  u'supuestos en los que puedo intervenir.'),
   bloque_supuestos(),
   clases[2], cab(u'02', u'Psicoterapia', u'Temas en los que podemos trabajar',
                  u'Consulta para adolescentes y juventudes. Si lo que te pasa no est\u00e1 '
                  u'en la lista, escr\u00edbeme igual.'),
   bloque_motivos(),
   clases[3], cab(u'03', u'Sobre m\u00ed', u'Hola, soy Thania'), bloque_bio(),
   clases[4], cab(u'04', u'Formaci\u00f3n', u'En qu\u00e9 me he formado',
                  u'Dos recorridos en paralelo, uno por cada \u00e1rea en la que trabajo.'),
   bloque_formacion(),
   clases[5], cab(u'05', u'Consultorio', u'D\u00f3nde nos vemos',
                  u'Abre la ruta directo en tu aplicaci\u00f3n, o mueve el mapa para '
                  u'reconocer la zona.'),
   bloque_mapa(),
   bloque_cierre(clases[6]))

def portada(clase, fondo):
    u"""Texto a la izquierda, logotipo a la derecha y en grande, credenciales
    cruzando debajo. Los tres son hijos directos de la rejilla: antes el
    bloque de marca colgaba de dentro del texto y por eso no se podia colocar."""
    return u"""
<header class="pt %s %s" id="inicio"><div class="w pt__g">
  <div class="pt__t">
    <h1>Acompa\u00f1o a <em>adolescentes</em> en consulta y a <em>familias</em> en procesos judiciales.</h1>
    <p class="pt__d">Dos trabajos distintos, con l\u00edmites \u00e9ticos distintos.
       Aqu\u00ed puedes ver cu\u00e1l de los dos es el que est\u00e1s buscando.</p>
    <div class="rutas rutas--2">
      <a class="b b--p" href="%s" target="_blank" rel="noopener">Escr\u00edbeme por WhatsApp</a>
      <a class="b b--s" href="#cotizacion">Pedir una cotizaci\u00f3n</a>
    </div>
  </div>
  <div class="lock">
    %s
    <p class="lock__b">Psicolog\u00eda forense y psicoterapia</p>
  </div>
  <dl class="firma">
    <div><dt>Psic\u00f3loga</dt><dd>Thania Huerta</dd></div>
    <div><dt>C\u00e9dula profesional</dt><dd>14661976</dd></div>
    <div><dt>Consejo de Psicolog\u00eda Forense</dt><dd>25-08-63</dd></div>
    <div><dt>Consultorio</dt><dd>Santiago de Quer\u00e9taro</dd></div>
  </dl>
</div></header>""" % (clase, fondo, WA, logo('lg lg--p'))

if __name__ == '__main__':
    salidas = [
      ('reticula.html', u'Indicio · Retícula', '_reticula.css', '#C7B296', 'rt',
       ['s--arena', 's--olivo', 's--crema', 's--cacao', 's--arena', 's--olivo', 's--crema', 's--arena', 's--cacao']),
      ('ventanal.html', u'Indicio · Ventanal', '_ventanal.css', '#EAE2D7', 'vn',
       ['s--crema', 's--olivo', 's--arena', 's--terracota', 's--crema', 's--olivo', 's--arena', 's--crema', 's--cacao']),
    ]
    for arch, tit, css, tema, cl, fondos in salidas:
        h = cabeza(tit, css, tema, fondos[8]) + portada(cl, fondos[0]) + cuerpo(fondos[1:]) + pie()
        io.open(D + arch, 'w', encoding='utf-8').write(h)
        print('%-16s %6d bytes' % (arch, os.path.getsize(D + arch)))
