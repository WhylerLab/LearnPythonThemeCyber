# # badge_gen-py

# OBJECTIVE
# Schreibe eine Funktion mit genau drei Parametern: Vorname, Nachname und Kennung (die Kennung ist eine numerische Runner-ID,
# z. B. 7 oder 42 – vergleichbar mit einer Mitarbeiternummer).
# Die Funktion setzt daraus ein Badge im festen Format NACHNAME(3 Grossbuchstaben)-KENNUNG(4-stellig, mit fuehrenden Nullen aufgefuellt)-vorname(klein geschrieben) zusammen, z. B. wuerde 'Nova', 'Reyes', 7 zu 'REY-0007-nova' werden.
# Nutze dafuer String-Methoden (Gross-/Kleinschreibung, Slicing, Auffuellen mit Nullen) statt die Teile nur zu verketten.
# Die Funktion muss format_badge(vorname, nachname, kennung) heissen.




def format_badge(vorname, nachname, kennung):
    # Vorname lowercase
    vorname = vorname.lower()

    # Nachname Uppercase
    nachname = nachname.upper()

    # Nachname maximal 3 Letter
    nachname = nachname[:3]

    # Ausgabe in der gewünschten Reihenfolge/Formatierung    
    return f"{nachname}-{kennung:04}-{vorname}"



# Eingabe der Runner Daten
vorname = input("Forename: ")
nachname = input("Lastname: ")
kennung = int(input("Runner-ID: "))



# Ausgabe der fertigen Badge
print(format_badge(vorname, nachname, kennung))