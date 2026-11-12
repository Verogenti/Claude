"""Infografica corso Reel: quale modello di Reel per quale obiettivo.
Stesso impianto grafico di infografiche/visualizzazioni-social.
"""
import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))

F_BOLD    = f"{FONT_DIR}/Poppins-Bold.ttf"
F_MEDIUM  = f"{FONT_DIR}/Poppins-Medium.ttf"
F_REGULAR = f"{FONT_DIR}/Poppins-Regular.ttf"
F_LIGHT   = f"{FONT_DIR}/Poppins-Light.ttf"

W, H = 1080, 1350
BLU      = (53, 90, 158)
BLU_DARK = (30, 55, 110)
GIALLO   = (245, 197, 24)
BIANCO   = (255, 255, 255)

MARGIN   = 64
FOOTER_Y = H - 52


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, f, max_w):
    lines, cur = [], ""
    for word in text.split():
        test = (cur + " " + word).strip()
        if draw.textbbox((0, 0), test, font=f)[2] <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_tracked(draw, xy, text, f, fill, tracking):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x - tracking


def tracked_width(draw, text, f, tracking):
    return sum(draw.textlength(c, font=f) for c in text) + tracking * (len(text) - 1)


# ---------------------------------------------------------------- contenuti
EYEBROW = "REEL:"
TITOLO  = ["Quale modello usare", "per quale obiettivo?"]
HEAD    = ["MODELLI DI REEL", "IN LANCIO", "NEL PED"]

ROWS = [
    ("CONOSCERE",
     "Presa di posizione, errore comune, mito da smontare, lettura di un trend.",
     "Almeno 1 Reel, sponsorizzato a ThruPlay.",
     "Spazio prioritario e continuo."),
    ("CONSIDERARE",
     "Tutorial o metodo, dietro le quinte, case study, risposta a una domanda frequente.",
     "Almeno 1 Reel, sponsorizzato a ThruPlay.",
     "Spazio prioritario, alternato ai Reel per conoscere."),
    ("COMPRARE",
     "Testimonianza, demo del prodotto o servizio, risposta alle obiezioni, offerta con scadenza.",
     "4 o 5 varianti a obiettivo conversione.",
     "Massimo un paio al mese in organico. Il resto in dark post."),
]

NOTA = ("La scelta dipende dall'obiettivo primario del momento. Un Reel non "
        "funziona in assoluto: funziona rispetto a quello che deve fare.")
URL = "www.veronicagentili.com"

# ---------------------------------------------------------------- canvas
img  = Image.new("RGB", (W, H), BLU)
draw = ImageDraw.Draw(img)

# --- header
y = 54
draw_tracked(draw, (MARGIN, y), EYEBROW, font(F_BOLD, 25), GIALLO, 2.2)
y += 44
f_titolo = font(F_BOLD, 56)
for line in TITOLO:
    draw.text((MARGIN, y), line, font=f_titolo, fill=BIANCO)
    y += 65
y += 8
draw.rounded_rectangle([(MARGIN, y), (MARGIN + 96, y + 7)], radius=3, fill=GIALLO)
y += 40

# --- griglia colonne
FASE_X0, FASE_X1 = MARGIN, 236
COLS = [(248, 560), (572, 788), (800, W - MARGIN)]

f_head = font(F_BOLD, 21)
for (x0, _), testo in zip(COLS, HEAD):
    draw_tracked(draw, (x0, y), testo, f_head, GIALLO, 1.6)
y += 44

ROWS_TOP, ROWS_BOTTOM = y, 1062
GAP, PAD_X, PAD_Y = 10, 20, 18

for size in range(24, 14, -1):
    f_body = font(F_REGULAR, size)
    lh = int(size * 1.44)
    heights, wrapped = [], []
    for _, *celle in ROWS:
        ls = [wrap(draw, t, f_body, (x1 - x0) - PAD_X * 2)
              for t, (x0, x1) in zip(celle, COLS)]
        wrapped.append(ls)
        heights.append(max(len(l) for l in ls) * lh + PAD_Y * 2)
    total = sum(heights) + GAP * (len(ROWS) - 1)
    if total <= ROWS_BOTTOM - ROWS_TOP:
        slack = (ROWS_BOTTOM - ROWS_TOP - total) // len(ROWS)
        heights = [h + slack for h in heights]
        break

f_fase = font(F_BOLD, 22)
row_y = ROWS_TOP
for (fase, *_), ls, rh in zip(ROWS, wrapped, heights):
    # etichetta fase, centrata nella colonna sinistra
    tw = tracked_width(draw, fase, f_fase, 1.4)
    cx = (FASE_X0 + FASE_X1) / 2
    draw_tracked(draw, (cx - tw / 2, row_y + rh // 2 - 17), fase, f_fase, BIANCO, 1.4)

    for (x0, x1), lines in zip(COLS, ls):
        draw.rounded_rectangle([(x0, row_y), (x1, row_y + rh)], radius=10, fill=BLU_DARK)
        ty = row_y + max(PAD_Y - 2, (rh - len(lines) * lh) // 2)
        for line in lines:
            draw.text((x0 + PAD_X, ty), line, font=f_body, fill=BIANCO)
            ty += lh
    row_y += rh + GAP

# --- nota finale
f_nota = font(F_MEDIUM, 26)
nota_lines = wrap(draw, NOTA, f_nota, W - MARGIN - (MARGIN + 34))
lh_n = 38
nota_y = 1110
draw.rounded_rectangle([(MARGIN, nota_y), (MARGIN + 7, nota_y + len(nota_lines) * lh_n)],
                       radius=3, fill=GIALLO)
for i, line in enumerate(nota_lines):
    draw.text((MARGIN + 34, nota_y + i * lh_n), line, font=f_nota, fill=BIANCO)

# --- footer brand
f_logo = font(F_BOLD, 27)
lx = MARGIN
draw.rounded_rectangle([(lx, FOOTER_Y - 15), (lx + 8, FOOTER_Y + 15)], radius=4, fill=GIALLO)
end_x = draw_tracked(draw, (lx + 22, FOOTER_Y - 20), "VERONICA", f_logo, BIANCO, 1.4)
draw_tracked(draw, (end_x + 12, FOOTER_Y - 20), "GENTILI", f_logo, GIALLO, 1.4)
draw.text((W - MARGIN, FOOTER_Y), URL, font=font(F_LIGHT, 24), fill=BIANCO, anchor="rm")

out = os.path.join(BASE, "20261112_reel_obiettivi.png")
img.save(out, "PNG")
print("OK", out, "corpo:", size, "fine righe:", row_y)
