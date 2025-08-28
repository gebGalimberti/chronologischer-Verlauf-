
import pandas as pd
import matplotlib.pyplot as plt

# Beispiel-Daten
data = {
    'Kategorie': ['A', 'B', 'C', 'D'],
    'Wert': [23, 45, 12, 67]
}

# DataFrame erstellen
df = pd.DataFrame(data)

# Bericht als Textdatei speichern
with open('bericht.txt', 'w') as f:
    f.write("Automatischer Bericht\n")
    f.write("=====================\n\n")
    f.write("Datenübersicht:\n")
    f.write(df.to_string(index=False))
    f.write("\n\nStatistische Zusammenfassung:\n")
    f.write(df.describe().to_string())

# Diagramm erstellen und speichern
plt.figure(figsize=(6, 4))
plt.bar(df['Kategorie'], df['Wert'], color='skyblue')
plt.title('Beispielhafte Datenanalyse')
plt.xlabel('Kategorie')
plt.ylabel('Wert')
plt.tight_layout()
plt.savefig('diagramm.png')
