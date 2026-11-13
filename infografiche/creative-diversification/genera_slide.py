"""Slide brandizzata VG: Creative Diversification Cheat Sheet (Meta Creative Shop, slide 7)."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))
F_BOLD, F_SEMI, F_MED, F_REG, F_LIGHT = (f"{FONT_DIR}/Poppins-{n}.ttf" for n in
                                         ("Bold", "SemiBold", "Medium", "Regular", "Light"))
W, H, MARGIN = 1080, 1350, 64
FOOTER_Y = H - 52
BLU, BOX, GIALLO, BIANCO = (53, 90, 158), (30, 55, 110), (245, 197, 24), (255, 255, 255)
GAP = 22

TITOLO = "CREATIVE DIVERSIFICATION"
SOTTOTITOLO = "La cheat sheet di Meta"
FONTE = 'Fonte: Meta Creative Shop, "Creative Diversification: Motivator worksheets and cheat sheet"'

SEZIONI = {
 "msg": ("MESSAGGIO", "Usa motivatori e barriere diversi per raggiungere pubblici nuovi, oltre a quelli abituali.", [
    ("Legati ai bisogni delle persone", ["motivatori e barriere", "benefici emotivi", "identificazione nella situazione"]),
    ("Legati a prodotto o brand", ["benefici funzionali", "benefici del servizio", "utilizzo del prodotto / demo"]),
    ("Legati alle promozioni", ["offerte", "eventi di vendita"])]),
 "fmt": ("FORMATO", "Combina video e immagini statiche nelle tue campagne.", [
    ("Formati principali", ["immagine statica", "video breve", "carosello", "catalog ads (carosello, collection, immagine singola)"]),
    ("Formati aggiuntivi", ["Shop ads (solo USA)", "annunci con tag prodotto"]),
    ("Proporzioni più efficaci", ["1:1", "4:5", "9:16"])]),
 "app": ("APPROCCIO CREATIVO", "Usa approcci creativi diversi per differenziarti e raggiungere nuovi pubblici su tutta la piattaforma.", [
    ("Lo-Fi", ["contenuti dei creator", "linguaggio dei Reel", "UGC (contenuti generati dagli utenti)"]),
    ("Hi-Fi / curato", ["focus sul prodotto", "focus sullo stile di vita", "illustrazione / animazione"]),
    ("Altro", ["statico animato"])]),
 "plc": ("POSIZIONAMENTI", "Attiva i posizionamenti automatici per sfruttare tutta la copertura dell'ecosistema Meta.", [
    ("Facebook e Instagram", ["feed", "storie", "reel", "ricerca", "in-stream (solo video)"]),
    ("Audience Network", ["banner nativi / interstitial", "rewarded ads"])]),
}
BEST = ("BEST PRACTICE", [
    "Mostra il brand subito, entro i primi 3 secondi",
    "Apri il video con un hook visivo forte",
    "Mostra come il prodotto o servizio aiuta le persone nella vita reale",
    "Inserisci una CTA chiara",
    "Tieni il video breve (6-15 secondi)",
    "Usa formati verticali e più proporzioni (9:16, 4:5, 1:1)",
    "Usa sia statico sia video per risultati migliori",
    "Progetta per la visione senza audio, ma premia chi ha l'audio attivo",
    "Usa gli overlay negli Advantage+ catalog ads per migliorare i risultati",
])

img = Image.new("RGB", (W, H), BLU)
d = ImageDraw.Draw(img)
F = lambda p, s: ImageFont.truetype(p, s)

def wrap(text, f, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    return lines + ([cur] if cur else [])

PADL, PADT, ACC = 20, 14, 5

def sezione(x, y, w, sez, s, draw=True):
    """Box evidenziato con titolo, descrizione e gruppi. Ritorna l'altezza."""
    titolo, desc, gruppi = sez
    ft, fd, fl, fi = F(F_BOLD, s + 4), F(F_MED, s), F(F_SEMI, s), F(F_REG, s)
    lh = int(s * 1.42); iw = w - PADL - 18
    ops, cy = [], y + PADT
    ops.append((x + PADL, cy, titolo, ft, GIALLO)); cy += int((s + 4) * 1.5)
    for l in wrap(desc, fd, iw): ops.append((x + PADL, cy, l, fd, BIANCO)); cy += lh
    for label, items in gruppi:
        cy += int(s * 0.55)
        ops.append((x + PADL, cy, label, fl, GIALLO)); cy += lh
        for l in wrap(" · ".join(items), fi, iw): ops.append((x + PADL, cy, l, fi, BIANCO)); cy += lh
    h = cy - y + PADT
    if draw:
        d.rectangle([x, y, x + w, y + h], fill=BOX)
        d.rectangle([x, y, x + ACC - 1, y + h], fill=GIALLO)
        for o in ops: d.text(o[:2], o[2], font=o[3], fill=o[4])
    return h

