# chronologischer-Verlauf-
# Let's scan the /mnt/data directory for the user's uploaded PDFs and parse metadata and text.
import os, re, json, textwrap
from datetime import datetime
from collections import defaultdict

import pandas as pd

# Try importing both PyPDF2 and pdfminer.six high-level if available
text_extractors = []
pages_extractors = []

try:
    import PyPDF2
    def extract_text_pypdf2(path):
        text = ""
        page_count = 0
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            page_count = len(reader.pages)
            # extract first N pages to save time; but here we want as full as possible
            for i in range(page_count):
                try:
                    t = reader.pages[i].extract_text() or ""
                except Exception:
                    t = ""
                text += "\n" + t
        return text, page_count
    text_extractors.append(extract_text_pypdf2)
except Exception as e:
    pass

# Fallback using pdfminer if available
try:
    from pdfminer.high_level import extract_text as pdfminer_extract_text
    def extract_text_pdfminer(path):
        text = pdfminer_extract_text(path)
        # page count not trivial; set None and let PyPDF2 handle if available
        return text, None
    text_extractors.append(extract_text_pdfminer)
except Exception:
    pass

# If neither available, we'll read nothing
assert text_extractors, "No PDF text extractor available"

# Gather PDFs matching the list
all_files = os.listdir("/mnt/data")
pdfs = [f for f in all_files if f.lower().endswith(".pdf")]

# The user pasted a list; we can optionally prioritize those names
priority_names = [
"10002208423_1_ASS und Kündigung (2).pdf",
"10002208423_1_ASS und Kündigung.pdf",
"10002208423_1_ASS und Kündigung_01 (2).pdf",
"10002282941_2_Deckungszusage außergerichtlich und für selbständiges Beweisverfahren.pdf",
"10002475062_1_FVA Bekl..pdf",
"10002475068_1_Mitt. wg. FV für Bekl..pdf",
"10002545284_1_Vertretungsanzeige und Aufforderungsschreiben.pdf",
"10003968086_1_Anforderung StN.pdf",
"10003997337_1_FVA StN wg. SV - Kopie.pdf",
"10003997337_1_FVA StN wg. SV.pdf",
"10004018210_1_Übersendungsschreiben.pdf",
"10004018213_1_Verfügung FV gewährt und Info angefragte SVs - Kopie.pdf",
"10004018213_1_Verfügung FV gewährt und Info angefragte SVs.pdf",
"10004093154_1_Auftragserteilung an SV Dr. Geisler.pdf",
"20252107_Sachstandsanfrage_freigegeben - Kopie.pdf",
"20252107_Sachstandsanfrage_freigegeben.pdf",
"20253007_Sachstandsanfrage_kein gutes Gefühl_freigegeben.pdf",
"2025_02_27 entwurf.pdf",
"25_02_27 Nachfrage bei Gericht - Kopie.pdf",
"25_02_27 Nachfrage bei Gericht.pdf",
"Absage Zriny im April.pdf",
"Antrag Durchführung selbständiges Beweisverfahren (2).pdf",
"Antwort 5 gutacher abtelefoniert.pdf",
"BESCHLUSS 2. Beauftragung SV Dr. Geisler vom 5.6 - Kopie.pdf",
"BESCHLUSS 2. Beauftragung SV Dr. Geisler vom 5.6.pdf",
"BEWEISBESCHLUSS - Kopie.pdf",
"BEWEISBESCHLUSS.pdf",
"BHU Dr. Randelzhofer.pdf",
"Bekl. StN zu Reisefähigkeit.pdf",
"Deckungszusage außergerichtlich und für selbständi.pdf",
"Erneute Stellungnahme bezüglich Rückfragen Beweiss.pdf",
"Glaubaftmachung Reiseunfähigkeit (2).pdf",
"Glaubaftmachung Reiseunfähigkeit.pdf",
"Keine Fristverlängerung gewährt.pdf",
"Mai antwort gericht - bedenken ob überhaupt notwendig ist -.pdf",
"Mitteilung wg. Anfrage bei mehreren SVs - Kopie.pdf",
"Mitteilung wg. Anfrage bei mehreren SVs.pdf",
"Schriftsatz zum weiteren Verfahrensgang und akutel.pdf",
"Stellungnahme 19.5. gerichtlicher Auftrag und seine probleme an mich weitergleitet.pdf",
"Stellungnahme auf Antwortschreiben (2).pdf",
"Stellungnahme auf Antwortschreiben.pdf",
"VERFÜGUNG Fristsetzung für Antragsgegnerin.pdf",
"VERFÜGUNG Fristsetzung für Antragsgegnerin01 (2).pdf",
"bitten um ergänzende Informationen (2).pdf",
"bitten um ergänzende Informationen.pdf",
"zK. Deckungszusage außergerichtlich und für selbst.pdf",
"Übersendung MD-GA.pdf",
"Übersendungsschreiben05.pdf",
"Übersendungsschreiben06 (2).pdf",
"Übersendungsschreiben06.pdf",
"Übersendungsschreiben11.6. zum Beschluss Anja G. die 2. vom 5.6. - Kopie.pdf",
"Übersendungsschreiben11.6. zum Beschluss Anja G. die 2. vom 5.6..pdf",
]

