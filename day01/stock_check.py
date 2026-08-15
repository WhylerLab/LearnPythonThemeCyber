# stock_check.py

# OBJECTIVE
# Schreibe eine Funktion, die eine Liste von vorhandenen Artikeln sowie einen gesuchten Artikelnamen entgegennimmt und prueft,
# ob der Artikel in der Liste enthalten ist. Nutze dazu geeignete Listen-Operationen (z. B. Zugriff, Durchlaufen oder den in-Operator),
# statt die Liste nur auszugeben. Die Funktion muss check_stock(...) heissen, damit sie vom Lagerterminal aufgerufen werden kann.



# Lagerliste
main_list = ["Tracer", "Jammer", "Cyberdeck", "Backup Drive"]



def check_stock(user_input):

    # Überprüfung ob die Usereingabe in der Liste vorhanden ist
    if user_input in main_list:
        return f"{user_input} is in stock!"

    return f"{user_input} is not in stock!"



# Eingabe des gesuchten Items
user_input = input("Search for your item: ")



# Ausgabe des Funktionsergebnisses
print(check_stock(user_input))
