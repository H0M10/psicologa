# -*- coding: utf-8 -*-
# Los cuatro bocetos mid-century, dibujados desde MIDCENTURY.md.
# El contenido de Thania se importa de build.py: se guarda una sola vez, asi
# que los cuatro lo llevan completo por construccion.
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _build import (WA, TEL, LAT, LNG, BIO, SUPUESTOS, MOTIVOS, CLINICA, FORENSE,
                   mapa, datos_practicos, formacion_ol, pie)
D = 'c:/Users/hanni/Desktop/THPSICOLOGOA/bocetos/'

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
<link rel="stylesheet" href="_mc.css">
<link rel="stylesheet" href="%s">
</head>
<body>''' % (tema, titulo, fuentes, css)

def li_filas(xs):   return u''.join([u'\n      <li>%s</li>' % x for x in xs])
def parrafos(xs):   return u''.join([u'\n      <p>%s</p>' % x for x in xs])

H1  = u'Acompa\u00f1o a <em>adolescentes</em> en consulta y a <em>familias</em> en procesos judiciales.'
SUB = u'Dos trabajos distintos, con l\u00edmites \u00e9ticos distintos. Aqu\u00ed puedes ver cu\u00e1l de los dos es el que est\u00e1s buscando.'
H2F = u'Cuando un proceso familiar necesita una valoraci\u00f3n psicol\u00f3gica'
SBF = u'Trabajo con abogados, juzgados y particulares. Estos son los supuestos en los que puedo intervenir.'
H2T = u'Temas en los que podemos trabajar'
SBT = u'Consulta para adolescentes y juventudes. Si lo que te pasa no est\u00e1 en la lista, escr\u00edbeme igual.'
H2M = u'En qu\u00e9 me he formado'
SBM = u'Dos recorridos en paralelo, uno por cada \u00e1rea en la que trabajo.'
H2D = u'D\u00f3nde nos vemos'
SBD = u'Abre la ruta directo en tu aplicaci\u00f3n, o mueve el mapa para reconocer la zona.'
H2C = u'Escr\u00edbeme, sin compromiso'
SBC = u'Cu\u00e9ntame qu\u00e9 necesitas y te digo si puedo ayudarte. Si es un asunto legal, p\u00eddeme una cotizaci\u00f3n; si es para consulta, agendamos.'
META = u'Revisi\u00f3n t\u00e9cnica de un dictamen ya emitido, para valorar su m\u00e9todo y sus conclusiones.'
COTI = u'Cu\u00e9ntame el asunto y la fecha l\u00edmite, y te devuelvo el alcance y el costo.'

def botones(clase=''):
    return u'''<div class="rutas rutas--2 %s">
      <a class="b b--p" href="%s" target="_blank" rel="noopener">Escr\u00edbeme por WhatsApp</a>
      <a class="b b--s" href="#cotizacion">Pedir una cotizaci\u00f3n</a>
    </div>''' % (clase, WA)

def cierre(env=u'<div class="w">', cierra=u'</div>', clase=u''):
    return u'''
<section class="cierre%s">%s
  <h2>%s</h2>
  <p>%s</p>
  <div class="rutas rutas--2">
    <a class="b b--p" href="%s" target="_blank" rel="noopener">Escribir por WhatsApp</a>
    <a class="b b--s" href="%s">Llamar ahora</a>
  </div>
%s</section>
</main>

<footer class="fin"><div class="w">
  <p>Thania Huerta Pacheco \u00b7 Psic\u00f3loga cl\u00ednica y forense \u00b7 C\u00e9dula 14661976</p>
  <p>Santiago de Quer\u00e9taro, Qro.</p>
</div></footer>''' % (clase, env, H2C, SBC, WA, TEL, cierra)

# ── A · Credenza ─────────────────────────────────────────────────────────
def renderA():
    h = cabeza(u'Credenza \u00b7 Thania Huerta Pacheco', '_mcA.css',
               'family=Jost:wght@300..600&family=Archivo:wght@400;500;600;700', '#F0E9DB')
    h += u'''
