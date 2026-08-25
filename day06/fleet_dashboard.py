# fleet_dashboard.py

# Aufgabe:
# Schreibe eine Funktion print_fleet_report(devices), die eine Liste beliebiger Device-Objekte (auch SmartLock, MotionSensor gemischt)
# entgegennimmt und für jedes Element .status_report() aufruft und das Ergebnis auf einer eigenen Zeile ausgibt.
# Keine Typ-Prüfung (isinstance, type(), etc.) innerhalb der Funktion erlaubt – die Funktion darf gar nicht wissen, welcher konkrete Gerätetyp gerade dran ist.
# Teste mit einer gemischten Liste aus mindestens einem Device, einem SmartLock und einem MotionSensor.

# Datei: fleet_dashboard.py · Methode: print_fleet_report(devices)



class Device:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location

    def status_report(self):
        return f"[{self.device_id}] at {self.location}: OK"


class SmartLock(Device):
    def status_report(self):
        return f"[{self.device_id}] at {self.location}: LOCKED"


class BatteryPowered:
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def battery_status(self):
        if self.battery_level < 20:
            return f"Battery: {self.battery_level}% (LOW!)"
        return f"Battery: {self.battery_level}%"


class MotionSensor(Device, BatteryPowered):
    def __init__(self, device_id, location, battery_level):
        Device.__init__(self, device_id, location)
        BatteryPowered.__init__(self, battery_level)

    def status_report(self):
        return Device.status_report(self) + " | " + self.battery_status()


def print_fleet_report(devices):
    for device in devices:
        print(device.status_report())


fleet = [
    Device("D-01", "Entrance"),
    SmartLock("SL-01", "Main Gate"),
    MotionSensor("MS-01", "Hallway", 15)
]

print_fleet_report(fleet)