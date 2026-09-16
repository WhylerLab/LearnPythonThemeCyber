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


su1 = StorageUnit("SU-01", 50)
su2 = StorageUnit("SU-02", 30)
su3 = StorageUnit("SU-03", 75)

print(StorageUnit.get_unit_count())