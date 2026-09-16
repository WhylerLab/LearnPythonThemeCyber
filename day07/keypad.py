# keypad.py

class Keypad:
    def __init__(self, device_id, pin) -> None:
        self.device_id = device_id
        self.pin = pin

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        if len(value) == 4 and value.isdigit():
            self._pin = value
        else:
            raise ValueError("PIN must be 4 digits")

    def __str__(self) -> str:
        return f"{self.device_id},{self.pin}"


try:
    print(f"{Keypad('K-01','4471')}")
except Exception as e:
    print(e)


try:
    print(f"{Keypad('K-01','44')}")
except Exception as e:
    print(e)