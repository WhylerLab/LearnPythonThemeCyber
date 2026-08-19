# crane_check.py

# OBJECTIVE
# Erstelle zwei Dateien. In crane_config.py: eine Modul-Konstante MAX_LOAD_KG = 5000 (kein Funktionsaufruf noetig, einfach die Variable auf Modulebene).
# In crane_check.py: importiere MAX_LOAD_KG aus crane_config und schreibe eine Funktion, die ein Gewicht (int) entgegennimmt und True zurueckgibt,
# wenn das Gewicht die Konstante NICHT ueberschreitet, sonst False. Die Funktion muss check_load(weight) heissen.
# Teste mit einem Wert unter und einem ueber der Grenze.



from crane_config import MAX_LOAD_KG

def check_load(weight):
    if weight <= MAX_LOAD_KG:
        return True
    return False

print(check_load(500))
print(check_load(50000))