from Entity import Entity
from Customer import Customer


class Trainer(Entity):
    Trainer_id = 1
    def __init__(self, name, Id, address, phone, email, gender, expertise=''):
        super().__init__(name, Id, address, phone, email)
        self.__gender = gender
        self.__expertise = expertise
        self._trainer_id = Trainer.trainer_id
        Trainer.Trainer_id += 1


    @property
    def expertise(self):
        return self.__expertise

    @expertise.setter
    def set_expertise(self, nwe_expertise):
        print('this is a expertise setter')
        self.__expertise = nwe_expertise







# Example usage
# if __name__ == "__main__":
#     # Creating customers and trainers
#     customer1 = RegularCustomer("001", "John Doe", 25, "Male", "C001", "Regular", ["Weights"])
#     customer2 = PremiumCustomer("002", "Jane Smith", 30, "Female", "C002", "Premium", ["Weights", "Yoga"])
#     trainer1 = Trainer("T001", "Mike Johnson", 35, "Male", "Trainer001", "Weightlifting")
#
#     # Creating fitness equipment
#     equipment1 = FitnessEquipment("E001", "Treadmill")
#     equipment2 = FitnessEquipment("E002", "Dumbbells")
#
#     # Creating training lessons
#     lesson1 = TrainingLesson("L001", "Weightlifting Class", "10:00 AM - 11:00 AM", 5)
#     lesson2 = TrainingLesson("L002", "Yoga Class", "4:00 PM - 5:00 PM", 10)
#
#     # Enrolling customers in training lessons
#     lesson1.enroll_customer(customer1)
#     lesson1.enroll_customer(customer2)
#     lesson2.enroll_customer(customer2)
#
#     # Displaying lesson details
#     lesson1.display_details()
#     lesson2.display_details()
#
#     # Checking equipment availability
#     print(f"Equipment {equipment1.get_name()} availability: {equipment1.check_availability()}")
#     print(f"Equipment {equipment2.get_name()} availability: {equipment2.check_availability()}")
#
#     # Updating equipment availability
#     equipment1.set_availability(False)
#     equipment2.set_availability(True)
#
#     # Checking updated equipment availability
#     print(f"Equipment {equipment1.get_name()} availability: {equipment1.check_availability()}")
#     print(f"Equipment {equipment2.get_name()} availability: {equipment2.check_availability()}")
#
#     # Calculating and generating invoice
#     payment = Payment()
#     invoice = payment.generate_invoice(customer1)
#     print(invoice)