"""Slide brandizzata VG: Creative Diversification Cheat Sheet (Meta Creative Shop, slide 7).
Layout a 5 colonne come l'originale Meta, palette e font del brand VG."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))
F_BOLD, F_SEMI, F_MED, F_REG, F_LIGHT = (f"{FONT_DIR}/Poppins-{n}.ttf" for n in
                                         ("Bold", "SemiBold", "Medium", "Regular", "Light"))
FORMATO = os.environ.get("VG_FORMATO", "orizzontale")  # orizzontale (16:9, come Meta) | verticale (4:5)
W, H = (1920, 1080) if FORMATO == "orizzontale" else (1080, 1350)
MARGIN = 64
FOOTER_Y = H - 52
BLU, BOX, CARD, GIALLO, BIANCO = (53, 90, 158), (30, 55, 110), (44, 76, 138), (245, 197, 24), (255, 255, 255)
GAP, R = 12, 10

TITOLO = "CREATIVE DIVERSIFICATION"
SOTTOTITOLO = "La cheat sheet di Meta"
FONTE = 'Fonte: Meta Creative Shop, "Creative Diversification: Motivator worksheets and cheat sheet"'

# (intestazione, descrizione, [(titolo gruppo | None, [(voce, rientro)])])
COLONNE = [
 ("MESSAGGIO", "Usa motivatori e barriere diversi per raggiungere pubblici nuovi, oltre a quelli abituali.", [
   ("Legati ai bisogni delle persone", [("Motivatori e barriere", 0), ("Benefici emotivi", 0), ("Identificazione nella situazione", 0)]),
   ("Legati a prodotto o brand", [("Benefici funzionali", 0), ("Benefici del servizio", 0), ("Utilizzo del prodotto / demo", 0)]),
   ("Legati alle promozioni", [("Offerte", 0), ("Eventi di vendita", 0)])]),
 ("FORMATO", "Combina video e immagini statiche nelle tue campagne.", [
   ("Formati principali", [("Immagine statica", 0), ("Video (breve)", 0), ("Carosello", 0), ("Catalog ads", 0),
                           ("Carosello", 1), ("Collection", 1), ("Immagine singola", 1)]),
   ("Formati aggiuntivi", [("Shop ads (solo USA)", 0), ("Annunci con tag prodotto", 0)]),
   ("Proporzioni più efficaci", [("1:1", 0), ("4:5", 0), ("9:16", 0)])]),
 ("APPROCCIO CREATIVO", "Usa approcci creativi diversi per differenziarti e raggiungere nuovi pubblici su tutta la piattaforma.", [
   ("Lo-Fi", [("Contenuti dei creator", 0), ("Linguaggio dei Reel", 0), ("UGC (contenuti generati dagli utenti)", 0)]),
   ("Hi-Fi / curato", [("Focus sul prodotto", 0), ("Focus sullo stile di vita", 0), ("Illustrazione / animazione", 0)]),
   ("Altro", [("Statico animato", 0)])]),
 ("POSIZIONAMENTI", "Attiva i posizionamenti automatici per sfruttare tutta la copertura dell'ecosistema Meta.", [
   ("Facebook e Instagram", [("Feed", 0), ("Storie", 0), ("Reel", 0), ("Ricerca", 0), ("In-stream (solo video)", 0)]),
   ("Audience Network", [("Banner nativi / interstitial", 0), ("Rewarded ads", 0)])]),
 ("BEST PRACTICE", "Segui queste best practice mentre costruisci le tue creatività.", [
   (None, [("Mostra il brand subito, entro i primi 3 secondi", 0),
           ("Apri il video con un hook visivo forte", 0),
           ("Mostra come il prodotto o servizio aiuta le persone nella vita reale", 0),
           ("Inserisci una CTA chiara", 0),
           ("Tieni il video breve (6-15 secondi)", 0),
           ("Usa formati verticali e più proporzioni (9:16, 4:5, 1:1)", 0),
           ("Usa sia statico sia video per risultati migliori", 0),
           ("Progetta per la visione senza audio, ma premia chi ha l'audio attivo", 0),
           ("Usa gli overlay negli Advantage+ catalog ads per migliorare i risultati", 0)])]),
]

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

COLW = (W - 2 * MARGIN - 4 * GAP) // 5
PAD = 12

# --- titolo + sottotitolo centrati
TMAX = 84 if FORMATO == "orizzontale" else 100
for ts in range(TMAX, 40, -2):
    if d.textlength(TITOLO, font=F(F_BOLD, ts)) <= W - 2 * MARGIN: break
y = 48 if FORMATO == "orizzontale" else 60
d.text((W // 2, y), TITOLO, font=F(F_BOLD, ts), fill=BIANCO, anchor="mt"); y += int(ts * 1.15)
d.text((W // 2, y), SOTTOTITOLO, font=F(F_BOLD, 54), fill=GIALLO, anchor="mt"); y += int(54 * 1.3) + (24 if FORMATO == "orizzontale" else 34)

f_fonte = F(F_LIGHT, 20)
FONTE_Y = FOOTER_Y - 56
LIST_BOTTOM = FONTE_Y - 24

def misura(s):
    """Altezze di header, descrizione e lista per corpo s."""
    fh, fd, fg, fi = F(F_BOLD, s + 1), F(F_MED, s - 1), F(F_SEMI, s), F(F_REG, s - 1)
    lh = int(s * 1.38); iw = COLW - 2 * PAD
    hh = max(len(wrap(c[0], fh, iw)) for c in COLONNE) * lh + 2 * PAD
    hd = max(len(wrap(c[1], fd, iw)) for c in COLONNE) * lh + 2 * PAD
    hl = 0
    for _, _, gruppi in COLONNE:
        h = PAD
        for g, voci in gruppi:
            if g: h += len(wrap(g, fg, iw)) * lh + 6
            for v, ind in voci:
                h += len(wrap(v, fi, iw - (s + 8) - ind * 18)) * lh + 7
            h += int(s * 0.9)
        hl = max(hl, h)
    return hh, hd, hl

for s in range(32, 12, -1):
    hh, hd, hl = misura(s)
    if y + hh + hd + GAP + hl <= LIST_BOTTOM: break
print("corpo", s)

fh, fd, fg, fi = F(F_BOLD, s + 1), F(F_MED, s - 1), F(F_SEMI, s), F(F_REG, s - 1)
lh = int(s * 1.38); iw = COLW - 2 * PAD
box = s - 3  # lato checkbox

for i, (head, desc, gruppi) in enumerate(COLONNE):
    x = MARGIN + i * (COLW + GAP)
    # header scuro con testo giallo + card descrizione (un unico blocco come in Meta)
    d.rounded_rectangle([x, y, x + COLW, y + hh + hd], R, fill=CARD)
    d.rounded_rectangle([x, y, x + COLW, y + hh], R, fill=BOX, corners=(True, True, False, False))
    hl_ = wrap(head, fh, iw)
    ty = y + (hh - len(hl_) * lh) // 2
    for l in hl_: d.text((x + COLW // 2, ty), l, font=fh, fill=GIALLO, anchor="mt"); ty += lh
    ty = y + hh + PAD
    for l in wrap(desc, fd, iw): d.text((x + COLW // 2, ty), l, font=fd, fill=BIANCO, anchor="mt"); ty += lh
    # card lista
    ly = y + hh + hd + GAP
    d.rounded_rectangle([x, ly, x + COLW, LIST_BOTTOM], R, fill=CARD)
    cy = ly + PAD + 4
    for g, voci in gruppi:
        if g:
            for l in wrap(g, fg, iw): d.text((x + PAD, cy), l, font=fg, fill=GIALLO); cy += lh
            cy += 6
        for v, ind in voci:
            bx = x + PAD + ind * 18
            tx = bx + box + 8
            ls = wrap(v, fi, x + COLW - PAD - tx)
            by = cy + (lh - box) // 2
            d.rectangle([bx, by, bx + box, by + box], outline=BIANCO, width=2)
            for l in ls: d.text((tx, cy), l, font=fi, fill=BIANCO); cy += lh
            cy += 7
        cy += int(s * 0.9)

# --- fonte
d.text((W // 2, FONTE_Y), FONTE, font=f_fonte, fill=BIANCO, anchor="mt")

# --- footer: logotipo + url
flg = F(F_BOLD, 27); x = MARGIN
for word, col in (("VERONICA", BIANCO), ("GENTILI", GIALLO)):
    for ch in word:
        d.text((x, FOOTER_Y), ch, font=flg, fill=col, anchor="lm"); x += d.textlength(ch, font=flg) + 1.4
    x += 12
d.text((W - MARGIN, FOOTER_Y), "www.veronicagentili.com", font=F(F_LIGHT, 24), fill=BIANCO, anchor="rm")

out = os.path.join(BASE, f"20261113_creative_diversification_cheat_sheet_{FORMATO}.png")
img.save(out, "PNG"); print(out)
