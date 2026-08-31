# -*- coding: utf-8 -*-
"""Carosello Instagram: ChatGPT Ads finalmente in Italia.

Formato 1080x1350 px (4:5), design system Veronica Gentili.
"""

import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("VG_FONT_DIR", os.path.join(BASE, "fonts"))
OUT_DIR = os.environ.get("VG_OUT_DIR", os.path.join(BASE, "slides"))

F_BOLD = f"{FONT_DIR}/Poppins-Bold.ttf"
F_MEDIUM = f"{FONT_DIR}/Poppins-Medium.ttf"
F_REGULAR = f"{FONT_DIR}/Poppins-Regular.ttf"
F_LIGHT = f"{FONT_DIR}/Poppins-Light.ttf"

W, H = 1080, 1350
BLU = (53, 90, 158)
BLU_DARK = (30, 55, 110)
BLU_TESTO = (30, 58, 110)
GIALLO = (245, 197, 24)
BIANCO = (255, 255, 255)
BIANCO_SOFT = (255, 255, 255, 200)

MARGIN = 64
FOOTER_Y = H - 52
CONTENT_BOTTOM = H - 110
BULLET_X = W // 2 - 20
URL = "www.veronicagentili.com"


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


def nuova_slide():
    img = Image.new("RGB", (W, H), BLU)
    return img, ImageDraw.Draw(img)


def draw_footer(draw):
    f_logo = font(F_BOLD, 27)
    end_x = draw_tracked(draw, (MARGIN, FOOTER_Y - 20), "VERONICA", f_logo, BIANCO, 1.4)
    draw_tracked(draw, (end_x + 12, FOOTER_Y - 20), "GENTILI", f_logo, GIALLO, 1.4)
    draw.text((W - MARGIN, FOOTER_Y), URL, font=font(F_LIGHT, 24),
              fill=(255, 255, 255), anchor="rm")


def draw_subject(draw, subject, top=40, max_size=130):
    for size in range(max_size, 58, -2):
        f = font(F_BOLD, size)
        if draw.textbbox((0, 0), subject, font=f)[2] <= W - MARGIN * 2:
            break
    draw.text((MARGIN, top), subject, font=f, fill=BIANCO)
    return top + int(size * 1.12)


