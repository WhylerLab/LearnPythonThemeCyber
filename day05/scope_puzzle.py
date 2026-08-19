# scope_puzzle.py

#OBJECTIVE
# Lege eine globale Variable status mit dem Wert "global" an. Schreibe eine Funktion outer(),
# die eine LOKALE Variable status mit dem Wert "enclosing" anlegt und darin eine innere Funktion definiert,
# die status ganz normal liest (kein nonlocal, kein global, nur lesen) und zurueckgibt. outer() ruft die innere Funktion auf und gibt deren Ergebnis zurueck.
# Erwartetes Ergebnis von outer(): 'enclosing' - NICHT 'global', obwohl es eine globale Variable mit demselben Namen gibt.


status = "gobal"

def outer():
    status = "enclosing"

    def inner():
        return status
    
    return inner()

print(outer())