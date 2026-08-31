# -*- coding: utf-8 -*-
"""Versione HTML del carosello, importabile in Canva come design editabile.

Ogni slide e' un blocco con data-document-role="page": Canva la importa come
pagina a se' stante e testo, colori e forme restano elementi modificabili.
Le misure ricalcano quelle dei PNG generati da genera_carosello.py.
"""

import base64
import io
import os

from fontTools import subset
from fontTools.ttLib import TTFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))
OUT = os.path.join(BASE, "chatgpt_ads_italia_canva.html")

# I font Poppins vengono sottoinsiemizzati sui soli caratteri usati e incorporati
# nell'HTML: il file resta autonomo anche senza rete, e Canva riconosce comunque
# il nome della famiglia.
PESI = {300: "Light", 400: "Regular", 500: "Medium", 700: "Bold"}


def facce_font(caratteri):
    regole = []
    for peso, nome in PESI.items():
        f = TTFont(os.path.join(FONT_DIR, f"Poppins-{nome}.ttf"))
        opzioni = subset.Options(flavor="woff2", layout_features=["*"])
        subsetter = subset.Subsetter(options=opzioni)
        subsetter.populate(text="".join(sorted(caratteri)))
        subsetter.subset(f)
        buf = io.BytesIO()
        f.flavor = "woff2"
        f.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        regole.append(
            "  @font-face { font-family: 'Poppins'; font-style: normal; "
            f"font-weight: {peso}; font-display: swap; "
            f"src: url(data:font/woff2;base64,{b64}) format('woff2'); }}")
    return "\n".join(regole)

W, H = 1080, 1350
MARGIN = 64
FOOTER_Y = H - 52
CONTENT_BOTTOM = H - 110
BULLET_X = W // 2 - 20
URL = "www.veronicagentili.com"


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def pagina(label, corpo, barra=False):
    bar = '<div class="barra-destra"></div>' if barra else ""
    return f'''<div class="pagina" data-document-role="page" data-label="{esc(label)}">
{bar}
{corpo}
  <div class="footer">
    <div class="logotipo">VERONICA&nbsp;<span class="giallo">GENTILI</span></div>
    <div class="sito">{URL}</div>
  </div>
</div>'''


def titolo_soggetto(testo, size):
    return (f'  <div class="soggetto" style="top:40px;font-size:{size}px;'
            f'line-height:{int(size * 1.12)}px">{esc(testo)}</div>')


