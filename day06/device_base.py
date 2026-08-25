# device_base.py

# AUFGABE:
# Erstelle eine Klasse Device mit __init__(self, device_id, location), die beide Werte als Instanzattribute speichert.
# Füge eine Methode status_report(self) hinzu, die exakt zurückgibt: f"[{self.device_id}] at {self.location}: OK".
# Erzeuge mindestens eine Instanz und ruf status_report() auf, um zu zeigen, dass es funktioniert.

# Datei: device_base.py · Klasse: Device · Methoden: __init__(self, device_id, location), status_report(self)



class Device:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location

    def status_report(self):
            return f"[{self.device_id}] at {self.location}: OK"

Test = Device(23, "home")

print(Test.status_report())