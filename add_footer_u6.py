# -*- coding: utf-8 -*-
"""Agrega el footer de navegación estilo cfn a todas las páginas de Unidad 6."""
import re, os

BASE = "D:/filosofia_experimental/"

FOOTER_CSS = """
/* ── Footer navegación (cfn) ── */
.class-footer-nav{background:linear-gradient(160deg,#07080f 0%,#0d1020 60%,#07080f 100%);border-top:2px solid rgba(250,204,21,.18);padding:52px 24px 38px;position:relative}
.class-footer-nav::before{content:'';position:absolute;top:-1px;left:50%;transform:translateX(-50%);width:80px;height:2px;background:#facc15;border-radius:0 0 4px 4px}
.class-footer-nav-inner{max-width:1000px;margin:0 auto}
.cfn-eyebrow{text-align:center;font-size:9px;font-weight:800;letter-spacing:.3em;text-transform:uppercase;color:rgba(250,204,21,.38);margin-bottom:30px;display:flex;align-items:center;justify-content:center;gap:12px}
.cfn-eyebrow::before,.cfn-eyebrow::after{content:'';flex:1;height:1px;background:rgba(255,255,255,.06)}
.cfn-grid{display:grid;grid-template-columns:1fr 68px 1fr;gap:10px;align-items:stretch;margin-bottom:24px}
.cfn-card{display:flex;align-items:center;gap:14px;padding:20px 22px;border-radius:14px;border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.025);text-decoration:none;color:inherit;transition:all .25s}
.cfn-card:hover{border-color:rgba(250,204,21,.4);background:rgba(250,204,21,.06);transform:translateY(-3px);box-shadow:0 12px 40px rgba(250,204,21,.1)}
.cfn-card.cfn-next{background:rgba(250,204,21,.06);border-color:rgba(250,204,21,.2);justify-content:flex-end;text-align:right}
.cfn-card.cfn-next:hover{background:rgba(250,204,21,.13);border-color:rgba(250,204,21,.55);box-shadow:0 12px 40px rgba(250,204,21,.15)}
.cfn-card.cfn-home{flex-direction:column;justify-content:center;align-items:center;gap:6px;background:rgba(255,255,255,.015);padding:14px 6px}
.cfn-card.cfn-home:hover{background:rgba(250,204,21,.06);border-color:rgba(250,204,21,.35)}
.cfn-arrow{font-size:16px;color:rgba(255,255,255,.35);flex-shrink:0;transition:color .2s}
.cfn-card:hover .cfn-arrow{color:rgba(250,204,21,.7)}
.cfn-card.cfn-next .cfn-arrow{color:rgba(250,204,21,.55)}
.cfn-body{display:flex;flex-direction:column;gap:1px}
.cfn-badge{font-size:8.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:rgba(250,204,21,.55)}
.cfn-dir{font-size:9px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:rgba(255,255,255,.25)}
.cfn-title{font-family:'Playfair Display',serif;font-size:13px;font-weight:700;color:rgba(255,255,255,.78);line-height:1.35;margin-top:2px}
.cfn-card.cfn-next .cfn-title{color:#facc15}
.cfn-home-icon{font-size:18px;color:rgba(250,204,21,.4);transition:color .25s}
.cfn-card.cfn-home:hover .cfn-home-icon{color:#facc15}
.cfn-home-label{font-size:8px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.22)}
.cfn-credits{text-align:center;font-size:10.5px;color:rgba(255,255,255,.16);padding-top:4px}
.cfn-credits a{color:rgba(250,204,21,.32);text-decoration:none;transition:color .2s}
.cfn-credits a:hover{color:#facc15}
@media(max-width:600px){
  .cfn-grid{grid-template-columns:1fr;gap:8px}
  .cfn-card.cfn-home{flex-direction:row;padding:14px 20px;justify-content:flex-start;gap:12px}
}
"""

