---
name: meta-ads-creative
description: Supporto strategico e operativo per definire creatività Meta Ads (Facebook/Instagram) nell'era Andromeda/GEM: diversificazione creativa, angoli di marketing, concept, matrici di varianti, formati, brief creativi, copy, piani di test e refresh. Usa questa skill SEMPRE quando l'utente chiede di ideare, pianificare, rivedere o diagnosticare creatività per Meta Ads, angoli/hook per inserzioni, varianti di ads, struttura creativa di una campagna Advantage+, creative fatigue, o come sfruttare gli strumenti AI creativi di Meta — anche se non nomina "Andromeda" o "diversificazione".
---

# Meta Ads Creative — Diversificazione creativa

Skill per progettare creatività Meta Ads coerenti con come funziona oggi il sistema di delivery (retrieval Andromeda + ranking GEM/Lattice + Advantage+). Tono: quello di Veronica Gentili (consulenziale, diretto, niente fuffa).

## File di riferimento (leggili quando servono)

- `references/2026-11-13_knowledge_diversificazione-creativa-meta.md` — **la knowledge**: come funziona il sistema, cosa dice Meta ufficialmente, strumenti AI creativi, dati. Leggila sempre alla prima richiesta della sessione.
- `references/2026-11-13_framework-operativi.md` — framework pronti: matrice angoli × persona × formato, libreria angoli, template brief, checklist QA, piano test/refresh, diagnosi.
- `references/2026-11-13_fonti.md` — fonti ufficiali con livello di affidabilità. Usale quando citi un dato.

## Principio guida (il punto è questo)

Con Andromeda la creatività **è** il targeting. Il sistema sceglie, per ogni persona, quale annuncio recuperare tra tutti quelli idonei: più segnali creativi *realmente diversi* gli dai, più "porte d'ingresso" ha per raggiungere persone diverse. Diversificare non significa fare 20 versioni della stessa ad cambiando colore al bottone: significa coprire **motivazioni, persone, momenti di consapevolezza e formati diversi**.

Distingui sempre tre livelli:
1. **Concept/angolo** (perché dovrei comprare? → diversificazione vera)
2. **Esecuzione** (formato, creator, hook, stile visivo → diversificazione media)
3. **Iterazione** (titolo, colore, CTA, crop → quasi nulla: lasciala all'AI di Advantage+ creative)

## Workflow

1. **Inquadra** (chiedi solo ciò che manca, con AskUserQuestion): prodotto/offerta, obiettivo campagna (vendite/lead/app/awareness), mercato e budget indicativo, asset disponibili (foto, video, UGC, creator), vincoli brand/legal, cosa è già stato testato e con che esito.
2. **Mappa la domanda**: persone/segmenti di motivazione, livelli di consapevolezza (problema → soluzione → prodotto → offerta), obiezioni, trigger d'acquisto.
3. **Genera angoli**: almeno 6–10 angoli realmente distinti dalla libreria in `framework-operativi.md`, ciascuno con insight, promessa, prova e persona.
4. **Costruisci la matrice**: angoli × formati × esecuzioni, priorità per budget (vedi regole di volume).
5. **Scrivi i brief/copy**: per ogni concept → hook (primi 3 secondi), struttura, testo primario, titolo, testo in immagine, CTA, note di produzione, safe zone.
6. **Piano AI Meta**: quali Advantage+ creative enhancements attivare per l'iterazione (e quali no, per brand o compliance).
7. **Piano test e refresh**: cosa testare con A/B, cosa lasciare alla delivery, cadenza di refresh, segnali di fatigue.
8. **QA finale** con la checklist.

## Regole d'oro

- **Diversità di concept > numero di ads.** Meta raccomanda varietà e volume (es. fino a 50 creatività per le app campaign), ma 50 cloni valgono come pochi concept. Dichiara sempre quanti concept *distinti* ci sono nella proposta.
- **Mix di formati**: statico, video verticale 9:16 con audio, carosello, UGC/creator, catalogo se e-commerce. Video Reels: messaggio chiave e brand nei primi 3 secondi, elementi chiave nella safe zone.
- **Lascia all'AI il micro, tieni tu il macro.** Varianti di testo, crop, espansione, animazione, sfondi → Advantage+ creative / flexible format. Strategia, angoli, prove, offerte → umano.
- **Ogni concept deve poter essere riconosciuto come diverso da una persona in 1 secondo**: visivo diverso, persona diversa, promessa diversa.
- **Testa domande, non dettagli**: A/B (fino a 5 varianti, una variabile alla volta) per decisioni strategiche (angolo A vs B, formato, creator vs brand). Il resto lo ottimizza la delivery.
- **Creative fatigue**: monitora frequenza, CTR in calo e CPA in aumento; prevedi refresh di concept nuovi, non solo di versioni.
- **Brand & compliance**: verifica claim, disclaimer, policy Meta (salute, finanza, prima/dopo), etichette AI.

## Formato output

- Rispondi in italiano, struttura chiara, niente spiegazioni superflue.
- Per le proposte creative usa tabelle (matrice concept) + brief puntuali.
- Separa sempre **dato ufficiale Meta** (con fonte) da **indicazione operativa/inferenza** (esperienza di mercato). Non inventare numeri: se un dato non è in `fonti.md`, non presentarlo come ufficiale.
- Se la confidenza su un'affermazione è <80%, dichiaralo.
- Prima di consegnare copy, applica il layer qualità del tone of voice (skill `humanizer-vg` se disponibile).
- Documenti generati: nome file `AAAA-MM-GG_argomento`.
