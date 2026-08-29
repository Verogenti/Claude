import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))

# Cartella dei font Poppins. Default: ./fonts accanto allo script.
# Override con VG_FONT_DIR (es. /usr/share/fonts/truetype/google-fonts).
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))

F_BOLD    = f"{FONT_DIR}/Poppins-Bold.ttf"
F_SEMI    = f"{FONT_DIR}/Poppins-SemiBold.ttf"
F_MEDIUM  = f"{FONT_DIR}/Poppins-Medium.ttf"
F_REGULAR = f"{FONT_DIR}/Poppins-Regular.ttf"
F_LIGHT   = f"{FONT_DIR}/Poppins-Light.ttf"

W, H = 1080, 1350
BLU       = (53, 90, 158)
BLU_DARK  = (30, 55, 110)
BLU_TESTO = (30, 58, 110)
GIALLO    = (245, 197, 24)
BIANCO    = (255, 255, 255)

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

def draw_tracked(draw, xy, text, f, fill, tracking, anchor_left=True):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x - tracking

def tracked_width(draw, text, f, tracking):
    return sum(draw.textlength(c, font=f) for c in text) + tracking * (len(text) - 1)

# ---------------------------------------------------------------- contenuti
EYEBROW = "SOCIAL NETWORK:"
TITOLO  = ["Quando viene contata", "una visualizzazione?"]
HEAD    = ["PIATTAFORMA", "VIEW DEL CONTENUTO", "VIEW VIDEO"]

ROWS = [
    ("INSTAGRAM",
     "Post o carosello mostrato a schermo. Nessuna soglia di tempo, le visualizzazioni ripetute contano.",
     "Il Reel parte o riparte. Nessun minimo di riproduzione."),
    ("FACEBOOK",
     "Foto, post o storia a schermo. Vista tre volte, tre view. Nessuna soglia di tempo dichiarata.",
     "Video o Reel riprodotto, senza durata minima. Le 3 second views restano a parte."),
    ("LINKEDIN",
     "Post visibile almeno al 50% per 300 millisecondi a un utente loggato.",
     "La view viene conteggiata quando il video viene guardato per più di 2 secondi. Sulle Pagine la soglia documentata è 3 secondi."),
    ("YOUTUBE",
     "Per i post della Community YouTube usa le Impressions, non le Views.",
     "Dal 24 agosto 2026 all'avvio della riproduzione. Shorts, video lunghi e dirette."),
    ("PINTEREST",
     "Il Pin compare a schermo.",
     "2 secondi di riproduzione con il 50% del video a schermo."),
    ("X",
     "Il post compare sullo schermo di un utente loggato.",
     "2 secondi con il 50% del player a schermo."),
]

NOTA = ("Dati riferiti alle visualizzazioni organiche. Lato advertising valgono "
        "soglie e criteri di conteggio diversi.")
FONTI = "Fonti ufficiali, agosto 2026"
URL   = "www.veronicagentili.com"

# ---------------------------------------------------------------- canvas
img  = Image.new("RGB", (W, H), BLU)
draw = ImageDraw.Draw(img)

# --- header
y = 54
f_eyebrow = font(F_BOLD, 25)
draw_tracked(draw, (MARGIN, y), EYEBROW, f_eyebrow, GIALLO, 2.2)
y += 44

f_titolo = font(F_BOLD, 56)
lh_t = 65
for line in TITOLO:
    draw.text((MARGIN, y), line, font=f_titolo, fill=BIANCO)
    y += lh_t
y += 8

# regola gialla sotto il titolo
draw.rounded_rectangle([(MARGIN, y), (MARGIN + 96, y + 7)], radius=3, fill=GIALLO)
y += 40

# --- griglia colonne
BAR_X0, BAR_W = MARGIN, 7
PLAT_X0, PLAT_X1 = 82, 262
C2_X0,  C2_X1   = 274, 646
C3_X0,  C3_X1   = 658, W - MARGIN

