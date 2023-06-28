class FitnessEquipment:
    def __init__(self, equipment_id, name):
        self._equipment_id = equipment_id
        self._name = name
        self._availability = True

    def get_equipment_id(self):
        return self._equipment_id

    def set_equipment_id(self, equipment_id):
        self._equipment_id = equipment_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def check_availability(self):
        return self._availability

    def set_availability(self, is_available):
        self._availability = is_available

