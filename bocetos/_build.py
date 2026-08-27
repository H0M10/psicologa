# -*- coding: utf-8 -*-
# Genera los bocetos 3, 4 y 5. El contenido de Thania vive aqui una sola vez,
# asi que los tres lo llevan completo por construccion. Lo que cambia es el
# diseno, no la informacion.
import io, os
D = 'c:/Users/hanni/Desktop/THPSICOLOGOA/bocetos/'

WA  = 'https://wa.me/524421375118?text=Hola%20Thania%2C%20vi%20tu%20p%C3%A1gina%20y%20me%20gustar%C3%ADa%20preguntarte%20algo.'
TEL = 'tel:+524421375118'
LAT, LNG = '20.572439', '-100.4184025'

BIO = [
 u'Soy psic\u00f3loga con formaci\u00f3n y experiencia profesional en los \u00e1mbitos cl\u00ednico y forense. Dentro del \u00e1rea forense trabajo principalmente en materia familiar, lo que me ha permitido comprender las distintas situaciones y necesidades que pueden presentarse en las familias. En el \u00e1rea cl\u00ednica, mi pr\u00e1ctica est\u00e1 dedicada exclusivamente al acompa\u00f1amiento de adolescentes y juventudes.',
 u'Eleg\u00ed trabajar con esta poblaci\u00f3n porque considero que la adolescencia es un momento decisivo en la construcci\u00f3n de las personas adultas del futuro. Acompa\u00f1arlos oportunamente puede generar cambios importantes en el presente, mientras desarrollan su identidad y su propia manera de relacionarse con el mundo.',
 u'Mi experiencia cl\u00ednica me permite crear espacios de crecimiento, cuestionamiento y desarrollo personal. Por su parte, mi formaci\u00f3n forense me ha ense\u00f1ado a comprender a cada persona dentro de un contexto m\u00e1s amplio. Aunque ambos \u00e1mbitos tienen objetivos y l\u00edmites \u00e9ticos diferentes, juntos enriquecen mi manera de comprender el comportamiento humano.',
 u'Disfruto estudiar y mantenerme en constante actualizaci\u00f3n. Procuro que mi trabajo se sustente en evidencia cient\u00edfica, pero tambi\u00e9n creo que la terapia puede ser cercana y creativa: disfruto crear materiales y adaptar actividades y herramientas a la personalidad, los intereses y las necesidades de cada adolescente.']

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

CLINICA = [
 (u'Licenciatura en Psicolog\u00eda', u'Universidad Aut\u00f3noma de Quer\u00e9taro'),
 (u'Maestr\u00eda en Psicoterapia Cognitivo Conductual', u'Centro de Psicoterapia Cognitiva'),
 (u'Diplomado en Psicoterapia Cognitivo Conductual', u'Centro de Psicoterapia Cognitiva'),
 (u'Diplomado en Psicoterapia Infantojuvenil', u'Centro de Atenci\u00f3n Psicol\u00f3gica y Capacitaci\u00f3n Integral')]

FORENSE = [
 (u'Maestr\u00eda en Investigaci\u00f3n y Evaluaci\u00f3n Criminal y Forense', u'Universidad Mondrag\u00f3n M\u00e9xico'),
 (u'Certificaci\u00f3n en An\u00e1lisis de Contexto en la Investigaci\u00f3n Criminal', u'Instituto de Ciencia Aplicada'),
 (u'Certificador en Psicolog\u00eda Forense', u'Ciencia Aplicada'),
 (u'Curso-taller de peritajes psicol\u00f3gicos en guarda y custodia', u'Con perspectiva de infancia'),
 (u'Curso de elaboraci\u00f3n de peritajes judiciales', u'Centro de SubjetividadEs, Identidad Cl\u00ednica y Forense')]

def cabeza(titulo, css, fuentes, tema):
    return u'''<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="%s">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?%s&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link rel="stylesheet" href="_base.css">
<link rel="stylesheet" href="_detalle.css">
<link rel="stylesheet" href="%s">
</head>
<body>''' % (tema, titulo, fuentes, css)

def pie():
    return u'''
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="_mapa.js"></script>
<script src="_detalle.js"></script>
<script src="_rv.js"></script>
</body>
</html>'''