# Filter to those that exist
pdfs_to_parse = [f for f in priority_names if f in pdfs]
# Also include any other pdfs in folder not listed, to be safe
for f in pdfs:
    if f not in pdfs_to_parse:
        pdfs_to_parse.append(f)

len(pdfs_to_parse), pdfs_to_pars10002208423_1_ASS und Kündigung (2).pdf — Kündigung/ASS — (n. v.) — Pfad: ./Anlagen/10002208423_1_ASS und Kündigung (2).pdf

10002208423_1_ASS und Kündigung.pdf — Kündigung/ASS — (n. v.) — Pfad: ./Anlagen/10002208423_1_ASS und Kündigung.pdf

10002208423_1_ASS und Kündigung_01 (2).pdf — Kündigung/ASS — (n. v.) — Pfad: ./Anlagen/10002208423_1_ASS und Kündigung_01 (2).pdf

10002282941_2_Deckungszusage außergerichtlich und für selbständiges Beweisverfahren.pdf — Deckungszusage — (n. v.) — Pfad: ./Anlagen/10002282941_2_Deckungszusage außergerichtlich und für selbständiges Beweisverfahren.pdf

10002475062_1_FVA Bekl..pdf — Stellungnahme/FVA (Bekl.) — (n. v.) — Pfad: ./Anlagen/10002475062_1_FVA Bekl..pdf

10002475068_1_Mitt. wg. FV für Bekl..pdf — Mitteilung/Fristverlängerung (Bekl.) — (n. v.) — Pfad: ./Anlagen/10002475068_1_Mitt. wg. FV für Bekl..pdf

10002545284_1_Vertretungsanzeige und Aufforderungsschreiben.pdf — Vertretungsanzeige/Aufforderung — (n. v.) — Pfad: ./Anlagen/10002545284_1_Vertretungsanzeige und Aufforderungsschreiben.pdf

10003968086_1_Anforderung StN.pdf — Anforderung Stellungnahme — (n. v.) — Pfad: ./Anlagen/10003968086_1_Anforderung StN.pdf

10003997337_1_FVA StN wg. SV - Kopie.pdf — Fristverlängerung/Stellungnahme (SV) — (n. v.) — Pfad: ./Anlagen/10003997337_1_FVA StN wg. SV - Kopie.pdf

10003997337_1_FVA StN wg. SV.pdf — Fristverlängerung/Stellungnahme (SV) — (n. v.) — Pfad: ./Anlagen/10003997337_1_FVA StN wg. SV.pdf

10004018210_1_Übersendungsschreiben.pdf — Übersendungsschreiben — (n. v.) — Pfad: ./Anlagen/10004018210_1_Übersendungsschreiben.pdf

10004018213_1_Verfügung FV gewährt und Info angefragte SVs - Kopie.pdf — Verfügung/Fristverlängerung — (n. v.) — Pfad: ./Anlagen/10004018213_1_Verfügung FV gewährt und Info angefragte SVs - Kopie.pdf

10004018213_1_Verfügung FV gewährt und Info angefragte SVs.pdf — Verfügung/Fristverlängerung — (n. v.) — Pfad: ./Anlagen/10004018213_1_Verfügung FV gewährt und Info angefragte SVs.pdf

