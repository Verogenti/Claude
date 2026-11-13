# Knowledge — Diversificazione creativa su Meta (stato dell'arte, novembre 2026)

> Legenda affidabilità: **[UFF]** = dichiarato da Meta in fonti ufficiali (engineering blog, newsroom, help center, earnings call). **[OPS]** = indicazione operativa dedotta dal funzionamento del sistema / prassi di mercato, non dichiarata da Meta. I dati Meta sono auto-dichiarati, non verificati da terzi.
> Fonti dettagliate in `2026-11-13_fonti.md`.

---

## 1. Perché la creatività è diventata la leva principale

### 1.1 La pipeline di delivery, semplificata

1. **Retrieval (Andromeda)** — da tutti gli annunci idonei, il sistema seleziona per ogni persona un sottoinsieme di candidati. **[UFF]** Il retrieval elabora circa tre ordini di grandezza (≈1.000×) più annunci rispetto alle fasi successive.
2. **Ranking (GEM + Lattice e modelli di ranking)** — i candidati vengono valutati prevedendo probabilità di click e conversione. **[UFF]** GEM è il foundation model per le raccomandazioni di annunci su Facebook e Instagram e predice congiuntamente CTR e CVR su superfici e obiettivi.
3. **Asta e consegna** — vince l'annuncio con il miglior valore totale (offerta × azione stimata + qualità).

Tradotto: se la tua creatività non viene *recuperata* nella fase 1 per una certa persona, non entra nemmeno in gara. E ciò che determina il recupero è sempre più il **contenuto dell'annuncio** (segnali di testo, immagine, video) in relazione al comportamento della persona.

### 1.2 Andromeda (dicembre 2024 → nuova generazione ottobre 2026)

- **[UFF]** Lanciato nel dicembre 2024 come motore di retrieval personalizzato per sostenere l'automazione Advantage+, costruito per gestire la crescita del numero di creatività idonee (anche quelle generate dall'AI). Usa un indice gerarchico; Meta dichiara un +8% di qualità degli annunci e la capacità di proporre un insieme **più diversificato** di candidati.
- **[UFF]** Meta collega esplicitamente la cosa alla creatività: man mano che gli inserzionisti caricano più creatività, il sistema usa modelli più complessi per scegliere quella giusta per ogni persona.
- **[UFF]** Ottobre 2026: nuova generazione di Andromeda con architettura *retrieval mixture-of-experts* co-progettata su GPU; Meta dichiara di valutare oltre **1 miliardo di annunci al secondo, 100× rispetto al sistema 2024**, e attribuisce la crescita del pool di candidati anche agli strumenti di AI generativa creativa (centinaia di milioni di nuovi annunci).
- **[UFF]** Q3 2026: miglioramenti ad Andromeda (complessità del modello e throughput) → +1,4% conversioni su Facebook. Q4 2025: efficienza di calcolo quasi triplicata.

### 1.3 GEM e Lattice

- **[UFF]** GEM (Generative Ads Recommendation Model, novembre 2025): modello centrale che trasferisce conoscenza ai modelli di ranking; al lancio +5% conversioni su Instagram Reels (come dichiarato da Meta). Nel 2026 è addestrato "a scala LLM" e diventa modello centrale unico.
- **[UFF]** Lattice: architettura di ranking che generalizza gli apprendimenti tra obiettivi e superfici invece di usare tanti modelli piccoli.
- **[UFF]** Novembre 2026, "Intelligent Delivery": un modello (Resource Core Model) decide quanto calcolo dedicare a ogni richiesta di annuncio prima del retrieval, perché il valore di calcolo extra varia per superficie, intento dell'utente e **qualità dei candidati**.

### 1.4 Cosa significa per la creatività **[OPS]**

- **La creatività fa targeting.** Con pubblici ampi (Advantage+ audience) e retrieval basato sul contenuto, ogni concept "parla" a un cluster diverso di persone. Concept diversi = più cluster raggiungibili.
- **Le creatività troppo simili tra loro competono per le stesse persone** e portano poco segnale incrementale. Nel mercato si parla di raggruppamento delle ads simili ("Entity ID"): **non ho trovato conferma in documentazione ufficiale Meta** di questo meccanismo specifico — trattalo come ipotesi plausibile, non come fatto (confidenza <80%).
- **Volume utile = volume di concept**, non di varianti cosmetiche.
- **Meno frammentazione strutturale**: Meta raccomanda di consolidare ad set simili per far lavorare meglio la delivery **[UFF]**; la segmentazione si sposta dagli ad set alle creatività **[OPS]**.

