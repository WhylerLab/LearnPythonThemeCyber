#gate_access.py

# OBJECTIVE
# Baue eine Routine, die wiederholt nach einem Code fragt. Nutze eine Schleife (while oder for), um die Abfrage zu wiederholen,
# bis entweder der richtige Code eingegeben wurde oder eine festgelegte Anzahl an Versuchen aufgebraucht ist.
# Setze eine passende Kontrollstruktur ein, um zwischen 'richtig', 'falsch, nochmal' und 'gesperrt' zu unterscheiden.
# Die Routine muss als Funktion check_code(...) vorliegen, damit sie vom Torsystem angesprochen werden kann.



def check_code():

    # Data-Types
    PASSWORD = "p@ssw0rd"
    attemp = 3
    user_input =""


    # Schleife und Bedingungen
    while attemp > 0:
        if user_input != PASSWORD and attemp > 0:

            # Eingabe des Passworts und anzeige der verbleibenden Versuche
            user_input = input(f">> Please enter the password, {attemp} attemps left: \n")

            # Wenn das Passwort richtig eingegeben wurde
            if user_input == PASSWORD:
                print("*** ACCESS GRANTED ***\n")
                break

            # Wenn das Passwort flasch eingegeben wurde
            else:
                print(">>> WRONG PASSWORD <<<\n")
                attemp = attemp - 1

        if attemp == 0:
            print(f"!!! ACCESS LOCKED !!!")
            break



# Aufruf der Funktion für Testzwecke
check_code()