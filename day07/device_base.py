# device_base.py

class Device:
    total_devices = 0
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        Device.total_devices += 1

    @classmethod
    def get_total(cls):
        return f"Total devices: {cls.total_devices}"

    @classmethod
    def from_config(cls, config):
        return cls(config["id"], config["loc"])

    def __eq__(self, other):
        return self.device_id == other.device_id


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

con = {"id": "D-05", "loc" : "Server Room"}

print_fleet_report(fleet)
print(Device.get_total())

neues_geraet = Device.from_config(con)
print(neues_geraet.status_report())


geraet1 = Device("D-09", "Lager")
geraet2 = Device("D-09", "Werkstatt")
geraet3 = Device("D-10", "Lager")

print(geraet1 == geraet2)  # erwartet: True (gleiche device_id)
print(geraet1 == geraet3)  # erwartet: False (unterschiedliche device_id)