---

## 2. Cosa dice Meta ufficialmente sulla diversificazione

- **[UFF]** Pagina "Performance Marketing": la *creative diversification* è una best practice esplicita — "Develop a variety of ad creative and enable AI to deliver the right message to the people most likely to be interested in it."
- **[UFF]** Advantage+ app campaigns: sezione "Prioritize creative diversification and differentiation" → fino a **50 creatività** con mix di formati; caricare un alto volume di asset e **rinnovarli alcune volte al mese** per evitare la fatigue.
- **[UFF]** Test continuo di immagini e video per individuare i top performer; il test frequente combatte la creative fatigue. Lanciare più creatività insieme con il **flexible format**.
- **[UFF]** Advantage+ creative per catalogo: usare più opzioni di copy con **value proposition diverse**. Possono servire **fino a 15 giorni** perché il sistema impari le combinazioni migliori.
- **[UFF]** Cannes 2026: per le campagne Vendite i dati di prodotto diventano un input centrale e il sistema **assembla in tempo reale l'annuncio migliore per ogni persona** a partire da dati prodotto + asset creativi.

---

## 3. Strumenti AI creativi di Meta (stato a novembre 2026)

### 3.1 Advantage+ creative (enhancements)
**[UFF]** Funzioni (nomi possono variare in Ads Manager; le funzioni AI hanno il logo AI; alcune sono attive di default e disattivabili):
- **Espandi immagine** (AI) — adatta l'immagine a più posizionamenti.
- **Generazione sfondi** — sfondi diversi per immagini prodotto.
- **Animazione immagine** — trasforma un'immagine statica in un breve video.
- **Modelli/template immagine**, **overlay di testo**, **sticker CTA** generati con AI (anche personalizzabili con prodotti, slogan, grafiche).
- **Variazioni di testo / generazione testo**: titoli, testo principale e, da Cannes 2026, **testo dentro l'immagine**, basato sullo storico di performance per "esplorare più angoli di messaggio".
- **Enhance CTA**, automazione descrizione, **traduzione del testo** nelle immagini.
- **Video generation**: da una o più immagini a video multi-scena con overlay di testo e musica (Video Generation 2.0, 2025); a Q3 2026 generazione video da una singola immagine in pochi secondi. **[UFF]** Nei test Meta (Q1 2026) gli inserzionisti che usano la video generation hanno visto conversion rate **>3% più alti**.
- **Brand identity**: testi e immagini generati coerenti con logo, colori, font e tone of voice (2025); a Cannes 2026 annunciata una soluzione creativa end-to-end che "assorbe" tono e identità del brand dallo storico pubblicitario (in parte in test).
- **Muse Image** (luglio 2026): modello di generazione immagini dei Meta Superintelligence Labs, in rollout dentro Advantage+ creative; consente anche di **creare immagini a partire da video**. Muse Video annunciato.
- **[UFF]** Standard enhancements: Meta dichiara **-4% costo per risultato** (link click, LPV, conversioni offsite) in uno studio su larga scala.
- **[UFF]** Adozione: quasi **10 milioni di inserzionisti** hanno usato almeno uno strumento AI creativo nel Q3 2026.
- **[UFF]** Trasparenza: le ads con immagini/video significativamente modificati dagli strumenti GenAI di Meta ricevono un'etichetta "AI info".

### 3.2 Flexible ad format
**[UFF]** Raggruppa più asset (immagini, video, testi) in una sola ad; il sistema sceglie il formato da mostrare. Regole API: almeno 1 immagine o video per gruppo, stesso tipo di CTA, **max 5 testi per tipo**.

### 3.3 Meta AI business assistant
**[UFF]** In test dal Q4 2025, nel 2026 sempre più proattivo: suggerisce ottimizzazioni anche creative. Esempio citato da Meta (Q3 2026): un inserzionista ha testato copy più lunghi su suggerimento dell'assistente → +57% acquisti, -36% costo per acquisto (caso singolo).

