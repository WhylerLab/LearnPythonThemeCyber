# manifest_kwargs.py

# OBJECTIVE
# Schreibe eine Funktion, die eine beliebige Anzahl an Keyword-Argumenten entgegennimmt (**details-Stil) und daraus einen zusammenfassenden String baut.
# Erwartetes Format: ', '.join(f'{k}={v}' for k, v in details.items()).
# Beispiel: build_manifest(weight=120, item="Tracer") liefert 'weight=120, item=Tracer' (Reihenfolge entspricht der Aufrufreihenfolge,
# da Dicts seit Python 3.7 die Einfuegereihenfolge behalten). Die Funktion muss build_manifest(**details) heissen.



def build_manifest(**details):
    return ', '.join(f'{k}={v}' for k, v in details.items())



# Als Schleife
def build_manifest2(**details):
    parts = []
    for k, v in details.items():
        parts.append(f"{k}={v}")
    return ', '.join(parts)



print(build_manifest(weight=120, item="Tracer",))
print(build_manifest2(weight=240, item="Scanner",))