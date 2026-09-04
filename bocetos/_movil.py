# -*- coding: utf-8 -*-
u"""Diagnostico de movil: medida de linea, tamanos, objetivos tactiles,
desbordes, ritmo vertical y cuanto hay que desplazar."""
import sys
from playwright.sync_api import sync_playwright
JS = r"""
() => {
  const R = {};
  R.alto = document.documentElement.scrollHeight;
  R.ancho = document.documentElement.scrollWidth;
  R.vw = window.innerWidth;

  // Medida de linea en caracteres, sobre parrafos y elementos de lista
  const medida = [];
  document.querySelectorAll('p, li, dd, .bio__b p, .cab__d').forEach(el => {
    const t = el.textContent.trim();
    if (t.length < 40) return;
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    if (r.width < 20) return;
    // ancho aproximado de caracter: 0.5 del tamano para una sans
    const ch = r.width / (parseFloat(cs.fontSize) * 0.5);
    medida.push({sel: el.className || el.tagName, ch: Math.round(ch),
                 px: Math.round(parseFloat(cs.fontSize)*10)/10, txt: t.slice(0,28)});
  });
  R.medida = medida;

  // Objetivos tactiles
  const toca = [];
  document.querySelectorAll('a, button, input, select, textarea, [role=button]').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return;
    if (getComputedStyle(el).display === 'none') return;
    toca.push({sel: (el.className||el.tagName).toString().split(' ')[0],
               w: Math.round(r.width), h: Math.round(r.height),
               txt: (el.textContent||'').trim().slice(0,20)});
  });
  R.toca = toca;

  // Desbordes horizontales
  const desborda = [];
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width > window.innerWidth + 2 || r.right > window.innerWidth + 2)
      desborda.push({sel: (el.className||el.tagName).toString().split(' ')[0],
                     w: Math.round(r.width), right: Math.round(r.right)});
  });
  R.desborda = desborda.slice(0, 8);

  // Alto de cada seccion, en pantallas
  R.secciones = Array.from(document.querySelectorAll('.pt, .s, .cierre')).map(el => {
    const r = el.getBoundingClientRect();
    return {sel: (el.className||'').toString().split(' ').slice(0,2).join('.'),
            id: el.id || '', alto: Math.round(r.height),
            pantallas: Math.round(r.height / window.innerHeight * 10) / 10};
  });
  return R;
}
"""
url, ancho = sys.argv[1], int(sys.argv[2])
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': ancho, 'height': 844},
                    device_scale_factor=3, is_mobile=True, has_touch=True)
    pg.goto(url, wait_until='networkidle'); pg.wait_for_timeout(1200)
    d = pg.evaluate(JS); b.close()

print(u'%s  ·  %d x 844' % (url.split('/')[-1], ancho))
print(u'  alto total %d px  =  %.1f pantallas' % (d['alto'], d['alto']/844.0))
if d['desborda']:
    print(u'  DESBORDA (ancho de ventana %d):' % d['vw'])
    for x in d['desborda']: print(u'     %-20s ancho %d, borde derecho %d' % (x['sel'], x['w'], x['right']))
else:
    print(u'  sin desbordes horizontales')

largas = [m for m in d['medida'] if m['ch'] > 45]
cortas = [m for m in d['medida'] if m['ch'] < 28]
print(u'\n  MEDIDA DE LINEA  (en movil lo comodo son 30-40 caracteres)')
print(u'     %d textos medidos · %d por encima de 45 · %d por debajo de 28'
      % (len(d['medida']), len(largas), len(cortas)))
for m in sorted(d['medida'], key=lambda x: -x['ch'])[:5]:
    print(u'     %3d ch  %4.1f px  %-16s %s' % (m['ch'], m['px'], str(m['sel'])[:16], m['txt']))

chicos = [t for t in d['toca'] if t['h'] < 44 or t['w'] < 44]
print(u'\n  OBJETIVOS TACTILES  (minimo 44x44)')
print(u'     %d medidos · %d por debajo' % (len(d['toca']), len(chicos)))
for t in chicos[:6]:
    print(u'     %3dx%-3d  %-16s %s' % (t['w'], t['h'], t['sel'][:16], t['txt']))

print(u'\n  ALTO POR SECCION')
for s in d['secciones']:
    aviso = '  <-- muy larga' if s['pantallas'] > 3 else ''
    print(u'     %-16s %5d px  %4.1f pantallas%s' % (s['id'] or s['sel'][:16], s['alto'], s['pantallas'], aviso))
