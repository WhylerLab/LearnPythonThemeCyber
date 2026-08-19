# load_validator.py

# OBJECTIVE
# Schreibe eine Funktion mit einem Parameter (Gewicht in kg, int oder float).
# Ist das Gewicht kleiner oder gleich 0, loese selbst einen ValueError mit der Nachricht "Gewicht muss positiv sein." aus (per raise, NICHT per return/print).
# Ist das Gewicht positiv, gib f"Gewicht akzeptiert: {weight}kg" zurueck. Die Funktion muss validate_weight(weight) heissen.
# Zeig in einem kurzen Testaufruf ausserhalb der Funktion, dass du den Fehler bei einem negativen Wert mit try/except auffangen und eine Meldung ausgeben kannst.


def validate_weight(weight):
    if weight > 0:
        return f"Gewicht akzeptiert: {weight}kg"
    
    raise ValueError("Gewicht muss positiv sein.")


try:
    print(validate_weight(-15))
except ValueError as error:
    print(error)