<header class="pt" id="inicio">
  <div class="w pt__g">
    <div>
      <h1>%s</h1>
      <p class="sub">%s</p>
      %s
      <p class="cred" style="margin-top:1.6rem;padding-top:1rem;border-top:1px solid var(--linea);display:flex;flex-wrap:wrap;gap:.3rem 1.5rem;font-size:.85rem;color:var(--suave);max-width:none">
        <span>C\u00e9dula profesional <b>14661976</b></span>
        <span>Consejo de Psicolog\u00eda Forense <b>25-08-63</b></span>
      </p>
    </div>
    <img class="pt__r" src="../assets/img/retrato.svg" alt="Retrato de Thania Huerta Pacheco">
  </div>
  <div class="est" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
</header>

<main>
<section class="fr" id="sobre-mi"><div class="w enc">
  <p class="k">Sobre m\u00ed</p>
  <div><h2>Hola, soy Thania</h2><div class="cuerpo">%s</div></div>
</div></section>

<section class="fr fr--bronce" id="forense"><div class="w enc">
  <p class="k">\u00c1rea forense</p>
  <div>
    <h2>%s</h2><p class="sub">%s</p>
    <ol class="filas">%s</ol>
    <div class="par">
      <div class="c"><h3>Metapericiales y an\u00e1lisis t\u00e9cnicos</h3><p>%s</p></div>
      <div class="c"><h3>C\u00f3mo empieza</h3><p>%s</p><p style="margin-top:.8rem;font-weight:600"><a href="#cotizacion">Pedir una cotizaci\u00f3n</a></p></div>
    </div>
  </div>
</div></section>

<section class="fr fr--lana" id="terapia"><div class="w enc">
  <p class="k">Psicoterapia</p>
  <div><h2>%s</h2><p class="sub">%s</p><ul class="rej">%s</ul></div>
</div></section>

<section class="fr" id="formacion"><div class="w enc">
  <p class="k">Formaci\u00f3n</p>
  <div>
    <h2>%s</h2><p class="sub">%s</p>
    <div class="vias">
      <div class="via"><h3>V\u00eda cl\u00ednica</h3><ol>%s
      </ol></div>
      <div class="via"><h3>V\u00eda forense</h3><ol>%s
      </ol></div>
    </div>
  </div>
</div></section>

<section class="fr fr--lana" id="donde"><div class="w enc">
  <p class="k">Consultorio</p>
  <div><h2>%s</h2><p class="sub">%s</p>%s%s</div>
</div></section>
''' % (H1, SUB, botones(), parrafos(BIO), H2F, SBF, li_filas(SUPUESTOS), META, COTI,
       H2T, SBT, li_filas(MOTIVOS), H2M, SBM,
       formacion_ol(CLINICA), formacion_ol(FORENSE), H2D, SBD, mapa(), datos_practicos())
    return h + cierre() + pie()

# ── B · Reticula ─────────────────────────────────────────────────────────
def renderB():
    h = cabeza(u'Ret\u00edcula \u00b7 Thania Huerta Pacheco', '_mcB.css',
               'family=Archivo:wght@400;500;600;700', '#F8F4EA')
    h += u'''
<header class="pt rt" id="inicio"><div class="w g">
  <p class="k c1-3">Psicolog\u00eda<br>cl\u00ednica y forense</p>
  <div class="c4-12">
    <h1>%s</h1>
    <p class="sub" style="max-width:44ch">%s</p>
    %s
    <p class="cred"><span>C\u00e9dula profesional <b>14661976</b></span><span>Consejo de Psicolog\u00eda Forense <b>25-08-63</b></span><span>Santiago de Quer\u00e9taro</span></p>
  </div>
  <div class="pt__b" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
</div></header>

<main>
<section class="s s--lana rt" id="sobre-mi"><div class="w g">
  <p class="k c1-3">01 \u2014 Sobre m\u00ed</p>
  <div class="c4-11"><h2>Hola, soy Thania</h2><div class="cuerpo" style="margin-top:1.4rem">%s</div></div>
</div></section>

