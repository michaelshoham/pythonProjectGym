from Entity import Entity
from Customer import Customer
from SQLconection import SQL3

class TreinerManager:
    customers_lst = []


    def CreateTableTrainersGym(self):
        SQL3.CreateTable(self, 'TrainersGym', ("name", 'TEXT', 'Id', 'INTEGER',
                                        'address', 'TEXT', 'phone', 'TEXT',
                                        'email', 'TEXT', 'gender', 'TEXT', 'expertise',
                                        'TEXT', 'trainer_id', 'TEXT'))


    def check_id_exists(self, id):
        SQL3.check_id_exists(self, 'TrainersGym', id)


    def add_trainer(self,  name, Id, address, phone, email, gender, expertise):
        new_trainer = Customer(name, Id, address, phone, email, gender, expertise)
        TreinerManager.customers_lst.append(new_trainer)

        if not self.check_id_exists(Id):
            import sqlite3
            con = sqlite3.connect('Gym.db')
            cur = con.cursor()
            cur.execute(
                'INSERT INTO TrainersGym (name, id, address,'
                ' phone, email, gender, age, expertise) '
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?,)',
                (new_trainer.name, new_trainer.id, new_trainer.address, new_trainer.phone, new_trainer.email,
                 new_trainer.gender, new_trainer.expertise))
            con.commit()
            cur.execute("SELECT customer_id FROM TrainersGym WHERE id = ?", (Id,))
            return cur.fetchone()
        else:
            print("ID already exists in the table.")
            return None

    def display_trainers(self):
        SQL3.display_records(self, 'TrainersGym')


    def remove_duplicate_records(self):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT id, COUNT(*) FROM TrainersGym GROUP BY id HAVING COUNT(*) > 1")
        duplicate_ids = cur.fetchall()


        cur.execute("""
            DELETE FROM TrainersGym
            WHERE ROWID NOT IN (
                SELECT MIN(ROWID)
                FROM TrainersGym
                GROUP BY id
            )
        """)
        con.commit()
        print("Duplicate records removed.")


    def get_trainer_record(self, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM TrainersGym WHERE id = ?", (Id,))
        duplicate_ids = cur.fetchall()

        return duplicate_ids

    def remove_trainer_record(self, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM TrainersGym WHERE id = ?", (Id,))

        cur.execute("DELETE FROM TrainersGym WHERE id = ?", (Id,))
        con.commit()
        print("Record deleted successfully.")
