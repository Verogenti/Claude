# Infografica — Quando viene contata una visualizzazione

Versione brandizzata Veronica Gentili dell'infografica sulle soglie di conteggio
delle view sui social network. Formato 1080x1350 px (4:5), pronto per Instagram.

## Design system applicato

| Elemento | Valore |
|---|---|
| Sfondo | `#355A9E` |
| Box | `#1E376E` |
| Accento | `#F5C518` |
| Testo | `#FFFFFF` |
| Font | Poppins (Bold / Medium / Regular / Light) |
| Margine | 64 px |
| Footer Y | H - 52 |

Elementi di brand: eyebrow gialla spaziata, regola gialla sotto il titolo,
barra di accento gialla su ogni riga, intestazioni di colonna gialle,
nota finale con barra gialla, footer con logotipo e `www.veronicagentili.com`.

## Loghi delle piattaforme

I nomi delle piattaforme sono sostituiti dai loghi ufficiali. Gli SVG sono in
`icons/` e arrivano da [Simple Icons](https://simpleicons.org) (licenza CC0);
i marchi restano dei rispettivi proprietari, qui usati a scopo informativo.

Due varianti:

- `vg_visualizzazioni_social_brandizzata.png` — loghi bianchi monocromatici (default)
- `vg_visualizzazioni_social_brandizzata_colore.png` — loghi nei colori ufficiali

Si sceglie con `VG_VARIANTE=bianco|colore`. Nella variante a colori X resta
bianco: il nero del marchio sparirebbe sul fondo blu.

## Come rigenerare

I font Poppins non sono versionati. Metterli in `fonts/` oppure puntare
`VG_FONT_DIR` a una cartella che li contiene:

```bash
pip install pillow cairosvg
mkdir -p fonts
for f in Poppins-Bold Poppins-SemiBold Poppins-Medium Poppins-Regular Poppins-Light; do
  curl -sSL -o "fonts/$f.ttf" \
    "https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/$f.ttf"
done
python3 genera_infografica.py                 # loghi bianchi
VG_VARIANTE=colore python3 genera_infografica.py   # loghi a colori
```

Il testo delle righe si modifica nella lista `ROWS` (il primo campo e' lo
slug del logo, che deve corrispondere a un file in `icons/`); altezza righe e corpo del
testo si adattano da soli allo spazio disponibile.

## Nota sul logo

Il logotipo nel footer e' composto tipograficamente in Poppins Bold perche'
`log_bianco.png` non era disponibile in questo ambiente. Per usare il logo
ufficiale, sostituire il blocco footer con il caricamento del PNG
(max_width 320 px, rimozione dello sfondo nero) come da design system.
