# main.py

# OBJECTIVE
# Erstelle einen Ordner dock_kit/ mit drei Dateien.
# In weight.py: eine Funktion lbs_to_kg(lbs), die Pfund in Kilogramm umrechnet (1 lb = 0.453592 kg) und auf 2 Nachkommastellen gerundet als float zurueckgibt.
# In labels.py: eine Funktion format_container_id(prefix, number), die f'{prefix.upper()}-{number:05}' zurueckgibt (5-stellig, mit fuehrenden Nullen).
# In __init__.py: importiere beide Funktionen aus ihren jeweiligen Modulen, damit sie direkt ueber from dock_kit import lbs_to_kg, format_container_id nutzbar sind.
# Teste beides in einer separaten main.py auf oberster Ebene (ausserhalb von dock_kit/) mit Beispielwerten.

from dock_kit import lbs_to_kg, format_container_id

print(lbs_to_kg(25))
print(format_container_id("test",8))