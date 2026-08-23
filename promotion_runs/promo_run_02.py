# promo_run_02.py

# Mindestens eine Funktion mit einem Default-Parameter (z. B. für eine optionale Einheit oder Formatierungsoption)
# Mindestens eine Stelle, die *args oder **kwargs sinnvoll nutzt (z. B. um variabel viele Zusatzangaben pro Sendung entgegenzunehmen)
# Robuste Fehlerbehandlung: Einige Datensätze enthalten fehlerhafte Gewichtsangaben (z. B. Text statt Zahl) – dein Skript darf dabei nicht abstürzen,
# sondern soll fehlerhafte Einträge sauber erkennen und im Bericht gesondert ausweisen
# Der Bericht selbst enthält mindestens: Anzahl gelieferter, ausstehender und beschädigter Sendungen, Gesamtgewicht der erfolgreich gelieferten Sendungen,
# und eine Liste der Artikel mit fehlerhaften Daten



# Name, Amount, Weight, Status
main_list = [
    ("Scanner", 150, 75, "delivered"),
    ("Jammer", 120, 60, "delivered"),
    ("Neurolink", 60, 30, "pending"),
    ("Optics", 30, "gew", "damaged"),
    ("Cyberlink", 800, 400, "delivered")
]


delivered = 0
pending = 0
damaged = 0

total_weight = 0

corrupt_list = []
delivered_list = []


# Weight tons to kg
def tons_to_kg(weight):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number.")

    return weight * 1000


# Main routine
for name, amount, weight, status in main_list:

    if status == "delivered":
        try:
            kg_weight = tons_to_kg(weight)
            total_weight += kg_weight
            delivered += 1
            delivered_list.append(name)

        except TypeError:
            corrupt_list.append(name)
            continue

    elif status == "pending":
        pending += 1

    elif status == "damaged":
        damaged += 1

        try:
            tons_to_kg(weight)
        except TypeError:
            corrupt_list.append(name)
            continue


# Delivered container protocol
def received_container(*items):
    return f"Delivered container packed with {len(items)} items: {', '.join(items)}"


# Protocol status
def log_entry(message, t_status="STANDARD"):
    return f"[{t_status}] {message}"


# Protocol
print()
print(log_entry("- Bericht"))
print("====================")
print(f"Total delivered container: {delivered}")
print(received_container(*delivered_list))
print(f"Total weight delivered container: {total_weight}kg")
print()
print(f"Pending container: {pending}")
print()
print(f"Damaged container: {damaged}")
print(f"Total corrupted container: {corrupt_list}")
print()