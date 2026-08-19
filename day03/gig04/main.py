# main.py

# OBJECTIVE
# Erstelle zwei Dateien im selben Ordner. In dock_tools.py: eine Funktion kg_to_tons(kg),
# die Kilogramm in Tonnen umrechnet und auf 2 Nachkommastellen gerundet als float zurueckgibt (1 Tonne = 1000 kg),
# sowie eine Funktion format_manifest(item, qty), die den String f'{item.upper()} x{qty}' zurueckgibt.
# In main.py: importiere beide Funktionen aus dock_tools und rufe sie mit Beispielwerten auf (z. B. kg_to_tons(2500) und format_manifest("crate", 12)),
# gib die Ergebnisse aus.



from dock_tools import kg_to_tons
from dock_tools import format_manifest

print(kg_to_tons(2500))
print(format_manifest("crate", 12))