<section class="s s--bronce s--osc rt" id="forense"><div class="w g">
  <p class="k c1-3">02 \u2014 \u00c1rea forense</p>
  <div class="c4-12">
    <h2>%s</h2><p class="sub">%s</p>
    <ol class="filas" style="margin-top:1.8rem">%s</ol>
    <div class="par">
      <div class="c"><h3>Metapericiales y an\u00e1lisis t\u00e9cnicos</h3><p>%s</p></div>
      <div class="c"><h3>C\u00f3mo empieza</h3><p>%s</p><p style="margin-top:.8rem;font-weight:600"><a href="#cotizacion" style="color:var(--papel)">Pedir una cotizaci\u00f3n</a></p></div>
    </div>
  </div>
</div></section>

<section class="s s--cil s--osc rt" id="terapia"><div class="w g">
  <p class="k c1-3">03 \u2014 Psicoterapia</p>
  <div class="c4-12"><h2>%s</h2><p class="sub">%s</p><ul class="rej" style="margin-top:1.8rem">%s</ul></div>
</div></section>

<section class="s s--lana rt" id="formacion"><div class="w g">
  <p class="k c1-3">04 \u2014 Formaci\u00f3n</p>
  <div class="c4-12"><h2>%s</h2><p class="sub">%s</p>
    <div class="vias">
      <div class="via"><h3>V\u00eda cl\u00ednica</h3><ol>%s
      </ol></div>
      <div class="via"><h3>V\u00eda forense</h3><ol>%s
      </ol></div>
    </div>
  </div>
</div></section>

<section class="s rt" id="donde"><div class="w g">
  <p class="k c1-3">05 \u2014 Consultorio</p>
  <div class="c4-12"><h2>%s</h2><p class="sub">%s</p>%s%s</div>
</div></section>
''' % (H1, SUB, botones(), parrafos(BIO), H2F, SBF, li_filas(SUPUESTOS), META, COTI,
       H2T, SBT, li_filas(MOTIVOS), H2M, SBM,
       formacion_ol(CLINICA), formacion_ol(FORENSE), H2D, SBD, mapa(), datos_practicos())
    return h + cierre(u'<div class="w g"><div class="c4-12">', u'</div></div>', u' s--mora s--osc') + pie()

# ── C · Silueta ──────────────────────────────────────────────────────────
def renderC():
    h = cabeza(u'Silueta \u00b7 Thania Huerta Pacheco', '_mcC.css',
               'family=Jost:wght@400..700&family=Archivo:wght@400;500;600;700', '#F0E9DB')
    h += u'''
<header class="pt" id="inicio"><div class="w pt__g">
  <div>
    <h1>%s</h1>
    <p class="sub">%s</p>
    %s
    <p class="cred"><span>C\u00e9dula profesional <b>14661976</b></span><span>Consejo forense <b>25-08-63</b></span></p>
  </div>
  <div class="sil">
    <i aria-hidden="true"></i><i aria-hidden="true"></i><i aria-hidden="true"></i>
    <img src="../assets/img/retrato.svg" alt="Retrato de Thania Huerta Pacheco">
  </div>
</div></header>

<main>
<section class="pl pl--lana" id="sobre-mi"><div class="w">
  <p class="k">Sobre m\u00ed</p><h2>Hola, soy Thania</h2>
  <div class="cuerpo">%s</div>
</div></section>

<section class="pl pl--a" id="forense"><div class="w">
  <p class="k">\u00c1rea forense</p><h2>%s</h2><p class="sub">%s</p>
  <ol class="filas">%s</ol>
  <div class="par">
    <div class="c"><h3>Metapericiales y an\u00e1lisis t\u00e9cnicos</h3><p>%s</p></div>
    <div class="c"><h3>C\u00f3mo empieza</h3><p>%s</p><p style="margin-top:.8rem;font-weight:600"><a href="#cotizacion" style="color:var(--barro)">Pedir una cotizaci\u00f3n</a></p></div>
  </div>
</div></section>

<section class="pl pl--b" id="terapia"><div class="w">
  <p class="k">Psicoterapia</p><h2>%s</h2><p class="sub">%s</p>
  <ul class="rej">%s</ul>
</div></section>