def best(x, y, w, s, draw=True):
    titolo, items = BEST
    ft, fi = F(F_BOLD, s + 4), F(F_REG, s)
    lh = int(s * 1.42); colw = (w - PADL - 20 - 24) // 2
    r = max(5, s // 3); tx = PADL + 2 * r + 12
    cols = [items[:5], items[5:]]
    top = y + PADT + int((s + 4) * 1.5)
    hs = []
    for ci, col in enumerate(cols):
        cx0 = x + PADL + ci * (colw + 24); cy = top
        for it in col:
            ls = wrap(it, fi, colw - tx + PADL)
            if draw:
                cyc = cy + lh // 2 + 1
                d.ellipse([cx0 + 1, cyc - r, cx0 + 1 + 2 * r, cyc + r], fill=GIALLO)
                for j, l in enumerate(ls): d.text((cx0 + tx - PADL, cy + j * lh), l, font=fi, fill=BIANCO)
            cy += len(ls) * lh + int(s * 0.45)
        hs.append(cy)
    h = max(hs) - y + PADT - int(s * 0.45)
    if draw:
        d.rectangle([x, y, x + w, y + h], fill=BOX)
        d.rectangle([x, y, x + ACC - 1, y + h], fill=GIALLO)
        d.text((x + PADL, y + PADT), titolo, font=ft, fill=GIALLO)
        best(x, y, w, s, draw=False) if False else None
        # ridisegna bullet sopra il box
        for ci, col in enumerate(cols):
            cx0 = x + PADL + ci * (colw + 24); cy = top
            for it in col:
                ls = wrap(it, fi, colw - tx + PADL); cyc = cy + lh // 2 + 1
                d.ellipse([cx0 + 1, cyc - r, cx0 + 1 + 2 * r, cyc + r], fill=GIALLO)
                d.text((cx0 + r + 1, cyc), "›", font=F(F_BOLD, max(10, 2 * r)), fill=BOX, anchor="mm")
                for j, l in enumerate(ls): d.text((cx0 + tx - PADL, cy + j * lh), l, font=fi, fill=BIANCO)
                cy += len(ls) * lh + int(s * 0.45)
    return h

# --- titolo autosize (max 100px, 1 riga) + sottotitolo giallo
for ts in range(100, 40, -2):
    if d.textlength(TITOLO, font=F(F_BOLD, ts)) <= W - 2 * MARGIN: break
y = 56
d.text((MARGIN, y), TITOLO, font=F(F_BOLD, ts), fill=BIANCO); y += int(ts * 1.18)
d.text((MARGIN, y), SOTTOTITOLO, font=F(F_BOLD, 54), fill=GIALLO); y += int(54 * 1.25) + 30

# --- auto-fit del corpo
f_fonte = F(F_LIGHT, 20)
fonte_lines = wrap(FONTE, f_fonte, W - 2 * MARGIN)
bottom = FOOTER_Y - 48 - len(fonte_lines) * 28 - 18
colw = (W - 2 * MARGIN - GAP) // 2
for s in range(26, 14, -1):
    hl = sezione(0, 0, colw, SEZIONI["msg"], s, False) + GAP + sezione(0, 0, colw, SEZIONI["fmt"], s, False)
    hr = sezione(0, 0, colw, SEZIONI["app"], s, False) + GAP + sezione(0, 0, colw, SEZIONI["plc"], s, False)
    hb = best(0, 0, W - 2 * MARGIN, s, False)
    if y + max(hl, hr) + GAP + hb <= bottom: break
print("corpo", s, "titolo", ts)

xl, xr = MARGIN, MARGIN + colw + GAP
# allinea le altezze delle due colonne
h1 = sezione(xl, y, colw, SEZIONI["msg"], s, False); h3 = sezione(xr, y, colw, SEZIONI["app"], s, False)
top_row = max(h1, h3)
def box_fixed(x, yy, sez, hmin):
    h = sezione(x, yy, colw, sez, s, False)
    d.rectangle([x, yy, x + colw, yy + hmin], fill=BOX); d.rectangle([x, yy, x + ACC - 1, yy + hmin], fill=GIALLO)
    # disegna il contenuto senza ridisegnare il box
    titolo, desc, gruppi = sez
    sezione_contenuto(x, yy, sez)
def sezione_contenuto(x, yy, sez):
    titolo, desc, gruppi = sez
    ft, fd, fl, fi = F(F_BOLD, s + 4), F(F_MED, s), F(F_SEMI, s), F(F_REG, s)
    lh = int(s * 1.42); iw = colw - PADL - 18; cy = yy + PADT
    d.text((x + PADL, cy), titolo, font=ft, fill=GIALLO); cy += int((s + 4) * 1.5)
    for l in wrap(desc, fd, iw): d.text((x + PADL, cy), l, font=fd, fill=BIANCO); cy += lh
    for label, items in gruppi:
        cy += int(s * 0.55); d.text((x + PADL, cy), label, font=fl, fill=GIALLO); cy += lh
        for l in wrap(" · ".join(items), fi, iw): d.text((x + PADL, cy), l, font=fi, fill=BIANCO); cy += lh

h2 = sezione(xl, 0, colw, SEZIONI["fmt"], s, False); h4 = sezione(xr, 0, colw, SEZIONI["plc"], s, False)
bot_row = max(h2, h4)
box_fixed(xl, y, SEZIONI["msg"], top_row); box_fixed(xr, y, SEZIONI["app"], top_row)
y2 = y + top_row + GAP
box_fixed(xl, y2, SEZIONI["fmt"], bot_row); box_fixed(xr, y2, SEZIONI["plc"], bot_row)
y3 = y2 + bot_row + GAP
best(MARGIN, y3, W - 2 * MARGIN, s)

# --- fonte
fy = FOOTER_Y - 48 - len(fonte_lines) * 28
for i, l in enumerate(fonte_lines): d.text((MARGIN, fy + i * 28), l, font=f_fonte, fill=BIANCO)

# --- footer: logotipo + url
fl = F(F_BOLD, 27)
x = MARGIN
for word, col in (("VERONICA", BIANCO), ("GENTILI", GIALLO)):
    for ch in word:
        d.text((x, FOOTER_Y), ch, font=fl, fill=col, anchor="lm"); x += d.textlength(ch, font=fl) + 1.4
    x += 12
d.text((W - MARGIN, FOOTER_Y), "www.veronicagentili.com", font=F(F_LIGHT, 24), fill=BIANCO, anchor="rm")

out = os.path.join(BASE, "20261113_creative_diversification_cheat_sheet.png")
img.save(out, "PNG"); print(out)
