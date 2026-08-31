# Carosello — ChatGPT Ads finalmente in Italia

8 slide 1080x1350 px (4:5), design system Veronica Gentili.

| Elemento | Valore |
|---|---|
| Sfondo | `#355A9E` |
| Accento | `#F5C518` |
| Testo | `#FFFFFF` |
| Font | Poppins (Bold / Medium / Regular / Light) |
| Margine | 64 px |
| Footer Y | H - 52 |

Slide 1 (cover) e slide 3-6 lasciano libera rispettivamente la metà superiore e
la colonna sinistra: sono gli spazi previsti per immagine o mockup.

## Come rigenerare

I font Poppins non sono versionati.

```bash
pip install pillow
mkdir -p fonts
for f in Poppins-Bold Poppins-SemiBold Poppins-Medium Poppins-Regular Poppins-Light; do
  curl -sSL -o "fonts/$f.ttf" \
    "https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/$f.ttf"
done
python3 genera_carosello.py
```

Il copy si modifica nel blocco `SLIDES` in fondo allo script; corpo del testo e
posizione verticale si adattano da soli allo spazio disponibile.

## Nota sul logo e sulla slide finale

Il logotipo nel footer e' composto tipograficamente in Poppins Bold perche'
`log_bianco.png` non e' disponibile in questo ambiente. La slide CTA finale
(`Instagram_Dark_Social__2_.png`) va appesa a mano come slide 9.
