from Entity import Entity
from Trainer import Trainer
from SQLconection import SQL3

class TreinerManager:
    trainers_lst = []

    def __init__(self):

        pass


    def CreateTableTrainersGym(self):
        SQL3.CreateTable(self, 'Trainers_Gym', ('name', 'TEXT', 'Id', 'INTEGER',
                                                'address', 'TEXT', 'phone', 'TEXT',
                                                'email', 'TEXT', 'gender', 'TEXT', 'expertise',
                                                'TEXT', 'trainer_id', 'TEXT'))



    def check_id_exists(self, id):
        return SQL3.check_id_exists(self, 'Trainers_Gym', id)


    def add_trainer(self,  name, Id, address, phone, email, gender, expertise):
        new_trainer = Trainer(name, Id, address, phone, email, gender, expertise)
        TreinerManager.trainers_lst.append(new_trainer)

        if not self.check_id_exists(Id):
            import sqlite3
            con = sqlite3.connect('Gym.db')
            cur = con.cursor()
            cur.execute(
                'INSERT INTO Trainers_Gym (name, id, address,'
                ' phone, email, gender, age, expertise) '
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?,)',
                (new_trainer.name, new_trainer.id, new_trainer.address, new_trainer.phone, new_trainer.email,
                 new_trainer.gender, new_trainer.expertise))
            con.commit()
            cur.execute("SELECT customer_id FROM Trainers_Gym WHERE id = ?", (Id,))
            TreinerManager.trainers_lst.append(new_trainer)
            return cur.fetchone()
        else:
            print("ID already exists in the table.")
            return None

    def display_trainers(self):
        SQL3.display_records(self, 'TrainersGym')


    def remove_duplicate_records(self):
        SQL3.remove_duplicate_records(self, 'TrainersGym')


    def add__or_chinge_Nwe_item_by_id(self,  column, item_value, id):
        SQL3.add_or_chinge_item_by_id(self, 'TrainersGym', column, item_value, id)


    def get_trainer_record(self, Id):
        SQL3.get_record(self, 'TrainersGym', Id)



    def remove_trainer_record(self, Id):
        SQL3.remove_record(self, 'TrainersGym', Id)


    def remove_one_trainer_record(self,column, Id):
        SQL3.remove_one_record(self, 'TrainersGym', column, Id)


    def print_customer_instance(self):
        for instance in TreinerManager.trainers_lst:
            print(instance.name, instance.id, instance.address,
                  instance.phone, instance.email, instance.gender,
                  instance.expertise, instance.trainer_id)


def main():
    manager = TreinerManager()
    manager.CreateTableTrainersGym()
    # manager.add_trainer('name', 22, 'address', 'phone', 'email', 'gender', 'expertise')

main()