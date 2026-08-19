# container_pack.py

# OBJECTIVE
# Schreibe eine Funktion, die eine beliebige Anzahl an Artikelnamen als einzelne Argumente entgegennimmt (kein Listen-Parameter, sondern *args-Stil)
# und einen zusammenfassenden String zurueckgibt. Erwartetes Format: f"Container packed with {len(items)} items: {', '.join(items)}".
# Beispiel: pack_container("Tracer", "Jammer") liefert 'Container packed with 2 items: Tracer, Jammer'. Die Funktion muss pack_container(*items) heissen.


def pack_container(*items):
    return f"Container packed with {len(items)} items: {', '.join(items)}"

print(pack_container("Tracer", "Jammer", "Scanner", "Logger"))