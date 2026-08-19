# crane_counter.py

# Schreibe eine Funktion make_counter() ohne Parameter.
# Sie definiert intern eine Funktion (z. B. count()), die bei jedem Aufruf den internen Zaehler um 1 erhoeht und den neuen Stand zurueckgibt,
# und gibt diese innere Funktion zurueck. Erwartetes Verhalten: counter = make_counter(),
# dann liefert counter() beim ersten Aufruf 1, beim zweiten Aufruf 2, beim dritten 3 usw. Der Zaehlerstand darf NICHT in einer globalen Variable liegen,
# sondern muss ausschliesslich per Closure + nonlocal gemerkt werden.



def make_counter():
    counter = 0
    def count():
        nonlocal counter
        counter += 1
        return counter
    return count