10004093154_1_Auftragserteilung an SV Dr. Geisler.pdf — Auftragserteilung an SV — (n. v.) — Pfad: ./Anlagen/10004093154_1_Auftragserteilung an SV Dr. Geisler.pdf

20252107_Sachstandsanfrage_freigegeben - Kopie.pdf — Sachstandsanfrage — 2025‑07‑21 — Pfad: ./Anlagen/20252107_Sachstandsanfrage_freigegeben - Kopie.pdf

20252107_Sachstandsanfrage_freigegeben.pdf — Sachstandsanfrage — 2025‑07‑21 — Pfad: ./Anlagen/20252107_Sachstandsanfrage_freigegeben.pdf

20253007_Sachstandsanfrage_kein gutes Gefühl_freigegeben.pdf — Sachstandsanfrage — 2025‑07‑30 — Pfad: ./Anlagen/20253007_Sachstandsanfrage_kein gutes Gefühl_freigegeben.pdf

2025_02_27 entwurf.pdf — Entwurf (Schriftsatz/Mail) — 2025‑02‑27 — Pfad: ./Anlagen/2025_02_27 entwurf.pdf

25_02_27 Nachfrage bei Gericht - Kopie.pdf — Nachfrage Gericht — 2025‑02‑27 (angenommen) — Pfad: ./Anlagen/25_02_27 Nachfrage bei Gericht - Kopie.pdf

25_02_27 Nachfrage bei Gericht.pdf — Nachfrage Gericht — 2025‑02‑27 (angenommen) — Pfad: ./Anlagen/25_02_27 Nachfrage bei Gericht.pdf

Absage Zriny im April.pdf — Absage (SV/Termin?) — (4/20xx aus Inhalt zu prüfen) — Pfad: ./Anlagen/Absage Zriny im April.pdf

Antrag Durchführung selbständiges Beweisverfahren (2).pdf — Antrag SBV — (n. v.) — Pfad: ./Anlagen/Antrag Durchführung selbständiges Beweisverfahren (2).pdf

Antwort 5 gutacher abtelefoniert.pdf — Mitteilung/Antwort (SV‑Anfrage) — (n. v.) — Pfad: ./Anlagen/Antwort 5 gutacher abtelefoniert.pdf

BESCHLUSS 2. Beauftragung SV Dr. Geisler vom 5.6 - Kopie.pdf — Beschluss (SV‑Beauftragung) — 05.06.(Jahr prüfen) — Pfad: ./Anlagen/BESCHLUSS 2. Beauftragung SV Dr. Geisler vom 5.6 - Kopie.pdf

BESCHLUSS 2. Beauftragung SV Dr. Geisler vom 5.6.pdf — Beschluss (SV‑Beauftragung) — 05.06.(Jahr prüfen) — Pfad: ./Anlagen/BESCHLUSS 2. Beauftragung SV Dr. Geisler vom 5.6.pdf

BEWEISBESCHLUSS - Kopie.pdf — Beweisbeschluss — (n. v.) — Pfad: ./Anlagen/BEWEISBESCHLUSS - Kopie.pdf

BEWEISBESCHLUSS.pdf — Beweisbeschluss — (n. v.) — Pfad: ./Anlagen/BEWEISBESCHLUSS.pdf

BHU Dr. Randelzhofer.pdf — BHU (Bericht/Behandlungsunterlage) — (n. v.) — Pfad: ./Anlagen/BHU Dr. Randelzhofer.pdf

Bekl. StN zu Reisefähigkeit.pdf — Stellungnahme (Bekl.) Reisefähigkeit — (n. v.) — Pfad: ./Anlagen/Bekl. StN zu Reisefähigkeit.pdf

Deckungszusage außergerichtlich und für selbständi.pdf — Deckungszusage — (n. v.) — Pfad: ./Anlagen/Deckungszusage außergerichtlich und für selbständi.pdf

Erneute Stellungnahme bezüglich Rückfragen Beweiss.pdf — Stellungnahme (Rückfragen Beweis) — (n. v.) — Pfad: ./Anlagen/Erneute Stellungnahme bezüglich Rückfragen Beweiss.pdf

