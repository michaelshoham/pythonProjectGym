from Entity import Entity
class GymEquipment(Entity):

    Equipment_id = 1

    def __init__(self, name, Id, brand, assignment):
        super().__init__(name, Id, None, None, None)
        self.__equipment_id = GymEquipment.Equipment_id
        GymEquipment.Equipment_id += 1
        self.__brand = brand
        self.__assignment = assignment
        self.__properties = {}



    @property
    def equipment_id(self):
        return self.__equipment_id

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, get_brand):
        print('this is a brand setter')
        self.__brand = get_brand

    @property
    def assignment(self):
        return self.__assignment

    @assignment.setter
    def assignment(self, get_assignment):
        print('this is a assignment setter')
        self.__assignment = get_assignment




