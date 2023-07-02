from Entity import Entity
from Customer import Customer
from CustomerMeneger import CustomersManager
from Trainer import Trainer
from TrainerManager import TreinerManager
from FitnessEquipment import GymEquipment
from FitnessEquipmentManager import FitnessEquipmentManager


def main():
    #class Enyity
    be_a_ninja = Entity('be_a_nunja', 200739977, 'begin', '0502626201', 'r@.com')
    be_a_ninja.print_data()
    print(be_a_ninja.address)
    be_a_ninja.address = 'menachem begin'
    be_a_ninja.print_data()

# main()