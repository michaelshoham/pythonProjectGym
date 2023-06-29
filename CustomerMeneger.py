from SQLconection import SQL3
from Entity import Entity
from Customer import Customer

class CustomerManager:



    def __init__(self):

        pass



    def CreateTableCustomersGym(self):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()

        try:
            cur.execute('CREATE TABLE CustomersGym_nwe (name TEXT, Id INTEGER, address TEXT, phone TEXT, email TEXT,'
                        ' gender TEXT, age INTEGER, height REAL, weight REAL, customer_id INTEGER, payment_plan TEXT)')
            con.commit()
        except sqlite3.OperationalError as e:
            print(e)

    def check_id_exists(self, id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT id FROM CustomersGym_nwe WHERE id = ?", (id,))
        row = cur.fetchone()

        if row is not None:
            return True
        else:
            return False

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

    def display_customers(self):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM CustomersGym_nwe")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    def remove_duplicate_records(self):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT id, COUNT(*) FROM CustomersGym_nwe GROUP BY id HAVING COUNT(*) > 1")
        duplicate_ids = cur.fetchall()


        cur.execute("""
            DELETE FROM CustomersGym_nwe
            WHERE ROWID NOT IN (
                SELECT MIN(ROWID)
                FROM CustomersGym_nwe
                GROUP BY id
            )
        """)
        con.commit()
        print("Duplicate records removed.")


    def get_customer_record(self, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM CustomersGym_nwe WHERE id = ?", (Id,))
        duplicate_ids = cur.fetchall()

        return duplicate_ids

    def remove_customer_record(self, Id):
        import sqlite3
        con = sqlite3.connect('Gym.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM CustomersGym_nwe WHERE id = ?", (Id,))

        cur.execute("DELETE FROM CustomersGym_nwe WHERE id = ?", (Id,))
        con.commit()
        print("Record deleted successfully.")



def main():
    if __name__ == '__main__':
        manager = CustomerManager()
        # manager.CreateTableCustomersGym()
        # print(manager.add_customer('omer', 200739977, 'ben nun 2', '0506857162', 'r6720441@mail.com,', 'mail'))
        # manager.display_customers()
        # manager.check_id_exists(200739977)
        # manager.remove_duplicate_records()
        # print(manager.get_customer_record(200739977))
        manager.remove_customer_record(200739977)
        manager.display_customers()

main()