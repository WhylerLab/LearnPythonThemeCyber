# crate_ledger.py

# OBJECTIVE
# Lege eine globale Variable total_crates mit Startwert 0 an.
# Schreibe eine Funktion add_crate(amount) mit einem Parameter, die total_crates um amount erhoeht (unter Nutzung von global) und den neuen Gesamtstand zurueckgibt.
# Erwartetes Verhalten: Start bei 0, nach add_crate(5) gibt die Funktion 5 zurueck UND die globale Variable total_crates ist danach ebenfalls 5.
# Ein zweiter Aufruf add_crate(3) muss 8 zurueckgeben.


total_crates = 0


def add_crate(amount):
    global total_crates
    total_crates = total_crates + amount
    return total_crates


add_crate(5)
add_crate(3)


print(total_crates)
