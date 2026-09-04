# -*- coding: utf-8 -*-
u"""Audita lo que el navegador calcula de verdad, no lo que dice el CSS.
Para cada elemento con texto: color calculado, fondo efectivo -subiendo por
los ancestros hasta encontrar uno opaco- y contraste entre los dos."""
import sys, io
from playwright.sync_api import sync_playwright

JS = r"""
() => {
  const lum = c => {
    const s = c.map(v => { v/=255; return v<=0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055,2.4); });
    return 0.2126*s[0]+0.7152*s[1]+0.0722*s[2];
  };
  const rgb = s => {
    let v = (s.match(/[\d.]+/g)||[]).map(Number);
    if (/^color\(/.test(s)) v = v.map((x,i) => i < 3 ? x*255 : x);  // srgb va de 0 a 1
    return v;
  };
  const opaco = s => { const v = rgb(s); return v.length>=3 && (v.length<4 || v[3] >= 0.8); };
  const fondoDe = el => {
    let n = el;
    while (n && n !== document.documentElement) {
      const bg = getComputedStyle(n).backgroundColor;
      if (opaco(bg)) return { color: bg, en: n.tagName.toLowerCase() +
        (n.className && typeof n.className === 'string' ? '.' + n.className.trim().split(/\s+/).join('.') : '') };
      n = n.parentElement;
    }
    return { color: getComputedStyle(document.body).backgroundColor, en: 'body' };
  };
  const out = [];
  document.querySelectorAll('body *').forEach(el => {
    const t = Array.from(el.childNodes)
      .filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
    if (!t || t.length < 2) return;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) < 0.1) return;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    let fg = rgb(cs.color); const f = fondoDe(el); let bgv = rgb(f.color);
    if (fg.length < 3 || bgv.length < 3) return;
    // Componer los alfas sobre el fondo: medirlos crudos falsea el contraste
    const mezcla = (a, b) => a.length > 3 && a[3] < 1
      ? a.slice(0,3).map((v,i) => v*a[3] + b[i]*(1-a[3])) : a.slice(0,3);
    const base = bgv.length > 3 && bgv[3] < 1
      ? mezcla(bgv, [255,255,255]) : bgv.slice(0,3);
    fg = mezcla(fg, base); bgv = base;
    let L1 = lum(fg), L2 = lum(bgv);
    if (L1 < L2) [L1, L2] = [L2, L1];
    const ratio = (L1 + 0.05) / (L2 + 0.05);
    const px = parseFloat(cs.fontSize), w = parseInt(cs.fontWeight) || 400;
    const grande = px >= 24 || (px >= 18.66 && w >= 700);
    out.push({
      sel: el.tagName.toLowerCase() + (el.id ? '#'+el.id : '') +
           (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : ''),
      txt: t.slice(0, 46), color: cs.color, fondo: f.color, fondoEn: f.en,
      ratio: Math.round(ratio*100)/100, px: Math.round(px*10)/10, peso: w,
      minimo: grande ? 3 : 4.5
    });
  });
  return out;
}
"""

def audita(url, ancho, alto):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': ancho, 'height': alto})
        pg.goto(url, wait_until='networkidle')
        pg.wait_for_timeout(900)
        datos = pg.evaluate(JS)
        b.close()
    return datos

if __name__ == '__main__':
    url, ancho = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 1280
    d = audita(url, ancho, 900)
    malos = [x for x in d if x['ratio'] < x['minimo']]
    print(u'%s  ·  %d px de ancho  ·  %d textos medidos' % (url.split('/')[-1], ancho, len(d)))
    if not malos:
        print(u'   sin fallos de contraste')
    else:
        print(u'   %d TEXTOS QUE NO SE LEEN:' % len(malos))
        vistos = set()
        for x in sorted(malos, key=lambda y: y['ratio']):
            k = (x['sel'], x['ratio'])
            if k in vistos: continue
            vistos.add(k)
            print(u'   %5.2f (pide %.1f)  %-30s %-22s' % (x['ratio'], x['minimo'], x['sel'][:30], x['txt'][:22]))
            print(u'          texto %s  sobre %s  (de %s)' % (x['color'], x['fondo'], x['fondoEn'][:34]))
