# 🛠️ Korrekturliste (Errata & Prüfprotokoll)

Dieses Dokument sammelt alle Fehler, Widersprüche und Korrekturen.  
Jeder Eintrag mit Datum → transparent und nachvollziehbar.

---

## 🔎 Typische Fehlerarten
- [DATE-ERROR] → falsches / unklarer Datumseintrag
- [COURT-ERROR] → falsches Gericht / Kammer
- [CASE-ERROR] → falsches oder fehlendes Aktenzeichen
- [TYPE-ERROR] → falsche Dokumentart (Beschluss/Verfügung/Mitteilung)
- [WHO-TO-WHO-ERROR] → falsche Zuordnung „wer → wen“

---

## 📑 Beispiel-Einträge

### LG Stuttgart – 2023
- **Fehler:** Eintrag „Beschluss Einleitung Beweisverfahren 2022“ war falsch.  
- **Korrektur:** Richtiges Datum → 2023-03-__.  
- **Aktenzeichen:** 716 XVII 610/23.  
- **Tagging:** [DATE-ERROR]  

---

### LG Stuttgart – 2023
- **Fehler:** Dokument „FVA Bekl.“ zunächst als „Beschluss“ eingetragen.  
- **Korrektur:** Richtige Dokumentart = **Verfügung (Fristverlängerung)**.  
- **Tagging:** [TYPE-ERROR]  

---

### AG München – 2025
- **Fehler:** Betreuerwechsel nicht dem Amtsgericht zugeordnet.  
- **Korrektur:** Richtiges Gericht = Amtsgericht München, Beschluss 2025-01-__.  
- **Tagging:** [COURT-ERROR]  

---

## 📌 To-Do
- [ ] Alle falschen Jahreszuordnungen berichtigen (2022 ≠ 2023).
- [ ] Alle Gerichtsdokumente prüfen → korrekt LG/AG/SG einordnen.
- [ ] Alle Dokumentarten korrekt abgrenzen (Beschluss / Verfügung / Mitteilung).
- [ ] Alle Aktenzeichen vereinheitlichen (z. B. 716 XVII 610/23).
