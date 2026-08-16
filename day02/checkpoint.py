# checkpoint.py

# OBJECTIVE
# Schreibe eine Funktion mit genau drei Parametern: ob ein Passierschein vorliegt (bool), die aktuelle Freigabestufe (int) und die erforderliche Mindeststufe (int).
# Die Funktion gibt True zurueck, wenn ein Passierschein vorliegt UND die Freigabestufe mindestens der erforderlichen entspricht, sonst False.
# Nutze dafuer einen logischen Operator (and), keine verschachtelten if-Bloecke. Rueckgabetyp ist ein reiner Boolean, kein String.
# Die Funktion muss check_access(has_pass, clearance_level, required_level) heissen.



def check_access(has_pass, clearance_level, required_level):
    return has_pass and clearance_level >= required_level



# Test Eingabe
print(check_access(True, 6, 5))