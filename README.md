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

len(pdfs_to_parse), pdfs_to_parse[:5]
