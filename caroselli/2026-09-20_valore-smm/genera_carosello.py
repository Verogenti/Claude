#!/usr/bin/env python3
"""Carosello Instagram 1080x1350 - il valore reale di una Social Media Manager."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))
OUT_DIR = os.environ.get("VG_OUT_DIR", BASE)

F_BOLD    = f"{FONT_DIR}/Poppins-Bold.ttf"
F_MEDIUM  = f"{FONT_DIR}/Poppins-Medium.ttf"
F_REGULAR = f"{FONT_DIR}/Poppins-Regular.ttf"
F_LIGHT   = f"{FONT_DIR}/Poppins-Light.ttf"

W, H = 1080, 1350
MARGIN = 64
CONTENT_W = W - MARGIN * 2
FOOTER_Y = H - 52
SEP_Y = FOOTER_Y - 44
CONTENT_BOTTOM = SEP_Y - 60

BLU      = (53, 90, 158)
BIANCO   = (255, 255, 255)
GIALLO   = (245, 197, 24)
BOX_BG   = (30, 55, 110)
BLU_DARK = (30, 58, 110)
URL = "veronicagentili.com"


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


def fit_one_line(draw, text, max_size, max_w, min_size=40):
    for size in range(max_size, min_size - 1, -2):
        f = font(F_BOLD, size)
        if draw.textbbox((0, 0), text, font=f)[2] <= max_w:
            return f, size
    return font(F_BOLD, min_size), min_size


def draw_tracked(draw, pos, text, f, fill, tracking):
    x, y = pos
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x


def new_slide():
    img = Image.new("RGB", (W, H), BLU)
    return img, ImageDraw.Draw(img)


def draw_footer(draw):
    draw.line([(MARGIN, SEP_Y), (W - MARGIN, SEP_Y)], fill=(255, 255, 255, 60), width=1)
    f_logo = font(F_BOLD, 27)
    lx = MARGIN
    draw.rounded_rectangle([(lx, FOOTER_Y - 15), (lx + 8, FOOTER_Y + 15)], radius=4, fill=GIALLO)
    lx += 22
    end_x = draw_tracked(draw, (lx, FOOTER_Y - 20), "VERONICA", f_logo, BIANCO, 1.4)
    draw_tracked(draw, (end_x + 12, FOOTER_Y - 20), "GENTILI", f_logo, GIALLO, 1.4)
    draw.text((W - MARGIN, FOOTER_Y), URL, font=font(F_LIGHT, 24), fill=BIANCO, anchor="rm")


def draw_block(draw, lines, f, lh, y, fill):
    for line in lines:
        draw.text((MARGIN, y), line, font=f, fill=fill)
        y += lh
    return y


# --- slide 1: cover -------------------------------------------------------
def slide_cover(riga1, riga2, sottotitolo):
    img, draw = new_slide()
    size = 104
    while size > 48:
        f = font(F_BOLD, size)
        w1 = draw.textbbox((0, 0), riga1, font=f)[2]
        w2 = draw.textbbox((0, 0), riga2, font=f)[2]
        if max(w1, w2) <= CONTENT_W:
            break
        size -= 2
    f_tit = font(F_BOLD, size)
    lh_tit = int(size * 1.10)

    f_sub = font(F_MEDIUM, 52)
    lh_sub = int(52 * 1.34)
    sub_lines = wrap(draw, sottotitolo, f_sub, CONTENT_W)

    total = lh_tit + 18 + lh_tit + 40 + lh_sub * len(sub_lines)
    y = CONTENT_BOTTOM - total

    draw.text((MARGIN, y), riga1, font=f_tit, fill=BIANCO)
    y += lh_tit + 18
    draw.text((MARGIN, y), riga2, font=f_tit, fill=GIALLO)
    y += lh_tit + 40
    draw_block(draw, sub_lines, f_sub, lh_sub, y, BIANCO)

    draw_footer(draw)
    return img


# --- slide interne --------------------------------------------------------
def slide_punto(label, titolo, corpo, box=None):
    img, draw = new_slide()

    f_label = font(F_MEDIUM, 24)
    lh_label = 34
    f_tit, size = fit_one_line(draw, titolo, 100, CONTENT_W)
    lh_tit = int(size * 1.12)

    f_body = font(F_REGULAR, 40)
    lh_body = int(40 * 1.45)
    body_lines = wrap(draw, corpo, f_body, CONTENT_W)

    f_box = font(F_MEDIUM, 33)
    lh_box = int(33 * 1.40)
    pad_x, pad_t, pad_b = 20, 14, 18
    box_lines = wrap(draw, box, f_box, CONTENT_W - pad_x - 28) if box else []
    box_h = pad_t + lh_box * len(box_lines) + pad_b if box else 0

    y = 90
    draw_tracked(draw, (MARGIN, y), label, f_label, GIALLO, 2.0)
    y += lh_label + 24
    draw.text((MARGIN, y), titolo, font=f_tit, fill=BIANCO)
    y += lh_tit + 60
    y = draw_block(draw, body_lines, f_body, lh_body, y, BIANCO)

    if box:
        y += 46
        draw.rectangle([(MARGIN, y), (W - MARGIN, y + box_h)], fill=BOX_BG)
        draw.rectangle([(MARGIN, y), (MARGIN + 5, y + box_h)], fill=GIALLO)
        ty = y + pad_t
        for line in box_lines:
            draw.text((MARGIN + 5 + pad_x, ty), line, font=f_box, fill=BIANCO)
            ty += lh_box

    draw_footer(draw)
    return img


# --- slide takeaway -------------------------------------------------------
def slide_takeaway(riga_bianca, riga_gialla, corpo):
    img, draw = new_slide()
    f_tit = font(F_BOLD, 66)
    lh_tit = int(66 * 1.16)
    l1 = wrap(draw, riga_bianca, f_tit, CONTENT_W)
    l2 = wrap(draw, riga_gialla, f_tit, CONTENT_W)

    f_body = font(F_REGULAR, 40)
    lh_body = int(40 * 1.45)
    l3 = wrap(draw, corpo, f_body, CONTENT_W)

    total = lh_tit * (len(l1) + len(l2)) + 18 + 48 + lh_body * len(l3)
    y = (160 + CONTENT_BOTTOM - total) // 2

    y = draw_block(draw, l1, f_tit, lh_tit, y, BIANCO)
    y += 18
    y = draw_block(draw, l2, f_tit, lh_tit, y, GIALLO)
    y += 48
    draw_block(draw, l3, f_body, lh_body, y, BIANCO)

    draw_footer(draw)
    return img


SLIDES = [
    lambda: slide_cover(
        "Non paghi una SMM",
        "solo per postare",
        'Quando ti affidi a una Social Media Manager, non la paghi solo per "gestire i social". Ma anche per questo.',
    ),
    lambda: slide_punto(
        "PUNTO 1", "Bug quotidiani",
        "Affrontare bug quotidiani che spuntano dal nulla.",
    ),
    lambda: slide_punto(
        "PUNTO 2", "Capire cosa non funziona",
        "Capire perché un post non parte, una campagna si blocca o un accesso sparisce.",
    ),
    lambda: slide_punto(
        "PUNTO 3", "Parlare con l'assistenza",
        "Cercare di parlare con l'assistenza quando qualcosa va storto.",
        box="Spoiler: spesso è impossibile.",
    ),
    lambda: slide_punto(
        "PUNTO 4", "Piattaforme che cambiano",
        "Stare dietro a funzioni, interfacce e regole che cambiano continuamente.",
    ),
    lambda: slide_takeaway(
        "Perché il vero valore di una SMM",
        "non è solo saper usare i social.",
        "È sapere cosa fare anche quando qualcosa cambia o non funziona.",
    ),
]

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for i, make in enumerate(SLIDES, start=1):
        path = os.path.join(OUT_DIR, f"2026-09-20_valore-smm_s{i:02d}.png")
        make().save(path, "PNG")
        print("OK", path)
