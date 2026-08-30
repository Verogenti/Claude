import io
import os

import cairosvg
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))

# Cartella dei font Poppins. Default: ./fonts accanto allo script.
# Override con VG_FONT_DIR (es. /usr/share/fonts/truetype/google-fonts).
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))

# Loghi social in SVG (Simple Icons, CC0).
ICON_DIR = os.path.join(BASE, "icons")

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

def load_icon(slug, size, colore):
    """Renderizza il logo SVG del social nel colore richiesto."""
    svg = open(os.path.join(ICON_DIR, f"{slug}.svg"), encoding="utf-8").read()
    svg = svg.replace("<svg ", f'<svg fill="{colore}" ', 1)
    png = cairosvg.svg2png(bytestring=svg.encode(),
                           output_width=size * 3, output_height=size * 3)
    return Image.open(io.BytesIO(png)).convert("RGBA").resize(
        (size, size), Image.LANCZOS)

# ---------------------------------------------------------------- contenuti
EYEBROW = "SOCIAL NETWORK:"
TITOLO  = ["Quando viene contata", "una visualizzazione?"]
HEAD    = ["VIEW DEL CONTENUTO", "VIEW VIDEO"]

# I loghi sostituiscono i nomi delle piattaforme.
# Colori ufficiali usati solo nella variante "colore".
COLORI_BRAND = {
    "instagram": "#E4405F", "facebook": "#0866FF", "linkedin": "#0A66C2",
    "youtube": "#FF0000", "pinterest": "#BD081C", "x": "#FFFFFF",
}

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
URL   = "www.veronicagentili.com"

# ---------------------------------------------------------------- variante
# "bianco" = loghi monocromatici bianchi (default, in linea col brand)
# "colore" = loghi nei colori ufficiali delle piattaforme
VARIANTE = os.environ.get("VG_VARIANTE", "bianco")
if VARIANTE not in ("bianco", "colore"):
    raise SystemExit("VG_VARIANTE deve essere 'bianco' o 'colore'")

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
PLAT_X0, PLAT_X1 = MARGIN, 184
C2_X0,  C2_X1   = 196, 600
C3_X0,  C3_X1   = 612, W - MARGIN
ICON_SIZE = 54

f_head = font(F_BOLD, 21)
head_y = y
draw_tracked(draw, (C2_X0, head_y), HEAD[0], f_head, GIALLO, 1.6)
draw_tracked(draw, (C3_X0, head_y), HEAD[1], f_head, GIALLO, 1.6)
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

row_y = ROWS_TOP
for (slug, _, _), (l2, l3), rh in zip(ROWS, wrapped, heights):
    # box piattaforma con logo centrato
    draw.rounded_rectangle([(PLAT_X0, row_y), (PLAT_X1, row_y + rh)],
                           radius=10, fill=BLU_DARK)
    colore = COLORI_BRAND[slug] if VARIANTE == "colore" else "#FFFFFF"
    icona = load_icon(slug, ICON_SIZE, colore)
    img.paste(icona,
              ((PLAT_X0 + PLAT_X1) // 2 - ICON_SIZE // 2,
               row_y + rh // 2 - ICON_SIZE // 2),
              icona)

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

suffisso = "" if VARIANTE == "bianco" else f"_{VARIANTE}"
out = os.path.join(BASE, f"vg_visualizzazioni_social_brandizzata{suffisso}.png")
img.save(out, "PNG")
print("OK", out, img.size, "corpo:", size, "fine righe:", row_y)
