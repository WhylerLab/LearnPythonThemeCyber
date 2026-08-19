# dock_log.py

# OBJECTIVE
# Schreibe eine Funktion mit zwei Parametern: eine Nachricht (str) und eine Dringlichkeitsstufe mit dem Standardwert "INFO".
# Die Funktion gibt f"[{severity}] {message}" zurueck. Erwartetes Verhalten:
# log_entry("Kran kalibriert") liefert '[INFO] Kran kalibriert', log_entry("Leck entdeckt", severity="CRITICAL") liefert '[CRITICAL] Leck entdeckt'.
# Die Funktion muss log_entry(message, severity="INFO") heissen.



def log_entry(message, severity="INFO"):
    return f"[{severity}] {message}"

print(log_entry("Kran kalibriert"))
print(log_entry("Leck entdeckt",severity="CRITICAL"))
