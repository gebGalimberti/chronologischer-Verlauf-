# 📂 Ordner `gesamt` – Zentrale Übersicht medizinischer und juristischer Dokumentation

## Zweck und Aufbau

Der Ordner `gesamt` enthält die wichtigsten Übersichtsdateien zum gesamten medizinischen und rechtlichen Verlauf. Hier werden alle relevanten Befunde, Dokumente, Termine und Timeline-Ereignisse chronologisch und strukturiert erfasst. Ziel ist eine zentrale, durchsuchbare und verlinkte Gesamtdokumentation – insbesondere zur Arbeit mit Schriftsätzen, Gerichtsakten und anwaltlicher Korrespondenz.

---

## Enthaltene Dateien

| Datei                  | Inhalt & Zweck                                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------|
| `Befunde_Gesamt.md`    | Tabellarische Übersicht aller medizinischen Befunde (Arztberichte, Gutachten, Klinikberichte) mit Verlinkungen zu Originaldokumenten, Diagnosen, Quellen und Relevanz für das Verfahren. |
| `Dokumente_Gesamt.md`  | Auflistung aller juristisch relevanten Dokumente: Schriftsätze, Beschlüsse, E-Mails, Vermerke – jeweils mit Titel, Dokumentart, Akteur, Gericht/Kanzlei, Datum, Aktenzeichen, sowie Verlinkung und Seitenangabe, sofern möglich. |
| `Termine_Gesamt.md`    | Übersicht aller wichtigen Termine (z.B. Gerichtstermine, Arztbesuche, Fristen, Besprechungen) mit Status, beteiligten Akteuren und Querverweisen. |
| `Timeline_Gesamt.md`   | Chronologischer Ablauf sämtlicher relevanter Ereignisse, inklusive Querverweisen zu Befunden und Dokumenten für schnellen Abgleich und Kontext. |

---

## Strukturelle Hinweise & Pflege

- **Chronologischer Aufbau:**  
  Alle Dateien sind nach Datum sortiert, um den Verlauf übersichtlich und nachvollziehbar zu dokumentieren.

- **Verlinkungen zu Originaldokumenten:**  
  Wenn möglich, werden direkte Links auf PDF-/MD-Dateien verwendet. Bitte möglichst immer den **Dokumenttitel** sowie die **Seitenzahl** (wenn relevant) angeben, z.B.:  
  `[Beschluss LG München, S.2](../dokumente/beschluesse/2023-07-25_LG-Beschluss.pdf)`

- **Dokumentarten & Akteure:**  
  Jede Dokumentationseinheit enthält die Art des Dokuments (z.B. Schriftsatz, Beschluss, E-Mail, Vermerk), die beteiligten Akteure (z.B. Rechtsanwalt, Kanzlei, Gericht, Sachverständige), und – wenn sinnvoll – den Ort (z.B. Stuttgart, München).

- **Querverweise & Abgleich:**  
  Zur schnellen Abstimmung mit Gerichtsakten und Schriftsätzen werden Einträge möglichst mit Aktenzeichen, Fundstellen und Links versehen.  
  Hinweise, Fragen und Rückmeldungen aus der anwaltlichen Zusammenarbeit oder aus Gerichtsakten werden dokumentiert und in den jeweiligen Kontext (z.B. Timeline, Befund) eingearbeitet.

- **Pflegehinweise:**  
  - Neue Einträge bitte immer zeitnah und vollständig mit allen verfügbaren Angaben (Datum, Titel, Dokumenttyp, Link, Akteur, Relevanz) ergänzen.
  - Bei späteren Ergänzungen oder Korrekturen bitte das Änderungsdatum und ggf. eine kurze Änderungsnotiz anfügen.
  - Rückfragen und Hinweise aus dem anwaltlichen/parteiischen Austausch bitte mit Quelle (z.B. E-Mail, Telefonnotiz) dokumentieren.

---

## Beispielhafte Tabelleneinträge

### Befunde_Gesamt.md

| Datum     | Arzt/Akteur         | Einrichtung/Ort      | Dokument (mit Link)                        | Art       | Kernaussage / Diagnose      | Quelle / Akte         | Relevanz           | Beleg/Seite      |
|-----------|---------------------|----------------------|--------------------------------------------|-----------|-----------------------------|----------------------|--------------------|------------------|
| 22.07.22  | Dr. Nessler         | Praxis Nessler       | [Erstvorstellung](../dokumente/befunde/2022-07-22.pdf) | Arztbericht | Falsches Behandlungsdatum   | Schriftsatz LG 12/22 | Falschdokumentation | S.1              |

