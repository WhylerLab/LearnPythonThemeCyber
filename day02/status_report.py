# status_report.py

# OBJECTIVE
# Schreibe eine Funktion mit zwei Parametern: Label (str) und Wert (int). Das Label wird linksbuendig auf eine feste Breite von 12 Zeichen aufgefuellt,
# der Wert rechtsbuendig auf 6 Zeichen, getrennt durch ': '. Erwartetes Format bei format_status("Power", 87): 'Power : 87' (12 Zeichen Label + ': ' + 6 Zeichen Wert).
# Nutze String-Ausrichtungsmethoden oder f-String-Formatierung, keine manuelle Leerzeichen-Verkettung. Die Funktion muss format_status(label, value) heissen.



def format_status(label, value):
    return f"{label:<12}: {value:>6}"



# Test Ein-/Ausgabe
print(format_status("Power",87))