def mapa(clase=''):
    return u'''
  <div class="mapa-caja %s">
    <div id="mapa" data-lat="%s" data-lng="%s" data-zoom="17"
         role="application" aria-label="Mapa del consultorio"></div>
    <button class="mapa-toque" id="mapaToque" type="button" hidden><span>Toca para mover el mapa</span></button>
    <p class="mapa-aviso" id="mapaAviso" hidden>No se pudo cargar el mapa.</p>
  </div>
  <div class="rutas">
    <a class="b b--p" href="https://www.google.com/maps/dir/?api=1&amp;destination=%s,%s" target="_blank" rel="noopener">Google Maps</a>
    <a class="b b--s" href="https://waze.com/ul?ll=%s,%s&amp;navigate=yes" target="_blank" rel="noopener">Waze</a>
    <a class="b b--s" href="https://maps.apple.com/?daddr=%s,%s" target="_blank" rel="noopener">Apple Maps</a>
  </div>''' % (clase, LAT, LNG, LAT, LNG, LAT, LNG, LAT, LNG)

def datos_practicos():
    return u'''
  <dl class="datos">
    <div><dt>Direcci\u00f3n</dt><dd>Mauricio Garc\u00e9s 808, La Joya<span>76180 Santiago de Quer\u00e9taro, Qro.</span></dd></div>
    <div><dt>Horario</dt><dd>Lunes a viernes, 9:00 a 14:00 y 16:00 a 21:00<span>S\u00e1bados de 9:00 a 13:00</span></dd></div>
    <div><dt>Tel\u00e9fono</dt><dd><a href="%s">442 137 5118</a><span>Tambi\u00e9n por WhatsApp</span></dd></div>
    <div><dt>C\u00e9dula</dt><dd>14661976<span>Consejo de Psicolog\u00eda Forense 25-08-63</span></dd></div>
  </dl>''' % TEL

def formacion_ol(lista):
    return u''.join([u'\n      <li><strong>%s</strong><em>%s</em></li>' % (a, b) for a, b in lista])

# ── 04 · Mosaico ─────────────────────────────────────────────────────────
# De su segunda imagen: los motivos geometricos de azulejo mid-century.
# Cuatro simbolos dibujados una vez y reutilizados con <use>.
SPRITE = u'''
<svg class="oculto" aria-hidden="true" focusable="false"><defs>
  <symbol id="t-petalo" viewBox="0 0 64 64">
    <path d="M32 4a28 28 0 0 1 0 56 28 28 0 0 1 0-56z" fill="none"/>
    <path d="M32 32C32 16 40 4 56 4 56 20 48 32 32 32z"/><path d="M32 32C48 32 60 40 60 56 44 56 32 48 32 32z"/>
    <path d="M32 32C32 48 24 60 8 60 8 44 16 32 32 32z"/><path d="M32 32C16 32 4 24 4 8 20 8 32 16 32 32z"/>
  </symbol>
  <symbol id="t-circulos" viewBox="0 0 64 64">
    <g fill="none" stroke="currentColor" stroke-width="3">
      <circle cx="32" cy="32" r="28"/><circle cx="32" cy="32" r="21"/>
      <circle cx="32" cy="32" r="14"/><circle cx="32" cy="32" r="7"/>
    </g><circle cx="32" cy="32" r="2.5"/>
  </symbol>
  <symbol id="t-estrella" viewBox="0 0 64 64">
    <path d="M32 2c2 16 12 26 28 30-16 4-26 14-28 30-2-16-12-26-28-30C20 28 30 18 32 2z"/>
  </symbol>
  <symbol id="t-abanico" viewBox="0 0 64 64">
    <path d="M6 56V24l8-8v40zM22 56V16l8-8v48zM38 56V8l8-8v56zM54 56V16l8-8v48z"/>
  </symbol>
</defs></svg>'''

def tile(nombre, clase=''):
    return u'<svg class="tile %s" aria-hidden="true"><use href="#t-%s"></use></svg>' % (clase, nombre)