Glaubaftmachung Reiseunfähigkeit (2).pdf — Glaubhaftmachung Reiseunfähigkeit — (n. v.) — Pfad: ./Anlagen/Glaubaftmachung Reiseunfähigkeit (2).pdf

Glaubaftmachung Reiseunfähigkeit.pdf — Glaubhaftmachung Reiseunfähigkeit — (n. v.) — Pfad: ./Anlagen/Glaubaftmachung Reiseunfähigkeit.pdf

Keine Fristverlängerung gewährt.pdf — Verfügung (keine FV) — (n. v.) — Pfad: ./Anlagen/Keine Fristverlängerung gewährt.pdf

Mai antwort gericht - bedenken ob überhaupt notwendig ist -.pdf — Antwort Gericht (Bedenken …) — (5/20xx aus Inhalt) — Pfad: ./Anlagen/Mai antwort gericht - bedenken ob überhaupt notwendig ist -.pdf

Mitteilung wg. Anfrage bei mehreren SVs - Kopie.pdf — Mitteilung (SV‑Anfragen) — (n. v.) — Pfad: ./Anlagen/Mitteilung wg. Anfrage bei mehreren SVs - Kopie.pdf

Mitteilung wg. Anfrage bei mehreren SVs.pdf — Mitteilung (SV‑Anfragen) — (n. v.) — Pfad: ./Anlagen/Mitteilung wg. Anfrage bei mehreren SVs.pdf

Schriftsatz zum weiteren Verfahrensgang und akutel.pdf — Schriftsatz Verfahrensgang — (n. v.) — Pfad: ./Anlagen/Schriftsatz zum weiteren Verfahrensgang und akutel.pdf

Stellungnahme 19.5. gerichtlicher Auftrag und seine probleme an mich weitergleitet.pdf — Stellungnahme (19.05.) — 19.05.(Jahr prüfen) — Pfad: ./Anlagen/Stellungnahme 19.5. gerichtlicher Auftrag und seine probleme an mich weitergleitet.pdf

Stellungnahme auf Antwortschreiben (2).pdf — Stellungnahme — (n. v.) — Pfad: ./Anlagen/Stellungnahme auf Antwortschreiben (2).pdf

Stellungnahme auf Antwortschreiben.pdf — Stellungnahme — (n. v.) — Pfad: ./Anlagen/Stellungnahme auf Antwortschreiben.pdf

VERFÜGUNG Fristsetzung für Antragsgegnerin.pdf — Verfügung (Fristsetzung) — (n. v.) — Pfad: ./Anlagen/VERFÜGUNG Fristsetzung für Antragsgegnerin.pdf

VERFÜGUNG Fristsetzung für Antragsgegnerin01 (2).pdf — Verfügung (Fristsetzung) — (n. v.) — Pfad: ./Anlagen/VERFÜGUNG Fristsetzung für Antragsgegnerin01 (2).pdf

bitten um ergänzende Informationen (2).pdf — Bitte um ergänzende Informationen — (n. v.) — Pfad: ./Anlagen/bitten um ergänzende Informationen (2).pdf

bitten um ergänzende Informationen.pdf — Bitte um ergänzende Informationen — (n. v.) — Pfad: ./Anlagen/bitten um ergänzende Informationen.pdf

zK. Deckungszusage außergerichtlich und für selbst.pdf — Deckungszusage (z. K.) — (n. v.) — Pfad: ./Anlagen/zK. Deckungszusage außergerichtlich und für selbst.pdf

Übersendung MD-GA.pdf — Übersendung MD‑GA (Gutachten?) — (n. v.) — Pfad: ./Anlagen/Übersendung MD-GA.pdf

Übersendungsschreiben05.pdf — Übersendungsschreiben — (05/20xx, aus Inhalt) — Pfad: ./Anlagen/Übersendungsschreiben05.pdf

Übersendungsschreiben06 (2).pdf — Übersendungsschreiben — (06/20xx, aus Inhalt) — Pfad: ./Anlagen/Übersendungsschreiben06 (2).pdf

Übersendungsschreiben06.pdf — Übersendungsschreiben — (06/20xx, aus Inhalt) — Pfad: ./Anlagen/Übersendungsschreiben06.pdf