### Dokumente_Gesamt.md

| Datum     | Akteur              | Gericht/Kanzlei      | Dokument (mit Link)                        | Art         | Inhalt / Betreff            | Aktenzeichen / Fundstelle | Verknüpfte Befunde | Beleg/Seite      |
|-----------|---------------------|----------------------|--------------------------------------------|-------------|-----------------------------|--------------------------|--------------------|------------------|
| 25.07.23  | LG Stuttgart        | LG Stuttgart         | [Beschluss v. 25.07.23](../dokumente/beschluesse/2023-07-25_LG-Beschluss.pdf) | Beschluss   | Beweisaufnahme              | LG 123/23, S.4           | Befund 07/23       | Original S.4     |

---

## Weiteres Vorgehen / Kontakt

- **Abgleich & Zusammenarbeit:**  
  Der regelmäßige Abgleich mit der Gerichtsakte und die parallele Einarbeitung von anwaltlichen Rückmeldungen ist essentiell.  
  Bei Fragen oder Unklarheiten bitte Rücksprache mit dem zuständigen Anwalt oder direkt im README-Ordner (`README/MASTER.md`) nachsehen.

- **Hinweis zur Ablage:**  
  Die Originaldokumente befinden sich im jeweiligen Unterordner (`../dokumente/...`).  
  Bitte alle Links und Querverweise aktuell halten.

---

*Letzte Aktualisierung: <!-- hier Datum eintragen -->*
----
## Abschnitt: Auswertung Outlook-Zusammenfassungen & Schriftverkehr

| Datum       | Absender / Empfänger         | Betreff / Thema                      | Art (E-Mail, Outlook, Vermerk) | Beteiligte Akteure (z.B. Kanzlei, Gericht, Arzt) | Kurzinhalt / Aussage         | Bezug zu Akte / Schriftsatz | Verlinkung / Speicherort      | Relevanz / Status         |
|-------------|-----------------------------|--------------------------------------|-------------------------------|-----------------------------------------------|------------------------------|-----------------------------|-------------------------------|---------------------------|
| 2024-08-27  | RA Müller → Gericht München | Fristverlängerung beantragt          | E-Mail                        | RA Müller, LG München                        | Antrag auf Frist, Begründung  | Schriftsatz LG 08/24        | [E-Mail (PDF)](../dokumente/schriftverkehr/2024-08-27_RA-Mueller-Frist.pdf) | in Akte, Antwort offen    |
| 2024-08-29  | Patient → KFO Dr. XY        | Bitte um Terminbestätigung           | Outlook                       | Patient, KFO Dr. XY                           | Nachfrage zum Kontrolltermin | Patientenakte 2024          | [Outlook-Export](../dokumente/schriftverkehr/2024-08-29_Termin_KFO.msg)    | Termin offen             |
| 2024-08-15  | Gericht → RA Müller         | Ladung zur mündlichen Verhandlung    | E-Mail                        | LG München, RA Müller                         | Anberaumung Verhandlungstermin| Gerichtsakte LG             | [Ladung](../dokumente/gericht/2024-08-15_Ladung.pdf)                      | Termin notiert           |

**Hinweise zur Pflege:**
- Für jede E-Mail/Korrespondenz bitte alle Spalten ausfüllen, insbesondere Betreff, Absender/Empfänger, Art (E-Mail/Outlook/Vermerk), Akteure, Kurzinhalt und den Bezug zu relevanten Akten oder Schriftsätzen.
- Nach Möglichkeit immer eine Verlinkung zum Originaldokument (z. B. PDF, MSG, Outlook-Export) angeben.
- Den Status (z.B. "Antwort offen", "erledigt", "in Akte übernommen") aktuell halten.
- Bei wichtigen rechtlichen/verfahrensbezogenen E-Mails zusätzlich in der Timeline_Gesamt.md referenzieren.

---

**Du kannst diesen Abschnitt beliebig erweitern und regelmäßig ergänzen.  
Soll ich dir bei der Übernahme konkreter E-Mails oder beim Ausfüllen der Tabelle helfen?** Sag einfach Bescheid!