f_head = font(F_BOLD, 21)
head_y = y
draw_tracked(draw, (PLAT_X0, head_y), HEAD[0], f_head, GIALLO, 1.6)
draw_tracked(draw, (C2_X0,  head_y), HEAD[1], f_head, GIALLO, 1.6)
draw_tracked(draw, (C3_X0,  head_y), HEAD[2], f_head, GIALLO, 1.6)
y = head_y + 44

# --- righe (auto-fit)
ROWS_TOP    = y
ROWS_BOTTOM = 1082
GAP         = 10
PAD_X, PAD_Y = 22, 18

for size in range(23, 14, -1):
    f_body = font(F_REGULAR, size)
    lh     = int(size * 1.44)
    heights, wrapped = [], []
    for _, c2, c3 in ROWS:
        l2 = wrap(draw, c2, f_body, (C2_X1 - C2_X0) - PAD_X * 2)
        l3 = wrap(draw, c3, f_body, (C3_X1 - C3_X0) - PAD_X * 2)
        wrapped.append((l2, l3))
        heights.append(max(len(l2), len(l3)) * lh + PAD_Y * 2)
    total = sum(heights) + GAP * (len(ROWS) - 1)
    if total <= ROWS_BOTTOM - ROWS_TOP:
        # distribuisce lo spazio residuo sulle righe, per riempire la griglia
        slack = (ROWS_BOTTOM - ROWS_TOP - total) // len(ROWS)
        heights = [h + slack for h in heights]
        break

f_plat = font(F_BOLD, 21)
row_y = ROWS_TOP
for (plat, _, _), (l2, l3), rh in zip(ROWS, wrapped, heights):
    # accento giallo
    draw.rounded_rectangle([(BAR_X0, row_y), (BAR_X0 + BAR_W, row_y + rh)],
                           radius=3, fill=GIALLO)
    # box piattaforma
    draw.rounded_rectangle([(PLAT_X0, row_y), (PLAT_X1, row_y + rh)],
                           radius=10, fill=BLU_DARK)
    ps = 21
    while draw.textlength(plat, font=font(F_BOLD, ps)) > (PLAT_X1 - PLAT_X0) - 36 and ps > 14:
        ps -= 1
    f_p = font(F_BOLD, ps)
    draw.text((PLAT_X0 + 18, row_y + rh // 2), plat, font=f_p, fill=BIANCO, anchor="lm")

    # celle testo
    for x0, x1, lines in ((C2_X0, C2_X1, l2), (C3_X0, C3_X1, l3)):
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
nota_h = len(nota_lines) * lh_n
nota_y = 1122
draw.rounded_rectangle([(MARGIN, nota_y), (MARGIN + BAR_W, nota_y + nota_h)],
                       radius=3, fill=GIALLO)
ny = nota_y
for line in nota_lines:
    draw.text((MARGIN + 34, ny), line, font=f_nota, fill=BIANCO)
    ny += lh_n

# --- riga fonti
draw.text((MARGIN, 1224), FONTI, font=font(F_LIGHT, 23), fill=(255, 255, 255))

# --- footer brand
f_logo = font(F_BOLD, 27)
lx = MARGIN
draw.rounded_rectangle([(lx, FOOTER_Y - 15), (lx + 8, FOOTER_Y + 15)], radius=4, fill=GIALLO)
lx += 22
end_x = draw_tracked(draw, (lx, FOOTER_Y - 20), "VERONICA", f_logo, BIANCO, 1.4)
draw_tracked(draw, (end_x + 12, FOOTER_Y - 20), "GENTILI", f_logo, GIALLO, 1.4)

draw.text((W - MARGIN, FOOTER_Y), URL, font=font(F_LIGHT, 24), fill=BIANCO, anchor="rm")

out = os.path.join(BASE, "vg_visualizzazioni_social_brandizzata.png")
img.save(out, "PNG")
print("OK", out, img.size, "body size:", size, "rows bottom:", row_y)