def render04():
    mosaico = u''.join([u'<div class="mo__c mo__c--%d">%s</div>' % (i + 1, tile(n))
                        for i, n in enumerate(['petalo','circulos','estrella','abanico',
                                               'circulos','petalo','abanico','estrella'])])
    sup = u''.join([u'\n      <li>%s<span>%s</span></li>' %
                    (tile(['petalo','circulos','estrella','abanico'][i % 4], 'tile--s'), s)
                    for i, s in enumerate(SUPUESTOS)])
    mot = u''.join([u'\n      <li>%s</li>' % m for m in MOTIVOS])
    bio = u''.join([u'\n      <p>%s</p>' % p for p in BIO])
    h = cabeza(u'Boceto 4 \u00b7 Mosaico \u00b7 Thania Huerta Pacheco', '_c04.css',
               'family=Outfit:wght@300..700&family=Karla:wght@400;500;600;700', '#E4E2DA')
    h += SPRITE
    h += u'''
<header class="top"><div class="w top__in">
  <a class="marca" href="#inicio">%s<b>Thania Huerta<span>Psic\u00f3loga cl\u00ednica y forense</span></b></a>
  <nav aria-label="Secciones">
    <a href="#sobre-mi">Sobre m\u00ed</a><a href="#forense">Forense</a>
    <a href="#terapia">Psicoterapia</a><a href="#formacion">Formaci\u00f3n</a><a href="#donde">Consultorio</a>
  </nav>
</div></header>

<main>
<section class="hero" id="inicio"><div class="w hero__g">
  <div class="hero__t">
    <h1>Acompa\u00f1o a adolescentes en consulta y a familias en procesos judiciales.</h1>
    <p class="lead">Dos trabajos distintos, con l\u00edmites \u00e9ticos distintos. Aqu\u00ed puedes ver cu\u00e1l de los dos es el que est\u00e1s buscando.</p>
    <div class="rutas rutas--2">
      <a class="b b--p" href="%s" target="_blank" rel="noopener">Escr\u00edbeme por WhatsApp</a>
      <a class="b b--s" href="#cotizacion">Pedir una cotizaci\u00f3n</a>
    </div>
    <p class="cred"><span>C\u00e9dula profesional <b>14661976</b></span><span>Consejo de Psicolog\u00eda Forense <b>25-08-63</b></span></p>
  </div>
  <div class="mo" aria-hidden="true">%s</div>
</div></section>

<section class="s s--papel" id="sobre-mi"><div class="w">
  <h2 class="tit">%sHola, soy Thania</h2>
  <div class="cuerpo">%s</div>
</div></section>

<section class="s s--verde" id="forense"><div class="w">
  <h2 class="tit">%sCuando un proceso familiar necesita una valoraci\u00f3n psicol\u00f3gica</h2>
  <p class="lead">Trabajo con abogados, juzgados y particulares. Estos son los supuestos en los que puedo intervenir.</p>
  <ul class="sup">%s
  </ul>
  <div class="par">
    <div class="par__c"><h3>Metapericiales y an\u00e1lisis t\u00e9cnicos</h3><p>Revisi\u00f3n t\u00e9cnica de un dictamen ya emitido, para valorar su m\u00e9todo y sus conclusiones.</p></div>
    <div class="par__c par__c--acc"><h3>C\u00f3mo empieza</h3><p>Cu\u00e9ntame el asunto y la fecha l\u00edmite, y te devuelvo el alcance y el costo.</p><p class="par__l"><a href="#cotizacion">Pedir una cotizaci\u00f3n</a></p></div>
  </div>
</div></section>

<section class="s s--verde" id="terapia"><div class="w">
  <h2 class="tit">%sTemas en los que podemos trabajar</h2>
  <p class="lead">Consulta para adolescentes y juventudes. Si lo que te pasa no est\u00e1 en la lista, escr\u00edbeme igual.</p>
  <ul class="mot">%s
  </ul>
</div></section>
''' % (tile('petalo','tile--m'), WA, mosaico, tile('circulos','tile--t'), bio,
       tile('estrella','tile--t'), sup, tile('petalo','tile--t'), mot)
    h += u'''
<section class="s s--papel" id="formacion"><div class="w">
  <h2 class="tit">%sEn qu\u00e9 me he formado</h2>
  <p class="lead">Dos recorridos en paralelo, uno por cada \u00e1rea en la que trabajo.</p>
  <div class="vias">
    <div class="via"><h3>V\u00eda cl\u00ednica</h3><ol>%s
    </ol></div>
    <div class="via"><h3>V\u00eda forense</h3><ol>%s
    </ol></div>
  </div>
</div></section>

<section class="s" id="donde"><div class="w">
  <h2 class="tit">%sD\u00f3nde nos vemos</h2>
  <p class="lead">Abre la ruta directo en tu aplicaci\u00f3n, o mueve el mapa para reconocer la zona.</p>
  %s
  %s
</div></section>

<section class="cierre"><div class="w">
  <div class="cierre__t" aria-hidden="true">%s%s%s%s</div>
  <h2>Escr\u00edbeme, sin compromiso</h2>
  <p>Cu\u00e9ntame qu\u00e9 necesitas y te digo si puedo ayudarte. Si es un asunto legal, p\u00eddeme una cotizaci\u00f3n; si es para consulta, agendamos.</p>
  <div class="rutas rutas--2">
    <a class="b b--p" href="%s" target="_blank" rel="noopener">Escribir por WhatsApp</a>
    <a class="b b--s" href="%s">Llamar ahora</a>
  </div>
</div></section>
</main>

<footer class="fin"><div class="w">
  <p>Thania Huerta Pacheco \u00b7 Psic\u00f3loga cl\u00ednica y forense \u00b7 C\u00e9dula 14661976</p>
  <p>Santiago de Quer\u00e9taro, Qro.</p>
</div></footer>''' % (tile('abanico','tile--t'), formacion_ol(CLINICA), formacion_ol(FORENSE),
                      tile('circulos','tile--t'), mapa(), datos_practicos(),
                      tile('estrella'), tile('petalo'), tile('circulos'), tile('abanico'),
                      WA, TEL)
    return h + pie()

