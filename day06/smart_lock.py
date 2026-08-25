# smart_lock.py

# Aufgabe: Erstelle SmartLock(Device) mit __init__(self, device_id, location, is_locked).
# Ruf darin super().__init__(device_id, location) auf, um die Basiswerte zu setzen, und speichere zusätzlich is_locked als Instanzattribut.
# Überschreibe status_report(self): ruf zuerst super().status_report() auf und häng je nach is_locked entweder " | Locked" oder " | Unlocked" an das Ergebnis an.
# Beispiel: bei is_locked=True und device_id="SL-01", location="Kunde A" lautet die Ausgabe exakt "[SL-01] at Kunde A: OK | Locked".

# Datei: smart_lock.py · Klasse: SmartLock (erbt von Device) · Methoden: __init__(self, device_id, location, is_locked), status_report(self)



class Device:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location

    def status_report(self):
        return f"[{self.device_id}] at {self.location}: OK"


class SmartLock(Device):
    def __init__(self, device_id, location, is_locked):
        super().__init__(device_id, location)
        self.is_locked = is_locked

    def locked(self):
        self.is_locked = True

    def unlocked(self):
        self.is_locked = False

    def status_report(self):
        status = "Locked" if self.is_locked else "Unlocked"
        return super().status_report() + f" | {status}"


test = SmartLock("SL-01", "Kunde A", True)



print(test.status_report())

test.unlocked()
print(test.status_report())

test.locked()
print(test.status_report())