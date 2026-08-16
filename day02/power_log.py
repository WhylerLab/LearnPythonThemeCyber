# power_log.py

# OBJECTIVE
# Schreibe eine Funktion mit einem Parameter: einer Liste von Zahlen (Verbrauchswerte in kWh).
# Berechne die Summe und den Durchschnitt aller Werte.
# Der Durchschnitt wird auf 2 Nachkommastellen gerundet ausgegeben.
# Erwartetes Rueckgabeformat: f"Total: {total}kWh, Average: {avg:.2f}kWh", z. B. bei [10, 15, 7] also 'Total: 32kWh, Average: 10.67kWh'.
# Die Funktion muss analyze_power(readings) heissen.



def analyze_power(readings):
    total = sum(readings)
    elements = len(readings)
    avg = total / elements

    return f"Total: {total}kWh, Average: {avg:.2f}kWh"

power_data = [128, 97, 115, 64, 78, 165]
print(analyze_power(power_data))