# ── 05 · Atomico ─────────────────────────────────────────────────────────
# Su misma paleta, invertida: fondo verde bosque y tipografia crema. Sirve
# para que vea como se comportan sus colores en oscuro, que es como se ve
# un consultorio con madera y luz calida de noche.
EST = u'''<svg class="est" viewBox="0 0 120 120" aria-hidden="true">
  <g stroke="currentColor" stroke-width="1.2" fill="none">
    <line x1="60" y1="0" x2="60" y2="120"/><line x1="0" y1="60" x2="120" y2="60"/>
    <line x1="17" y1="17" x2="103" y2="103"/><line x1="103" y1="17" x2="17" y2="103"/>
  </g>
  <circle cx="60" cy="60" r="9" fill="currentColor"/>
  <g fill="currentColor"><circle cx="60" cy="6" r="3.5"/><circle cx="60" cy="114" r="3.5"/>
   <circle cx="6" cy="60" r="3.5"/><circle cx="114" cy="60" r="3.5"/></g>
</svg>'''

def render05():
    sup = u''.join([u'\n      <li><span>%02d</span>%s</li>' % (i + 1, s)
                    for i, s in enumerate(SUPUESTOS)])
    mot = u''.join([u'\n      <li>%s</li>' % m for m in MOTIVOS])
    bio = u''.join([u'\n      <p>%s</p>' % p for p in BIO])
    h = cabeza(u'Boceto 5 \u00b7 At\u00f3mico \u00b7 Thania Huerta Pacheco', '_c05.css',
               'family=Josefin+Sans:wght@300..600&family=Lora:ital,wght@0,400..600;1,400',
               '#22301F')
    h += u'''
<header class="ap" id="inicio">
  <div class="ap__est" aria-hidden="true">%s</div>
  <p class="ap__k">Psicolog\u00eda cl\u00ednica y forense</p>
  <h1>Thania Huerta Pacheco</h1>
  <p class="ap__d">Acompa\u00f1o a adolescentes en consulta y a familias en procesos judiciales. Dos trabajos distintos, con l\u00edmites \u00e9ticos distintos.</p>
  <div class="rutas rutas--2">
    <a class="b b--p" href="%s" target="_blank" rel="noopener">Escr\u00edbeme por WhatsApp</a>
    <a class="b b--s" href="#cotizacion">Pedir una cotizaci\u00f3n</a>
  </div>
  <p class="ap__c"><span>C\u00e9dula profesional <b>14661976</b></span><span>Consejo de Psicolog\u00eda Forense <b>25-08-63</b></span><span>Santiago de Quer\u00e9taro</span></p>
</header>

<main>
<section class="s" id="sobre-mi"><div class="w">
  <div class="s__c"><p class="k">Sobre m\u00ed</p><h2>Hola, soy Thania</h2></div>
  <div class="cuerpo">%s</div>
</div></section>

<div class="div" aria-hidden="true">%s</div>

<section class="s s--verde" id="forense"><div class="w">
  <div class="s__c"><p class="k">\u00c1rea forense</p>
    <h2>Cuando un proceso familiar necesita una valoraci\u00f3n psicol\u00f3gica</h2>
    <p class="lead">Trabajo con abogados, juzgados y particulares. Estos son los supuestos en los que puedo intervenir.</p></div>
  <ol class="sup">%s
  </ol>
  <div class="par">
    <div class="par__c"><h3>Metapericiales y an\u00e1lisis t\u00e9cnicos</h3><p>Revisi\u00f3n t\u00e9cnica de un dictamen ya emitido, para valorar su m\u00e9todo y sus conclusiones.</p></div>
    <div class="par__c"><h3>C\u00f3mo empieza</h3><p>Cu\u00e9ntame el asunto y la fecha l\u00edmite, y te devuelvo el alcance y el costo.</p><p class="par__l"><a href="#cotizacion">Pedir una cotizaci\u00f3n</a></p></div>
  </div>
</div></section>

<div class="div" aria-hidden="true">%s</div>

<section class="s" id="terapia"><div class="w">
  <div class="s__c"><p class="k">Psicoterapia</p><h2>Temas en los que podemos trabajar</h2>
    <p class="lead">Consulta para adolescentes y juventudes. Si lo que te pasa no est\u00e1 en la lista, escr\u00edbeme igual.</p></div>
  <ul class="mot">%s
  </ul>
</div></section>
''' % (EST, WA, bio, EST, sup, EST, mot)
    h += u'''
<div class="div" aria-hidden="true">%s</div>

<section class="s s--vino" id="formacion"><div class="w">
  <div class="s__c"><p class="k">Formaci\u00f3n</p><h2>En qu\u00e9 me he formado</h2>
    <p class="lead">Dos recorridos en paralelo, uno por cada \u00e1rea en la que trabajo.</p></div>
  <div class="vias">
    <div class="via"><h3>V\u00eda cl\u00ednica</h3><ol>%s
    </ol></div>
    <div class="via"><h3>V\u00eda forense</h3><ol>%s
    </ol></div>
  </div>
</div></section>

<div class="div" aria-hidden="true">%s</div>

<section class="s" id="donde"><div class="w">
  <div class="s__c"><p class="k">Consultorio</p><h2>D\u00f3nde nos vemos</h2>
    <p class="lead">Abre la ruta directo en tu aplicaci\u00f3n, o mueve el mapa para reconocer la zona.</p></div>
  %s
  %s
</div></section>

<section class="cierre"><div class="w">
  <div class="cierre__e" aria-hidden="true">%s</div>
  <h2>Escr\u00edbeme, sin compromiso</h2>
  <p>Cu\u00e9ntame qu\u00e9 necesitas y te digo si puedo ayudarte. Si es un asunto legal, p\u00eddeme una cotizaci\u00f3n; si es para consulta, agendamos.</p>
  <div class="rutas rutas--2">
    <a class="b b--p" href="%s" target="_blank" rel="noopener">Escribir por WhatsApp</a>
    <a class="b b--s" href="%s">Llamar ahora</a>
  </div>
</div></section>
</main>

<footer class="fin"><div class="w">
  <p>Thania Huerta Pacheco \u00b7 Psic\u00f3loga cl\u00ednica y forense \u00b7 C\u00e9dula 14661976</p>
  <p>Santiago de Quer\u00e9taro, Qro.</p>
</div></footer>''' % (EST, formacion_ol(CLINICA), formacion_ol(FORENSE), EST,
                      mapa(), datos_practicos(), EST, WA, TEL)
    return h + pie()

if __name__ == '__main__':
    for n, fn in [('4', render04), ('5', render05)]:
        ruta = D + 'propuesta-%s.html' % n
        io.open(ruta, 'w', encoding='utf-8').write(fn())
        print('propuesta-%s.html  %d bytes' % (n, os.path.getsize(ruta)))
