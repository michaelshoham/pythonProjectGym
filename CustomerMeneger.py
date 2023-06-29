from SQLconection import SQL3
from Entity import Entity
from Customer import Customer

class CustomersManager:
    customer_instance = []



    def __init__(self):

        pass



    def CreateTableCustomersGym(self):
        SQL3.CreateTable(self, 'CustomersGym_nwe', ("name", 'TEXT', 'Id', 'INTEGER',
                                        'address', 'TEXT', 'phone', 'TEXT',
                                        'email', 'TEXT', 'gender', 'TEXT', 'age',
                                        'INTEGER', 'height', 'REAL', 'weight', 'REAL',
                                        'customer_id', 'INTEGER', 'payment_plan', 'TEXT'))


    def check_id_exists(self, id):
        SQL3.check_id_exists(self, 'CustomersGym_nwe', id)


    def add_customer(self, name, Id, address, phone, email, gender, age=0, height=0, weight=0):
        new_customer = Customer(name, Id, address, phone, email, gender, age, height, weight)

        if not self.check_id_exists(Id):
            import sqlite3
            con = sqlite3.connect('Gym.db')
            cur = con.cursor()
            cur.execute(
                'INSERT INTO CustomersGym_nwe (name, id, address,'
                ' phone, email, gender, age, height, weight,'
                ' customer_id, payment_plan) '
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (new_customer.name, new_customer.id, new_customer.address, new_customer.phone, new_customer.email,
                 new_customer.gender, new_customer.age, new_customer.height, new_customer.weight,
                 new_customer.customer_id, new_customer.payment_plan))
            con.commit()
            cur.execute("SELECT customer_id FROM CustomersGym_nwe WHERE id = ?", (Id,))
            return cur.fetchone()
        else:
            print("ID already exists in the table.")
            return None

    def add__or_chinge_Nwe_item_by_id(self,  column, item_value, id):
        SQL3.add_or_chinge_item_by_id(self, 'CustomersGym_nwe', column, item_value, id)


    def display_customers(self):
        SQL3.display_records(self, 'CustomersGym_nwe')


    def remove_duplicate_customers(self):
        SQL3.remove_duplicate_records(self, 'CustomersGym_nwe')



    def get_customer_record(self, Id):
        SQL3.get_record(self, 'CustomersGym_nwe', Id)


    def remove_customer_record(self, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM CustomersGym_nwe WHERE id = ?", (Id,))

        cur.execute("DELETE FROM CustomersGym_nwe WHERE id = ?", (Id,))
        con.commit()
        print("Record deleted successfully.")


    def remove_one_customer_record(self,column, Id):
        SQL3.remove_one_record(self, 'CustomersGym_nwe', column, Id)


    # def print_customer_instance(self, item):
    #     for elem in CustomersManager.customer_instance:
    #         print(elem.)



def main():
    if __name__ == '__main__':
        manager = CustomersManager()
        manager.CreateTableCustomersGym()
        # print(manager.add_customer('omer', 200739977, 'ben nun 2', '0506857162', 'r6720441@mail.com,', 'mail'))
        # manager.display_customers()
        # manager.check_id_exists(200739977)
        manager.remove_duplicate_customers()
        # print(manager.get_customer_record(200739977))
        # manager.remove_customer_record(200739977)
        manager.remove_one_customer_record('name', 200739977)
        manager.add__or_chinge_Nwe_item_by_id('name', 'moshe', 200739977)
        manager.display_customers()

main()