### 3.4 Creator
**[UFF]** Creator Marketplace + Partnership Ads Hub → **Meta Creator Marketing Hub** (annunciato a Cannes 2026). Live video ads in arrivo su Instagram.

### 3.5 Come usarli bene **[OPS]**
- L'AI di Meta è eccellente per **iterazione e adattamento** (formati, crop, varianti testuali, animazioni): moltiplica le esecuzioni di un concept.
- **Non genera strategia**: angolo, insight, prova, offerta e posizionamento restano il lavoro che fa la differenza. Se tutti usano gli stessi tool, il vantaggio competitivo torna sul concept.
- Controlla sempre gli output (claim, coerenza di brand, testi tradotti, mani/prodotti generati). Disattiva enhancements non adatti (es. musica su brand premium, sfondi su prodotti regolamentati).
- Verifica l'impatto: Meta stessa raccomanda **split test** enhancements vs ads standard, perché dynamic/Advantage+ mostrano solo performance aggregate.

---

## 4. Formati e specifiche che contano

- **[UFF]** 9:16 per Stories e Reels. Reels ads sono sonore salvo audio disattivato dall'utente; >75% delle visualizzazioni Reels su Instagram è con audio attivo (dato 2024).
- **[UFF]** Studio Meta (15 A/B test, 2022–2023): aggiungere video 9:16 con audio ed elementi chiave nella safe zone → circa **-5% costo per risultato e +11% conversion rate** in media.
- **[UFF]** Safe zone Reels: lasciare libero circa **14% in alto, 35% in basso, 6% per lato** da testo, logo ed elementi chiave.
- **[UFF]** Regola dei 3 secondi: catturare l'attenzione e inserire messaggio chiave o brand nei primi 3 secondi.
- **[UFF]** Reels ads con musica e voiceover hanno ottenuto risposte del pubblico migliori di quelle senza audio (2023).

---

## 5. Test, misurazione e fatigue

- **[UFF]** A/B test: fino a **5 varianti**; una sola variabile per test; Meta garantisce che nessuno veda entrambe le versioni. Evitare test "informali" accendendo/spegnendo ad set.
- **[UFF]** Dynamic creative e Advantage+ mostrano solo risultati aggregati → non sostituiscono lo split test.
- **[UFF]** Creative fatigue = il pubblico ha visto troppe volte la stessa creatività. Segnali: **CTR in calo e CPA in aumento al crescere della frequenza**. Ads Manager mostra raccomandazioni di fatigue. Pubblici troppo ristretti aumentano costi e fatigue.
- **[OPS]** Leggi i risultati per **concept**, non per singola ad: aggrega per angolo/formato con naming coerente (es. `ANG-prova-sociale_FMT-ugc_PER-mamme_v2`).
- **[OPS]** Non spegnere troppo presto: dai a ogni nuovo concept il tempo/volume per uscire dalla fase di apprendimento prima di giudicarlo.

---

## 6. Errori ricorrenti (il problema non è l'algoritmo)

1. **Falsa diversificazione**: 15 ads, stessa promessa, stesso visual, testo diverso. Per il sistema è quasi un'unica creatività.
2. **Solo bottom-funnel**: tutte offerte e sconti; nessun angolo per chi non sa ancora di avere il problema.
3. **Brand-only**: solo creatività patinate, nessun UGC/creator, nessuna dimostrazione.
4. **Iperframmentazione**: tanti ad set con poche ads ciascuno → poco segnale.
5. **Refresh cosmetico**: alla fatigue si cambia colore invece di portare un concept nuovo.
6. **AI senza strategia**: delegare a Advantage+ la generazione di "idee" che sono solo varianti.
7. **Lettura dei dati per singola ad** invece che per concept → decisioni sul rumore, non sul segnale.

---

## 7. Cosa resta incerto (da dichiarare al cliente)

- Meccanismo esatto con cui Meta raggruppa o penalizza creatività simili: non documentato ufficialmente.
- Numero "ideale" di creatività per ad set: Meta dà indicazioni solo per alcuni prodotti (es. fino a 50 nelle app campaign). Le regole di volume in `framework-operativi.md` sono indicazioni operative, non regole Meta.
- I dati di performance citati sono auto-dichiarati da Meta.
- Diverse funzioni (soluzione creativa end-to-end, Muse Video per ads) sono in test o rollout: verificarne la disponibilità nell'account.