Übersendungsschreiben11.6. zum Beschluss Anja G. die 2. vom 5.6. - Kopie.pdf — Übersendungsschreiben — 11.06.(Jahr prüfen) — Pfad: ./Anlagen/Übersendungsschreiben11.6. zum Beschluss Anja G. die 2. vom 5.6. - Kopie.pdf

Übersendungsschreiben11.6. zum Beschluss Anja G. die 2. vom 5.6..pdf — Übersendungsschreiben — 11.06.(Jahr prüfen) — Pfad: ./Anlagen/Übersendungsschreiben11.6. zum Beschluss Anja G. die 2. vom 5.6..pdfe[:5]
# 📄 Chronologischer Verlauf – Ergebnisse

- [10002208423_1_ASS und Kündigung](verfahren/10002208423_1_ASS%20und%20Kündigung.pdf)  
  > Kündigungsschreiben (ASS)

- [10002208423_1_ASS und Kündigung (2)](verfahren/10002208423_1_ASS%20und%20Kündigung%20(2).pdf)  
  > Zweite Fassung Kündigungsschreiben

- [1000228941_2_Deckungszusage außergerichtlich und für selbständiges Beweisverfahren](verfahren/1000228941_2_Deckungszusage%20außergerichtlich%20und%20für%20selbständiges%20Beweisverfahren.pdf)  
  > Deckungszusage Rechtsschutz

- [10002475062_1_FVA Bekl.](verfahren/10002475062_1_FVA%20Bekl..pdf)  
  > FVA Beklagte Partei

- [10002475068_1_Mitt. wg. FV für Bekl.](verfahren/10002475068_1_Mitt.%20wg.%20FV%20für%20Bekl..pdf)  
  > Mitteilung wegen Verfahren Beklagte Partei

- [1000254528_1_Vertretungsanzeige und Aufforderungsschreiben](verfahren/1000254528_1_Vertretungsanzeige%20und%20Aufforderungsschreiben.pdf)  
  > Vertretungsanzeige / Aufforderungsschreiben

- [1000396806_1_Anforderung StN](verfahren/1000396806_1_Anforderung%20StN.pdf)  
  > Anforderung StN

- [10003997337_1_FVA StN wg. SV](verfahren/10003997337_1_FVA%20StN%20wg.%20SV.pdf)  
  > FVA StN wegen Sachverständigen

- [10004018210_1_Übersendungsschreiben](verfahren/10004018210_1_Übersendungsschreiben.pdf)  
  > Übersendungsschreiben

- [10004018213_1_Verfügung FV gewährt und Info angefragte SVs](verfahren/10004018213_1_Verfügung%20FV%20gewährt%20und%20Info%20angefragte%20SVs.pdf)  
  > Verfügung FV gewährt / Infos SVs

- [10004093154_1_Auftragserteilung an SV Dr. Geisler](verfahren/10004093154_1_Auftragserteilung%20an%20SV%20Dr.%20Geisler.pdf)  
  > Auftrag an Sachverständige Dr. Geisler

- [20252107_Sachstandsanfrage_freigegeben](verfahren/20252107_Sachstandsanfrage_freigegeben.pdf)  
  > Sachstandsanfrage freigegeben

- [20253007_Sachstandsanfrage_kein gutes Gefühl freigegeben](verfahren/20253007_Sachstandsanfrage_kein%20gutes%20Gefühl%20freigegeben.pdf)  
  > Sachstandsanfrage „kein gutes Gefühl“

- [25_02_27_entwurf](verfahren/25_02_27_entwurf.pdf)  
  > Entwurf vom 27.02.2025

- [25_02_27_Nachfrage bei Gericht](verfahren/25_02_27_Nachfrage%20bei%20Gericht.pdf)  
  > Nachfrage bei Gericht (27.02.2025)

- [25_02_27_Nachfrage bei Gericht – Kopie](verfahren/25_02_27_Nachfrage%20bei%20Gericht%20-%20Kopie.pdf)  
  > Nachfrage bei Gericht – Kopie

- [Absage Zriny im April](verfahren/Absage%20Zriny%20im%20April.pdf)  
  > Absage Zriny (April)
