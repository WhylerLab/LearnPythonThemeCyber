# motion_sensor.py

# Aufgabe: Erstelle eine eigenständige Klasse BatteryPowered mit __init__(self, battery_level) und einer Methode battery_status(self),
# die f"Battery: {self.battery_level}%" zurückgibt – ist battery_level kleiner als 20, hänge zusätzlich " (LOW!)" an.
# Erstelle dann MotionSensor(Device, BatteryPowered) mit __init__(self, device_id, location, battery_level),
# der beide Eltern-__init__-Methoden explizit aufruft (keine automatische Verkettung). Überschreibe status_report(self),
# sodass sie Device.status_report(self) + " | " + self.battery_status() zurückgibt. Gib zum Schluss testweise MotionSensor.__mro__ aus,
# um die Auflösungsreihenfolge zu sehen.

# Datei: motion_sensor.py · Klassen: BatteryPowered, MotionSensor (erbt von Device UND BatteryPowered) · Methoden: battery_status(self), status_report(self)


class Device:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location

    def status_report(self):
        return f"[{self.device_id}] at {self.location}: OK"



class BatteryPowered:
    def __init__(self, battery_level):
        self.battery_level = battery_level
        

    def battery_status(self):
        if self.battery_level < 20:
            return f"Battery: {self.battery_level}% (LOW!)"
        else:
            return f"Battery: {self.battery_level}%"


class MotionSensor(Device, BatteryPowered):
    def __init__(self, device_id, location, battery_level):
        Device.__init__(self, device_id, location)
        BatteryPowered.__init__(self, battery_level)

    def status_report(self):
        return Device.status_report(self) + " | " + self.battery_status()



sensor = MotionSensor("MS-01", "Kagerou Labs", 15)

print(sensor.status_report())
print(MotionSensor.__mro__)