def footer_html(prev_href, prev_badge, prev_dir, prev_title,
                next_href, next_badge, next_dir, next_title):
    return f"""
<nav class="class-footer-nav">
  <div class="class-footer-nav-inner">
    <p class="cfn-eyebrow">CONTINUAR NAVEGANDO</p>
    <div class="cfn-grid">
      <a href="{prev_href}" class="cfn-card cfn-prev">
        <span class="cfn-arrow"><i class="fa-solid fa-arrow-left"></i></span>
        <div class="cfn-body">
          <span class="cfn-badge">{prev_badge}</span>
          <span class="cfn-dir">{prev_dir}</span>
          <span class="cfn-title">{prev_title}</span>
        </div>
      </a>
      <a href="index.html" class="cfn-card cfn-home" title="Inicio">
        <i class="fa-solid fa-house cfn-home-icon"></i>
        <span class="cfn-home-label">Inicio</span>
      </a>
      <a href="{next_href}" class="cfn-card cfn-next">
        <div class="cfn-body">
          <span class="cfn-badge">{next_badge}</span>
          <span class="cfn-dir">{next_dir}</span>
          <span class="cfn-title">{next_title}</span>
        </div>
        <span class="cfn-arrow"><i class="fa-solid fa-arrow-right"></i></span>
      </a>
    </div>
    <p class="cfn-credits">Filosofía e Historia de la Ciencia y la Tecnología &middot; 6to Año &middot; <a href="index.html">Los Polvorines, 2026</a></p>
  </div>
</nav>"""

# Definición de footers para cada archivo
PAGES = {
    "unidad6-introduccion.html": footer_html(
        "index.html",          "INICIO",     "Volver a",          "Revista Filosofía&amp;Ciencia",
        "unidad6-clase32.html","U6 · C-32",  "Primera clase",     "Clasificación de las ciencias"
    ),
    "unidad6-clase32.html": footer_html(
        "unidad6-introduccion.html","U6 · INTRO","Introducción",   "Introducción a la Unidad 6",
        "unidad6-clase33.html",     "U6 · C-33", "Clase siguiente","La geometría como caso bisagra"
    ),
    "unidad6-clase33.html": footer_html(
        "unidad6-clase32.html","U6 · C-32","Clase anterior",  "Clasificación de las ciencias",
        "unidad6-clase34.html","U6 · C-34","Clase siguiente", "Sistemas axiomáticos: los ladrillos del razonamiento"
    ),
    "unidad6-clase34.html": footer_html(
        "unidad6-clase33.html","U6 · C-33","Clase anterior",  "La geometría como caso bisagra",
        "unidad6-clase35.html","U6 · C-35","Clase siguiente", "El método indirecto y las geometrías no euclideanas"
    ),
    "unidad6-clase35.html": footer_html(
        "unidad6-clase34.html","U6 · C-34","Clase anterior",  "Sistemas axiomáticos",
        "unidad6-clase36.html","U6 · C-36","Clase siguiente", "Completitud, consistencia e independencia"
    ),
    "unidad6-clase36.html": footer_html(
        "unidad6-clase35.html","U6 · C-35","Clase anterior",  "El método indirecto y las geometrías",
        "unidad6-clase37.html","U6 · C-37","Clase siguiente", "Argumentar bien: validez y falacias"
    ),
    "unidad6-clase37.html": footer_html(
        "unidad6-clase36.html","U6 · C-36","Clase anterior",  "Completitud, consistencia e independencia",
        "index.html",          "INICIO",    "Fin de Unidad 6",   "Volver a la Revista"
    ),
}

for filename, footer in PAGES.items():
    filepath = BASE + filename
    if not os.path.exists(filepath):
        print(f"  SKIP (no existe): {filename}")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Saltar si ya tiene footer
    if 'class-footer-nav' in content:
        print(f"  SKIP (ya tiene footer): {filename}")
        continue

    # 1. Agregar CSS antes del cierre de </style>
    # Buscar el último </style> antes del </head>
    head_end = content.find('</head>')
    last_style_close = content.rfind('</style>', 0, head_end)
    if last_style_close == -1:
        print(f"  ERROR: no se encontró </style> en {filename}")
        continue
    content = content[:last_style_close] + FOOTER_CSS + content[last_style_close:]

    # 2. Insertar footer HTML justo antes de </body>
    body_close = content.rfind('</body>')
    if body_close == -1:
        print(f"  ERROR: no se encontró </body> en {filename}")
        continue
    content = content[:body_close] + footer + '\n' + content[body_close:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  OK: {filename}")

print("\nDone.")
