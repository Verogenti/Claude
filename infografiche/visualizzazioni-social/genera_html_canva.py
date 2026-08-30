"""Genera la versione HTML dell'infografica, importabile in Canva come design
editabile (testo, forme e loghi restano elementi modificabili).

L'attributo data-document-role="page" dice a Canva dove inizia la pagina.
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(BASE, "icons")

# Stesso contenuto di genera_infografica.py
EYEBROW = "SOCIAL NETWORK:"
TITOLO = ["Quando viene contata", "una visualizzazione?"]
HEAD = ["VIEW CONTENUTO", "VIEW VIDEO"]

ROWS = [
    ("instagram",
     "Post o carosello mostrato a schermo. Nessuna soglia di tempo, le visualizzazioni ripetute contano.",
     "Il Reel parte o riparte. Nessun minimo di riproduzione."),
    ("facebook",
     "Foto, post o storia a schermo. Vista tre volte, tre view. Nessuna soglia di tempo dichiarata.",
     "Video o Reel riprodotto, senza durata minima. Le 3 second views restano a parte."),
    ("linkedin",
     "Post visibile almeno al 50% per 300 millisecondi a un utente loggato.",
     "La view viene conteggiata quando il video viene guardato per più di 2 secondi. Sulle Pagine la soglia documentata è 3 secondi."),
    ("youtube",
     "Per i post della Community YouTube usa le Impressions, non le Views.",
     "Dal 24 agosto 2026 all'avvio della riproduzione. Shorts, video lunghi e dirette."),
    ("pinterest",
     "Il Pin compare a schermo.",
     "2 secondi di riproduzione con il 50% del video a schermo."),
    ("x",
     "Il post compare sullo schermo di un utente loggato.",
     "2 secondi con il 50% del player a schermo."),
]

NOTA = ("Dati riferiti alle visualizzazioni organiche. Lato advertising valgono "
        "soglie e criteri di conteggio diversi.")
FONTI = "Fonti ufficiali, agosto 2026"
URL = "www.veronicagentili.com"


def icona(slug):
    """SVG inline, ripulito e forzato a bianco."""
    svg = open(os.path.join(ICON_DIR, f"{slug}.svg"), encoding="utf-8").read()
    svg = re.sub(r"<title>.*?</title>", "", svg)
    svg = svg.replace("<svg ", '<svg class="logo" fill="#FFFFFF" ', 1)
    return svg


righe = []
for slug, c2, c3 in ROWS:
    righe.append(
        f'      <div class="cella-logo">{icona(slug)}</div>\n'
        f'      <div class="cella">{c2}</div>\n'
        f'      <div class="cella">{c3}</div>'
    )

html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Quando viene contata una visualizzazione</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
  body {{ margin: 0; }}
  .pagina {{
    width: 1080px; height: 1350px; box-sizing: border-box;
    padding: 54px 64px 0; position: relative;
    background: #355A9E; color: #FFFFFF;
    font-family: 'Poppins', 'Helvetica Neue', Arial, sans-serif;
  }}
  .eyebrow {{ font-weight: 700; font-size: 25px; letter-spacing: 2.2px; color: #F5C518; }}
  h1 {{ font-weight: 700; font-size: 56px; line-height: 65px; margin: 19px 0 0; }}
  .regola {{ width: 96px; height: 7px; background: #F5C518; border-radius: 3px; margin-top: 16px; }}
  .griglia {{
    margin-top: 36px; display: grid;
    grid-template-columns: 120px 404px 404px;
    column-gap: 12px; row-gap: 10px;
  }}
  .intestazione {{ font-weight: 700; font-size: 21px; letter-spacing: 1.6px; color: #F5C518; padding-bottom: 8px; }}
  .cella-logo {{ display: flex; align-items: center; justify-content: center; }}
  .logo {{ width: 54px; height: 54px; }}
  .cella {{
    background: #1E376E; border-radius: 10px; padding: 18px 22px;
    font-weight: 400; font-size: 20px; line-height: 29px;
    display: flex; align-items: center;
  }}
  .nota {{ display: flex; gap: 27px; margin-top: 38px; }}
  .nota-barra {{ width: 7px; background: #F5C518; border-radius: 3px; flex: none; }}
  .nota p {{ font-weight: 500; font-size: 26px; line-height: 38px; margin: 0; }}
  .fonti {{ font-weight: 300; font-size: 23px; margin-top: 24px; }}
  .footer {{
    position: absolute; left: 64px; right: 64px; bottom: 38px;
    display: flex; justify-content: space-between; align-items: center;
  }}
  .logotipo {{ display: flex; align-items: center; gap: 22px; font-weight: 700; font-size: 27px; letter-spacing: 1.4px; }}
  .logotipo-barra {{ width: 8px; height: 30px; background: #F5C518; border-radius: 4px; }}
  .logotipo .giallo {{ color: #F5C518; }}
  .sito {{ font-weight: 300; font-size: 24px; }}
</style>
</head>
<body>
<div class="pagina" data-document-role="page" data-label="Quando viene contata una visualizzazione">

  <div class="eyebrow">{EYEBROW}</div>
  <h1>{TITOLO[0]}<br>{TITOLO[1]}</h1>
  <div class="regola"></div>

  <div class="griglia">
      <div></div>
      <div class="intestazione">{HEAD[0]}</div>
      <div class="intestazione">{HEAD[1]}</div>
{chr(10).join(righe)}
  </div>

  <div class="nota">
    <div class="nota-barra"></div>
    <p>{NOTA}</p>
  </div>

  <div class="fonti">{FONTI}</div>

  <div class="footer">
    <div class="logotipo">
      <div class="logotipo-barra"></div>
      <span>VERONICA&nbsp;<span class="giallo">GENTILI</span></span>
    </div>
    <div class="sito">{URL}</div>
  </div>

</div>
</body>
</html>
"""

out = os.path.join(BASE, "vg_visualizzazioni_social_canva.html")
open(out, "w", encoding="utf-8").write(html)
print("OK", out, len(html), "byte")
