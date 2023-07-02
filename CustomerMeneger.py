from SQLconection import SQL3
from Entity import Entity
from Customer import Customer

class CustomersManager:
    customer_instance = []



    def __init__(self):

        pass



    def CreateTableCustomersGym(self):
        SQL3.CreateTable(self, 'CustomersGym', ('row_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                                ' name TEXT, ID INTEGER,'
                                                ' address TEXT,'
                                                ' phone TEXT, '
                                                ' email TEXT, '
                                                ' gender TEXT, '
                                                ' age INTEGER,'
                                                ' height INTEGER,'
                                                ' weight INTEGER,'
                                                ' payment_plan TEXT'))



    def check_id_exists(self, ID):
        return SQL3.check_id_exists(self, 'CustomersGym', ID)


    def add_customer(self, name, ID, address, phone, email, gender, age=0, height=0, weight=0):
        new_customer = Customer(name, ID, address, phone, email, gender, age, height, weight)

        if not self.check_id_exists(ID):
            import sqlite3
            con = sqlite3.connect('Gym.db')
            cur = con.cursor()
            cur.execute('''
                INSERT INTO CustomersGym (name, address,
                 phone, email, gender, age, height, weight,
                 ID, payment_plan) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (new_customer.name, new_customer.address
                 , new_customer.phone, new_customer.email,
                 new_customer.gender, new_customer.age,
                 new_customer.height, new_customer.weight,
                 new_customer.id, new_customer.payment_plan))
            con.commit()
            cur.execute("SELECT row_id FROM CustomersGym WHERE ID = ?", (ID,))
            CustomersManager.customer_instance.append(new_customer)
            return cur.fetchone()
        else:
            print("ID already exists in the table.")
            return None


    def add__or_chinge_Nwe_item_by_id(self,  column, item_value, id):
        SQL3.add_or_chinge_item_by_id(self, 'CustomersGym', column, item_value, id)


    def display_customers(self):
        SQL3.display_records(self, 'CustomersGym')


    def remove_duplicate_customers(self):
        SQL3.remove_duplicate_records(self, 'CustomersGym')



    def get_customer_record(self, Id):
        SQL3.get_record(self, 'CustomersGym', Id)


    def remove_customer_record(self, Id):
        SQL3.remove_record(self, 'CustomersGym', Id)



    def remove_one_customer_record(self,column, Id):
        SQL3.remove_one_record(self, 'CustomersGym', column, Id)


    def print_customer_instance(self):
        for instance in CustomersManager.customer_instance:
            print(instance.name, instance.id, instance.address,
                  instance.phone, instance.email, instance.gender,
                  instance.age, instance.height, instance.weight,
                  instance.payment_plan)



def main():
    if __name__ == '__main__':
        manager = CustomersManager()
        manager.CreateTableCustomersGym()
        print(manager.add_customer('omer', 200739977, 'ben nun 2', '0506857162',
                                   'r6720441@mail.com,', 'mail'))
        print(manager.add_customer('moshe', 200739999, 'ben nun 4', '0506957162',
                                   'r67204481@mail.com,', 'fmail'))
        manager.add_customer('michael', 308094556, 'trumpeldor 59', '0506720441', 'ruth@gmail.com', 'female')
        manager.display_customers()
        manager.check_id_exists(200739977)
        # manager.remove_duplicate_customers()
        # print(manager.get_customer_record(200739977))
        # manager.remove_customer_record(200739977)
        # manager.remove_one_customer_record('name', 200739977)
        # manager.add__or_chinge_Nwe_item_by_id('name', 'moshe', 200739977)
        # manager.display_customers()
        # manager.print_customer_instance()

main()