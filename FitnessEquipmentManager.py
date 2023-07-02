from SQLconection import SQL3
from Entity import Entity
from Customer import Customer
from FitnessEquipment import GymEquipment

class FitnessEquipmentManager:
    Fitness_instance = []



    def __init__(self):
        self.__availability = True



    def isavailability(self):
        return self._availability

    def set_availability(self, is_available):
        self._availability = is_available

    @property
    def is_availability(self):
        return self.__availability

    @is_availability.setter
    def is_availability(self, is_availability):
        print('this is a is_availability setter')
        self.__availability = is_availability





    def CreateTableEquipmentGym(self):
        SQL3.CreateTable(self, 'EquipmentGym', ('Id',
                                                'Equipment_name',
                                                'Equipment_brand',
                                                'Equipment_assignment',
                                                'equipment_id'))

    def add_equipment(self, Equipment_name, Id, Equipment_brand, assignment):
        new_equipment = GymEquipment(Equipment_name, Id, Equipment_brand, assignment)
        FitnessEquipmentManager.Fitness_instance.append(new_equipment)


        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute(
            'INSERT INTO EquipmentGym (Id,'
            ' Equipment_name, Equipment_brand,'
            ' Equipment_assignment, equipment_id) VALUES '
            '(?, ?, ?, ?, ?)',
            (new_equipment.equipment_id, new_equipment.name, new_equipment.id, new_equipment.brand,
             new_equipment.assignment))

        con.commit()

        return cur.fetchone()


    def add__or_chinge_Nwe_item_by_id(self,  column, item_value, equipment_id):
        SQL3.add_or_chinge_item_by_id(self, 'EquipmentGym', column, item_value, equipment_id)


    def display_equipment(self):
        SQL3.display_records(self, 'EquipmentGym')





    def get_equipment_record(self, equipment_id):
        SQL3.get_record(self, 'EquipmentGym', equipment_id)


    def remove_equipment_record(self, equipment_id):
        SQL3.remove_record(self, 'EquipmentGym', equipment_id)



    def remove_one_equipment_record(self,column, equipment_id):
        SQL3.remove_one_record(self, 'EquipmentGym', column, equipment_id)


    def print_equipment_instance(self):
        for instance in FitnessEquipmentManager.Fitness_instance:
            print(instance.equipment_id, instance.name, instance.id,
                  instance.brand, instance.assignment)



# def main():
#     if __name__ == '__main__':
#         manager = FitnessEquipmentManager()
#         manager.CreateTableEquipmentGym()
#         print(manager.add_equipment('blake', 555, 'cat', 'dumbbells'))

        # manager.check_id_exists(200739977)
        # manager.remove_duplicate_customers()
        # print(manager.get_customer_record(200739977))
        # manager.remove_customer_record(200739977)
        # manager.remove_one_customer_record('name', 200739977)
        # manager.add__or_chinge_Nwe_item_by_id('name', 'moshe', 200739977)
        # manager.display_customers()
        # manager.print_customer_instance()

def main():
    manager = FitnessEquipmentManager()
    # manager.CreateTableEquipmentGym()
    manager.display_equipment()
    # result = manager.add_equipment('blake', 555, 'cat', 'dumbbells')
    # print(result)
    manager.print_equipment_instance()
    print(FitnessEquipmentManager.Fitness_instance)
    manager.remove_equipment_record(1)

if __name__ == '__main__':
    main()