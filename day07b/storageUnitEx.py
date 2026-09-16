# storageUnit.py

class StorageUnit:
    unit_count = 0

    def __init__(self, unit_id, capacity) -> None:
        self.unit_id = unit_id
        self.capacity = capacity
        StorageUnit.unit_count += 1

    @classmethod
    def get_unit_count(cls):
        return f"Storage units: {cls.unit_count}"

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be negative")
        else:
            self._capacity = value



su1 = StorageUnit("SU-01", 50)
su2 = StorageUnit("SU-02", 30)
su3 = StorageUnit("SU-03", 75)

try:
    su4 = StorageUnit("SU-03", -10)
except ValueError as e:
    print(e)

print(StorageUnit.get_unit_count())