def bullet_lista(items, top, size=34):
    lh = int(size * 1.42)
    gap = max(22, size // 2 + 8)
    r = size // 3 + 3
    freccia = max(10, r - 2)
    righe = []
    for i, t in enumerate(items):
        mt = 0 if i == 0 else gap
        righe.append(
            f'    <li style="margin-top:{mt}px">'
            f'<span class="pallino" style="width:{r * 2}px;height:{r * 2}px;'
            f'margin-top:{lh // 2 - r}px;font-size:{freccia}px">&gt;</span>'
            f'<span class="voce">{esc(t)}</span></li>')
    return (f'  <ul class="bullet" style="top:{top}px;left:{BULLET_X + 4}px;'
            f'font-size:{size}px;line-height:{lh}px">\n'
            + "\n".join(righe) + "\n  </ul>")


def nota_gialla(testo, size=32):
    lh = int(size * 1.42)
    return (f'  <div class="nota" style="font-size:{size}px;line-height:{lh}px">'
            f'<span class="nota-barra"></span><span>{esc(testo)}</span></div>')


PAGINE = []

# --- 1. cover
PAGINE.append(pagina("Cover", f'''  <div class="cover">
    <div class="cover-titolo">CHATGPT ADS</div>
    <div class="cover-titolo giallo">FINALMENTE IN ITALIA</div>
    <div class="cover-sub">Da oggi puoi comprare inserzioni su ChatGPT in autonomia.</div>
  </div>'''))

# --- 2. introduttiva
PAGINE.append(pagina("Cosa e' successo", "\n".join([
    titolo_soggetto("COSA È SUCCESSO", 102),
    '''  <div class="testo" style="top:276px">
    <p>ChatGPT Ads era arrivato in Europa questo mese, Italia inclusa, ma si comprava solo tramite agenzie partner selezionate.</p>
    <p>Da oggi cambia. OpenAI ha aperto la beta self service di Ads Manager in tutti e 31 i mercati europei. Entri, crei la campagna, la gestisci. Senza intermediari.</p>
    <p class="chiusura">Ecco cosa devi sapere prima di aprire l'account.</p>
  </div>''',
])))

# --- 3. cosa cambia
PAGINE.append(pagina("Cosa cambia", "\n".join([
    titolo_soggetto("COSA CAMBIA", 130),
    bullet_lista([
        "Accesso diretto alla creazione e alla gestione delle campagne, senza passare da un partner",
        "Aperto a startup, PMI e aziende strutturate, non solo ai grandi budget",
        "Chi preferisce continuare con agenzie e partner tech può farlo lo stesso",
        "L'accesso resta legato a categoria approvata e inserzioni conformi alle policy di OpenAI",
    ], top=394),
])))

# --- 4. categorie ammesse
PAGINE.append(pagina("Chi puo' fare adv", "\n".join([
    titolo_soggetto("CHI PUÒ FARE ADV", 102),
    bullet_lista([
        "Lifestyle e articoli per la casa",
        "Servizi locali",
        "Viaggi ed esperienze",
        "Prodotti digitali e formazione",
    ], top=466),
    nota_gialla("Finanza, sanità e servizi legali entrano solo con approvazione manuale, caso per caso."),
])))

# --- 5. categorie escluse
PAGINE.append(pagina("Chi resta fuori", "\n".join([
    titolo_soggetto("CHI RESTA FUORI", 114),
    bullet_lista([
        "Dating e contenuti sessuali",
        "Claim sulla salute, alcol e droghe",
        "Gioco d'azzardo",
        "Contenuti politici",
    ], top=473),
    nota_gialla("Al lancio tutte le categorie non ammesse sono vietate. L'elenco può cambiare mentre il programma cresce."),
])))

# --- 6. regole
PAGINE.append(pagina("Come funzionano", "\n".join([
    titolo_soggetto("COME FUNZIONANO", 94),
    bullet_lista([
        "Gli annunci sono segnalati e separati dalle risposte di ChatGPT",
        "Non influenzano le risposte",
        "Gli inserzionisti non vedono le conversazioni degli utenti né i loro dati personali",
        "Creatività e landing page devono essere coerenti. Un annuncio sul food delivery non può portare a un servizio di consegna alcolici",
    ], top=350),
])))

# --- 7. il numero
PAGINE.append(pagina("Il numero", '''  <div class="takeaway" style="top:278px">
    <div class="tk" style="font-size:72px;line-height:83px">ChatGPT Ads ha fatto</div>
    <div class="tk giallo" style="font-size:100px;line-height:116px">1 miliardo di dollari</div>
    <div class="tk" style="font-size:60px;line-height:69px">di ricavi ricorrenti annuali in meno di 200 giorni.</div>
    <div class="tk-sub">Nessuna piattaforma pubblicitaria era mai arrivata a quella cifra a quella velocità.</div>
  </div>''', barra=True))

# --- 8. takeaway
PAGINE.append(pagina("Takeaway", '''  <div class="takeaway" style="top:186px">
    <div class="tk" style="font-size:88px;line-height:102px">Non è il momento di</div>
    <div class="tk giallo" style="font-size:100px;line-height:116px">spostare budget.</div>
    <div class="tk" style="font-size:72px;line-height:83px">È il momento di capire come funziona.</div>
    <div class="tk-sub">Il canale è giovane, le categorie aperte sono poche, i dati sono pochissimi. Se rientri, apri l'account e testa con una cifra che puoi permetterti di bruciare. Ti porti a casa l'apprendimento prima che il costo del click salga.</div>
  </div>''', barra=True))


CARATTERI = set("".join(PAGINE)) | set(" 0123456789")
FONT_FACES = facce_font(CARATTERI)

html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>ChatGPT Ads finalmente in Italia</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
{FONT_FACES}
  body {{ margin: 0; background: #1E376E; }}
  .pagina {{
    width: {W}px; height: {H}px; box-sizing: border-box;
    position: relative; overflow: hidden;
    background: #355A9E; color: #FFFFFF;
    font-family: 'Poppins', 'Helvetica Neue', Arial, sans-serif;
  }}
  .giallo {{ color: #F5C518; }}
  .barra-destra {{ position: absolute; right: 0; top: 0; width: 10px; height: {H // 2}px; background: #F5C518; }}

  .soggetto {{ position: absolute; left: {MARGIN}px; right: {MARGIN}px; font-weight: 700; }}

  .cover {{ position: absolute; left: {MARGIN}px; right: {MARGIN}px; bottom: 132px; }}
  .cover-titolo {{ font-weight: 700; font-size: 88px; line-height: 97px; }}
  .cover-sub {{ font-weight: 500; font-size: 44px; line-height: 59px; color: #E2EAF8; margin-top: 28px; }}

  .testo {{ position: absolute; left: {MARGIN}px; width: {W - MARGIN * 2}px; }}
  .testo p {{ font-weight: 400; font-size: 46px; line-height: 69px; margin: 0 0 41px; }}
  .testo p.chiusura {{ font-weight: 500; font-size: 50px; line-height: 70px; color: #F5C518; margin: 13px 0 0; }}

  .bullet {{ position: absolute; margin: 0; padding: 0; list-style: none; width: 492px; font-weight: 400; }}
  .bullet li {{ display: flex; align-items: flex-start; gap: 14px; }}
  .pallino {{
    flex: none; background: #F5C518; color: #1E3A6E; border-radius: 50%;
    font-weight: 700; line-height: 1; display: flex;
    align-items: center; justify-content: center;
  }}
  .voce {{ width: 450px; }}

  .nota {{
    position: absolute; left: {MARGIN}px; width: {W - MARGIN * 2}px; bottom: 168px;
    transform: translateY(50%); display: flex; gap: 22px;
    font-weight: 500; color: #F5C518;
  }}
  .nota-barra {{ flex: none; width: 6px; background: #F5C518; }}

  .takeaway {{ position: absolute; left: {MARGIN}px; width: {W - MARGIN * 2 - 20}px; }}
  .tk {{ font-weight: 700; margin-bottom: 18px; }}
  .tk-sub {{ font-weight: 400; font-size: 42px; line-height: 62px; color: #E2EAF8; margin-top: 40px; }}

  .footer {{
    position: absolute; left: {MARGIN}px; right: {MARGIN}px; top: {FOOTER_Y - 20}px;
    display: flex; justify-content: space-between; align-items: center;
  }}
  .logotipo {{ font-weight: 700; font-size: 27px; letter-spacing: 1.4px; }}
  .sito {{ font-weight: 300; font-size: 24px; }}

  @media print {{
    @page {{ size: {W}px {H}px; margin: 0; }}
    body {{ background: #FFFFFF; }}
    .pagina {{ break-after: page; }}
    .pagina:last-child {{ break-after: auto; }}
  }}
</style>
</head>
<body>
{chr(10).join(PAGINE)}
</body>
</html>
"""

open(OUT, "w", encoding="utf-8").write(html)
print("OK", OUT, len(html), "byte,", len(PAGINE), "pagine")
