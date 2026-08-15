# signal_convert.py

# OBJECTIVE
# Schreibe eine Funktion, die einen Zahlenwert in Metern entgegennimmt und ihn in Kilometer umrechnet.
# Nutze dafür einen arithmetischen Operator (keine Typumwandlung wie str()/float() als Umrechnung missverstehen – das ist keine Einheitenumrechnung).
# Die Funktion gibt einen formatierten String zurueck, der sowohl den Original- als auch den umgerechneten Wert lesbar zeigt, z. B. per f-String.
# Die Funktion muss convert_value(meters) heissen und darf keine eigene input()-Abfrage enthalten – der Wert kommt ausschliesslich ueber den Parameter rein.



# Funktion convert_value()
def convert_value(meters):

# Data-Type convertieren
    kilometers = meters / 1000
    return f"{meters}m = {kilometers}km"


# Eingabewert entgegennehmen
meters = int(input(">>> Input the number in meters: "))


# Ausgabe der Funktion
print(convert_value(meters))