def misura_checklist(draw, items, available_h, x_left, max_size=34, min_size=17):
    text_x = x_left + 46
    max_w = W - text_x - MARGIN
    size = min_size
    all_lines, lh, gap, total = [], 0, 0, 0
    for size in range(max_size, min_size - 1, -1):
        f = font(F_REGULAR, size)
        lh = int(size * 1.42)
        gap = max(22, size // 2 + 8)
        total, all_lines = 0, []
        for text in items:
            ls = wrap(draw, text, f, max_w)
            all_lines.append(ls)
            total += len(ls) * lh + gap
        total -= gap
        if total <= available_h:
            break
    return size, lh, gap, all_lines, total


def disegna_checklist(draw, misura, y_start, x_left):
    size, lh, gap, all_lines, _ = misura
    bullet_cx = x_left + 18
    text_x = x_left + 46
    f = font(F_REGULAR, size)
    bullet_r = size // 3 + 3
    f_freccia = font(F_BOLD, max(10, bullet_r - 2))
    y = y_start
    for ls in all_lines:
        first_line_cy = y + lh // 2
        draw.ellipse([(bullet_cx - bullet_r, first_line_cy - bullet_r),
                      (bullet_cx + bullet_r, first_line_cy + bullet_r)], fill=GIALLO)
        draw.text((bullet_cx, first_line_cy), ">", font=f_freccia,
                  fill=BLU_TESTO, anchor="mm")
        for j, line in enumerate(ls):
            draw.text((text_x, y + j * lh), line, font=f, fill=BIANCO)
        y += len(ls) * lh + gap
    return y - gap


def slide_cover(riga1, riga2, sottotitolo):
    img, draw = nuova_slide()
    f_title = font(F_BOLD, 88)
    lh_title = int(88 * 1.1)
    f_sub = font(F_MEDIUM, 44)
    lh_sub = int(44 * 1.35)
    sub_lines = wrap(draw, sottotitolo, f_sub, W - MARGIN * 2)

    total_h = lh_title * 2 + 28 + lh_sub * len(sub_lines)
    y = FOOTER_Y - 80 - total_h

    draw.text((MARGIN, y), riga1, font=f_title, fill=BIANCO)
    draw.text((MARGIN, y + lh_title), riga2, font=f_title, fill=GIALLO)
    y += lh_title * 2 + 28
    for line in sub_lines:
        draw.text((MARGIN, y), line, font=f_sub, fill=(226, 234, 248))
        y += lh_sub

    draw_footer(draw)
    return img


def slide_testo(subject, paragrafi, chiusura=None):
    """Slide introduttiva: titolo soggetto piu' paragrafi a tutta larghezza."""
    img, draw = nuova_slide()
    title_bottom = draw_subject(draw, subject)
    zona_top = title_bottom + 70
    zona_bottom = CONTENT_BOTTOM - 40
    available_h = zona_bottom - zona_top
    max_w = W - MARGIN * 2

    for size in range(46, 25, -1):
        f = font(F_REGULAR, size)
        lh = int(size * 1.5)
        blocchi = [wrap(draw, p, f, max_w) for p in paragrafi]
        total = sum(len(b) * lh for b in blocchi) + (len(blocchi) - 1) * int(size * 0.9)
        f_ch, ch_lines, lh_ch = None, [], 0
        if chiusura:
            f_ch = font(F_MEDIUM, size + 4)
            ch_lines = wrap(draw, chiusura, f_ch, max_w)
            lh_ch = int((size + 4) * 1.4)
            total += int(size * 1.5) + len(ch_lines) * lh_ch
        if total <= available_h:
            break

    y = zona_top + max(0, (available_h - total) // 2)
    for blocco in blocchi:
        for line in blocco:
            draw.text((MARGIN, y), line, font=f, fill=BIANCO)
            y += lh
        y += int(size * 0.9)

    if chiusura:
        y += int(size * 0.6)
        for line in ch_lines:
            draw.text((MARGIN, y), line, font=f_ch, fill=GIALLO)
            y += lh_ch

    draw_footer(draw)
    return img


def slide_bullet(subject, items, nota=None):
    """Colonna sinistra libera per immagine, bullet nella colonna destra."""
    img, draw = nuova_slide()
    title_bottom = draw_subject(draw, subject)
    zona_top = title_bottom + 110

    nota_lines, nota_h, f_nota, lh_nota = [], 0, None, 0
    if nota:
        f_nota = font(F_MEDIUM, 32)
        lh_nota = int(32 * 1.42)
        nota_lines = wrap(draw, nota, f_nota, W - MARGIN * 2 - 28)
        nota_h = len(nota_lines) * lh_nota

    nota_bottom = H - 168
    zona_bottom = (nota_bottom - nota_h - 60) if nota else CONTENT_BOTTOM
    available_h = zona_bottom - zona_top

    misura = misura_checklist(draw, items, available_h, BULLET_X)
    y_start = zona_top + max(0, (available_h - misura[4]) // 2)
    disegna_checklist(draw, misura, y_start, BULLET_X)

    if nota:
        y = nota_bottom - nota_h
        draw.rectangle([(MARGIN, y + 2), (MARGIN + 6, y + nota_h - 12)], fill=GIALLO)
        for line in nota_lines:
            draw.text((MARGIN + 28, y), line, font=f_nota, fill=GIALLO)
            y += lh_nota

    draw_footer(draw)
    return img


def slide_takeaway(blocchi, sottotesto, barra=True):
    """blocchi: lista di (testo, percorso_font, size, colore)."""
    img, draw = nuova_slide()
    if barra:
        draw.rectangle([(W - 10, 0), (W, H // 2)], fill=GIALLO)

    max_w = W - MARGIN * 2 - 20
    scala = 1.0
    while scala > 0.5:
        righe = []
        total = 0
        for testo, fpath, size, colore in blocchi:
            s = int(size * scala)
            f = font(fpath, s)
            ls = wrap(draw, testo, f, max_w)
            lh = int(s * 1.16)
            righe.append((ls, f, lh, colore))
            total += len(ls) * lh + int(s * 0.22)
        s_sub = int(42 * min(scala + 0.08, 1.0))
        f_sub = font(F_REGULAR, s_sub)
        sub_lines = wrap(draw, sottotesto, f_sub, max_w)
        lh_sub = int(s_sub * 1.48)
        total += 56 + len(sub_lines) * lh_sub
        if total <= CONTENT_BOTTOM - 150:
            break
        scala -= 0.04

    y = max(150, (CONTENT_BOTTOM - total) // 2)
    for ls, f, lh, colore in righe:
        for line in ls:
            draw.text((MARGIN, y), line, font=f, fill=colore)
            y += lh
        y += int(lh * 0.18)

    y += 40
    for line in sub_lines:
        draw.text((MARGIN, y), line, font=f_sub, fill=(226, 234, 248))
        y += lh_sub

    draw_footer(draw)
    return img


SLIDES = []

SLIDES.append(slide_cover(
    "CHATGPT ADS",
    "FINALMENTE IN ITALIA",
    "Da oggi puoi comprare inserzioni su ChatGPT in autonomia.",
))

SLIDES.append(slide_testo(
    "COSA È SUCCESSO",
    [
        "ChatGPT Ads era arrivato in Europa questo mese, Italia inclusa, ma si comprava solo tramite agenzie partner selezionate.",
        "Da oggi cambia. OpenAI ha aperto la beta self service di Ads Manager in tutti e 31 i mercati europei. Entri, crei la campagna, la gestisci. Senza intermediari.",
    ],
    "Ecco cosa devi sapere prima di aprire l'account.",
))

SLIDES.append(slide_bullet(
    "COSA CAMBIA",
    [
        "Accesso diretto alla creazione e alla gestione delle campagne, senza passare da un partner",
        "Aperto a startup, PMI e aziende strutturate, non solo ai grandi budget",
        "Chi preferisce continuare con agenzie e partner tech può farlo lo stesso",
        "L'accesso resta legato a categoria approvata e inserzioni conformi alle policy di OpenAI",
    ],
))

SLIDES.append(slide_bullet(
    "CHI PUÒ FARE ADV",
    [
        "Lifestyle e articoli per la casa",
        "Servizi locali",
        "Viaggi ed esperienze",
        "Prodotti digitali e formazione",
    ],
    nota="Finanza, sanità e servizi legali entrano solo con approvazione manuale, caso per caso.",
))

SLIDES.append(slide_bullet(
    "CHI RESTA FUORI",
    [
        "Dating e contenuti sessuali",
        "Claim sulla salute, alcol e droghe",
        "Gioco d'azzardo",
        "Contenuti politici",
    ],
    nota="Al lancio tutte le categorie non ammesse sono vietate. L'elenco può cambiare mentre il programma cresce.",
))

SLIDES.append(slide_bullet(
    "COME FUNZIONANO",
    [
        "Gli annunci sono segnalati e separati dalle risposte di ChatGPT",
        "Non influenzano le risposte",
        "Gli inserzionisti non vedono le conversazioni degli utenti né i loro dati personali",
        "Creatività e landing page devono essere coerenti. Un annuncio sul food delivery non può portare a un servizio di consegna alcolici",
    ],
))

SLIDES.append(slide_takeaway(
    [
        ("ChatGPT Ads ha fatto", F_BOLD, 72, BIANCO),
        ("1 miliardo di dollari", F_BOLD, 100, GIALLO),
        ("di ricavi ricorrenti annuali in meno di 200 giorni.", F_BOLD, 60, BIANCO),
    ],
    "Nessuna piattaforma pubblicitaria era mai arrivata a quella cifra a quella velocità.",
))

SLIDES.append(slide_takeaway(
    [
        ("Non è il momento di", F_BOLD, 88, BIANCO),
        ("spostare budget.", F_BOLD, 100, GIALLO),
        ("È il momento di capire come funziona.", F_BOLD, 72, BIANCO),
    ],
    "Il canale è giovane, le categorie aperte sono poche, i dati sono pochissimi. Se rientri, apri l'account e testa con una cifra che puoi permetterti di bruciare. Ti porti a casa l'apprendimento prima che il costo del click salga.",
))

os.makedirs(OUT_DIR, exist_ok=True)
for i, img in enumerate(SLIDES, start=1):
    path = os.path.join(OUT_DIR, f"chatgpt_ads_italia_s{i:02d}.png")
    img.save(path, "PNG")
    print("scritta", path)
