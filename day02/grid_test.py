# grid_test.py

# OBJECTIVE
# Schreibe eine Funktion mit einem Parameter: der Kantenlaenge (int) des Musters.
# Die Funktion druckt (kein return noetig) ein Quadrat aus '#'-Zeichen, pro Zeile durch je ein Leerzeichen getrennt.
# Nutze zwei ineinander verschachtelte Schleifen (aeussere fuer Zeilen, innere fuer Spalten).
# Erwartete Ausgabe bei print_grid(3) pro Zeile: '# # #' (3 Zeilen exakt in diesem Format, jede fuer sich per print ausgegeben).
# Die Funktion muss print_grid(size) heissen.



def print_grid(size):
    for i in range(size):
        columns = []
        
        for j in range(size):
            columns.append("#")
        print(" ".join(columns))



print_grid(3)