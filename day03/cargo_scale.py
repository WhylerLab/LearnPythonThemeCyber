# cargo_scale.py

# OBJECTIVE
# Schreibe ein Skript, das per input() zwei Werte abfragt: Gesamtgewicht (kg) und Anzahl Kisten.
# Fange beim Umwandeln der Eingaben in Zahlen einen ValueError ab und gib bei ungueltiger Eingabe die Meldung 'Ungueltige Eingabe,
# bitte eine Zahl verwenden.' aus, statt abzustuerzen. Danach berechnest du in einer separaten Funktion calc_average(total_weight, crate_count)
# das Durchschnittsgewicht pro Kiste (Gesamtgewicht / Kistenzahl). Ist crate_count gleich 0, faengt die Funktion intern einen ZeroDivisionError
# ab und gibt den String 'Keine Kisten vorhanden, Durchschnitt nicht berechenbar.' zurueck. Sonst gibt sie f'Durchschnitt: {avg:.2f}kg pro Kiste' zurueck.



def calc_average(total_weight, crate_count):
    try:
        avg = total_weight / crate_count
        return f"Durchschnitt: {avg:.2f}kg pro Kiste"
    except ZeroDivisionError:
        return "Keine Kisten vorhanden, Durchschnitt nicht berechenbar."


try:
    total_weight = float(input("Gesamtgewicht (kg): "))
    crate_count = int(input("Anzahl Kisten: "))

    print(calc_average(total_weight, crate_count))

except ValueError:
    print("Ungueltige Eingabe, bitte eine Zahl verwenden.")