<section class="pl pl--lana" id="formacion"><div class="w">
  <p class="k">Formaci\u00f3n</p><h2>%s</h2><p class="sub">%s</p>
  <div class="vias">
    <div class="via"><h3>V\u00eda cl\u00ednica</h3><ol>%s
    </ol></div>
    <div class="via"><h3>V\u00eda forense</h3><ol>%s
    </ol></div>
  </div>
</div></section>

<section class="pl pl--c" id="donde"><div class="w">
  <p class="k">Consultorio</p><h2>%s</h2><p class="sub">%s</p>%s%s
</div></section>
''' % (H1, SUB, botones(), parrafos(BIO), H2F, SBF, li_filas(SUPUESTOS), META, COTI,
       H2T, SBT, li_filas(MOTIVOS), H2M, SBM,
       formacion_ol(CLINICA), formacion_ol(FORENSE), H2D, SBD, mapa(), datos_practicos())
    return h + cierre() + pie()

# ── D · Ventanal ─────────────────────────────────────────────────────────
def renderD():
    h = cabeza(u'Ventanal \u00b7 Thania Huerta Pacheco', '_mcD.css',
               'family=Outfit:wght@200..600&family=Hanken+Grotesk:wght@300..600', '#F8F4EA')
    h += u'''
<header class="pt" id="inicio">
  <div class="pt__f" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="wa"><div class="pt__v">
    <h1>%s</h1>
    <p class="sub">%s</p>
    %s
    <p class="cred">
      <span>C\u00e9dula profesional <b>14661976</b></span>
      <span>Consejo de Psicolog\u00eda Forense <b>25-08-63</b></span>
      <span>Santiago de Quer\u00e9taro, Qro.</span>
    </p>
  </div></div>
</header>

<main>
<section class="s" id="sobre-mi"><div class="w">
  <p class="k">Sobre m\u00ed</p><h2>Hola, soy Thania</h2>
  <div class="cuerpo">%s</div>
</div></section>

<section class="s s--verde" id="forense"><div class="w">
  <p class="k">\u00c1rea forense</p><h2>%s</h2><p class="sub">%s</p>
  <ol class="filas">%s</ol>
  <div class="par">
    <div class="c"><h3>Metapericiales y an\u00e1lisis t\u00e9cnicos</h3><p>%s</p></div>
    <div class="c"><h3>C\u00f3mo empieza</h3><p>%s</p><p style="margin-top:.9rem;font-weight:600"><a href="#cotizacion" style="color:var(--aguacate)">Pedir una cotizaci\u00f3n</a></p></div>
  </div>
</div></section>

<section class="s" id="terapia"><div class="w">
  <p class="k">Psicoterapia</p><h2>%s</h2><p class="sub">%s</p>
  <ul class="rej">%s</ul>
</div></section>

<section class="s s--lana" id="formacion"><div class="w">
  <p class="k">Formaci\u00f3n</p><h2>%s</h2><p class="sub">%s</p>
  <div class="vias">
    <div class="via"><h3>V\u00eda cl\u00ednica</h3><ol>%s
    </ol></div>
    <div class="via"><h3>V\u00eda forense</h3><ol>%s
    </ol></div>
  </div>
</div></section>

<section class="s" id="donde"><div class="wa">
  <div class="w" style="margin-inline:0"><p class="k">Consultorio</p><h2>%s</h2><p class="sub">%s</p></div>
  %s
  <div class="w" style="margin-inline:0">%s</div>
</div></section>
''' % (H1, SUB, botones(), parrafos(BIO), H2F, SBF, li_filas(SUPUESTOS), META, COTI,
       H2T, SBT, li_filas(MOTIVOS), H2M, SBM,
       formacion_ol(CLINICA), formacion_ol(FORENSE), H2D, SBD, mapa(), datos_practicos())
    return h + cierre() + pie()

if __name__ == '__main__':
    for nombre, fn in [('credenza', renderA), ('reticula', renderB),
                       ('silueta', renderC), ('ventanal', renderD)]:
        ruta = D + 'mc-%s.html' % nombre
        io.open(ruta, 'w', encoding='utf-8').write(fn())
        print('mc-%-9s %6d bytes' % (nombre + '.html', os.path.getsize(ruta)))
